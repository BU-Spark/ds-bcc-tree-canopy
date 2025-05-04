# Data Dictionary

| Field                         | Type    | Description                                                            |
|-------------------------------|---------|------------------------------------------------------------------------|
| **Name**                      | String  | Neighborhood name                                                      |
| **Canopy_pct**                | Float   | Tree canopy coverage (%)                                               |
| **SV_key_nb**                 | Float   | Social Vulnerability Score: average of Low Income %, LEP %, Disability %|
| **LowIncome_pct**             | Float   | % of households below the poverty line                                 |
| **LEP_pct**                   | Float   | % of residents with Limited English Proficiency                        |
| **Disability_pct**            | Float   | % of residents reporting a disability                                  |

> **SV_key_nb** is computed by averaging the three metrics (LowIncome_pct, LEP_pct, Disability_pct) because those showed the strongest negative correlations with canopy cover.
