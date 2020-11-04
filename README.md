# Improving Research with Big Data Visualization: A Look at Firearm Deaths in the United States

# About This Project

The script finalproject.py creates ArcMap documents, exporting them to pdf. The information mapped comes from the CDC.
The data contains information on the number of deaths caused by firearms in the United States, broken up by year and state.
This data is joined to shapefiles to produce a standardized map for each year.
The pdfs this script creates are already provided in the results folder.

*Disclaimer: Not affiliated with ESRI or CDC*  
**CDC data has restrictions on it**, see [terms of use](https://wonder.cdc.gov/mcd-icd10.html "CDC Wonder Database").

---

## Files Needed to Run

All files needed to run are provided in this repo:

1. 20 folders labeled for each year 1999-2018 and one labeled results  
   * Each year should contain a folder for each category:
        * allCauses
        * suicide
        * homicide
        * legalIntervention
        * unintentional
        * undetermined
2. dataTables folder with a subfolder for each category, each containing the csv files from the CDC
3. shapeFiles folder containing the shapefiles used in this project
4. layout folder containg a .lyr file for each category (for symbology) and two .mxd (for pdf or jpg layout)
5. The following python files:  
   + finalproject  
   + createDocuments  
   + modifyElements  
   + getStats  
   + createChoropleth

---

## How to Run

If you are using IDLE, make sure to open version that came with your ArcGIS suite.

1. Open finalproject.py
2. Change the wrkspc path found on line 17  
   + The path should match the path to the Thesis/Code directory on your computer
3. Choose True/False for pdf and jpg (lines 20-21) depending on the results you want to produce
4. Run finalproject.py
