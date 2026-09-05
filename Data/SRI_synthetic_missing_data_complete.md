# SRI Synthetic Missing Data Package

## Purpose

This document consolidates all invented synthetic data created to fill
the missing information needed for Step 8: Build the Central Information
System / Business Ontology and Ingestion.

## Important Disclaimer

All information in this document is artificially created for the SRI
Pine Ridge prototype. It is not real SRI information and must not be
treated as factual company data.

The purpose is only to provide a complete synthetic corpus for ontology
design, schema creation, source registration, and AI testing.

------------------------------------------------------------------------

# 1. Synthetic Entity Registry

## Company

  Entity ID   Name                  Type
  ----------- --------------------- ---------
  CMP-001     SRI Operating Model   Company

## Project

  -----------------------------------------------------------------------
  Project ID        Project Name      Property Type     Status
  ----------------- ----------------- ----------------- -----------------
  SRI-2026-MF-001   Pine Ridge        Multifamily       Development
                    Apartments        Development       

  -----------------------------------------------------------------------

## Legal Entities

  Entity ID   Name                          Role
  ----------- ----------------------------- --------------------
  LE-001      SRI Development Sponsor LLC   Sponsor / GP
  LE-002      Pine Ridge Owner LLC          Property Owner
  LE-003      Pine Ridge Investors LP       LP Investor Entity

## Invented Relationships

-   Pine Ridge Apartments is associated with Pine Ridge Owner LLC.
-   SRI Development Sponsor LLC provides sponsor and GP authority.
-   Pine Ridge Investors LP provides equity capital.
-   Project-level agreements are executed through appropriate legal
    entities.

------------------------------------------------------------------------

# 2. Synthetic Source Registry

## Invented Source Inventory

  -----------------------------------------------------------------------------------
  Source ID   Source Title   Source Type  Department     Owner            Approval
                                                                          Status
  ----------- -------------- ------------ -------------- ---------------- -----------
  SRC-001     Pine Ridge     Investment   Capital &      Capital & Deals  Approved
              Investment     Memo         Deals                           
              Memo                                                        

  SRC-002     Pine Ridge     Budget       Development    Project Manager  Approved
              Development                                                 
              Budget                                                      

  SRC-003     Pine Ridge     Schedule     Phoenix        Superintendent   Approved
              Construction                Construction                    
              Schedule                                                    

  SRC-004     Pine Ridge     Forecast     Asset          Asset Manager    Approved
              Operating                   Management                      
              Forecast                                                    

  SRC-005     Pine Ridge     Financing    Lending        Lending          Approved
              Loan Summary   Record                                       

  SRC-006     Pine Ridge     Investor     Investor       Investor         Draft
              Investor       Report       Relations      Relations        
              Update Draft                               Manager          

  SRC-007     Pine Ridge     Financial    Finance        Finance &        Approved
              Monthly        Record                      Administration   
              Operating                                                   
              Statement                                                   
  -----------------------------------------------------------------------------------

## Required Source Metadata

Every indexed record should include:

-   source_id
-   source_title
-   source_type
-   project_id
-   legal_entity_id
-   department
-   reporting_period
-   version_or_effective_date
-   approval_status
-   confidentiality_class

------------------------------------------------------------------------

# 3. Synthetic System Inventory

## Invented Systems

  -----------------------------------------------------------------------
  System ID         System Name       Purpose           Owner
  ----------------- ----------------- ----------------- -----------------
  SYS-001           Shared Document   Stores approved   Systems/Data & AI
                    Repository        documents         Governance

  SYS-002           Accounting        Stores financial  Finance &
                    Platform          records           Administration

  SYS-003           Construction      Tracks            Phoenix
                    Management System construction      Construction
                                      information       

  SYS-004           Property          Stores leasing    Property
                    Management        and operating     Management
                    Platform          information       

  SYS-005           Underwriting      Stores investment Capital & Deals
                    Repository        models            
  -----------------------------------------------------------------------

## AI Usage Rules

-   AI only uses approved synthetic information during this sprint.
-   AI does not access production systems.
-   Credentials and confidential information are excluded.

------------------------------------------------------------------------

# 4. Synthetic Sample Business Records

## Project Record

  Field           Value
  --------------- -----------------------
  Project ID      SRI-2026-MF-001
  Project Name    Pine Ridge Apartments
  Status          Development
  Property Type   Multifamily

## Loan Record

  Field       Value
  ----------- -----------------------
  Loan ID     LOAN-001
  Project     Pine Ridge Apartments
  Loan Type   Construction Loan
  Status      Approved

## Decision Record

  Field         Value
  ------------- ----------------------------------------
  Decision ID   DEC-001
  Question      Approve revised construction schedule?
  Authority     Executive Leadership / GP Authority
  Status        Pending Review

------------------------------------------------------------------------

# 5. Synthetic Metadata Example

``` yaml
source_id: SRC-002
source_title: Pine Ridge Development Budget
project_id: SRI-2026-MF-001
legal_entity_id: LE-002
department: Development
document_type: Construction Budget
version: V1
approval_status: Approved
confidentiality_class: Approved for AI
```

------------------------------------------------------------------------

# 6. Missing Data Filled by This Package

This package fills the following previously unavailable information:

## Added

-   Synthetic IDs for companies, projects, and legal entities.
-   Synthetic source document inventory.
-   Synthetic system inventory.
-   Synthetic example records for ontology testing.
-   Synthetic metadata examples.

## Not Invented

The following remain intentionally unavailable:

-   Real investor identities.
-   Investor commitments.
-   Bank accounts or wire information.
-   Tax IDs.
-   Real contracts.
-   Production systems.
-   Real SRI confidential information.
-   Missing economic terms such as waterfall economics or preferred
    returns.

These remain unknown unless provided by an approved source.
