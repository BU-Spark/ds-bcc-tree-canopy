# Boston Tree Canopy Analysis (Spring 2025)

## Overview

This project, conducted in collaboration with Councilor Ben Weber, investigates the spatial distribution of Boston’s urban tree canopy. Our focus is to distinguish between public and private tree canopy, analyze trends over time, and identify disparities across land use types and neighborhoods—particularly in Environmental Justice communities. The project aims to inform equitable policy interventions through rigorous geospatial and statistical analysis.

## Objectives

### Primary Question
- How can we distinguish between public and privately owned tree canopy in Boston using geospatial data and land use classifications?

### Supplementary Questions
- What percentage of Boston's tree canopy is on public vs. residential parcels?
- How does tree canopy coverage vary by neighborhood and land use type?
- What are the trends in canopy loss or gain (2014–2019)?
- Which areas have the greatest potential for expanding tree canopy?
- Are there disparities in canopy coverage in marginalized communities?
- How does tree canopy *height* change by ownership type (2014–2019)?

## Methodology

### Data Sources
- **2014–2019 Tree Canopy Change Assessment**  
- **2019 Parcel Land Use & Ownership Data**  
- **2024 Parcel Dataset (for ROW classification)**  
- **Property Assessment FY2019 (for exempt/public flags)**  
- **Environmental Justice Census Tract Data**  
- **Boston Street Tree Inventory (2022–present)**  

### Tools Used
- ArcGIS (for spatial joins and overlay)
- Python (Pandas, GeoPandas for data cleaning & analysis)
- Looker Studio (for dashboard visualizations)
- Excel (manual owner name standardization)
- GitHub (code and notebook repository)

### Public vs. Private Classification
- Public parcels were identified via:
  - Owner name matching using keywords and fuzzy logic (e.g., “CITY OF BOSTON”, “BPDA”)
  - Property tax exemption codes (`PTYPE` codes starting with ‘9’)  
  - Cross-referencing with the Public Tree Protection Ordinance
- Manual validation yielded **60 public owners**, including:
  - Boston Water & Sewer Commission, Boston Public Schools, Commonwealth of Mass, etc.
  - Excluded ambiguous or privately affiliated entities (e.g., private universities)

### Tree Canopy Metrics
- % coverage calculated relative to land area and canopy area
- Separate calculations for total canopy, public vs. private, and land use
- Spatial overlay used to intersect canopy polygons with parcel data
- Neighborhood-level aggregation performed via census tract joins

## Key Findings

- **Public parcels** had **40.79%** canopy coverage
- **Private parcels** had **23.52%** canopy coverage
- Only **18.5%** of total canopy is located on public land
- **Residential parcels** make up **38.57%** of canopy area
- **Institutional land** accounts for **44.87%** of canopy area
- **Jamaica Plain** leads neighborhoods with **44.7%** canopy coverage
- Tree canopy **increased by 2%** on public land and **decreased by 0.81%** on private land (2014–2019)

## Inequity & EJ Analysis
- Merged tree canopy and EJ data by census tract
- Early results suggest disparities in canopy coverage by demographic group
- Blockers remain in full coverage due to missing census tracts in the EJ dataset

## Expansion Potential
- **47%** of potential canopy expansion area is on **public** land
- **41%** is on **private** land
- ROW areas (e.g., sidewalks) also offer significant potential but require classification using newer 2024 datasets

## Blockers & Challenges

| Category | Description |
|---------|-------------|
| **Ownership Complexity** | Over **134,000** unique owners; inconsistent names (e.g., “BOSTON REDEVLOPMENT AUTH”, “CITY OF BOSTON SCHOOL DEPT”) required manual cleaning and fuzzy matching |
| **ROW Classification** | 2019 data lacked clear public/private ROW labeling — solution: use 2024 dataset’s `POLY TYPE` column (e.g., `ROW`, `PRIV_ROW`) to reclassify |
| **Looker Studio Limits** | Some datasets (e.g., environmental justice CSV) failed to render due to Looker Studio size restrictions |
| **School Parcel Naming** | Boston Public Schools often listed under unique/abbreviated names, making consistent filtering challenging |
| **GitHub Upload Limits** | Large geospatial datasets exceeded GitHub’s file size limits — requires external linking or compression |

## Next Steps

- Classify ROW canopy using 2024 parcels data (`POLY TYPE`)
- Continue work on canopy height trends (2014–2019)
- Refine EJ tract joins to ensure full coverage
- Finalize 5–7 visualizations and complete the client-facing report
- Push updated Jupyter notebooks and cleaned datasets to GitHub

## Contributors

- Rachel Young  
- Grace Chong  
- Amelia Jennings  
- Talya Beydoun
- Gui Marques 
- Councilor Ben Weber (Client)  
- Julissa Mijares (TPM)  
- Tony Wu (PM)

---


