"""
GIS Development Exercise Scenario:
Among a list of 28 settlements for which we have lat/lon coordinates, we have to identify 10 settlements having the highest population living in their proximity (max 15km).
 
Input datasets: 
settlements.csv (fields: name, lat_WGS84, lon_WGS84)
pop_density.tif (Number of bands: 1, pixel value: inhab./km2, Coordinate System: GCS_WGS_1984)
 
Task:
Identify 10 settlements with the highest population living within 15 km.
 
Available technology:
Python with ArcPy or Open Source library
 
Questions:
	1.	What kind of solution you think is most suitable: a) Stand alone script b) ArcMap/QGIS custom toolbox. Justify your choice.
	2.	List the different steps that the script should enchain to accomplish the task.
	3.	What geospatial library/ies would you use for the spatial operations?
	4.	Provide the list of the 10 settlements with the highest population living within 15 km, associated with the estimated population.
	5.	Provide the python script performing the task in an executable .py file. (The containing folder must be finally zipped)
"""