# Dataset Documentation (SP25)

## Project Information

**Project Name**  
City Councilor Benjamin Weber: Boston Tree Canopy Equity

**GitHub Repository**  
https://github.com/BU-Spark/ds-bcc-tree-canopy

**Google Drive Folder**  
Spark!-owned folder  
https://drive.google.com/drive/folders/1B718VdWHsRmir2jxxE4EMXRKt5ThdJ7w?usp=drive_link

**Project Description**  
This project assesses whether more socially vulnerable Boston neighborhoods systematically have less tree canopy. We built an interactive ArcGIS map, exportable data & data dictionary, and a composite vulnerability score to highlight environmental inequities.

**Client**  
Councilor Ben Weber

**Client Contacts**  
- Bonnie DeLaune, bonnie.delaune@boston.gov  
- Jordan Frias, jordan.frias@boston.gov  

**Course**  
DS539 Spark! Data Science X-Lab Practicum

## Dataset Information

**Datasets Used**  
- Canopy Change Assessment: Parcels Tree Canopy Metrics (ArcGIS Open Data)  
- Climate Ready Boston: Social Vulnerability (City of Boston Open Data)  

**Derived Datasets**  
- Boston_Neighborhoods_SVscore_Canopy.geojson  
- data/neighborhood_tree_canopy_stats.csv  

**Data Dictionary**  
See `data/DATA_DICTIONARY.md`  

**Keywords / Tags**  
Geospatial, Environmental Justice, Urban Forestry, Equity, GIS, Sustainability

## Dataset Details

| Field               | Type   | Description                                                                                          |
|---------------------|--------|------------------------------------------------------------------------------------------------------|
| Name                | String | Neighborhood name (e.g., Dorchester, Roxbury)                                                        |
| Canopy_pct          | Float  | Percent of land area under tree canopy                                                               |
| SV_key_nb           | Float  | Composite Vulnerability Score: average of LowIncome_pct, LEP_pct, Disability_pct                     |
| LowIncome_pct       | Float  | % of households below the poverty line                                                               |
| LEP_pct             | Float  | % of residents with Limited English Proficiency                                                      |
| Disability_pct      | Float  | % of residents reporting a disability                                                                |

## Collection & Processing

- **Sources**: SVI data from City of Boston; canopy metrics from Boston Open Data  
- **Cleaning**: Joined in Python notebook (`EJ_Weber_CT.ipynb`); computed `SV_key_nb`  
- **Export**: GeoJSON published in ArcGIS Online; CSV via Data → Export → CSV  

## Usage & Next Steps

- **Current**: Interactive map + charts illustrating inequity patterns  
- **Future**: Guide tree-planting prioritization; inform policy reports  
