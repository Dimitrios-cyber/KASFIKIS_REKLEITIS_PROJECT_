import streamlit as st # for the web app 
import folium # for the map 
import pandas as pd # for the dataframes 
import numpy as np # for the math calculations
from streamlit_folium import st_folium # for embedding the map to the streamlit app 


df = pd.read_excel('fires_coor.xlsx') # reading the fires_coor excel by the full path 
#df = pd.read_excel('/Users/Chris/Desktop/Python_lessons/Fire_map/fires_coor.xlsx') # reading the fires_coor excel by the full path 

lon = list(df.loc[:, 'X-ENGAGE'].to_numpy()) # saving the coordinates
lat = list(df.loc[:, 'Y-ENGAGE'].to_numpy())
weight = list(df.loc[:, 'intensity'].to_numpy()) # saving the intensity 


for i in range(len(weight)): # going through the length of the locations
  if np.isnan(weight[i]): # if the weight has a nan value then make it 0
    weight[i] = 0.0
    

data = {'lat': lat, 'lon': lon, 'weight': weight} # creating a dictionary with keys the strings 'lat', 'lon', 'weight' and values their respective lists
data_list = [(i,j,k) for i,j,k in zip(lat,lon,weight)] # creating a list that contains a tuple with the lat lon weight values for every location

m = folium.Map(location=[lon[1], lat[1]], zoom_start=7.5, width=1300, height=100) # creating the map with center as the longitude and latitude of the second location 

# quantiles will be quantisizing the intensity so that different colors are assigned for different fire intensities
q0 = np.quantile(weight, 0.7)
q1 = np.quantile(weight, 0.81)
q3 = np.quantile(weight, 0.90)
q4 = np.quantile(weight, 0.95)

# putting a different value in the color variable for different values of intensities
for i, j, w in data_list:
    color = '#2E68E6'  # blue color

    if w > q0:
        color = '#EFEA79'  # yellow color
    if w > q1:
        color = '#DC791C'
    if w > q3:
        color = '#F74D4D'
    if w > q4:
        color = '#400101'  # red color
    
    # creating a circle around each location with a radius of 700 that has the respective color to its intensity 
    folium.Circle(
        location=(j, i),
        radius=700,
        fill=True,
        color=color,
        fill_color=color
    ).add_to(m) # adding the circle to the map 

st.write('#### ?????????????? ??????????????????')
st.write('# ?? ???????????? ???????????????? ????????????????????.')
st.write('##### 12 ???????????????????? 2023.')
st.write('##### ???????????????? ????????????????????,  ?????????????????? ??????????????????')
st.write('''*?????? ???????????? ?????????? ?????????????? ?????? ?????? ?????????? ?????? 2021 ???????? ?????????????? ??????
???????????????????????????? ?????? ???? ???????????????? ?????? ???????????????? ???????????????? ???? ???????????????? ??????
???????????? ???????? ?????????????? ?????? 2007. ???????????? ???????????????? ?????? ?????????? ???????????? ?????????? ????????
???????? ?????? ????????.*''')
st.write('''???????? ?????? ?????? ?????????????? ?????? ?????????????????? ?????? [?????????????????????????? ??????????????????](https://www.fireservice.gr/el/synola-dedomenon), ???????????????????????????? ?????? ???? ???????????????? ?????? ????????????????, ?????? ?????????????? ??????
?????? ?????????????????? ?????????? ???????? ?????? ???????????????????????? ?????????? ?????? ???? 2000 ?????? ???? 2021.''')


fire_counts = pd.read_excel('fire_counts.xlsx')
#fire_counts = pd.read_excel('/Users/Chris/Desktop/Python_lessons/Fire_map/fire_counts.xlsx')



fire_counts.columns = ['??????????????', '??????????????????', 'intensity']

st.write(fire_counts.iloc[:,0:2].head(3))

st.write('''?? ?????????????????? ?????????????? ?????? ?????????????????? ?????? ???????????????? ???????? ???????????? ?????? ???? 2000
?????? ???? 2021 ???????????????????? ???????? 1247. ?? ?????????????????? ???? ?????? ?????????? ?????????? ????????
?????????????????? ???????????????? ?????? ?????????????? ??????????????????.''')

# st.write(fire_counts[fire_counts['intensity'] < q0  ])
# st.write(fire_counts[ (fire_counts['intensity'] >= q0) & (fire_counts['intensity'] < q1) ])
# st.write(fire_counts[ (fire_counts['intensity'] >= q1) & (fire_counts['intensity'] < q3) ])
# st.write(fire_counts[ (fire_counts['intensity'] >= q3) & (fire_counts['intensity'] < q4) ])
# st.write(fire_counts[(fire_counts['intensity'] >= q4) ])

