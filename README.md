# Lake City & Hinsdale County Housing Plan

A comprehensive strategic housing plan for Lake City and Hinsdale County, Colorado — the state's most remote and least populated county. Led by Western Spaces, LLC with support from Dynamic Planning + Science, Proximity Green, and Triple Point Strategic Consulting.

## Current Status

**Adopted February 18, 2026** — The Lake City & Hinsdale County Comprehensive Housing Plan was jointly adopted by the Town of Lake City Board of Trustees and the Hinsdale County Board of County Commissioners.

- **Official plan page:** [townoflakecityco.gov/lake-city-hinsdale-county-comprehensive-housing-plan](https://www.townoflakecityco.gov/lake-city-hinsdale-county-comprehensive-housing-plan)
- **Public comment period:** Closed January 31, 2026 — one letter of support received, no other comments
- **Final joint work session:** February 11, 2026

## Project Timeline

| Phase | Period | Focus |
|-------|--------|-------|
| Research & Engagement | Apr - Jun 2025 | Surveys, data analysis, community input |
| Strategy Development | Jul - Oct 2025 | Goals, strategies, feasibility analysis |
| Implementation Planning | Nov - Dec 2025 | Priorities, roles, launch plan |
| Plan Finalization | Jan - Feb 2026 | Public comment, revisions, adoption |

## Directory Guide

### `website/`
Public-facing project website hosted at [lakecityhousing.com](https://lakecityhousing.com). Contains `index.html`, all presentation HTML files served to the public, PDFs (full plan, executive summary, read-ahead packets), team photos, and meeting presentation archives.

### `meetings/`
All meeting materials organized by series:
- **`series_1_summer_2025/`** — Foundation phase. Steering Committee #1 (Jul 30) and Joint Session #1 (Aug 13). Needs assessment, goal setting.
- **`series_2_fall_2025/`** — Strategy phase. Steering Committee #2 (Sep 4) and Joint Session #2 (Oct 1). Four strategies defined with action cards.
- **`series_3_implementation/`** — Implementation phase. Steering Committee #3 (Nov 14) and Joint Session #3 (Nov 19). Implementation priorities, revenue feasibility, decision packets.
- **`series_4_winter_2026/`** — Final phase. Joint Session #4 (Feb 11). Plan adoption prep, decision summary handout, final presentation. Also contains bi-weekly steering committee agendas and the Quick Recap notes.
- **`archive/`** — Older/superseded materials.

### `survey/`
Raw survey data and analysis scripts. Household survey (97 responses) and employer survey (21 responses). Includes CSV exports, Python analysis scripts, and summary memos on housing preferences, employment sectors, unit mix recommendations.

### `report/`
Housing plan document files. Working drafts, executive summary PDF (Typst-generated), proforma analysis (Henson Street apartment), and the archive of earlier chapter drafts.

### `silverton/`
Silverton & San Juan County case study — a comparable rural Colorado community. Housing authority structure analysis, implementation considerations, strategy crosswalk, funding/partner research. Used as a model for Lake City's approach (coordinator ROI, housing authority formation).

### `petition/`
Rural resort reclassification petition materials. Hinsdale County memo on petition to reclassify as a rural resort community, plus submitted petition documents. Enables access to higher AMI levels for MIHA funding.

### `hna-hap/`
Housing Needs Assessment (HNA) and Housing Action Plan (HAP) data and guides, per SB 24-174 requirements. Contains data files and reference guides.

### `fast/`
Fast-track permitting and development incentives. Municipal code (Lake City), code analysis (PDF), and guidance documents. Supports the $100K DOLA fast-track funding ($50K Town + $50K County).

### `programs/`
Employer survey results and program analysis. Survey export data, analysis scripts, and results memo.

### `dashboard/`
Streamlit-based interactive housing survey dashboard. Python app (`housing_survey_dashboard.py`) for visualizing household survey data. Includes setup instructions, test files, and requirements.

## Team

| Name | Organization | Role |
|------|-------------|------|
| Sarah Brown McClain | Western Spaces, LLC | Project Lead and Housing Specialist |
| Ethan Mobley | Dynamic Planning + Science | Land Use Feasibility and GIS |
| Grant Bennett | Proximity Green | Development Specialist |
| Jeff Moffett | Triple Point Strategic Consulting | Financial Feasibility |

## Partners

- **Town of Lake City** — [townoflakecityco.gov](https://www.townoflakecityco.gov/)
- **Hinsdale County** — [hinsdalecounty.colorado.gov](https://hinsdalecounty.colorado.gov/)
- **Colorado Department of Local Affairs (DOLA)** — [cdola.colorado.gov](https://cdola.colorado.gov/)

## Key Documents

| Document | Location |
|----------|----------|
| Full Housing Plan (PDF) | `website/Lake-City-Hinsdale-Housing-Plan.pdf` |
| Executive Summary (PDF) | `website/Housing-Plan-Executive-Summary.pdf` |
| Decision Summary Handout | `meetings/series_4_winter_2026/joint_session/Decision_Summary_Handout.md` |
| Joint Session #4 Presentation | `meetings/series_4_winter_2026/joint_session/Joint_Session_4_Presentation.html` |
| Revenue Feasibility Study | `meetings/series_3_implementation/steering_group/Revenue_Feasibility_Study.md` |
| Silverton Case Study | `silverton/Silverton_Complete_Analysis_for_LakeCity.md` |
| Survey Results Memo | `programs/survey_results_memo.md` |

## Key Stats

- **72%** of housing is seasonal/vacant
- **0%** rental vacancy rate
- **77%** of residents view housing availability as critical
- **24** jobs unfilled due to housing shortages
- **843 → 774** population declining (2010–2025)
- **$563K** median home price
- **1 in 5** households at risk of displacement
- **87 units** of documented housing shortage
- **20–40** housing opportunities targeted over 10 years

## Four Core Strategies

1. **Policies & Incentives** — Fast-track permitting, ADU ordinance, STR regulation, lease incentives
2. **Optimize Existing Stock** — Acquisition/rehab, anti-displacement, preservation fund
3. **Sustainable Revenue** — Mill levy, inclusionary zoning, fee-in-lieu, grant leverage
4. **Strategic Development** — Land banking, Lake Fork site (28 units, MHN grant), employer partnerships
