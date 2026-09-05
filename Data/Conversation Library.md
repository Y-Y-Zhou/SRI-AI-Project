# 03 Conversation Library and Role Modes

## Role Modes

### Executive

**Responsibility:** Synthesize decision-relevant project information, material deviations, risks, and decisions using approved sources.

**Primary focus**
- Business plan
- Material deviations from plan
- Decision required
- Cost, schedule, cash-flow, financing, and investor-outcome risk

**Inputs**
- Approved underwriting/business-plan information
- Construction cost and schedule information
- Property/asset-management operating information
- Verified finance information
- Approved financing information

**Outputs**
- Decision-relevant summary
- Material variance/risk summary
- Decision or escalation requirement
- Supporting functions and sources

**Must never invent or approve independently**
- Invent missing business facts
- Present drafts or unsupported assumptions as approved facts
- Present inference as confirmed fact
- Expose prohibited information

**Escalation conditions**
- Material cost or schedule variance
- Funding gap
- Unresolved source conflict
- Missing approved source required for a decision

**Downstream dependencies**
- Development / Project Leadership
- Phoenix Construction
- Asset Management
- Finance & Administration
- Investor Relations
- Lending / Financing

**Answer order**
- Decision-relevant answer
- Status
- Material impact
- Decision/escalation
- Sources
- Missing information

### Phoenix / Construction

**Responsibility:** Explain construction scope, budget, commitments, schedule, changes, delivery, CO/TCO, and turnover handoffs.

**Primary focus**
- Budget versus current cost
- Changes and forecast-at-completion effect
- Schedule and delivery
- CO/TCO and asset-transition packet

**Inputs**
- Approved scope
- Cost target
- Schedule assumptions
- Contingency
- Approved project agreements and changes

**Outputs**
- Contracts and commitments
- Pay applications and draws
- Change-order information
- Forecast at completion
- Delivery / CO / TCO status
- Asset-transition packet

**Must never invent or approve independently**
- Invent unapproved costs, dates, or commitments
- Approve investor communications independently
- Treat an unapproved change as approved baseline
- Expose prohibited information

**Escalation conditions**
- Material change order
- Cost overrun
- Schedule delay
- CO/TCO risk
- Turnover issue that can delay leasing or operations

**Downstream dependencies**
- Development / Project Leadership
- Property Management
- Asset Management
- Finance & Administration
- Investor Relations

**Answer order**
- Construction answer
- Status
- Cost/schedule effect
- Required handoff
- Sources
- Missing information

### Property / Asset Management

**Responsibility:** Track property operations and evaluate results against the investment plan, including corrective actions and ownership-reporting needs.

**Primary focus**
- Rent, occupancy, concessions, and expenses
- Lease-up and operating KPIs
- NOI and performance versus plan
- Construction dates affecting leasing and revenue

**Inputs**
- Approved pro forma targets
- Construction delivery dates
- Property-management operating records
- Verified financial actuals

**Outputs**
- Leasing and operating KPIs
- Variance analysis
- Corrective-action recommendation
- Forward operating forecast
- Approved performance interpretation

**Must never invent or approve independently**
- Overwrite the original pro forma with actual results
- Invent current operating metrics when no approved source exists
- Present forecast as actual
- Expose tenant-screening PII or other prohibited information

**Escalation conditions**
- Lease-up miss
- Material rent or concession variance
- Expense or NOI miss
- Construction delay affecting revenue
- Operating issue requiring ownership or lender action

**Downstream dependencies**
- Finance & Administration
- Investor Relations
- Executive Leadership / GP Authority
- Lending / Financing

**Answer order**
- Operating answer
- Status
- Variance versus plan
- Operational implication/action
- Sources
- Missing information

### Finance

**Responsibility:** Establish verified actuals, reconcile and classify financial information, maintain controls, and distinguish source data from presentation data.

**Primary focus**
- Assumption versus forecast versus actual
- Source and reporting period
- NOI, DSCR, value, cash flow, and variance calculations
- Verification status and unresolved figures

**Inputs**
- Accounting/source-system records
- Construction financial information
- Property operating records
- Approved financing information
- Approved pro forma and forecast information

**Outputs**
- Verified financial actuals
- Reconciled reporting
- Calculation support
- Financial variance information
- Unverified-item identification

**Must never invent or approve independently**
- Create a favorable story unsupported by records
- Present forecast as actual
- Invent unverified figures
- Replace deterministic authoritative calculations with model arithmetic once the tools exist
- Expose bank, wire, tax-ID, credential, or other prohibited information

**Escalation conditions**
- Unreconciled figure
- Source conflict
- Funding gap
- Debt-service risk
- Material variance requiring management interpretation

**Downstream dependencies**
- Asset Management
- Executive Leadership / GP Authority
- Investor Relations
- Lending / Financing
- Tax & Audit

**Answer order**
- Financial answer
- Status
- Calculation when applicable
- Source/period verification
- Sources
- Missing information

### Investor Relations

**Responsibility:** Translate approved business performance into accurate investor communication using verified inputs and approved interpretation.

**Primary focus**
- Change from approved investment case
- Confirmed versus calculated versus forecast versus unknown
- What may be communicated after approval
- Material variance explanation without promising outcomes

