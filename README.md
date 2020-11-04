# Improving Research with Big Data Visualization: A Look at Firearm Deaths in the United States

**A Thesis by Lily Jim**

---

## Abstract
*Finding the right questions to conduct research on can be challenging. Even after discovering the cause of a problem, effectively communicating findings based off of statistical information to the American public proves to be yet another common hurdle. Visualizing big data can help find the right questions to ask, and it provides a way to graphically represent the information for the general public.*

*Big data is becoming more common, so we should adapt the way we approach research. Starting with the data itself, instead of a hypothesis, can be beneficial. By visualizing big data, patterns can be discovered that could have gone unnoticed when confined to answering a specific question. Starting with graphical information also allows studies to easily include images in reports, making them more digestible for the average consumer. It also allows an emphasis to be put on visual consistency, which is necessary to compare compilations of images. To exemplify the benefits of starting with visualized big data, maps depicting twenty years of data on deaths caused by firearms in the United States are produced. The process to produce more maps using data from the Centers for Disease Control and Prevention is included.*

---

## About the Code

This code is designed to be used with data from the CDC's WONDER database and work with ESRI's ArcMap 10.5. 

Data on deaths caused by firearms is provided in the [dataTables](https://github.com/lmjim/Thesis/tree/main/Code/dataTables) folder.
The results the code produces when run on this data is provided separately from the code, under [Example_Results](https://github.com/lmjim/Thesis/tree/main/Example_Results). 

The included five scripts produce map documents, displaying the data in relations to states, and exports to pdf and/or jpg.

*Disclaimer: Not affiliated with ESRI or CDC*  
**CDC data has restrictions on it, see [terms of use](https://wonder.cdc.gov/mcd-icd10.html "CDC Wonder Database").**

---

## Running the Example

1. Create some empty directories for the code to reference (these should be located in Code):
    * 20 folders labeled for each year 1999-2018 (ex. 2015)  
      Each year should contain a folder for each category:  
      + allCauses
      + suicide
      + homicide
      + legalIntervention
      + unintentional
      + undetermined
    * Another folder labeled "results"
      This should contain two sub-folders:
      + jpgs
      + pdfs
2. The following files are provided:
    * dataTables folder with a subfolder for each category, each containing the csv files from the CDC
    * shapeFiles folder containing the shapefiles used in this project
    * layout folder containg a .lyr file for each category (for symbology) and two .mxd (for pdf or jpg layout)
    * The following Python files:  
      + finalproject  
      + createDocuments  
      + modifyElements  
      + getStats  
      + createChoropleth
3. Open *IDLE (Python GUI)* or *Python (command line)* included with ArcGIS
4. Edit finalproject.py
    * Change the wrkspc path found on line 17
      + The path should match the path to the Thesis/Code directory on your computer
    * Choose True/False for pdf and jpg (lines 20-21) depending on the results you want to produce
5. Run finalproject.py

---

## Using Other Data

1. Create some empty directories for the code to reference
    * A folder for each year the data covers (ex. 2015)  
    Each year should contain a folder for each category chosen  
    * Another folder labeled "results"
      This should contain two sub-folders:
      + jpgs
      + pdfs
2. Replace the contents of dataTables
    * There should be a folder for each category chosen
    Each of those folders should contain your data (.csv files)  
    Follow the naming convention used by the example  
    "data" followed by the year and ending in ".csv"
3. Create templates
    * <TODO add instructions>
4. Open *IDLE (Python GUI)* or *Python (command line)* included with ArcGIS
5. Edit finalproject.py
    * Change the wrkspc path found on line 17
      + The path should match the path to the Thesis/Code directory on your computer
    * Choose True/False for pdf and jpg (lines 20-21) depending on the results you want to produce
    * <TODO add instructions>
6. Run finalproject.py
