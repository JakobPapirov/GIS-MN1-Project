def percent_of_tot(Distance):
  import arcpy  
  global list  
  if len(list) == 0:
    with arcpy.da.SearchCursor(r"Z:\Studies\T05\04 GIS MN1\Projekt\Kayak2019\ArcGIS\Routes\route_actual_västerås_västerås", ["Distance"]) as cursor:  
      for row in cursor:  
        list.append(row[0]) 
    del cursor, row 
  S = sum(list)  
  return Distance / S * 100