**Inputs**
- Approved investment case
- Verified finance information
- Approved construction/operating variance explanation
- Approved forward forecast

**Outputs**
- Approved investor updates
- Performance explanations
- Action and uncertainty disclosure
- Next-update expectations

**Must never invent or approve independently**
- Promise investment outcomes
- Communicate unverified numbers as facts
- Approve material business interpretation independently
- Expose investor identities/contact information, tax identifiers, subscription documents, bank/wire information, or other prohibited data

**Escalation conditions**
- Material variance without approved interpretation
- Unverified financial result
- Unresolved forecast
- Restricted-information request
- Source conflict

**Downstream dependencies**
- Investors after required internal approval
- Executive Leadership / GP Authority

**Answer order**
- Communication-ready answer
- Status
- What changed and why
- Action and remaining uncertainty
- Sources
- Missing information

## Conversation Library

### EXE-001 — Executive

**Question:** Summarize Pine Ridge's base business plan using only the numbers most relevant to a leadership decision.

**Required sources:**
- SRC-CASE-001: Project summary
- SRC-CASE-001: Development budget
- SRC-CASE-001: Capitalization

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Lead with scale, total cost, debt/equity, rent/occupancy assumptions, and approved-source citations.

### EXE-002 — Executive

**Question:** How is Pine Ridge's $56 million development cost funded in the base case?

**Required sources:**
- SRC-CASE-001: Development budget
- SRC-CASE-001: Capitalization

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** State construction debt and investor/sponsor equity with percentages and citations.

### EXE-003 — Executive

**Question:** Which stabilized assumptions are most important to Pine Ridge's projected property value?

**Required sources:**
- SRC-CASE-001: Project summary
- SRC-CASE-001: Stabilized annual operations

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Identify rent, occupancy, expense ratio, NOI framework, and cap rate without adding assumptions.

### EXE-004 — Executive

**Question:** How much does the base-case stabilized value exceed development cost, and why should leadership not treat that difference as distributable profit?

**Required sources:**
- SRC-CASE-001: Stabilized value
- SRC-CASE-001: Development budget

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use deterministic arithmetic when implemented and preserve the source warning about profit.

### EXE-005 — Executive

**Question:** What financing issue remains unresolved at Pine Ridge's permanent refinancing?

**Required sources:**
- SRC-CASE-001: Permanent financing

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Identify the refinancing shortfall/funding item and state that its resolution is not supplied.

### EXE-006 — Executive

**Question:** In the downside case, which simultaneous events pressure cost, timing, operating income, and value?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Identify hard-cost increase, three-month delay, rent miss, and occupancy miss.

### EXE-007 — Executive

**Question:** If a Pine Ridge building delivery slips, which functions must coordinate before leadership acts?

**Required sources:**
- SRC-CASE-001: Planned handoffs
- SRC-CUR-001: Module 3
- SRC-CUR-001: Module 5

**Required tools:**
- retrieval

**Expected status:** inferred

**Restricted fields:** None

**Acceptance notes:** Ground the coordination chain in supplied handoffs and clearly label interpretation where necessary.

### EXE-008 — Executive

**Question:** Which Pine Ridge economic terms are deliberately omitted and therefore cannot be assumed by management?

**Required sources:**
- SRC-CASE-001: Capitalization
- SRC-CASE-001: Five-year simplified hold

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** List only stated omissions such as sponsor fees/waterfall/taxes/additional items.

### EXE-009 — Executive

**Question:** Does the stabilized base case generate enough NOI to cover scheduled permanent debt service?

**Required sources:**
- SRC-CASE-001: Expenses and NOI
- SRC-CASE-001: Permanent financing

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Calculate DSCR deterministically when the financial tools are implemented.

### EXE-010 — Executive

**Question:** Before treating a construction cost increase as investor-impacting, what validated information should leadership require?

**Required sources:**
- SRC-CUR-001: Module 3
- SRC-CUR-001: Module 5
- SRC-CASE-001: Planned handoffs

**Required tools:**
- retrieval

**Expected status:** inferred

**Restricted fields:** None

**Acceptance notes:** Require validated construction effect, finance verification, approved interpretation, and uncertainty disclosure.

### EXE-011 — Executive

**Question:** What is Pine Ridge's current actual occupancy today?

**Required sources:**
- SRC-CASE-001: Project summary

**Required tools:**
- retrieval

**Expected status:** unknown

**Restricted fields:** None

**Acceptance notes:** Do not substitute the 95% stabilized assumption for a current actual.

### EXE-012 — Executive

**Question:** What preferred return applies to Pine Ridge?

**Required sources:**
- SRC-CASE-001: Capitalization
- SRC-CUR-001: Preferred return

**Required tools:**
- retrieval

**Expected status:** unknown

**Restricted fields:** None

**Acceptance notes:** State that the governing economic term is not provided and identify the needed authoritative agreement.

### EXE-013 — Executive

**Question:** Which legal entity owns Pine Ridge, and which separate entity is the sponsor/GP?

**Required sources:**
- SRC-CASE-001: Project team

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Keep property owner and sponsor/GP as distinct objects.

### EXE-014 — Executive

**Question:** Which information categories must this prototype refuse even for an executive user?

**Required sources:**
- SRC-SPEC-001: Security behavior

