"""
Name: Lily Jim
Updated: 11/2/2020
Description: configure document elements to be ready to export
"""

import arcpy # import ArcGIS functions
import getStats # import related file

"""PDF ---------------------------------------------------------------------------------------------------------"""
'''Create and configure all text elements'''
def configTextPDF(years, wrkspc, category, titleStr):
    info = False
    if category == "allCauses":
        info = True
    for year in years:
        currentDataSet = "data" + str(year) # define currect data set
        document = wrkspc + "\\" + str(year) + "\\" + category + "\\" + category + "PDF" + ".mxd" # define map document path
        mxd = arcpy.mapping.MapDocument(document) # open map document

        # Create a total of 8 textboxes
        elemlist = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT") # get list of text elements
        i = 0
        j = 5
        if info:
            j = 7
            totalDeaths = getStats.getTotal(wrkspc, currentDataSet, document) # get total number of deaths for the year (used later on)
            maxDeaths = getStats.getMax(wrkspc, currentDataSet, document) # get top two states with worst number of deaths for the year
            maxCrudeRate = getStats.getCrudeMax(wrkspc, currentDataSet, document, category) # get top two states with worst rate of death for the year
        while i < j:
            elemlist[0].clone() # element 0 is a textbox, so clone it
            i = i + 1
        del elemlist
        
        # Modify text elements
        elemlist = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT") # get current list of text elements
        note = elemlist[0] # define variable
        note.name = "note" # set element name
        hawaii = elemlist[1] # define variable
        hawaii.name = "hawaiiLabel" # set element name
        hawaii.text = "Hawaii" # set what the text says
        alaska = elemlist[2] # define variable
        alaska.name = "alaskaLabel" # set element name
        alaska.text = "Alaska" # set what the text says
        contUS = elemlist[3] # define variable
        contUS.name = "contUSLabel" # set element name
        contUS.text = "Contiguous United States" # set what the text says
        sources = elemlist[4] # define variable
        sources.name = "sources" # set element name
        sources.text = "Sources: NYU Spatial Data Repository; United States Census Bureau; Centers for Disease Control and Prevention, CDC" # set what the text says
        author = elemlist[5] # define variable
        author.name = "author" # set element name
        author.text = "Created by: Lily Jim" # set what the text says
        if info: # these statistics are not accuracte when there is suppression
            note.text = "* Crude Rate is per 100,000 based on state's population" # set what the text says
            analysis = elemlist[6] # define variable
            analysis.name = "analysis" # set element name
            analysis.text = maxDeaths[0] + " has the highest total number of deaths followed by " + maxDeaths[1] + ".\n" + maxCrudeRate[0] + " has the highest crude rate followed by " + maxCrudeRate[1] + "." # set what the text says
            total = elemlist[7] # define variable
            total.name = "total" # set element name
            total.text = "Total Number of Deaths Caused by Firearms: " + str(totalDeaths) # set what the text says
        else:
            note.text = "* Crude Rate is per 100,000 \n  based on state's population\n-\nThe CDC suppresses data\nin areas with death counts \nof 9 or fewer" # when there's no statistics, there's suppression
        title = elemlist[j+1] # title is the last item in the elemlist
        title.name = "title" # set element name
        title.text = "Deaths Caused by Firearms in " + str(year) + titleStr # set title

        # Set text positions
        # Note
        note.fontSize = 10.0
        if info:
            note.elementHeight =  0.1552
            note.elementWidth = 3.447
            note.elementPositionX = 6.45
            note.elementPositionY = 1.85
            # Analysis
            analysis.fontSize = 9.53
            analysis.elementHeight = 0.30
            analysis.elementWidth = 3.9645
            analysis.elementPositionX = 6.2
            analysis.elementPositionY = 2.1
            # Total
            total.fontSize = 12.89
            total.elementHeight = 0.20
            total.elementWidth = 4.1882
            total.elementPositionX = 6.1
            total.elementPositionY = 2.45
        else:
            note.elementHeight =  0.9537
            note.elementWidth = 1.764
            note.elementPositionX = 6.9
            note.elementPositionY = 1.6
        # Hawaii
        hawaii.fontSize = 10.0
        hawaii.elementHeight = 0.150
        hawaii.elementWidth = 0.4028
        hawaii.elementPositionX = 3.717
        hawaii.elementPositionY = 1.8
        # Alaska
        alaska.fontSize = 10.0
        alaska.elementHeight = 0.15
        alaska.elementWidth = 0.4028
        alaska.elementPositionX = 1.7172
        alaska.elementPositionY = 1.8
        # Contiguous US
        contUS.fontSize = 12.89
        contUS.elementHeight = 0.20
        contUS.elementWidth = 2.0296
        contUS.elementPositionX = 6.8
        contUS.elementPositionY = 2.8
        # Sources
        sources.fontSize = 9.67
        sources.elementHeight = 0.150
        sources.elementWidth = 7.484
        sources.elementPositionX = 2.7
        sources.elementPositionY = 7.3
        # Author
        author.fontSize = 9.66
        author.elementHeight = 0.150
        author.elementWidth = 1.1786
        author.elementPositionX = 1.1
        author.elementPositionY = 7.3
        # Title
        title.fontSize = 19.33
        title.elementHeight = 0.30
        title.elementWidth = 4.2979
        title.elementPositionX = 3.3511
        title.elementPositionY = 7.45

        # Save the document
        mxd.save()
    return

