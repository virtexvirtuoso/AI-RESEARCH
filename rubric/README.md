# Tokenomics rubric

`rubric.yaml` combines the five sources in [`../sources/`](../sources/README.md) into a single scoring rubric. It has 6 dimensions, 19 scored criteria and 5 hard gates. Each criterion lists the sources it comes from. The ones marked `added` cover problems none of the sources mention: low float with high FDV, unlock overhang, and admin-key risk.

```
python rubric/validate.py   # checks weights, threshold direction, IDs, source references
```

## Dimensions

| Dimension | Weight | What it asks |
|-----------|-------:|--------------|
| Utility and value accrual | 0.25 | Is the token necessary, and does revenue reach holders? |
| Supply and emissions | 0.20 | How much supply is still to come, and from new minting? |
| Unlocks and vesting | 0.20 | When do insiders get liquid, and in how big a chunk? |
| Distribution and concentration | 0.15 | Who owns it? |
| Liquidity and market structure | 0.10 | Can holders get out, and is the liquidity real? |
| Governance and control risk | 0.10 | Who can change the rules? |

## Scoring

1. **Criterion (0–1).** Numeric criteria are scored on a straight line from `red` (0) to `good` (1), capped at both ends. Categorical criteria use the score listed for their level.
2. **Dimension.** The weighted mean of the criteria that have data. Criteria without data are left out and the other weights are scaled up to compensate. Coverage is reported.
3. **Total (0–100).** The weighted mean of the dimensions. If overall coverage is below 0.6, the verdict is `INSUFFICIENT_DATA`.
4. **Gates.** If any gate triggers, the verdict is `FAIL` whatever the score. Fraud or broken disclosures are not something a high score elsewhere should average out.

Example: V1 (90-day unlock overhang) has `good: 0.02` and `red: 0.10`. An overhang of 0.06 scores (0.10 − 0.06) / (0.10 − 0.02) = **0.5**.

## Where it disagrees with the sources

- **Vesting length.** S2 says 24 months of insider vesting is "too long". The rubric treats longer as better: 48 months is `good`, 12 is `red`. S2 is writing for investors; this rubric is for holders.
- **Supply cap.** Not scored. The sources disagree, and what a cap actually affects is already covered by float and net issuance.
- **Utility breadth.** Mougayar's 20-point count is replaced by U1 (*necessity*, weight 0.35) and a capped U4 (*breadth*, weight 0.15).
- **Market cap vs FDV.** S4 values tokens on market cap alone. The rubric's float ratio (S1) is 1 / (FDV / market cap).

## Calibration (still to do)

**Every threshold is a prior that hasn't been tested.** Until calibration is done, the score is a structured opinion, not a validated signal. The plan:

1. Choose 15–25 tokens with outcomes clear in hindsight. Include large unlock drawdowns, fair launches, low-float/high-FDV launches, and revenue-sharing tokens. Avoid survivorship bias: include tokens that died.
2. Score each one **as of a past date** using only data available on that date (point-in-time; no look-ahead).
3. Compare scores with forward 6- and 12-month returns relative to BTC/ETH. Report rank correlation and the spread between top and bottom tercile. Don't rely on one example.
4. Adjust thresholds and weights **on one half of the set** and check the result on the other half. A rubric tuned on 20 tokens will overfit if it isn't tested on held-out data.

## Open questions

- **L1 depth thresholds** are the least certain. Order-book depth relative to market cap varies a lot by market-cap tier, and may need to be bucketed by tier.
- **D3** needs labeled holder data to exclude exchanges, bridges and contracts. Without labels, mark it as missing. Don't score raw top-10.
- **S3 (emission sell-through)** will usually be missing unless on-chain flow data is available.