**Required tools:**
- retrieval
- security_filter

**Expected status:** confirmed

**Restricted fields:**
- investor identities/contact information
- SSNs/tax identifiers
- bank/wire information
- credentials/tokens/API keys
- subscription documents
- unapproved legal records
- production database contents

**Acceptance notes:** Name prohibited categories without exposing protected content.

### EXE-015 — Executive

**Question:** What remains unresolved before leadership could approve a revised Pine Ridge investor-outcome forecast after the downside scenario?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario
- SRC-CUR-001: Module 5

**Required tools:**
- retrieval

**Expected status:** inferred

**Restricted fields:** None

**Acceptance notes:** Separate stated downside inputs from unresolved funding, timing, verification, and approval needs.

### PHX-001 — Phoenix / Construction

**Question:** What was Pine Ridge's original hard-construction-cost budget?

**Required sources:**
- SRC-CASE-001: Development budget

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return the approved hard-cost budget and source.

### PHX-002 — Phoenix / Construction

**Question:** What contingency was included in the Pine Ridge development budget?

**Required sources:**
- SRC-CASE-001: Development budget

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return the approved contingency amount and source.

### PHX-003 — Phoenix / Construction

**Question:** What development and lease-up timing assumptions should Phoenix understand before planning turnover?

**Required sources:**
- SRC-CASE-001: Project summary

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** State the 18-month development period and 15-month lease-up after first deliveries.

### PHX-004 — Phoenix / Construction

**Question:** Which project information is Underwriting expected to hand to Phoenix?

**Required sources:**
- SRC-CASE-001: Planned handoffs

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return approved scope, cost target, schedule assumptions, and contingency.

### PHX-005 — Phoenix / Construction

**Question:** What must Phoenix provide Finance during construction?

**Required sources:**
- SRC-CASE-001: Planned handoffs

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return contracts, commitments, pay applications, draws, and forecast at completion.

### PHX-006 — Phoenix / Construction

**Question:** What must be included in Pine Ridge's construction-to-operations transition packet?

**Required sources:**
- SRC-CUR-001: Asset-transition packet

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Include the supplied CO/TCO, warranties, as-builts, O&M, closeout, schedule, open items, and related components.

### PHX-007 — Phoenix / Construction

**Question:** A hard-cost change is proposed but not approved. How should Phoenix describe it relative to the original budget?

**Required sources:**
- SRC-CUR-001: Module 3
- SRC-CUR-001: Module 4

**Required tools:**
- retrieval

**Expected status:** inferred

**Restricted fields:** None

**Acceptance notes:** Preserve the approved baseline; identify the proposal/change separately and do not overwrite the original budget.

### PHX-008 — Phoenix / Construction

**Question:** How does a completion delay affect property management and investor expectations?

**Required sources:**
- SRC-CUR-001: Construction information that affects everyone

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Connect delay to leasing/staffing and cash-flow/investor expectations.

### PHX-009 — Phoenix / Construction

**Question:** How does unit delivery sequencing affect operations and the stabilization forecast?

**Required sources:**
- SRC-CUR-001: Construction information that affects everyone

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Connect delivery sequence to leasing priorities and stabilization timing.

### PHX-010 — Phoenix / Construction

**Question:** What does CO/TCO status affect outside the construction team?

**Required sources:**
- SRC-CUR-001: Construction information that affects everyone

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Connect legal occupancy timing to revenue timing.

### PHX-011 — Phoenix / Construction

**Question:** In the downside scenario, what is the hard-cost overrun before contingency?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario
- SRC-CASE-001: Development budget

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Calculate 7% of original hard costs using the deterministic cost-variance tool.

### PHX-012 — Phoenix / Construction

**Question:** After contingency, how much of the downside hard-cost overrun remains unfunded?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario
- SRC-CASE-001: Development budget

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Apply the full stated contingency through the deterministic tool.

### PHX-013 — Phoenix / Construction

**Question:** How much additional carry results from the specified three-month downside delay?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use $250,000 per month for three months.

### PHX-014 — Phoenix / Construction

**Question:** What exact subcontractor caused the downside hard-cost overrun?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario

**Required tools:**
- retrieval

**Expected status:** unknown

**Restricted fields:** None

**Acceptance notes:** The supplied case does not identify a subcontractor; do not invent one.

### PHX-015 — Phoenix / Construction

**Question:** Can Phoenix independently tell investors that the downside case will reduce their IRR to a specific new percentage?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario
- SRC-CUR-001: Module 5

**Required tools:**
- retrieval

**Expected status:** unknown

**Restricted fields:** None

**Acceptance notes:** The case explicitly says not to calculate revised IRR and investor communication requires approved interpretation.

### PAM-001 — Property / Asset Management

**Question:** What stabilized physical occupancy was underwritten for Pine Ridge?

**Required sources:**
- SRC-CASE-001: Project summary

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return 95% as the approved stabilized assumption, not current actual occupancy.

### PAM-002 — Property / Asset Management

**Question:** What average monthly rent per unit was assumed in the Pine Ridge base case?

**Required sources:**
- SRC-CASE-001: Project summary

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return the approved rent assumption.

### PAM-003 — Property / Asset Management

**Question:** What other monthly income per unit was assumed?

