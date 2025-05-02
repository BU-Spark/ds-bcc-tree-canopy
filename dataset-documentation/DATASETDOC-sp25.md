***Project Information*** 

* What is the project name? 
    * City Councilor Benjamin Weber: Boston Tree Canopy
* What is the link to your project’s GitHub repository?
   * https://github.com/BU-Spark/ds-bcc-tree-canopy
* What is the link to your project’s Google Drive folder? \*\**This should be a Spark\! Owned Google Drive folder \- please contact your PM if you do not have access\*\**<br>
    * https://drive.google.com/drive/folders/1B718VdWHsRmir2jxxE4EMXRKt5ThdJ7w?usp=drive_link
* In your own words, what is this project about? What is the goal of this project?   

  This project, developed in partnership with Councilor Ben Weber, investigates the distribution of Boston’s tree canopy to assess differences between City of Boston owned trees and non-city owned trees. The goal behind distinguishing this difference is to understand which trees are protected by the Boston Public Tree Protection Ordinance that was passed in 2023 and took effect in 2024. The ordinance was passed in support of the Urban Forest Plan, which aims to protect and enhance the city's trees. Using a geospatial and data-driven approach, we aim to uncover patterns in canopy distribution, identify disparities across neighborhoods and land use types, and inform urban forestry strategies and environmental justice efforts. <br>

  The goal of this project is to understand how much of Boston's tree canopy is currently unprotected by the tree ordinance to advocate for extending the ordinance to non-city owned tree canopy in Boston.  
* Who is the client for the project?  
  Councilor Ben Weber
* Who are the client contacts for the project?  
  Bonnie Delane bonnie.delaune@boston.gov
  <br>Jordan Frias jordan.frias@boston.gov
* What class was this project part of? <br>
  DS539 Spark! Data Science X-Lab Practicum

***Dataset Information***

* What data sets did you use in your project? Please provide a link to the data sets, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.  
    * https://github.com/BU-Spark/ds-bcc-tree-canopy/tree/dev/datasets
    * https://drive.google.com/drive/folders/1FEWEYNu06IH8EFCK7HiTExHoQ44nwiZR?usp=drive_link

For this project, a number of different datasets were used to answer each of the question. These are links for where to access the data for download.

The [Canopy Change Assessment: Parcels Tree Canopy Metrics](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::canopy-change-assessment-tree-canopy-metrics/explore?layer=4) dataset has instances that represent property at a parcel level, which essentially represents a specific piece of property that a person, entity, or organization owns. Each row contains columns that describe how much tree canopy coverage area and how much potential land canopy there is on each piece of land. 
 

The [Canopy Change Assessment: Neighborhoods Tree Canopy Metrics](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::canopy-change-assessment-tree-canopy-metrics/explore?layer=1) dataset has instances that groups property at a neighborhood level. Each row contains columns that describe how much tree canopy coverage area and how much potential land there is in each neighborhood.

