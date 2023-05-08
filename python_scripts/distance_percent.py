def percent_of_tot(Distance):
  import arcpy  
  global list  
  if len(list) == 0:
    with arcpy.da.SearchCursor(r"Z:\Studies\T05\04 GIS MN1\Projekt\Kayak2019\ArcGIS\Database\kayak_2019_project_routes.gdb\", ["Acres"]) as cursor:  
      for row in cursor:  
        list.append(row[0]) 
    del cursor, row 
  S = sum(list)  
  return acres / S * 100
__esri_field_calculator_splitter__
foo(!Distance!)