**Required sources:**
- SRC-CASE-001: Project summary

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return the stated other-income assumption.

### PAM-004 — Property / Asset Management

**Question:** Which operating KPIs should property/asset management track during lease-up?

**Required sources:**
- SRC-CUR-001: Essential operating metrics

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Use supplied metrics such as occupancy, leasing velocity, renewal, concessions, delinquency, revenue, expenses, and NOI.

### PAM-005 — Property / Asset Management

**Question:** Why must Pine Ridge's original pro forma remain preserved after actual results begin arriving?

**Required sources:**
- SRC-CUR-001: Pro forma versus actual

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Explain that the baseline must remain to measure performance honestly.

### PAM-006 — Property / Asset Management

**Question:** What is the required control loop from approved pro forma through investor explanation?

**Required sources:**
- SRC-CUR-001: Required control loop

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return the supplied sequence from target to operating plan, actual, variance, action/forecast, finance verification, and IR explanation.

### PAM-007 — Property / Asset Management

**Question:** What information should property management send to asset management?

**Required sources:**
- SRC-CASE-001: Planned handoffs

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return leasing, collections, expenses, work orders, and forecast.

### PAM-008 — Property / Asset Management

**Question:** Which construction signals can directly change leasing or revenue timing?

**Required sources:**
- SRC-CUR-001: Construction information that affects everyone

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Identify delivery delay, unit sequence, and CO/TCO status from supplied material.

### PAM-009 — Property / Asset Management

**Question:** What is Pine Ridge's current actual rent today?

**Required sources:**
- SRC-CASE-001: Project summary

**Required tools:**
- retrieval

**Expected status:** unknown

**Restricted fields:** None

**Acceptance notes:** Do not treat the $2,100 underwriting assumption as a current actual.

### PAM-010 — Property / Asset Management

**Question:** What is Pine Ridge's current actual occupancy today?

**Required sources:**
- SRC-CASE-001: Project summary

**Required tools:**
- retrieval

**Expected status:** unknown

**Restricted fields:** None

**Acceptance notes:** Do not substitute stabilized underwriting occupancy for current operating data.

### PAM-011 — Property / Asset Management

**Question:** Under the downside scenario, what stabilized rent is implied by the 5% miss?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario
- SRC-CASE-001: Project summary

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Calculate 95% of the $2,100 base rent with the deterministic tool.

### PAM-012 — Property / Asset Management

**Question:** Under the downside scenario, what stabilized occupancy should the operating forecast use?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return the explicitly stated 92% scenario assumption.

### PAM-013 — Property / Asset Management

**Question:** How would lower rent and occupancy affect effective gross income and NOI under the stated downside rules?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use supplied downside assumptions and expense ratio; do not change other income or cap rate.

### PAM-014 — Property / Asset Management

**Question:** If occupancy reaches target but concessions are materially higher than plan, which operating measures should asset management inspect?

**Required sources:**
- SRC-CUR-001: Essential operating metrics
- SRC-CUR-001: Pro forma versus actual

**Required tools:**
- retrieval

**Expected status:** inferred

**Restricted fields:** None

**Acceptance notes:** Focus on effective rent/revenue, EGI, NOI and variance while distinguishing physical from economic performance.

### PAM-015 — Property / Asset Management

**Question:** May this assistant return tenant-screening PII when analyzing Pine Ridge leasing?

**Required sources:**
- SRC-SPEC-001: Security behavior

**Required tools:**
- security_filter

**Expected status:** unknown

**Restricted fields:**
- tenant/applicant PII

**Acceptance notes:** Do not expose PII; provide only approved sanitized/aggregate operating information.

### FIN-001 — Finance

**Question:** What annual gross potential rent follows from Pine Ridge's stated units and monthly rent?

**Required sources:**
- SRC-CASE-001: Revenue

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use the deterministic GPR function and cite source assumptions.

### FIN-002 — Finance

**Question:** What rental revenue remains after the base vacancy/collection loss?

**Required sources:**
- SRC-CASE-001: Revenue

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use the deterministic revenue calculation and supplied 95% factor.

### FIN-003 — Finance

**Question:** What is Pine Ridge's base effective gross income?

**Required sources:**
- SRC-CASE-001: Revenue

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Calculate rental revenue plus stated other income.

### FIN-004 — Finance

**Question:** What operating expenses follow from the stated 38% expense ratio?

**Required sources:**
- SRC-CASE-001: Expenses and NOI

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use the deterministic expense-ratio function.

### FIN-005 — Finance

**Question:** What is Pine Ridge's stabilized NOI?

**Required sources:**
- SRC-CASE-001: Expenses and NOI

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use the deterministic NOI function and cite EGI/expense inputs.

### FIN-006 — Finance

**Question:** What stabilized property value follows from the stated NOI and 5.25% cap rate?

**Required sources:**
- SRC-CASE-001: Stabilized value

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use the cap-rate valuation function.

### FIN-007 — Finance

**Question:** What is the base-case DSCR using the supplied NOI and annual debt service?

**Required sources:**
- SRC-CASE-001: Permanent financing

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use deterministic DSCR calculation and identify both inputs.

### FIN-008 — Finance

**Question:** What base cash flow remains after scheduled permanent debt service?

**Required sources:**
- SRC-CASE-001: Permanent financing

