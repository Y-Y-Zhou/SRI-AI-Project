# 02 Business Ontology

## Purpose

Defines the business objects, relationships, ownership, and metadata
required for the SRI Project Intelligence Assistant.

## Core Objects

### Company

Fields: - Company ID - Company Name - Operating Functions

### Legal Entity

Fields: - Entity ID - Legal Name - Entity Type - Role

### Project / Property

Fields: - Project ID - Project Name - Property Type - Status - Location

Relationships: - Has legal entities - Has loans - Has contracts - Has
budgets - Has operating statements

### Department / Function

Fields: - Function ID - Function Name - Responsibilities - Owner
Position

### Investor

Fields: - Investor ID - Investor Type - Related Entity

### Loan

Fields: - Loan ID - Borrower - Lender - Principal - Terms - Status

### Pro Forma

Fields: - Pro Forma ID - Project ID - Version - Approval Status -
Assumptions

### Construction Budget

Fields: - Budget ID - Project ID - Cost Categories - Version - Status

### Contract / Commitment

Fields: - Contract ID - Parties - Effective Date - Status

### Schedule Milestone

Fields: - Milestone ID - Project ID - Date - Status

### Unit / Lease

Fields: - Unit ID - Project ID - Lease Status

### Operating Statement

Fields: - Statement ID - Project ID - Period - Revenue - Expenses - NOI

### Distribution

Fields: - Distribution ID - Project ID - Period - Amount

### Investor Report

Fields: - Report ID - Project ID - Period - Approval Status

### Source Document

Fields: - Source ID - Title - Source Type - Location - Version

### Decision

Fields: - Decision ID - Question - Authority - Status

## Identity Rules

-   One canonical Project ID per project.
-   Aliases cannot replace legal entities, properties, loans, or
    contracts.
-   Approved versions are preserved.

## Required Metadata

-   Project ID
-   Legal Entity
-   Department
-   Record Type
-   Reporting Period
-   Source System
-   Source Identifier
-   Owner
-   Approval Status
-   Version / Effective Date
-   Confidentiality Classification

## AI Governance

-   Approved information may be indexed according to access rules.
-   Restricted information requires permission controls.
-   Confidential information cannot be used by AI.
-   Missing information returns unknown.
