"""
Name: Lily Jim
Updated: 11/2/2020
Description: create maps from CDC data
"""

import arcpy # import ArcGIS functions
from arcpy import env # import env for ease of use
import datetime as dt # import access to time

# Import related files
import createDocuments
import modifyElements
import createChoropleth

# Set path to code
wrkspc = r"C:\Users\<your path here>\Thesis\Code" # define workspace path

# Toggle output
pdf = True
jpg = True

"""PDF ---------------------------------------------------------------------------------------------------------"""
def createPDFs(years, category, title, symbology):
    # Create standalone PDFs
    print "Starting PDFs for " + category
    pdfBlankDocument = wrkspc + "\\layout\\pdfLayout.mxd" # path to document template
    
    # Import data and set up frames
    createDocuments.setUpPDF(years, wrkspc, pdfBlankDocument, category)
    print "Done with data frame setup"
    
    # Add text elements
    modifyElements.configTextPDF(years, wrkspc, category, title)
    print "Done with text configuration"

    # Adjust north arrow
    modifyElements.configNorthArrow(years, wrkspc, category)
    print "Done with north arrow configuration"

    # Change map display into choropleth
    createChoropleth.changeDisplayPDF(years, wrkspc, symbology, category)
    print "Done with display changes"

    # Move legend
    modifyElements.configLegendPDF(years, wrkspc, category)
    print "Done with legend configuration"

    # Export to pdf
    for year in years:
        currentDataSet = "data" + str(year) # define currect data set
        document = wrkspc + "\\" + str(year) + "\\" + category + "\\" + category + "PDF" + ".mxd" # define map document path
        docPDF = wrkspc + "\\results\\pdfs\\" + category + str(year) + ".pdf" # define pdf path
        mxd = arcpy.mapping.MapDocument(document) # open map document
        arcpy.mapping.ExportToPDF(mxd, docPDF) # export map document to pdf
        print "Exported " + str(year)
    print "Done exporting " + category + " PDFs\n"
    return
    
"""JPG ---------------------------------------------------------------------------------------------------------"""    
def createJPGs(years, category, title, symbology):
    # Create images
    print "Starting JPGs for " + category
    jpgBlankDocument = wrkspc + "\\layout\\imageLayout.mxd" # path to document template
    
    # Import data and set up frames
    createDocuments.setUpJPG(years, wrkspc, jpgBlankDocument, category)
    print "Done with data frame setup"
    
    # Add text elements
    modifyElements.configTextJPG(years, wrkspc, category, title)
    print "Done with text configuration"

    # Change map display into choropleth
    createChoropleth.changeDisplayJPG(years, wrkspc, symbology, category)
    print "Done with display changes"

    # Move legend
    modifyElements.configLegendJPG(years, wrkspc, category)
    print "Done with legend configuration"

    # Export to jpg
    for year in years:
        currentDataSet = "data" + str(year) # define currect data set
        document = wrkspc + "\\" + str(year) + "\\" + category + "\\" + category + ".mxd" # define map document path
        docJPG = wrkspc + "\\results\\jpgs\\" + category + str(year) + ".jpg" # define jpg path
        mxd = arcpy.mapping.MapDocument(document) # open map document
        arcpy.mapping.ExportToJPEG(mxd, docJPG, resolution=300) # export map document to jpg
        print "Exported " + str(year)
    print "Done exporting " + category + " JPGs\n"
    return

"""Main ---------------------------------------------------------------------------------------------------------"""
def main():
    # Call functions to produce wanted output of pdfs
    env.workspace = wrkspc # set GIS workspace
    env.overwriteOutput = True # allow files to be overrided
    
    years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018] # define all the years of data
    categories = ["allCauses", "homicide", "suicide", "legalIntervention", "unintentional", "undetermined"]
    titles = ["", " - Homicides", " - Suicides", " - Legal Intervention", " - Unintentional", " - Undetermined Intent"] 
    
    # symbology templates:
    allCauses = arcpy.mapping.Layer(wrkspc + "\\layout\\allCausesSymbology.lyr")
    homicide = arcpy.mapping.Layer(wrkspc + "\\layout\\homicideSymbology.lyr")
    suicide = arcpy.mapping.Layer(wrkspc + "\\layout\\suicideSymbology.lyr")
    legalIntervention = arcpy.mapping.Layer(wrkspc + "\\layout\\legalInterventionSymbology.lyr")
    unintentional = arcpy.mapping.Layer(wrkspc + "\\layout\\unintentionalSymbology.lyr")
    undetermined = arcpy.mapping.Layer(wrkspc + "\\layout\\undeterminedSymbology.lyr")
    
    symbologies = [allCauses, homicide, suicide, legalIntervention, unintentional, undetermined]
    
    # To test a single year and category:
    #years = [2015]
    #categories = ["allCauses"]
    #titles = [""] # note: allCauses category does not extended default title, so append empty string
    #symbologies = [allCauses]
    
    i = 0
    num = len(categories)
    while i < num:
        if pdf:
            createPDFs(years, categories[i], titles[i], symbologies[i])
        if jpg:
            createJPGs(years, categories[i], titles[i], symbologies[i])
        i += 1
    return

if __name__ == "__main__":
    print dt.datetime.now() # print starting time
    main() # run main
    print dt.datetime.now() # print finishing time