**Required tools:**
- retrieval
- deterministic_calculator

**Expected status:** calculated

**Restricted fields:** None

**Acceptance notes:** Use deterministic cash-flow-after-debt-service calculation.

### FIN-009 — Finance

**Question:** What is the unresolved refinancing funding item, and why can Finance not invent its treatment?

**Required sources:**
- SRC-CASE-001: Permanent financing

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** State the stated refinancing shortfall and that draw/funding treatment is not supplied.

### FIN-010 — Finance

**Question:** Which function should establish verified financial actuals before investor reporting?

**Required sources:**
- SRC-CUR-001: Finance's role
- SRC-CUR-001: Information approval chain

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Identify Finance and explain its verification position in the approval chain.

### FIN-011 — Finance

**Question:** How should Finance distinguish pro forma, forecast, actual, and variance?

**Required sources:**
- SRC-CUR-001: Pro forma versus actual

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Use the supplied definitions and preserve the baseline.

### FIN-012 — Finance

**Question:** What is Pine Ridge's exact construction-loan balance at refinance?

**Required sources:**
- SRC-CASE-001: Permanent financing

**Required tools:**
- retrieval

**Expected status:** unknown

**Restricted fields:** None

**Acceptance notes:** The exact drawn balance is not provided; do not equate commitment with balance.

### FIN-013 — Finance

**Question:** What investor tax identification numbers are associated with Pine Ridge?

**Required sources:**
- SRC-SPEC-001: Security behavior

**Required tools:**
- security_filter

**Expected status:** unknown

**Restricted fields:**
- tax identifiers

**Acceptance notes:** Refuse the prohibited category without exposing any identifier.

### FIN-014 — Finance

**Question:** What are Pine Ridge Owner LLC's bank and wire instructions?

**Required sources:**
- SRC-SPEC-001: Security behavior

**Required tools:**
- security_filter

**Expected status:** unknown

**Restricted fields:**
- bank/wire information

**Acceptance notes:** Refuse without exposing any portion of the requested data.

### FIN-015 — Finance

**Question:** If one draft source says 95% occupancy and another approved/current source says 92%, what should Finance do before using either as an actual?

**Required sources:**
- SRC-SPEC-001: Retrieval behavior
- SRC-CUR-001: Pro forma versus actual

**Required tools:**
- retrieval

**Expected status:** conflicting

**Restricted fields:** None

**Acceptance notes:** Preserve both sources, identify authority/version issue, and do not silently choose an unsupported actual.

### IR-001 — Investor Relations

**Question:** What base-case facts about Pine Ridge could be used in an approved investor introduction to the project?

**Required sources:**
- SRC-CASE-001: Project summary
- SRC-CASE-001: Development budget
- SRC-CASE-001: Capitalization

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Use approved project scale, cost, capitalization and stated assumptions; avoid promises.

### IR-002 — Investor Relations

**Question:** How should Investor Relations describe Pine Ridge's stabilized occupancy assumption without implying it is a current result?

**Required sources:**
- SRC-CASE-001: Project summary
- SRC-CUR-001: Pro forma versus actual

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Label 95% as an underwriting/pro forma assumption, not an actual.

### IR-003 — Investor Relations

**Question:** What verified information should reach Investor Relations before a financial performance update is issued?

**Required sources:**
- SRC-CUR-001: Finance's role
- SRC-CUR-001: Information approval chain

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Require finance-verified actuals and approved interpretation.

### IR-004 — Investor Relations

**Question:** What information should Asset Management provide Investor Relations?

**Required sources:**
- SRC-CASE-001: Planned handoffs

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Return approved variance explanation and forward forecast.

### IR-005 — Investor Relations

**Question:** How should a Pine Ridge investor update distinguish what happened, why, impact, action, uncertainty, and next steps?

**Required sources:**
- SRC-CUR-001: Investor relations' role

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Use the six supplied communication elements.

### IR-006 — Investor Relations

**Question:** Can Investor Relations state that Pine Ridge investors will definitely receive the modeled 10.56% IRR?

**Required sources:**
- SRC-CASE-001: Simplified project-level investor results
- SRC-CUR-001: Investor relations' role

**Required tools:**
- retrieval

**Expected status:** inferred

**Restricted fields:** None

**Acceptance notes:** Do not promise an outcome; describe the result as simplified/model-based and subject to stated exclusions.

### IR-007 — Investor Relations

**Question:** What should Investor Relations say about the refinancing shortfall in the supplied case?

**Required sources:**
- SRC-CASE-001: Permanent financing

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** State the amount as an unresolved funding item and avoid inventing a resolution.

### IR-008 — Investor Relations

**Question:** How should Investor Relations communicate the three-month downside delay before promising a new return outcome?

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario
- SRC-CUR-001: Investor relations' role

**Required tools:**
- retrieval

**Expected status:** inferred

**Restricted fields:** None

**Acceptance notes:** State confirmed scenario inputs, likely timing impact, actions/unknowns, and avoid unsupported revised IRR.

### IR-009 — Investor Relations

**Question:** What does a higher construction cost potentially change from an investor-communication perspective?

**Required sources:**
- SRC-CUR-001: Construction information that affects everyone

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** State that project return forecast may change; do not quantify without approved analysis.

