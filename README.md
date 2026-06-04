# Long-Term Investment Intelligence Screener

This repository contains a TradingView Pine Script screener designed for long-term stock idea generation. It is a **decision-support tool**, not a blind buy/sell system and not financial advice.

## What the screener does

The Pine indicator calculates two core outputs:

- **Research Score (0-100):** business quality, growth, balance sheet strength, valuation, technical confirmation, and manually reviewed external-event inputs.
- **Buy Intent Score (0-10):** actionability after red flags and hard gates are applied.

The final intent classification is numeric for TradingView screening:

| Intent Code | Classification |
| ---: | --- |
| 6 | Buy Zone |
| 5 | Investable Candidate |
| 4 | Wait for Pullback |
| 3 | Watchlist |
| 2 | Manual Review |
| 1 | Avoid |

## Why external review inputs exist

Pine Script cannot freely call arbitrary live news APIs, SEC filing APIs, funding databases, or geopolitical data providers from inside the chart. Because of that, the indicator includes manual inputs for an outside research workflow:

- External data confidence
- Recent news/catalyst score
- SEC/material filing risk
- Funding/dilution risk
- Geopolitical/sector risk
- Macro backdrop

These inputs let you update the chart decision model after verifying data outside TradingView.

## Files

- `pine/long_term_investment_intelligence_screener.pine` — TradingView Pine v6 indicator.
- `docs/external_verification_workflow.md` — checklist for verifying candidates before investing.

## Suggested workflow

1. Add the Pine script to TradingView.
2. Use TradingView Pine Screener/Data Window columns to sort by Research Score, Buy Intent Score, Intent Code, Red Flag Count, and Data Confidence Code.
3. For any candidate with Intent Code 5 or 6, perform the external verification checklist.
4. Update the external-review inputs in the Pine script settings.
5. Re-check whether the stock remains Buy Zone, Investable, Watchlist, Manual Review, or Avoid.

## Important disclaimer

This project is for research and education. It does not guarantee performance and should not replace professional financial advice, your own due diligence, or risk management.
