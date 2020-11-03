"""
Name: Lily Jim
Updated: 11/2/2020
Description: update display of information using symbology templates
"""
    
import arcpy # import ArcGIS functions

"""PDF ---------------------------------------------------------------------------------------------------------"""
'''Change symbology of states to a choropleth of crude rate'''
def changeDisplayPDF(years, wrkspc, symbology, category):
    statesSymbology = symbology
    naSymbology = arcpy.mapping.Layer(wrkspc + "\\layout\\naSymbology.lyr") # Set North America to a gray color
    for year in years: # for each year
        document = wrkspc + "\\" + str(year) + "\\" + category + "\\" + category + "PDF" + ".mxd" # define map document path
        mxd = arcpy.mapping.MapDocument(document) # open map document
        dfs = arcpy.mapping.ListDataFrames(mxd) # get list of data frames
        for df in dfs: # for each data frame
            lyrs = arcpy.mapping.ListLayers(mxd, "", df) # get list of layers
            arcpy.mapping.UpdateLayer(df, lyrs[1], statesSymbology) # update states layer to match wanted symbology
            arcpy.mapping.UpdateLayer(df, lyrs[2], naSymbology) # update N.A. layer to match wanted symbology
        
        mxd.save() # save the document
    return

"""JPG ---------------------------------------------------------------------------------------------------------"""
'''Change symbology of states to a choropleth of crude rate'''
def changeDisplayJPG(years, wrkspc, symbology, category):
    statesSymbology = symbology
    for year in years: # for each year
        document = wrkspc + "\\" + str(year) + "\\" + category + "\\" + category + ".mxd" # define map document path
        mxd = arcpy.mapping.MapDocument(document) # open map document
        dfs = arcpy.mapping.ListDataFrames(mxd) # get list of data frames
        for df in dfs: # for each data frame
            lyrs = arcpy.mapping.ListLayers(mxd, "", df) # get list of layers
            arcpy.mapping.UpdateLayer(df, lyrs[1], statesSymbology) # update states layer to match wanted symbology
        
        mxd.save() # save the document
    return