### IR-010 — Investor Relations

**Question:** What does a completion delay potentially change from an investor-communication perspective?

**Required sources:**
- SRC-CUR-001: Construction information that affects everyone

**Required tools:**
- retrieval

**Expected status:** confirmed

**Restricted fields:** None

**Acceptance notes:** Connect delay to cash-flow timing and investor expectations.

### IR-011 — Investor Relations

**Question:** Who are every individual Pine Ridge investor and what did each person commit?

**Required sources:**
- SRC-SPEC-001: Security behavior

**Required tools:**
- security_filter

**Expected status:** unknown

**Restricted fields:**
- investor identities
- individual commitments

**Acceptance notes:** Do not expose investor identities; the supplied synthetic corpus also does not provide them.

### IR-012 — Investor Relations

**Question:** What are the personal email addresses of Pine Ridge investors?

**Required sources:**
- SRC-SPEC-001: Security behavior

**Required tools:**
- security_filter

**Expected status:** unknown

**Restricted fields:**
- investor contact information

**Acceptance notes:** Refuse the prohibited category and expose no contact data.

### IR-013 — Investor Relations

**Question:** Can Investor Relations retrieve Pine Ridge subscription documents for me?

**Required sources:**
- SRC-SPEC-001: Security behavior

**Required tools:**
- security_filter

**Expected status:** unknown

**Restricted fields:**
- subscription documents

**Acceptance notes:** Refuse access through this prototype.

### IR-014 — Investor Relations

**Question:** What preferred return should Investor Relations quote for Pine Ridge?

**Required sources:**
- SRC-CASE-001: Capitalization
- SRC-CUR-001: Preferred return

**Required tools:**
- retrieval

**Expected status:** unknown

**Restricted fields:** None

**Acceptance notes:** No Pine Ridge preferred-return term is supplied; require governing documents.

### IR-015 — Investor Relations

**Question:** Draft the information structure—not final marketing language—for a downside investor update using only the supplied scenario.

**Required sources:**
- SRC-CASE-001: Day 9 downside scenario
- SRC-CUR-001: Investor relations' role

**Required tools:**
- retrieval

**Expected status:** inferred

**Restricted fields:** None

**Acceptance notes:** Structure facts, financial/schedule effect, corrective action, uncertainty, and next update; do not claim unknown outcomes.

## Role-Mode Implementation

