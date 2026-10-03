# Sources

Notes on the material originally clipped into `tokenomics overview` (commit `7f0a190`). This repo is public, so the copied article text has been replaced with summaries and attribution. The original clip is still in git history.

Each source has an ID (`S1`–`S5`) that `rubric/rubric.yaml` uses in its `sources:` fields.

| ID | Title | Author / publisher | Date | URL | Reliability |
|----|-------|--------------------|------|-----|-------------|
| S0 | Untitled summary of factors (lines 1–9 of the clip) | Unknown; looks like an AI summary of S5 | ~2023 | — | Low: derived, adds nothing new |
| S1 | *Tokenomics — A Business Guide to Token Usage, Utility and Value* | William Mougayar (Medium) | 2017 | URL not captured, still needs one | Medium: original framework, but written for ICOs |
| S2 | *What Are Good and Bad Project Tokenomics* | DAOLaunch (HackerNoon) | 2022-02-14 | [hackernoon.com](https://hackernoon.com/what-are-good-and-bad-project-tokenomics) | Low: a launchpad marketing itself; the numbers contain an error |
| S3 | *Tokenomics: 4 Crucial Factors to Consider* (explainer) | Unknown | ~2022 | Not captured | Low–medium: introductory |
| S4 | *Tokenomics: How to Value Crypto the Right Way [2023]* | Unknown | 2023 | Not captured | Low: contains factual errors |
| S5 | *100 questions you should ask yourself when analyzing tokenomics* | Unknown; originally a Twitter thread | ~2022 | Not captured | Medium: the most thorough source, but only questions with no thresholds |

## S1: Mougayar, token utility framework

- Defines a token as a privately issued unit of value that an organization uses to run its business model and share rewards with its stakeholders.
- Main argument: how the token is **used** matters more than how the sale is engineered. "Usage without value linkage is a waste."
- **Six token roles:** Right (access, governance, ownership-like claims), Value Exchange (earning and spending inside the ecosystem), Toll (pay-per-use, security deposits, gas), Function (onboarding, incentives), Currency (internal payment rail), Earnings (profit or benefit sharing).
- **20-question checklist**, one point per "yes". The author says a high score is *necessary but not sufficient*.
- **Limitation:** it scores how *many* uses a token has, not whether those uses create demand that can't be met some other way. A token can tick many boxes and still be unnecessary.

## S2: DAOLaunch, good / bad / ugly case studies

- Topics covered: vesting, product-market fit, the team and its backers, checking that audits are real (look the project up on the auditor's own site).
- **Case A ("good"):** userbase 27%, ecosystem 33%, dev team 33%, private 10%, community 5%, treasury 10%, legal/advisors 2%. **These add up to 120%.** Either the categories overlap or the source is wrong, so don't use it as a reference distribution. Public vesting is 20% at TGE then 20% per month; private cliffs are 9–16 months.
- **Case B ("bad"):** seed + private = 19% versus a 2% public allocation. Insider vesting is a 3-month cliff then 24 months linear, which the author calls *too long*.
- **Case C ("ugly"):** allocations split into needlessly many lines; public sale 67% unlocked at TGE with 1-month vesting, on a 0.83% allocation.
- **Bias:** an IDO launchpad writing about IDO structures. It recommends 12–20-month vesting for VCs because 24 months is "too long" for investors. That is the investor's point of view, not the token holder's. The rubric does not follow it.

## S3: introductory explainer

- Four factors: **utility, supply and price-stability mechanisms, distribution, governance**.
- Supply: a cap is not automatically good. ETH has no cap because issuance pays validators, while BTC has a cap and a halving schedule. Supply can be controlled through issuance limits and through burns, buybacks or halvings.
- Distribution examples: the ETH crowdsale (60M of 72M ETH, about 83%, to buyers), BTC's fair launch (Satoshi's ~1.1M BTC never moved), and UNI's genesis split (15% airdrop, 2% liquidity mining, 43% treasury, 21.51% team, 17.8% investors, 0.69% advisors; 4-year vesting except the airdrop and liquidity mining). The UNI figures add up to 100%.
- Governance: how centralized it is, on-chain or off-chain, how hard it is to make a proposal, quorum, and the team's background.

## S4: "How to Value Crypto" (2023)

- Covers the three supply definitions (circulating, total, max), market cap = price × circulating supply, consensus mechanism, utility, distribution, burns.
- **Factual errors:**
  - It says "Most new projects prefer an environmentally friendly mechanism, so **PoW** has gained high popularity". This should say PoS.
  - It credits "tokenomics" to B.F. Skinner in 1972. The behavioral-psychology "token economy" is usually traced to Ayllon & Azrin (1968). The Skinner attribution has no support.
  - It says BNB has burned "over 150,000 BNB". By 2023 the actual figure was in the tens of millions, so this is off by orders of magnitude.
- It uses market cap only, never FDV, so it misses dilution entirely. **Not used for any threshold.**

## S5: 100-question checklist

- Sections: General, Token launch, Supply, Demand, Token utility, Past performance, Bear-market and current questions.
- Questions S0–S4 don't cover, all of them useful for the rubric:
  - FDV at launch, and market cap ÷ FDV over time (Q23–24)
  - top-10 and top-100 holder share (Q29–30); unlock timing (Q31); who receives emissions and whether they sell (Q36–37)
  - whether cash flows are **dilutive or redistributive** (Q64); how concentrated governance votes are (Q67); minimum tokens needed to make a proposal (Q69)
  - token velocity = transaction volume ÷ market cap (Q79); liquidity depth and whether everyone can exit at once (Q9, Q86–87)
  - "Can the project function without a token?" (Q17), the most important single question for utility
- **Transcription problems in the clip:** Q1–17 have no numbers, Q44 is garbled (`44Ath th jt il btittt?`), Q78 is missing, and several questions are run together on one line.

## Clean-up applied

- 40 NUL bytes removed. They made git treat the file as binary.
- Where the PDF extraction dropped the "fi" and "fl" letter pairs, the summaries above restore them ("denition" → "definition", "specic" → "specific", "t" → "fit").
- The verbatim text is replaced by these notes. Recover it with `git show 7f0a190:"tokenomics overview"`.
