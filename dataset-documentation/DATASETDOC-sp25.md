## Project Information

**Project Name**  
City Councilor Benjamin Weber: Boston Tree Canopy Equity

**GitHub Repository**  
https://github.com/BU-Spark/ds-bcc-tree-canopy

**Google Drive Folder**  
*Spark!-owned folder*  
[Drive Folder Link](https://drive.google.com/drive/folders/1B718VdWHsRmir2jxxE4EMXRKt5ThdJ7w?usp=drive_link)

**Project Description**  
This project assesses whether more socially vulnerable Boston neighborhoods systematically have less tree canopy. We built an interactive ArcGIS map, exportable data & data dictionary, and a composite vulnerability score to highlight environmental inequities.

**Client**  
Councilor Ben Weber

**Client Contacts**  
- Bonnie DeLaune, bonnie.delaune@boston.gov  
- Jordan Frias, jordan.frias@boston.gov  

**Course**  
DS539 Spark! Data Science X-Lab Practicum

---

## Dataset Information

**Datasets Used**  
- [Canopy Change Assessment: Parcels Tree Canopy Metrics](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::canopy-change-assessment-tree-canopy-metrics/explore?layer=4)  
- [Climate Ready Boston: Social Vulnerability](https://data.boston.gov/dataset/climate-ready-boston-social-vulnerability)

**Derived Datasets**  
- **Boston_Neighborhoods_SVscore_Canopy.geojson** (feature layer for the 17 neighborhoods)  
- **data/neighborhood_tree_canopy_stats.csv** (exported table of canopy % and vulnerability metrics)

**Data Dictionary**  
See [`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md) for field definitions.

**Keywords / Tags**  
Geospatial, Environmental Justice, Urban Forestry, Equity, GIS, Sustainability

---

### Dataset Details

| Field               | Type   | Description                                                                                          |
|---------------------|--------|------------------------------------------------------------------------------------------------------|
| **Name**            | String | Neighborhood name (e.g., Dorchester, Roxbury)                                                        |
| **Canopy_pct**      | Float  | Percent of land area under tree canopy (from Boston canopy metrics)                                  |
| **SV_key_nb**       | Float  | Composite Vulnerability Score: average of LowIncome_pct, LEP_pct, Disability_pct                     |
| **LowIncome_pct**   | Float  | % of households below the poverty line                                                               |
| **LEP_pct**         | Float  | % of residents with Limited English Proficiency                                                      |
| **Disability_pct**  | Float  | % of residents reporting a disability                                                                |

---

## Composition & Format

- **Instances**: 17 neighborhood polygons  
- **Formats**:  
  - GeoJSON for spatial layer  
  - CSV for tabular data  

---

## Collection Process

- **Sources**:  
  - Social vulnerability from Climate Ready Boston SVI (City of Boston Open Data)  
  - Canopy metrics from City of Boston “Parcels Tree Canopy Metrics” layer  
- **Processing**:  
  - Cleaned and joined data in Python (see `EJ_Weber_CT.ipynb`)  
  - Published GeoJSON feature layer in ArcGIS Online  
  - Exported table to CSV via ArcGIS Online → Data → Export to CSV  

---

## Preprocessing

- Joined canopy & SVI tracts to neighborhood boundaries using GeoPandas  
- Computed `SV_key_nb` by averaging the three strongest-correlating vulnerability metrics (Low Income, LEP, Disability)  

---

## Usage & Next Steps

- **Current**: Interactive map with embedded ArcGIS viewer + charts illustrating inequity patterns  
- **Future**: Guide tree-planting prioritization in high-need neighborhoods; inform policy briefs  

---

## Access & Contribution

- **Access Level**: Public (ArcGIS Online map + GitHub repository)  
- **Contribute**: Fork this repo and send a Pull Request to update data, dictionary, or embed page  
