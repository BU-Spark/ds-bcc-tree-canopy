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

## Technical Architecture
The analysis was done on one primary question(How can we distinguish between public and privately owned tree canopy in Boston using geospatial data and land use classifications?) and six supplementary questions listed above. The analysis for all questions was done in either excel or code in a Jupyter Notebook file. The various CSV files used to code are contained in the datasets folder that houses the data we used and classified for this project. We primarily used Python and Pandas were the primary tools, but for visualizing a dashboard we used Looker Studio, which will soon be available and uploaded. 

## How to Run
Download a recent version of Python, download Jupyter after Python has been installed. You can download Anaconda or use Google Colab to clone the project, run all cells and the notebook should generate all analysis. If there is a missing package, add a 'pip install' to the top line of the .ipynb file and re-run all following cells.

## Methodology

### Data Sources
- **2014–2019 Parcel Tree Canopy Change Assessment**
- **2014–2019 Neighborhoods Tree Canopy Change Assessment**  
- **Environmental Justice Census Tract Data**  

### Supplementary References 
- **Property Assessment FY2019 (for exempt/public flags)**:  Will allow you to interpret PTYPE columns and determine tax-exempt parcels of land, which we broadly interpreted as publicly owned. Can be found on [Analyze Boston](https://data.boston.gov/dataset/property-assessment/resource/d6c1268c-cd83-4dc3-a914-bba1ed59da6d).
- **Boston Street Tree Inventory (2022–present)**: Will allow you to look up who owns a specific street in Boston.
- **2024 Parcel Dataset (for ROW classification)**: Parcel datasets are published for every year in Boston. They contain a column called POLY_TYPE that has potential to be used to classify right-of-way area, such as sidewalks, roads, and streets, as public or privately owned. Our dataset was from 2019, which lacked this column. However, this can potential be used for the future Canopy Assessments that will be done every five years. 

### Tools Used
- ArcGIS (for spatial joins and overlays)
- Python (Pandas, GeoPandas for data cleaning & analysis)
- Looker Studio (for dashboard visualizations)
- Excel (manual owner name standardization)
- GitHub (code and notebook repository)

### Public vs. Residential Classification
The initial questions were posed as public vs residential. We interpreted public as property owned by the City of Boston and protected by the tree ordinance. Any other parcels were considered non-city owned and we aggregated right-of-way(ROW) tree canopy separately because we could not distinguish between public and private streets. 
- City-owned parcels were identified via:
  - Fuzzy matching owner names to be similar to:
    * City of Boston
    * Boston Water and Sewer Commission
    * Boston Housing Authority
    * Boston Public Schools
    * Boston Redevelopment Authority
    * Boston Planning and Development Agency 
  - Cross-referencing with the Public Tree Protection Ordinance
- Manual validation yielded **61 public owners**, including:
  - Used a Fuzzy Matching threshold of 78, then manually reviewed owner names for errors
  - Boston Water & Sewer Commission, Boston Housing Authority etc.
  - Excluded ambiguous or privately affiliated entities (e.g., private universities)

### Tree Canopy Metrics
For neighborhoods and land use we calculated:
- % coverage calculated relative to land area
For public vs private tree canopy we calculated:
- % coverage calculated relative to total canopy area

## Key Findings

- **City-owned parcels** had **18.47%** canopy coverage
- **Non-city owned parcels** had **70.12%** canopy coverage
- **ROW parcels** had **11.41%** canopy coverage
- **Residential parcels** make up **38.57%** of canopy area
- **Institutional land** accounts for **44.87%** of canopy area
- **Jamaica Plain** leads neighborhoods with **44.7%** canopy coverage
- Tree canopy **increased by 2%** on public land and **decreased by 0.81%** on private land (2014–2019)

## Inequity & EJ Analysis
- Merged tree canopy and EJ data by census tract
- Blockers remain in merging the datasets and combining columns in the EJ dataset
  
## Expansion Potential
- **47%** of potential canopy expansion area is on **public** land
- **41%** is on **private** land
- ROW areas (e.g., sidewalks) also have **20%** of land that has potential for expansion 

## Blockers & Challenges

| Category | Description |
|---------|-------------|
| **Ownership Complexity** | Over **134,000** unique owners; inconsistent names (e.g., “BOSTON REDEVLOPMENT AUTH”, “CITY OF BOSTON SCHOOL DEPT”) required manual cleaning and fuzzy matching |
| **ROW Classification** | 2019 data lacked clear public/private ROW labeling — solution: aggregate ROW data separately|
| **Looker Studio Limits** | Some datasets (e.g., environmental justice CSV) failed to render due to Looker Studio size restrictions |
| **GitHub Upload Limits** | Large geospatial datasets exceeded GitHub’s file size limits — requires external linking or compression |
| **ArcGIS Pro Limits** | ArcGIS Pro is only compatible with Windows. Any geospatial files should be opened using a computer with ArcGIS Pro downloaded. |

## Next Steps
Future teams can work on:
- Improving the Fuzzy Matching process to more accurately distinguish between city-owned and non-city owned trees
  - Potentially develop a methodology to use the authoritative source on city-owned property: [2022 Citywide Land Audit](https://www.boston.gov/housing/citywide-land-audit)
  - We faced blockers because there are disrepencies in the 2019 and 2022 parcels
  - In addition, there were differences in ownership between 2019 and 2022 that we could not reconcile
- Reference another dataset to classify ROW data as city or non-city owned
  - In the next LIDAR dataset, there may be a column named "POLY_TYPE" that would allow streets to be labeled "ROW" or "PRIV_ROW", which may help distinguish
  - This column was not available in the 2019 data
- Compare 2019 tree canopy metrics to future LIDAR data published by Analyze Boston and collected by the Boston Parks and Recreation Department every five years. 

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


