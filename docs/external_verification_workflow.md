# External Verification Workflow

Use this checklist before turning any screener candidate into an actual investment decision.

## 1. Data verification gate

Verify that the most important financial values broadly match across at least two independent sources.

Recommended fields:

- Revenue, preferably trailing twelve months and latest fiscal year.
- Net income and EPS.
- Free cash flow.
- Total debt and shareholder equity.
- Current ratio or short-term liquidity.
- Profit margin and return on equity.
- P/E, price-to-sales, and price-to-book where applicable.

If sources disagree materially, set **External data confidence** to `Low` or `Manual Review` in the Pine indicator.

## 2. SEC and company filing gate

For U.S. stocks, review recent filings before trusting a candidate:

- 10-K for annual business quality, risk factors, debt, and segment trends.
- 10-Q for latest quarterly financial condition.
- 8-K for material current events.
- S-1, 424B, or other registration/prospectus filings for offering or dilution risk.
- Form 4 for insider buying or selling context.
- DEF 14A for governance and compensation concerns.

Escalate the indicator's filing risk input when you find unresolved investigations, restatements, going-concern language, major management departures, cyber incidents, customer losses, or legal/regulatory issues.

## 3. Funding and dilution gate

Recent financing can be positive or negative. Classify it before buying.

Positive or neutral examples:

- Strategic financing from a strong partner.
- Debt refinancing at manageable cost.
- Buyback funded by healthy free cash flow.

Negative examples:

- Equity offering after weak cash flow.
- Convertible notes with meaningful dilution potential.
- Distress financing.
- Rising share count without clear shareholder-value creation.

Set **Funding/dilution risk** to `High` or `Severe` when financing appears necessary because of weak operations or liquidity pressure.

## 4. News and catalyst gate

Classify recent company news from the last 30-90 days.

Positive catalysts:

- Earnings beat with raised guidance.
- Major contract win.
- Product approval or launch with credible revenue impact.
- Strategic partnership.
- Credit rating upgrade.
- Insider buying with meaningful size.

Negative catalysts:

- Guidance cut.
- Earnings miss with deteriorating margins.
- SEC/DOJ investigation.
- Product recall.
- CEO/CFO resignation without clear succession.
- Cyber breach.
- Major customer loss.
- Credit downgrade.

Map the result to the Pine input **Recent news/catalyst score** from `-3` to `+3`.

## 5. Geopolitical and sector risk gate

Check whether the company has material exposure to:

- Sanctions, tariffs, export controls, or foreign regulatory pressure.
- Taiwan/China semiconductor risk.
- Russia/Ukraine or Middle East conflict exposure.
- Shipping lane disruption.
- Commodity supply shocks.
- Currency translation risk.
- Emerging-market political instability.
- Sector-specific regulation such as banking, healthcare, defense, big tech, or energy policy.

Set **Geopolitical/sector risk** to `High` or `Severe` when a single geopolitical development could materially impair revenue, margins, assets, or supply chains.

## 6. Macro backdrop gate

Evaluate whether the current macro environment is a tailwind or headwind for the company.

Examples:

- Banks: rates, yield curve, credit losses.
- REITs and utilities: rates and refinancing costs.
- Homebuilders: mortgage rates and housing affordability.
- Energy: oil/gas prices and OPEC/supply shocks.
- Retail: consumer spending, unemployment, credit stress.
- Industrials: PMI, capex cycle, supply chains.

Set **Macro backdrop** accordingly in the Pine settings.

## 7. Final decision discipline

Avoid treating any single output as a final decision. A higher-quality process is:

1. Pine screener finds candidates.
2. External data and filings verify the candidate.
3. News, funding, geopolitical, and macro risks are scored.
4. Pine external inputs are updated.
5. Final intent is reviewed again.
6. Position size and risk plan are decided separately.

The strongest candidates should have strong fundamentals, acceptable valuation, technical confirmation, low red flags, clean recent events, and verified data.