The [Canopy Change Assessment: Parcels Tree Canopy Change Metrics](https://bostonopendata-boston.opendata.arcgis.com/maps/boston::canopy-change-assessment-tree-canopy-change-metrics/about) dataset has instances that represent property at a parcel level, which essentially represents a specific piece of property that a person, entity, or organization owns. This dataset differs from the [Canopy Change Assessment: Parcels Tree Canopy Change Metrics](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::canopy-change-assessment-tree-canopy-change-metrics/explore?layer=8&location=42.312109%2C-71.032757%2C11.72) becuase it contains columns that have tree canopy gain and loss between the years of 2014 and 2019.

The [Citywide Land Audit](https://data.boston.gov/dataset/city-land-audit-public1) dataset has instance that represent parcels that are owned by the City of Boston and it's quasi-agencies. 

[EJ Communities Data (CoB)](https://data.boston.gov/dataset/climate-ready-boston-social-vulnerability)


* Please provide a link to any data dictionaries for the datasets in this project. If one does not exist, please create a data dictionary for the datasets used in this project. **(Example of data dictionary)**  
    * https://data.boston.gov/dataset/canopy-change-assessment-data-dictionary
    * https://github.com/BU-Spark/ds-bcc-tree-canopy/tree/dev/data/DATA_DICTIONARY.md
* What keywords or tags would you attach to the data set?  
  * Domain(s) of Application: Computer Vision, Object Detection, OCR, Image Classification, Image Segmentation, Facial Recognition, NLP, Topic Modeling, Sentiment Analysis, Named Entity Recognition, Text Classification, Summarization, Anomaly Detection, Other
    * Geospatial Mapping/Analysis
    * potential for Text Classification in next steps.
  * Sustainability, Health, Civic Tech, Voting, Housing, Policing, Budget, Education, Transportation, etc.
    * Sustainability, Environmental Preservation, Environmental Justice, Urban Forestry, Equity

*The following questions pertain to the datasets you used in your project.*   
*Motivation* 

* For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description. 

  * The datasets were all collected as part of the Canopy Change Assessment: 2014-2019 report comissioned by the Boston Parks and Recreation Department. It consists of metrics aggregated from satellite imagery and leaf-on LiDAR to paint a picture of canopy coverage. The Boston Parks and Recreation Department plans to collect the data every five years to inform the Urban Forest Plan, which focuses on how to prioritize, preserve, and grow tree canopy in Boston. Before this data was collected, there was a gap in knowledge of how much of Boston's tree canopy degrades or grows over time. After the data was collected, the University of Vermont published their tree canopy assessment report, which helped inform policy for the Urban Forest Plan. 

  * The Citywide Land Audit was collected in 2022 to identify areas of city owned land (parcels) that were vacant and could be used to improve the lives of Bostonians. 

*Composition*

* What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? What is the format of the instances (e.g., image data, text data, tabular data, audio data, video data, time series, graph data, geospatial data, multimodal (please specify), etc.)? Please provide a description.

  * There are not multiple types of instances for any dataset because each row represents a unique area of property. In the geospatial file of the dataset, the instances are represented by polygons for all datasets. 

  * The [Canopy Change Assessment: Tree Canopy Metrics](https://data.boston.gov/dataset/canopy-change-assessment-tree-canopy-metrics/resource/dc7dd2a1-7b81-48a6-b95f-32f8af8e35d0) dataset contains multiple files for download, which each group land differently. The datasets available for download include land grouped by parcel, neighborhood, ward, and census tract. To answer the questions in the project description, we focused on using the file named ["PARCELS Tree Canopy Metrics"]((https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::canopy-change-assessment-tree-canopy-change-metrics/explore?layer=8&location=42.312109%2C-71.032757%2C11.72) ), which aggregates land at the parcel level. In this dataset, each instance represents a piece of property in Boston owned by an individual, organization, or entity.  

   * The [Canopy Change Assessment: Neighborhoods Tree Canopy Metrics](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::canopy-change-assessment-tree-canopy-metrics/explore?layer=1) dataset has instances that represent a neighborhood. Each row contains columns that describe how much tree canopy coverage area and how much potential land there is in each neighborhood.

  * The [Canopy Change Assessment: Parcels Tree Canopy Change Metrics](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::canopy-change-assessment-tree-canopy-change-metrics/explore?layer=8&location=42.312109%2C-71.032757%2C11.72) dataset has instances that represent property at a parcel level, which essentially represents a specific piece of property that a person, entity, or organization owns, such as a home. Each instance contains further information about each piece of property. 
  * Tree_Canopy_Height_Change_2014_to_2019 dataset has instances that include:
    * A unique identifier for each (OBJECTID)
    * Each instance is classified as having either “Gain”, “Loss”, or “No Change” in tree canopy height from 2014 to 2019 (Class_name)
    * Tree canopy height in 2019 (CanHghtT2)
    * Tree canopy height in 2014 (CanHghtT1)
    * (Shape_Leng), (ShapeSTArea), (ShapeSTLength) are geospatial features to be used in GIS analysis

   * The [Citywide Land Audit](https://data.boston.gov/dataset/city-land-audit-public1) dataset has instances that represent a parcel of land owned by the City of Boston or a quasi-agency. Each row contains columns that describe the location and ownership of the parcels of land.



* How many instances are there in total (of each type, if appropriate)?  

  * For the [Canopy Change Assessment: Tree Canopy Metrics](https://data.boston.gov/dataset/canopy-change-assessment-tree-canopy-metrics/resource/dc7dd2a1-7b81-48a6-b95f-32f8af8e35d0) and [Canopy Change Assessment: Parcels Tree Canopy Change Metrics](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::canopy-change-assessment-tree-canopy-change-metrics/explore?layer=8&location=42.312109%2C-71.032757%2C11.72) dataset, there are 173,875 instances, which each represent a parcel of land, including one instance that represents all right-of-way areas. 

  * For the [Canopy Change Assessment: Neighborhoods Tree Canopy Metrics](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::canopy-change-assessment-tree-canopy-metrics/explore?layer=1) dataset, there are 17 instances of neighborhoods.

  * For the Tree_Canopy_Height_Change_2014_to_2019 dataset there are 1048575 instances.

  * The [Citywide Land Audit](https://data.boston.gov/dataset/city-land-audit-public1) dataset has 2940 instances that represent a parcel of land owned by the City of Boston or a quasi-agency. Each row contains columns that describe the location and ownership of the parcels of land.


* Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable). 

  * The datasets are a comprehensive collection of all possible area in Boston in 2014 and in 2019. 

* What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.  

  * Each instance represents a parcel of land and the data includes features either describing the parcel or the tree canopy on the parcels. The [Canopy Change Assessment: Tree Canopy Metrics](https://data.boston.gov/dataset/canopy-change-assessment-tree-canopy-metrics/resource/dc7dd2a1-7b81-48a6-b95f-32f8af8e35d0) contains 72 features. One of the key features is "PID", which is a 10-digit code that is a unique identifier for each parcel. In addition, we used the column "LU_GENERAL", which represent land use, to group tree canopy by land use. To answer the questions "What percentage of Boston's tree canopy is located on public land versus residential parcels?", "How does tree canopy coverage vary across neighborhoods and land use types?", "What are the trends in tree canopy loss or gain (2014-2019) for public and residential areas?", and "Which areas have the highest potential for expanding tree canopy, and are they public or residential spaces?", we used aggregated metrics from the Tree Canopy Metrics and Tree Canopy Change Metrics in order to calculate the percentages of area. We used the parcel ID's from the Citywide Land Audit to classify parcels as  city owned and we classified the rest of the parcels as "non-city owned." We specificaly used key fields, such as **TC_E_A**(Tree canopy existing area), **TC_Land_A** (Land area), **TC_P_A**(Possible area),**TreeCanopy**(2014 total canopy area baseline), **TreeCano_1** (2019 total canopy area), **Gain** (Tree canopy area gain), and **Loss**(Tree canopy area loss), in order to answer our questions. 

  * Other Columns include: 'FID', 'FID_Boston', 'BOSTON_LAN', 'FID_COB_FY', 'PID', 'CM_ID',
       'GIS_ID', 'OWNER', 'ST_NUM', 'ST_NAME', 'ST_NAME_SU', 'UNIT_NUM',
       'ZIPCODE', 'LU', 'PTYPE', 'LOTSIZE', 'MAIL_ADDRE', 'MAIL_CS',
       'MAIL_ZIP', 'OWN_OCC', 'GROSS_AREA', 'BLDG_AREA', 'AV_TOTAL', 'AV_LAND',
       'AV_BLDG', 'GROSS_TAX', 'NUM_FLOORS', 'PID_LONG', 'FULL_ADDRE', 'CITY',
       'STArea__', 'STLength__', 'Shape_STAr', 'Shape_STLe', 'LU_GENERAL',
       'TC_ID', 'Shape_Leng', 'OBJECTID', 'TC_ID_1', 'Total_A', 'Can_A',
       'Grass_A', 'Soil_A', 'Water_A', 'Build_A', 'Road_A', 'Paved_A',
       'Perv_A', 'Imperv_A', 'Can_P', 'Grass_P', 'Soil_P', 'Water_P',
       'Build_P', 'Road_P', 'Paved_P', 'Perv_P', 'Imperv_P', 'OBJECTID_1',
       'TC_ID_12', 'VALUE_0', 'TC_E_A', 'TC_Pv_A', 'TC_Land_A', 'TC_Pi_A',
       'TC_P_A', 'TC_E_P', 'TC_Pv_P', 'TC_P_P', 'TC_Pi_P', 'Shape__Area',
       'Shape__Length'

**EJ Communities Dataset**

| Field               | Type   | Description                                                                                          |
|---------------------|--------|------------------------------------------------------------------------------------------------------|
| Name                | String | Neighborhood name (e.g., Dorchester, Roxbury)                                                        |
| Canopy_pct          | Float  | Percent of land area under tree canopy                                                               |
| SV_key_nb           | Float  | Composite Vulnerability Score: average of LowIncome_pct, LEP_pct, Disability_pct                     |
| LowIncome_pct       | Float  | % of households below the poverty line                                                               |
| LEP_pct             | Float  | % of residents with Limited English Proficiency                                                      |
| Disability_pct      | Float  | % of residents reporting a disability                                                                |


* Is there any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include redacted text.   

  * The instance representing all rights-of-way, which are all roads, sidewalks, and streets in Boston, has missing data for multiple columns, including "OWNER" and "PID." This information is most likely not available because the polygon represents all streets so there would most likely be many owners rather than just one and there would most likely not be a unique "PID" since the street is not concentrated in a specific area, like a regular parcel of land would be. Otherwise all other rows are not missing any values. 
* Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them  
  * No. 
* Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.  
  * The record/polygon in the Tree Canopy Metrics dataset that represents all ROW data has "PID" = " " so it does not appear null despite not containing identifying information. 
* Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources,   

  * The dataset does not refer to external resources. It's geospatial data collected using LIDAR by the Boston Parks and Recreation Department.
  * Are there guarantees that they will exist, and remain constant, over time;  
  
    * As far as we know, the dataset should remain available on Analyze Boston. 
  * Are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created)?  
  
    * No
  * Are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points as appropriate.   

    * None of the datasets have restrictions. However, ArcGIS Pro was integral to being able to analyze the geospatial files available. 
* Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)? If so, please provide a description.   

  * None of the datasets have confidential information. All data was made publicly available by Analyze Boston. 
* Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.   

  * The dataset does not contain any data that may be offensive, insulting, threatening, or might otherwise cause anxiety. Most of the fields relate to tree canopy area or describing the parcel location.
* Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? If so, please describe how.   

  * Yes, the Tree Canopy Metrics and Canopy Change Metrics datasets contain the names of owners of parcels of land, including their addresses in Boston. 
* Dataset Snapshot, if there are multiple datasets please include multiple tables for each dataset. 

**Canopy Change Assessment: Parcels Tree Canopy Metrics dataset**
| Size of dataset | 85.5 MB |
| :---- | :---- |
| Number of instances | 173,875 |
| Number of fields  | 72 |
| Labeled classes | N/A |
| Number of labels  | N/A |

**Canopy Change Assessment: Tree Canopy Change Metrics dataset**
| Size of dataset | 74.9 MB |
| :---- | :---- |
| Number of instances | 173,875 |
| Number of fields  | 53 |
| Labeled classes | N/A |
| Number of labels  | N/A |

**Canopy Change Assessment: Neighborhoods Tree Canopy Metrics**
| Size of dataset | 7 KB |
| :---- | :---- |
| Number of instances | 17 |
| Number of fields  | 40 |
| Labeled classes | N/A |
| Number of labels  | N/A |

**Citywide Land Audit**
| Size of dataset | 1.1 MB |
| :---- | :---- |
| Number of instances | 2940 |
| Number of fields  | 10 |
| Labeled classes | N/A |
| Number of labels  | N/A |

**Tree_Canopy_Height_Change_2014_to_2019**
| Size of dataset | 319 MB |
| :---- | :---- |
| Number of instances | 4,560,574 |
| Number of fields  | 7 |
| Labeled classes | 3 (Gain, Loss, No Change) |
| Number of labels  | 1 (Class_name) |


  
*Collection Process*

* What mechanisms or procedures were used to collect the data (e.g., API, artificially generated, crowdsourced \- paid, crowdsourced \- volunteer, scraped or crawled, survey, forms, or polls, taken from other existing datasets, provided by the client, etc)? How were these mechanisms or procedures validated?  
  * The data collecated used 2019 high resolution land cover and 2019 leaf-on LiDAR, which looked at tree canopy from an aerial view.
* If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?  
  * The Canopy Change Assessment: Tree Canopy Change Metrics dataset contains a snapshot of tree canopy taken in 2014 and 2019. However, the Canopy Change Assessment: Tree Canopy Metrics dataset only shows information on tree canopy in 2019. This is not necessarily a sampling strategy, but the nature of the data is that it is collected every five years as a snapshot of the current period of time.
* Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created. 
  * The tree canopy LIDAR data was collected in 2014 and 2019. This matches the timeframes in the [Canopy Change Assessment: 2014-2019 report](https://storymaps.arcgis.com/stories/43dccf3f51104a86ac8c4790a13e9d71)

*Preprocessing/cleaning/labeling* 

* Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.   
  * We only labeled the polygon representing right-of-way to have a "PID" and "OWNER" equal to "ROW" because we wanted to distinguish it as a its own category outside of city vs non-city owned because there are both publicly and privately owned streets that we cannot distinguish between yet with our given data. 
  * To utilize the Citywide Land Audit, we used a series of spatial joins and overlay intersections to classify polygons of canopy as city owned and non-city owned. This file is located in the Google Drive](https://drive.google.com/file/d/1PXy_gCq0qiHonpmPounpgT8sgUCpyZrE/view?usp=drive_link).

  * For the Environmental Justice Communities Analysis: 
    * **Sources**: SVI data from City of Boston; canopy metrics from Boston Open Data  
    * **Cleaning**: Joined in Python notebook (`EJ_Weber_CT.ipynb`); computed `SV_key_nb`  
    * **Export**: GeoJSON published in ArcGIS Online; CSV via Data → Export → CSV  
* Were any transformations applied to the data (e.g., cleaning mismatched values, cleaning missing values, converting data types, data aggregation, dimensionality reduction, joining input sources, redaction or anonymization, etc.)? If so, please provide a description. 
  * The PID needed to be converted to a string data type to ensure that any 10-digit codes that started with a 0 were read in properly. The column 'ownership' was created in order to distinguish between city-owned and non-city owned parcels of land. We classified based on whether the column "OWNER" fit our definition of city-owned, which can be found in our analysis_for_question_1_3_4.ipynb in our Github under question 1.
  * In order to recalculated the geometry of tree canopy polygons and classify their ownership, we had to perform a series of spatial joins and overlay intersect functions, which can be found in the ArcGIS Pro file in our [Google Drive](https://drive.google.com/file/d/1PXy_gCq0qiHonpmPounpgT8sgUCpyZrE/view?usp=drive_link) Raw Data folder. However, this file was mainly used for preprocessing instead of visualization and can only be opened on a computer that has ArcGIS Pro downloaded, which requires Windows. 
* Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.  
  * The "raw" data is the same as before: https://github.com/BU-Spark/ds-bcc-tree-canopy/tree/dev/datasets
* Is the code that was used to preprocess/clean the data available? If so, please provide a link to it (e.g., EDA notebook/EDA script in the GitHub repository). 
  * https://github.com/BU-Spark/ds-bcc-tree-canopy/tree/dev/analysis_for_question_1_3_4.ipynb

*Uses* 

* What tasks has the dataset been used for so far? Please provide a description.   
  * The Citywide land audit dataset has been used to distinguish between city-owned and non-city owned parcels of land by considering all Parcel ID'S in the dataset to be owned by the City of Boston, or its related agencies. By doing so, we were able to calculate the percentage of tree canopy protected vs not protected by the tree ordinance. 
  In addition, the Tree Canopy Metrics and Tree Canopy Change data was used to calculate tree canopy coverage across neighborhoods and land use types, trends in tree canopy loss or gain (2014-2019) for city-owned and non-city owned areas, areas with the highest potential for expanding tree canopy, and disparities in tree canopy coverage in neighborhoods using the columns provided in the dataset. These datasets were also used to calculate tree canopy percentages by neighborhood and by land use, estimate potential areas for expanding tree canopy (categorized by public, private, and ROW) and evaluate inequities in tree canopy coverage across neighborhoods, particularly in marginalized communities using environmental justice (EJ) data.

* What (other) tasks could the dataset be used for?  
  * The dataset can be used to do further analysis by utilizing other datasets that contain information on publicly vs privately owned roads in order to further distinguish all land in Boston that is protected by the ordinance. Population datasets can be combined with these datasets to understand how much tree canopy there is in densely populated areas and determine if there are disparities in tree canopy for communities. 
  * Understanding trends between 2019 data and the newly collected 2024 LIDAR data that will be published 
  * Support policy evaluation by assessing how the tree ordinance impacted canopy growth.
  * Identifying heat islands or air quality issues that could be associated with areas with low canopy for public health initiatives.
  * Planning urban tree canopy growth projects by highlighting areas of with high potential but low current coverage



* Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?   
  * The tree canopy area is already aggregated in the datasets as US Survey Feet units, but if someone wanted to use a different map units or different aggregation of land parcels from a different year, the geographic metrics would most likely have to be recalculated. For example, existing tree canopy, canopy gain/loss, and potential canopy area would all need to be recalculated if you wanted to use the 2022 version of parcels. 
  * In the Tree Canopy Metrics Parcels dataset, the ROW (Right of Way) areas were grouped together without detailed ownership breakdowns, affecting fine-grained analysis.
  * The Tree Canopy Metrics uses 2019 parcels, while Citywide Land Audit data is from 2022, meaning ownership might have changed.

* Are there tasks for which the dataset should not be used? If so, please provide a description.
  * This dataset only covers 2019 tree canopy in depth. While 2014 tree canopy can be observed in the dataset Tree Canopy Change Metrics, the focus of the dataset is to take the absolute difference in tree canopy between 2014 and 2019. This is historical data and does not reflect current canopy.
  * Due to changes in parcel ownership, the data is an outdated source of truth. 
  * The dataset is also limited to classifying tree canopy area, but not necessarily the specific center point where trees are physically planted due to the limitations of LIDAR scans. 


*Distribution*

* Based on discussions with the client, what access type should this dataset be given (eg., Internal (Restricted), External Open Access, Other)?
  * Open Access. All data used for this project is publicly available on Analyze Boston.

*Maintenance* 

* If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description. 
  * Yes, there are many other datasets that can be used to enrich the analysis that can be done in support of extending the tree ordinance to non-city owned trees, such as data on population density to determine if there are disparities in which residential areas have the most tree canopy coverage. Also, parks highly skew the dataset in neighborhoods like Jamaica Plains, which can be accounted for more in future analysis/questions. 
  
  * In addition, our method to distinguish between city-owned and non-city owned trees using the [Citywide Land Audit](https://www.boston.gov/housing/citywide-land-audit) had some short comings as there were parcel differences between the audit and the Tree Canopy Metric datasets, which meant that 34 parcels that were in the audit were not captured in our analysis of tree canopy gain/loss or potential tree canopy area because we didn't have the geospatial datasets to be able to recalculate those metrics. A future team could work on a methodology to reconcile these parcel differences or obtain the raw geospatial files from Analyze Boston to retrace how the Tree Canopy Metrics dataset did calculate gain/loss and potential tree canopy area fields from the LIDAR scans.  

  * Current mechanisms: GitHub repository (with README, DATASETDOC.md, and Jupyter Notebooks) is already set up for version control and collaboration.Others could fork the GitHub repository to add newer data (e.g., post-2019 tree canopy layers). They can correct ownership classifications as updated data becomes available. They could also integrate additional datasets like newer EJ communities files, future canopy assessments, or population data.


*Other*

* Is there any other additional information that you would like to provide that has not already been covered in other sections?
  * None

