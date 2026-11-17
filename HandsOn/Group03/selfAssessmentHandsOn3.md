# Self-assessment Hands-on 3 - Group03

- [x] The datasets were imported into OpenRefine
- [x] The openrefine directory has a JSON file with the operations done over the data
- [x] The csv directory has the updated versions of the datasets (*-updated.csv)
- [x] The data were cleaned to remove errors
- [x] The data were transformed to make the RDF generation easier

## Comments on the self-assessment (If required)

We imported into OpenRefine the two datasets we chose in Hands-on 1 (the air quality stations and the hourly measurements) and saved the operations of each one in the openrefine folder. The cleaned files are in the csv folder with the "-updated" ending, and we kept the original files too.

In the stations file we fixed some addresses that had extra spaces, we removed the coordinate columns that were repeated in other formats and kept only the latitude and longitude in decimal degrees, we changed the start date to the yyyy-mm-dd format and we changed the pollutant columns from "X" or empty to true/false.

In the hourly file we added the full station code (for example 28079004) so it can be joined with the stations file, and a date column in yyyy-mm-dd format. Then we removed the columns that were not needed anymore. We decided to keep one row per day with the 24 hours in columns, because one row per hour would make the file too big. We will split the hours when we generate the RDF.

We did not change the measured values or their flags, because we still don't know exactly what the flags mean. We also left empty the street fields that are missing for two stations.

After cleaning we checked that both files still have the same number of rows as the original ones and that all the station codes of the hourly file exist in the stations file.