'''Change the size and placement of the north arrow'''
def configNorthArrow(years, wrkspc, category):
    for year in years:
        document = wrkspc + "\\" + str(year) + "\\" + category + "\\" + category + "PDF" + ".mxd" # define map document path
        mxd = arcpy.mapping.MapDocument(document) # open map document
        northArrow = arcpy.mapping.ListLayoutElements(mxd, "MAPSURROUND_ELEMENT", "North Arrow")[0] # get north arrow
        northArrow.name = "northArrow"
        northArrow.elementHeight = 0.35
        northArrow.elementWidth = 0.168
        northArrow.elementPositionX = 1.05
        northArrow.elementPositionY = 3.15

        # Save document
        mxd.save()
    return

'''Change size and placement of the legend'''
def configLegendPDF(years, wrkspc, category):
    for year in years:
        document = wrkspc + "\\" + str(year) + "\\" + category + "\\" + category + "PDF" + ".mxd" # define map document path
        mxd = arcpy.mapping.MapDocument(document) # open map document
        legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT")[0] # get legend
        legend.elementHeight = 1.6
        legend.elementWidth = 0.9857
        legend.elementPositionX = 5.1
        legend.elementPositionY = 1.2

        # Save document
        mxd.save()
    return

"""JPG ---------------------------------------------------------------------------------------------------------"""
'''Create and configure all text elements'''
def configTextJPG(years, wrkspc, category, titleStr):
    for year in years:
        document = wrkspc + "\\" + str(year) + "\\" + category + "\\" + category + ".mxd" # define map document path
        mxd = arcpy.mapping.MapDocument(document) # open map document
        
        # Modify text elements
        elemlist = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT") # get current list of text elements
        note = elemlist[0] # define variable
        note.name = "note" # set element name
        note.text = "* Crude Rate is per 100,000\nbased on state's population" # set what the text says
        title = elemlist[1] # define variable
        title.name = "title" # set element name
        title.text = "Deaths Caused by Firearms in " + str(year) + titleStr # set title

        # Set text positions
        # Note
        note.fontSize = 8.0
        note.elementHeight =  0.2519
        note.elementWidth = 1.4082
        note.elementPositionX = 7.5418
        note.elementPositionY = 0.05
        # Title
        title.fontSize = 14.0
        title.elementHeight = 0.2172
        title.elementWidth = 3.2746
        title.elementPositionX = 0.8627
        title.elementPositionY = 3.9328

        # Save the document
        mxd.save()
    return

'''Change size and placement of the legend'''
def configLegendJPG(years, wrkspc, category):
    for year in years:
        document = wrkspc + "\\" + str(year) + "\\" + category + "\\" + category + ".mxd" # define map document path
        mxd = arcpy.mapping.MapDocument(document) # open map document
        legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT")[0] # get legend
        legend.elementHeight = 1.5303
        legend.elementWidth = 0.9855
        legend.elementPositionX = 7.9145
        legend.elementPositionY = 0.35

        # Save document
        mxd.save()
    return
