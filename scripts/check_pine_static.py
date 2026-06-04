#!/usr/bin/env python3
"""Lightweight static checks for the Pine script artifact.

This is not a TradingView compiler. It verifies the repository contains the
expected indicator features and avoids a few common accidental regressions.
"""
from pathlib import Path

PINE = Path("pine/long_term_investment_intelligence_screener.pine")
text = PINE.read_text()
required_tokens = [
    "//@version=6",
    "indicator(",
    "request.financial",
    "Research Score",
    "Buy Intent Score",
    "Intent Code",
    "Red Flag Count",
    "External Event Score",
    "alertcondition",
    "table.new",
]
missing = [token for token in required_tokens if token not in text]
if missing:
    raise SystemExit(f"Missing expected Pine tokens: {missing}")

if text.count("plot(") < 10:
    raise SystemExit("Expected at least 10 screener-compatible plot outputs")

if "request.http" in text:
    raise SystemExit("Pine must not imply unsupported arbitrary HTTP requests")

print(f"Static Pine checks passed for {PINE} ({len(text.splitlines())} lines)")
