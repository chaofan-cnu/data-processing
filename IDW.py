import arcpy
from arcpy import env
import numpy as np
env.workspace = "E:/2020/arcgisdata/idw"
inPointFeatures = "test.shp"
fields = arcpy.ListFields("test.shp")
list=[]
for field in fields:
    list.append(field.name)
arcpy.CheckOutExtension("3D")
index = 3
colnums = 65
cellSize = 300
outRasterPath = "E:/2020/arcgisdata/idw/"
while index<colnums:
    strindex = str(index)
    outRaster = outRasterPath +strindex
    zField = list[index]
    outRaster = arcpy.Idw_3d(inPointFeatures, zField, outRaster,cellSize)
    index = index + 1
    
    
    
  

   