st.write('\
        ???? ?? ?????????????? ???????????????? ???? ?????????? ???????? ???????? ?? ?????????????? ?????????????????? ???????????????? ?????????? ???????? ???? 1. \
        \n???? ?? ?????????????? ???????????????? ???? ?????????? ?????????????? ???????? ?? ?????????????? ?????????????????? ???????????????? ?????????? ???????????? ?????? 2 ?????? ?????? 3 \
        \n???? ?? ?????????????? ???????????????? ???? ?????????? ?????????????????? ???????? ?? ?????????????? ?????????????????? ???????????????? ?????????? ???????????? ?????? 4 ?????? ?????? 7. \
        \n???? ?? ?????????????? ???????????????? ???? ?????????? ?????????????? ???????? ?? ?????????????? ?????????????????? ???????????????? ?????????? ???????????? ?????? 8 ?????? ?????? 15. \
        \n???? ?? ?????????????? ???????????????? ???? ?????????? ???????????? ?????????????? ???????? ?? ?????????????? ?????????????????? ???????????????? ?????????? ???????????? ?????? 16 ?????? ?????? 142. ')
st_folium(m) # using st_folium to add the map to the streamlit app


#st.image('/Users/Chris/Desktop/Python_lessons/Fire_map/pie.png')
st.image('pie.png')

st.write('???????????????????????? ?????? ?? ?????????????? ?????? ???? ???????????? ???????????????????? ???????????????????? ?????????????? ?????? ???????? ?????? ?????????????????? ???????????????? ???? 142 ?????? 41 ?????????????????? ????????????????????. ?????? ???? ?????????????????? ???????????????? ?????????????????????? ???? ?????????? ???????????????? ?????????????????? ??????????????????.')
st.markdown('#### ???????? ?????????????? ????????????????')

#st.image('/Users/Chris/Desktop/Python_lessons/Fire_map/landhist.png')
st.image('landhist.png')

st.write("1 ) " + '''??????????, ?????????????? ???? ???? ??????. 1 ?????? ???????????? 3 ??. 998/79, ???????????????? ???? ????????????????
???????????? ???????????? ?????????? ???? ???????????? ?????????? ???????? ???????? ???????????????? ?????????????????? ??????
??????????????, ???? ??????????, ???????? ???? ?????? ???????? ???????????????????????? ?????????????? ?????? ????????????,
?????????????????? ???????? ?????? ?????????????????? ???????????????????????????? ?????? ???????????????????????????? ????????,
?????????????????? ???????????????????????? (????????????????????????????????) ?????? ?????????????????? ???????????? ????????????????????
(??????????????????).''')

st.write('''2 ) ???????????? ????????????, ???????? ???????????????? ???????? ??????. 2 ?????? ?????????? ??????????, ?????????????? ????????
?????? ???????????????? (??????????) ???????????? ?? ?????????? ?????????????? ????????????????, ?????????? ?? ????????????????,
?????????? ??????????.''')

st.write('''3 ) ???? ???????????????????????????? ???????????????? ???????????????????? ???????????????????????? ???????????? ?????? ??????????????
?????? ?????????????????? ????????????????. ?????? ???????????????????????????? ??????????????????????, ?????????? ??????????
?????????????? ?????????????? ?????? ?????????? ???????????? ???????? ?????? ?????? ?????????????? ?????? ????????????????????????
?????? ???? ???????????????????????????? ???????????? ????????????. ????????????, ???? ?????????????? ????????????????????????????
???????????????? ???????????????????????????? ?????? ???? ???????????? ?????????????????? ???? ?????????????? ????????????????.''')

st.write('''?????????????????? ???????????????????? ?????????????????????? ?????? ?? ???????????? ???????????????????? ?????? ??????????????????.
?????????? ???????? ???????? ???????????????? ?????????? ???? ???????????? ???????????????????? ?????? ?????? ????????????????
????????????????, ?????? ?????? ?????????????? ?????????????????????????????? ????????????????????. ???????? ?????? ??????
???????????????????? ?????? ?????????? ???????????? ???????????????????? ???????????? ???? ???????????????????? ?? ????????
?????????????? ???????? ?????????????? ?????????????????? ???? ???????????? ?????? ???? 2000 ?????? ???? 2021.''')


fire_time = pd.read_excel('fire_time.xlsx')
#fire_time = pd.read_excel('/Users/Chris/Desktop/Python_lessons/Fire_map/fire_time.xlsx')


mean_time = fire_time['???????????? ????????????????????(????????)'].mean()

fire_time = fire_time.iloc[:, 1::]

st.write(fire_time)

st.write('?? ?????????? ???????????? ???????????????????? ?????????? : {} ????????.'.format(round(mean_time,2)))


#st.image('/Users/Chris/Desktop/Python_lessons/Fire_map/extinguish_time.png')
st.image('extinguish_time.png')

st.write('''???????????????????? ???????? ?????????????? ?????? ???????????????? ???????? ???????????? ?????? 2013 ?? ?????????? ????????????????
???? ?????? ?????? ?????? ?????????????? ??????????, ?????? ???????? ???????? ?????????????? ?????? ???????????? ?????? 2017 ????????????????
???? ?????? ????????.''')

