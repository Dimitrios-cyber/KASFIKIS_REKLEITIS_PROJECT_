
import pandas as pd
from geopy.geocoders import Nominatim

# creating a function that returns the coordinates if location is valid
def get_coordinates(areas):
  geolocator = Nominatim(user_agent="my_application")  # nomatim is a geocoder that will return the latitude and longitude of the areas
  coordinates = []

  for area in areas: # going through all the areas
    location = geolocator.geocode(area) # getting the coordinates
    if location: # if the location is valid add as a tuple the coordinates to the list
      coordinates.append((location.latitude, location.longitude))
    else: # alse add nothing
      coordinates.append(None)

  return coordinates


df = pd.read_excel('fires.xlsx') # reading the fires.xlsx that was created in the Attica_fires notebook

df = df.iloc[:,1::] # dropping the first column 

areas = list(df.loc[:, 'Περιοχή'].to_numpy()) # creating a list of all the areas

coor = get_coordinates(areas) # getting the coordinates list of all the areas

#coor = [(37.9631043, 22.636893), None, (37.9460412, 23.7695132), (37.96497535, 23.778454915282282), None, None, None, (39.112862449999994, 21.21464573663784), (38.0708339, 23.877298), (38.0682001, 23.7800629), (38.2236445, 23.923496), None, None, (38.2846853, 23.8631552), (38.16699065, 23.905629158319535), (38.0125815, 23.7772109), None, (38.1068395, 23.8425642), None, None, None, None, None, None, None, None, (37.9223361, 23.4675299), None, (40.4800867, 23.136266), (39.6242416, 20.3218411), (37.883436, 23.4630589), None, (37.901493, 23.4868647), (37.9480551, 23.6423089), (40.8772872, 25.5468041), (37.9841559, 23.4384403), (37.9913985, 23.493738), (37.9435309, 23.557137), None, (37.9507828, 23.5289128), None, None, None, (37.9065532, 23.4146175), (38.0620067, 23.7089143), (39.5677704, 20.8769752), (37.9598842, 23.432984), (37.6357429, 22.7291724), None, None, (37.7911412, 20.7755856), None, None, (37.707161, 23.5054243), (38.9636349, 20.74412340857545), None, (38.0008706, 23.6344742), (37.9655363, 23.5626386), None, None, (37.9635338, 23.6056318), None, (40.2694001, 22.5218605), None, None, None, (38.058688, 23.5888352), None, None, (38.0791202, 23.5217004), None, None, (38.0422432, 23.495708290164455), None, (38.047608, 23.5348663), None, None, None, None, (41.349233850000005, 26.493086239949), None, (38.0451871, 23.4954424), None, (37.9965887, 23.3445017), None, (38.1036218, 23.6693778), (38.4324632, 21.879755), None, None, None, (38.0761407, 23.6361215), None, None, (38.0761407, 23.6361215), None, None, (60.8937495, 10.894256), (38.1007794, 23.5633753), None, None, (35.2071906, 25.1011069), None, None, None, None, None, (-21.3612672, -51.8572739), None, (38.0135351, 23.7362659), None, None, (37.6811469, 23.9438919), None, (41.6250818, 8.9074488), None, None, None, (40.4126442, 22.9110734), None, (37.8161479, 24.0030394), (37.717219, 23.9456524), None, None, None, None, None, (39.1255985, 23.6516213), (37.973260350000004, 23.75249958492367), None, (37.7204438, 24.0482089), (43.501445, 2.3188283), None, (37.8828306, 23.9323453), None, None, (37.6370576, 23.3951917), None, None, (36.4454721, 28.2214483), None, None, (38.2898595, 23.8237368), (46.3144754, 11.0480288), (38.0841607, 23.7368653), (38.20577, 23.8367212), (38.2158722, 23.8771927), (37.8083817, 23.9776656), None, (37.7142551, 24.0548015), (37.7375619, 23.9521915), (37.9537116, 23.8523932), (37.8983067, 23.8739999), (11.7902463, 77.7980929), (39.1050446, 26.5442451), (38.2163741, 23.8678642), (38.304395, 23.7533067), (37.9869029, 23.7269762), (38.0850569, 23.7059206), (45.8228924, 25.0466557), (34.8733883, 33.07636679688559), None, (38.1294473, 23.7573686), (38.0128111, 23.6955137), (38.1036218, 23.6693778), (38.042469, 23.683763), (37.540279, 22.8924125), (37.7490677, 23.9061656), (38.2236445, 23.923496), (41.260082, 22.9994915), (38.0645401, 22.9246799), (37.332093, 23.46646349926514), (38.1667829, 23.4174609), (38.3562389, 21.5614054), (36.8469656, 22.3238706), (37.4971612, 23.3626476), (38.1010059, 23.8836998), (38.0915732, 23.821732323430016), (38.0221347, 23.7848706), (39.957373950000004, 26.238017461011644), (38.0016292, 23.9410271), (38.0571337, 23.884623664572068), (38.1532724, 23.9620892), (38.0546653, 23.8081533), (37.827753, 23.9678826), (8.9646526, 76.62024418435345), (37.9383706, 23.508373587712107), (37.9650175, 23.6207952), (38.047608, 23.5348663), (36.219683, 22.9793409), (38.0024952, 23.740768), (37.5806766, 23.3914157)]

for i in range(len(df)): # i is running through all the indexes of the dataframe 
    if coor[i] != None: # if coordinates are not none 
        df.loc[i, 'X-ENGAGE'] = coor[i][0] # then add the coordinates to the columns X-ENGAGE and Y-ENGAGE of the dataframe 
        df.loc[i, 'Y-ENGAGE'] = coor[i][1]


df = df.dropna(subset=['X-ENGAGE', 'Y-ENGAGE']) # dropping the areas without coordinates

df.to_excel('fires_coor.xlsx') # saving the file 
