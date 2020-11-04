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
    ("data" followed by the year and ending in ".csv")
3. Create symbology templates
    * For this step you will need to work in ArcMap directly
    * Add the US_states shapefile to the map document
    * Add the csv file with the minimum crude rate for the category
    * Join the csv file to the shapefile
    * Change the symbology to use graduated colors (such as light red to dark red)
    * Manually set the classification to be the equivalent of equal intervals across the entire category's data  
      You cannot simply select the method because it will set the breaks according to only that year's data  
      You may consider having the last class cover a larger interval due to extraneous values  
    * Set the labels to use the same precision your data uses
    * Save the layer as file  
    * This will be used as a symbology template
    * Repeat this step for each category
4. The following files are provided:
    * shapeFiles folder containing the shapefiles used in this project
    * layout folder containg two .mxd (for pdf or jpg layout)
    * The following Python files:  
      + finalproject  
      + createDocuments  
      + modifyElements  
      + getStats  
      + createChoropleth
5. Open *IDLE (Python GUI)* or *Python (command line)* included with ArcGIS
6. Edit finalproject.py
    * Change the wrkspc path found on line 17
      + The path should match the path to the Thesis/Code directory on your computer
    * Choose True/False for pdf and jpg (lines 20-21) depending on the results you want to produce
    * Update lines 99-111
      + *years* is a list of all the years the dataset covers
      + *categories* is a list of the CDC categories the dataset covers  
        the names in this list match the names of the folders within each folder year and dataTables
      + each entry in *titles* appends the default title  
        the order corresponds to the order of *categories*  
            - Note: to change the default title, edit lines 66 and 179 in modifyElements.py
      + The symbology templates refer to the templates created in step 3  
            - Update/Remove/Create the paths to each layer file  
            - Make sure to update the *symbologies* list on line 111
     * Note: the first time you run this code on your own dataset, you may want to limit the number of years or categories  
         You can update and use lines 114-117 instead of lines 99-101, 111 to run a small test
7. Run finalproject.py