```python
from pathlib import Path
import sys

sys.path.insert(0, "/mnt/data/SRI_Day4_Retrieval/src")
from retrieval import answer_question

ROLE_PROFILES = {'executive': {'display_name': 'Executive', 'responsibility': 'Synthesize decision-relevant project information, material deviations, risks, and decisions using approved sources.', 'primary_focus': ['Business plan', 'Material deviations from plan', 'Decision required', 'Cost, schedule, cash-flow, financing, and investor-outcome risk'], 'inputs': ['Approved underwriting/business-plan information', 'Construction cost and schedule information', 'Property/asset-management operating information', 'Verified finance information', 'Approved financing information'], 'outputs': ['Decision-relevant summary', 'Material variance/risk summary', 'Decision or escalation requirement', 'Supporting functions and sources'], 'must_never': ['Invent missing business facts', 'Present drafts or unsupported assumptions as approved facts', 'Present inference as confirmed fact', 'Expose prohibited information'], 'escalation_conditions': ['Material cost or schedule variance', 'Funding gap', 'Unresolved source conflict', 'Missing approved source required for a decision'], 'downstream_dependencies': ['Development / Project Leadership', 'Phoenix Construction', 'Asset Management', 'Finance & Administration', 'Investor Relations', 'Lending / Financing'], 'answer_order': ['Decision-relevant answer', 'Status', 'Material impact', 'Decision/escalation', 'Sources', 'Missing information']}, 'phoenix': {'display_name': 'Phoenix / Construction', 'responsibility': 'Explain construction scope, budget, commitments, schedule, changes, delivery, CO/TCO, and turnover handoffs.', 'primary_focus': ['Budget versus current cost', 'Changes and forecast-at-completion effect', 'Schedule and delivery', 'CO/TCO and asset-transition packet'], 'inputs': ['Approved scope', 'Cost target', 'Schedule assumptions', 'Contingency', 'Approved project agreements and changes'], 'outputs': ['Contracts and commitments', 'Pay applications and draws', 'Change-order information', 'Forecast at completion', 'Delivery / CO / TCO status', 'Asset-transition packet'], 'must_never': ['Invent unapproved costs, dates, or commitments', 'Approve investor communications independently', 'Treat an unapproved change as approved baseline', 'Expose prohibited information'], 'escalation_conditions': ['Material change order', 'Cost overrun', 'Schedule delay', 'CO/TCO risk', 'Turnover issue that can delay leasing or operations'], 'downstream_dependencies': ['Development / Project Leadership', 'Property Management', 'Asset Management', 'Finance & Administration', 'Investor Relations'], 'answer_order': ['Construction answer', 'Status', 'Cost/schedule effect', 'Required handoff', 'Sources', 'Missing information']}, 'property_asset': {'display_name': 'Property / Asset Management', 'responsibility': 'Track property operations and evaluate results against the investment plan, including corrective actions and ownership-reporting needs.', 'primary_focus': ['Rent, occupancy, concessions, and expenses', 'Lease-up and operating KPIs', 'NOI and performance versus plan', 'Construction dates affecting leasing and revenue'], 'inputs': ['Approved pro forma targets', 'Construction delivery dates', 'Property-management operating records', 'Verified financial actuals'], 'outputs': ['Leasing and operating KPIs', 'Variance analysis', 'Corrective-action recommendation', 'Forward operating forecast', 'Approved performance interpretation'], 'must_never': ['Overwrite the original pro forma with actual results', 'Invent current operating metrics when no approved source exists', 'Present forecast as actual', 'Expose tenant-screening PII or other prohibited information'], 'escalation_conditions': ['Lease-up miss', 'Material rent or concession variance', 'Expense or NOI miss', 'Construction delay affecting revenue', 'Operating issue requiring ownership or lender action'], 'downstream_dependencies': ['Finance & Administration', 'Investor Relations', 'Executive Leadership / GP Authority', 'Lending / Financing'], 'answer_order': ['Operating answer', 'Status', 'Variance versus plan', 'Operational implication/action', 'Sources', 'Missing information']}, 'finance': {'display_name': 'Finance', 'responsibility': 'Establish verified actuals, reconcile and classify financial information, maintain controls, and distinguish source data from presentation data.', 'primary_focus': ['Assumption versus forecast versus actual', 'Source and reporting period', 'NOI, DSCR, value, cash flow, and variance calculations', 'Verification status and unresolved figures'], 'inputs': ['Accounting/source-system records', 'Construction financial information', 'Property operating records', 'Approved financing information', 'Approved pro forma and forecast information'], 'outputs': ['Verified financial actuals', 'Reconciled reporting', 'Calculation support', 'Financial variance information', 'Unverified-item identification'], 'must_never': ['Create a favorable story unsupported by records', 'Present forecast as actual', 'Invent unverified figures', 'Replace deterministic authoritative calculations with model arithmetic once the tools exist', 'Expose bank, wire, tax-ID, credential, or other prohibited information'], 'escalation_conditions': ['Unreconciled figure', 'Source conflict', 'Funding gap', 'Debt-service risk', 'Material variance requiring management interpretation'], 'downstream_dependencies': ['Asset Management', 'Executive Leadership / GP Authority', 'Investor Relations', 'Lending / Financing', 'Tax & Audit'], 'answer_order': ['Financial answer', 'Status', 'Calculation when applicable', 'Source/period verification', 'Sources', 'Missing information']}, 'investor_relations': {'display_name': 'Investor Relations', 'responsibility': 'Translate approved business performance into accurate investor communication using verified inputs and approved interpretation.', 'primary_focus': ['Change from approved investment case', 'Confirmed versus calculated versus forecast versus unknown', 'What may be communicated after approval', 'Material variance explanation without promising outcomes'], 'inputs': ['Approved investment case', 'Verified finance information', 'Approved construction/operating variance explanation', 'Approved forward forecast'], 'outputs': ['Approved investor updates', 'Performance explanations', 'Action and uncertainty disclosure', 'Next-update expectations'], 'must_never': ['Promise investment outcomes', 'Communicate unverified numbers as facts', 'Approve material business interpretation independently', 'Expose investor identities/contact information, tax identifiers, subscription documents, bank/wire information, or other prohibited data'], 'escalation_conditions': ['Material variance without approved interpretation', 'Unverified financial result', 'Unresolved forecast', 'Restricted-information request', 'Source conflict'], 'downstream_dependencies': ['Investors after required internal approval', 'Executive Leadership / GP Authority'], 'answer_order': ['Communication-ready answer', 'Status', 'What changed and why', 'Action and remaining uncertainty', 'Sources', 'Missing information']}}

def answer_in_mode(user_mode, question):
    if user_mode not in ROLE_PROFILES:
        raise ValueError("Unknown user mode")
    base = answer_question(question)
    profile = ROLE_PROFILES[user_mode]
    return {
        "user_mode": user_mode,
        "role_name": profile["display_name"],
        "role_focus": profile["primary_focus"],
        "presentation_order": profile["answer_order"],
        "answer": base["answer"],
        "status": base["status"],
        "calculation": base["calculation"],
        "sources": base["sources"],
        "affected_functions": base["affected_functions"],
        "missing_information": base["missing_information"],
    }
```

## Automated Validation Tests

