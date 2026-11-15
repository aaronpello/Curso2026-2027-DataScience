# Hands-on Assignment 3 – Self assessment

## Checklist

**The "openrefine" directory:**
- [x] Contains the JSON file with the operations performed over the data.

**The "csv" directory:**
- [x] Contains the updated versions of the datasets (`*-updated.csv`).

**The "selfAssessmentHandsOn3.md" file:**
- [x] Includes the self-assessment of the assignment.

## Comments on self-assessment

During this assignment, we used OpenRefine to clean and prepare the datasets for the RDF generation phase. Based on our previous data analysis, the team performed the following key cleaning operations:

1. **Date Normalization (Air Quality Dataset):** We identified that a significant portion of the rows had the day and month swapped in the `Fecha` column. We used OpenRefine transformations to standardize all dates to the `YYYY-MM-DD` format.
2. **Time Standardization (Air Quality Dataset):** The `Hora` column had inconsistent formats (e.g., `4:00` vs `14:00:00`). We normalized the format to ensure consistency across the dataset.
3. **Area Values Correction (Districts Dataset):** We observed that the `gis.gis.DISTRITOS.area` column had an error where some values were multiplied by 10. We applied a GREL expression in OpenRefine to divide those specific values by 10, correcting the surface area calculations.
4. **Preservation of Multiple District Geometries:** During the cleaning process, we identified that district code 17 (POBLATS DEL NORD) appears in four different records, each containing a distinct geometry. These records were initially at risk of being incorrectly treated as duplicates. We decided to preserve all four records, keeping their original `_id` and `WKT` values. This is important because each geometry must remain identifiable and available for its corresponding DistrictGeometry resource in our ontology.

All cleaned datasets have been exported as `*-updated.csv` and the OpenRefine operation histories have been saved as JSON files.
