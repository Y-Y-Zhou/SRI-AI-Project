# Final Integrated Prototype --- SRI Project Intelligence Assistant

## Purpose

This document combines all prototype components into one integrated
system design before rerunning the official 50-question evaluation.

The workflow is:

User Question\
→ Project Identification\
→ Approved Information Retrieval\
→ Role Mode Selection\
→ Financial Calculation (if needed)\
→ Security / Reliability Checks\
→ Structured Final Answer with Citations

------------------------------------------------------------------------

# 1. Information Retrieval Layer

## Function

The assistant retrieves approved information from the Pine Ridge corpus.

The retrieval layer must:

-   Search only approved AI-accessible information
-   Respect project scope
-   Preserve metadata
-   Return source citations
-   Prefer approved/current information

Every answer should maintain:

-   Source ID
-   Source title
-   Section/location
-   Approval status

------------------------------------------------------------------------

# 2. Role-Based Response Layer

The same information is presented differently depending on the user.

## Executive Mode

Focus:

-   Business plan
-   Material deviations
-   Risks
-   Decisions required

Output structure:

1.  Executive summary
2.  Confirmed facts
3.  Key risks
4.  Decision required
5.  Sources
6.  Unknown information

------------------------------------------------------------------------

## Phoenix / Construction Mode

Focus:

-   Budget
-   Schedule
-   Change orders
-   Delivery
-   Turnover

Output structure:

1.  Construction status
2.  Cost impact
3.  Schedule impact
4.  Required handoffs
5.  Sources
6.  Missing information

------------------------------------------------------------------------

## Property / Asset Management Mode

Focus:

-   Occupancy
-   Revenue
-   Expenses
-   NOI
-   Operating performance

Output structure:

1.  Operating result
2.  Performance versus plan
3.  Operational impact
4.  Corrective actions
5.  Sources
6.  Unknown information

------------------------------------------------------------------------

## Finance Mode

Focus:

-   Verified actuals
-   Assumptions versus actuals
-   Financial calculations
-   Controls

Output structure:

1.  Financial answer
2.  Inputs used
3.  Calculation
4.  Verification status
5.  Sources
6.  Missing information

------------------------------------------------------------------------

## Investor Relations Mode

Focus:

-   Approved investor communication
-   Performance explanation
-   Uncertainty disclosure

Output structure:

### 1. Executive Summary

Short communication-ready conclusion.

### 2. Confirmed Facts

Only approved facts with citations.

### 3. Calculated Results

Clearly label calculations.

Format:

Inputs: - Input 1 - Input 2

Method: - Formula used

Output: - Result

### 4. Forecast / Scenario Information

Clearly separate:

-   Base case
-   Downside case
-   Future expectations

Never describe forecasts as actual results.

### 5. What Changed and Why

Explain:

-   Original expectation
-   New information
-   Impact area

### 6. Action Plan

Identify:

-   Responsible department
-   Required action
-   Follow-up

### 7. Remaining Unknowns

Identify:

-   Missing information
-   Required source
-   Responsible owner

------------------------------------------------------------------------

# 3. Deterministic Financial Calculation Engine

## Principle

The AI retrieves inputs but does not perform authoritative financial
calculations itself.

The calculation engine performs:

------------------------------------------------------------------------

## Gross Potential Rent

Formula:

GPR = Units × Monthly Rent × 12

------------------------------------------------------------------------

## Effective Gross Income

Formula:

EGI = GPR × (1 - Vacancy/Loss Rate) + Other Income

------------------------------------------------------------------------

## Operating Expenses

Formula:

Operating Expenses = EGI × Expense Ratio

------------------------------------------------------------------------

## Net Operating Income

Formula:

NOI = EGI - Operating Expenses

------------------------------------------------------------------------

## DSCR

Formula:

DSCR = NOI / Annual Debt Service

------------------------------------------------------------------------

## Property Value

Formula:

Property Value = NOI / Capitalization Rate

------------------------------------------------------------------------

## Cost Variance

Formula:

Dollar Variance = Actual Cost - Budget Cost

Percentage Variance = Dollar Variance / Budget Cost

------------------------------------------------------------------------

## Remaining Contingency

Formula:

Remaining Contingency = Original Contingency - Used Contingency

------------------------------------------------------------------------

## Funding Gap

Formula:

Funding Gap = Required Funding - Available Funding

------------------------------------------------------------------------

## Cash Flow After Debt Service

Formula:

Cash Flow After Debt Service = NOI - Annual Debt Service

------------------------------------------------------------------------

## Equity Multiple

Formula:

Equity Multiple = Total Equity Returned / Total Equity Invested

------------------------------------------------------------------------

# 4. Cross-Department Reasoning Framework

For questions involving multiple departments:

## Step 1 --- Identify Impact Areas

Classify:

-   Construction
-   Operations
-   Finance
-   Investor Relations
-   Legal/Compliance
-   Executive Decision

------------------------------------------------------------------------

## Step 2 --- Identify Ownership

Map:

Issue → Primary Owner → Supporting Departments

Example:

Construction delay:

Primary: Phoenix Construction

Supporting: - Property Management - Asset Management - Finance -
Investor Relations - Executive Leadership

------------------------------------------------------------------------

## Step 3 --- Analyze Department Impact

### Phoenix Construction

Check:

-   Scope
-   Cost
-   Schedule
-   Delivery

### Property / Asset Management

Check:

-   Leasing
-   Occupancy
-   Revenue
-   NOI

### Finance

Check:

-   Cash flow
-   Funding
-   Debt service
-   Reporting

### Investor Relations

Check:

-   Communication requirement
-   Approved interpretation

### Executive Leadership

Check:

-   Decision
-   Escalation
-   Approval

------------------------------------------------------------------------

## Step 4 --- Final Response Structure

Every complex answer should contain:

1.  Summary
2.  Confirmed facts
3.  Department impacts
4.  Financial impact
5.  Required actions
6.  Unknowns/conflicts
7.  Sources

------------------------------------------------------------------------

# 5. Unknown Information Handling

If information is unavailable:

The assistant must:

-   Say unknown
-   Explain missing information
-   Identify required source

The assistant must not:

-   Guess
-   Convert assumptions into facts
-   Present forecasts as actuals

------------------------------------------------------------------------

# 6. Conflict Handling

If sources disagree:

The assistant must:

-   Identify the conflict
-   Preserve both sources
-   Determine source authority/version
-   Avoid silently choosing one answer

------------------------------------------------------------------------

# 7. Security Controls

The assistant refuses requests for:

-   Investor identities
-   Investor contact information
-   SSNs/tax identifiers
-   Bank/wire information
-   Credentials
-   API keys
-   Subscription documents
-   Unapproved legal records
-   Production database contents

------------------------------------------------------------------------

# 8. End-to-End Example

Question:

"What is Pine Ridge's stabilized NOI?"

Process:

1.  Identify Pine Ridge project.
2.  Retrieve approved inputs:
    -   Units
    -   Rent
    -   Vacancy/loss
    -   Other income
    -   Expense ratio
3.  Run deterministic NOI calculation.
4.  Apply user role formatting.
5.  Check security and uncertainty rules.
6.  Return:
    -   NOI result
    -   Inputs
    -   Formula
    -   Source citations
    -   Missing information if applicable

------------------------------------------------------------------------

# 9. Evaluation Readiness

This prototype is designed to be tested against:

-   Retrieval accuracy
-   Citation accuracy
-   Financial calculation accuracy
-   Role-based reasoning
-   Unknown handling
-   Conflict handling
-   Security refusal behavior

The official 50-question evaluation should be run only after this
integrated prototype is finalized.