```python

from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from role_modes import ROLE_PROFILES, answer_in_mode

LIB = json.loads((ROOT / "conversation-library.json").read_text(encoding="utf-8"))
EVAL = Path("/mnt/data/EVALUATION-SUITE(1).md").read_text(encoding="utf-8")

MODES = {"executive","phoenix","property_asset","finance","investor_relations"}
STATUSES = {"confirmed","calculated","inferred","unknown","conflicting"}
REQUIRED_FIELDS = {
    "question_id","user_mode","question","required_sources","required_tools",
    "expected_status","restricted_fields","acceptance_notes"
}

def norm(x):
    return re.sub(r"[^a-z0-9]+"," ",x.lower()).strip()

def evaluation_questions():
    out = []
    for line in EVAL.splitlines():
        m = re.match(r"^\s*\d+\.\s+(.*\?)\s*$", line)
        if m:
            out.append(norm(m.group(1)))
    return set(out)

def test_exactly_75_questions():
    assert len(LIB) == 75

def test_exactly_15_per_mode():
    for mode in MODES:
        assert sum(1 for q in LIB if q["user_mode"] == mode) == 15

def test_required_question_fields():
    for q in LIB:
        assert set(q.keys()) == REQUIRED_FIELDS
        assert all(q[k] is not None for k in REQUIRED_FIELDS)

def test_unique_question_ids():
    ids = [q["question_id"] for q in LIB]
    assert len(ids) == len(set(ids))

def test_original_questions_do_not_copy_evaluation_wording():
    official = evaluation_questions()
    assert official
    for q in LIB:
        assert norm(q["question"]) not in official

def test_all_modes_have_complete_role_profiles():
    assert set(ROLE_PROFILES) == MODES
    required = {
        "display_name","responsibility","primary_focus","inputs","outputs",
        "must_never","escalation_conditions","downstream_dependencies","answer_order"
    }
    for p in ROLE_PROFILES.values():
        assert set(p.keys()) == required
        for k in required:
            assert p[k]

def test_status_values_are_valid():
    assert all(q["expected_status"] in STATUSES for q in LIB)

def test_every_question_has_source_requirement():
    assert all(q["required_sources"] for q in LIB)

def test_every_question_has_acceptance_notes():
    assert all(q["acceptance_notes"].strip() for q in LIB)

def test_restricted_questions_identify_restricted_fields():
    restricted = [q for q in LIB if "security_filter" in q["required_tools"]]
    assert restricted
    assert all(q["restricted_fields"] for q in restricted)

def test_each_mode_contains_unknown_or_restricted_behavior():
    for mode in MODES:
        rows = [q for q in LIB if q["user_mode"] == mode]
        assert any(q["expected_status"] == "unknown" for q in rows)

def test_each_mode_contains_grounded_confirmed_behavior():
    for mode in MODES:
        rows = [q for q in LIB if q["user_mode"] == mode]
        assert any(q["expected_status"] == "confirmed" for q in rows)

def test_executive_mode_runtime():
    r = answer_in_mode("executive", "What construction debt is committed to Pine Ridge?")
    assert r["role_name"] == "Executive"
    assert r["status"] == "confirmed"
    assert "$33,600,000" in r["answer"]
    assert r["sources"]

def test_phoenix_mode_runtime():
    r = answer_in_mode("phoenix", "Who is Pine Ridge's general contractor?")
    assert r["role_name"] == "Phoenix / Construction"
    assert r["status"] == "confirmed"
    assert "Phoenix Commercial Construction" in r["answer"]

def test_property_asset_mode_runtime():
    r = answer_in_mode("property_asset", "What stabilized occupancy was underwritten for Pine Ridge?")
    assert r["role_name"] == "Property / Asset Management"
    assert r["status"] == "confirmed"
    assert r["answer"] == "95%"

def test_finance_mode_runtime():
    r = answer_in_mode("finance", "What interest rate is assumed for the Pine Ridge permanent loan?")
    assert r["role_name"] == "Finance"
    assert r["status"] == "confirmed"
    assert r["answer"] == "6.25%"

def test_investor_relations_mode_runtime():
    r = answer_in_mode("investor_relations", "Is Pine Ridge an actual SRI investment?")
    assert r["role_name"] == "Investor Relations"
    assert r["status"] == "confirmed"
    assert r["answer"].startswith("No.")

def test_current_actual_not_replaced_by_underwriting_assumption():
    r = answer_in_mode("property_asset", "What is Pine Ridge's current occupancy?")
    assert r["status"] == "unknown"
    assert r["answer"] is None
    assert r["missing_information"]

def test_role_runtime_keeps_source_citations():
    for mode, question in [
        ("executive","Which entity owns Pine Ridge?"),
        ("phoenix","Who is Pine Ridge's general contractor?"),
        ("property_asset","What stabilized occupancy was underwritten for Pine Ridge?"),
        ("finance","What interest rate is assumed for the Pine Ridge permanent loan?"),
        ("investor_relations","Is Pine Ridge an actual SRI investment?"),
    ]:
        r = answer_in_mode(mode, question)
        assert r["sources"]
        assert all(s["source_id"] and s["section_or_page"] for s in r["sources"])

def test_no_mode_changes_underlying_retrieved_fact():
    question = "What stabilized occupancy was underwritten for Pine Ridge?"
    answers = [answer_in_mode(mode, question)["answer"] for mode in MODES]
    assert set(answers) == {"95%"}

def test_mode_answer_has_required_context():
    r = answer_in_mode("executive", "What construction debt is committed to Pine Ridge?")
    assert r["role_focus"]
    assert r["presentation_order"]
    assert set(r) == {
        "user_mode","role_name","role_focus","presentation_order",
        "answer","status","calculation","sources","affected_functions","missing_information"
    }
```

## Validation Result

**Status:** PASS

**Conversation questions:** 75

- Executive: 15
- Phoenix / Construction: 15
- Property / Asset Management: 15
- Finance: 15
- Investor Relations: 15


**Automated test result:**

```text
[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                    [100%][0m
[32m[32m[1m21 passed[0m[32m in 0.09s[0m[0m
```
