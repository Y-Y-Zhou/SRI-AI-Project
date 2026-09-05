# 04 Deterministic Financial Tools

## Purpose

This document defines the financial calculation tools used by the SRI
Project Intelligence Assistant.

The AI should retrieve approved inputs from sources, pass inputs into
deterministic calculations, and explain the output. The AI should not
perform authoritative arithmetic itself.

------------------------------------------------------------------------

# Tool 1 --- Gross Potential Rent (GPR)

## Formula

GPR = Units × Monthly Rent × 12

## Inputs

-   Number of units
-   Monthly rent per unit

## Output

-   Annual gross potential rent

------------------------------------------------------------------------

# Tool 2 --- Effective Gross Income (EGI)

## Formula

EGI = Gross Potential Rent × (1 - Vacancy/Loss Rate) + Other Income

## Inputs

-   Gross potential rent
-   Vacancy/collection loss rate
-   Other income

## Output

-   Effective gross income

------------------------------------------------------------------------

# Tool 3 --- Operating Expenses

## Formula

Operating Expenses = Effective Gross Income × Expense Ratio

## Inputs

-   Effective gross income
-   Operating expense ratio

## Output

-   Annual operating expenses

------------------------------------------------------------------------

# Tool 4 --- Net Operating Income (NOI)

## Formula

NOI = Effective Gross Income - Operating Expenses

## Inputs

-   Effective gross income
-   Operating expenses

## Output

-   Net operating income

------------------------------------------------------------------------

# Tool 5 --- DSCR

## Formula

DSCR = NOI / Annual Debt Service

## Inputs

-   NOI
-   Annual debt service

## Output

-   Debt service coverage ratio

------------------------------------------------------------------------

# Tool 6 --- Property Value

## Formula

Property Value = NOI / Capitalization Rate

## Inputs

-   NOI
-   Capitalization rate

## Output

-   Implied property value

------------------------------------------------------------------------

# Tool 7 --- Cost Variance

## Formula

Cost Variance = Actual Cost - Budgeted Cost

Variance Percentage = Cost Variance / Budgeted Cost

## Inputs

-   Budgeted cost
-   Actual cost

## Output

-   Dollar variance
-   Percentage variance

------------------------------------------------------------------------

# Tool 8 --- Remaining Contingency

## Formula

Remaining Contingency = Original Contingency - Used Contingency

## Inputs

-   Original contingency
-   Used contingency

## Output

-   Remaining contingency

------------------------------------------------------------------------

# Tool 9 --- Funding Gap

## Formula

Funding Gap = Required Funding - Available Funding

## Inputs

-   Required funding
-   Available funding

## Output

-   Funding shortfall or surplus

------------------------------------------------------------------------

# Tool 10 --- Cash Flow After Debt Service

## Formula

Cash Flow After Debt Service = NOI - Annual Debt Service

## Inputs

-   NOI
-   Annual debt service

## Output

-   Remaining cash flow

------------------------------------------------------------------------

# Tool 11 --- Equity Multiple

## Formula

Equity Multiple = Total Equity Returned / Total Equity Invested

## Inputs

-   Total equity returned
-   Total equity invested

## Output

-   Equity multiple

------------------------------------------------------------------------

# Pine Ridge Validation Cases

## Case 1 --- NOI Calculation

Inputs:

-   Units: 200
-   Monthly rent: \$2,100
-   Vacancy/loss: 5%
-   Other income: \$30,000
-   Expense ratio: 38%

Expected:

-   GPR: \$5,040,000
-   EGI: \$4,818,000
-   Operating expenses: \$1,830,840
-   NOI: \$2,987,160

------------------------------------------------------------------------

## Case 2 --- DSCR

Inputs:

-   NOI: \$2,987,160
-   Annual debt service: \$2,042,520

Expected:

-   DSCR: approximately 1.46x

------------------------------------------------------------------------

## Case 3 --- Property Value

Inputs:

-   NOI: \$2,987,160
-   Cap rate: 5.25%

Expected:

-   Value: approximately \$56,898,286

------------------------------------------------------------------------

# Testing Requirements

Each calculation must:

-   Accept structured inputs
-   Return deterministic outputs
-   Preserve input sources
-   Be independently testable
-   Return errors for missing required inputs
-   Avoid making assumptions not provided by approved sources
