# 🧠 Delay Discounting – Math & Logic

## What is Delay Discounting?

Delay Discounting (DD) measures how much someone devalues a reward based on how long they have to wait for it. People who are more impulsive tend to prefer smaller, immediate rewards over larger, delayed ones.

## Indifference Average (`Indiff_Avg`)

For each of the 6 delay rounds, the task adjusts the immediate reward value until the participant reaches a point of indifference. Because the task uses an adaptive staircase, the final immediate value (`NOW`) shown in each round is treated as the participant’s indifference point. We calculate `Indiff_Avg` by averaging the final `NOW` values across all 6 delay rounds.

## Discount Rate (`k`)

To quantify discounting, we calculate a `k` value for each delay round using the formula:  
k = (1000 - indiff) / (indiff × delay)

Where:  
- `indiff` is the final NOW value for that delay round  
- `delay` is the number of days  
- 1000 is the fixed delayed reward in each of the 6 rounds. 

We then average the six `k` values across all delay rounds and take the natural log of that average. This log transformation normalizes the distribution of `k`, making the final log-transformed `k` score our key index of impulsivity.

## Summary

| Metric        | What It Captures                            | Interpretation                |
|---------------|----------------------------------------------|--------------------------------|
| `Indiff_Avg`  | Average final NOW values across delays       | Higher = more patient          |
| `k`           | Log of average discount rate across delays   | More negative = less impulsive |
