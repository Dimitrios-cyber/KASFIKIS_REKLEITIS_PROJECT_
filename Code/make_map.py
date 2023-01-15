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

st.write('#### ΑΝΑΛΥΣΗ ΔΕΔΟΜΕΝΩΝ')
st.write('# Η Αττική καίγεται διαχρονικά.')
st.write('##### 12 Ιανουαρίου 2023.')
st.write('##### Κασφίκης Αλέξανδρος,  Ρεκλείτης Δημήτριος')
st.write('''*Δύο χρόνια έχουν περάσει απο την φωτιά του 2021 στην περιοχή των
Θρακομακεδόνων και οι κάτοικοι της περιοχής ξαναζουν τα γεγονότα της
φωτιάς στην Πάρνηθα του 2007. Πολλές περιοχές του νομού Αττική έχουν καεί
πάνω μία φορά.*''')
st.write('''Μέσα απο την ανάλυση των στοιχείων της [πυροσβεστικής υπηρεσίας](https://www.fireservice.gr/el/synola-dedomenon), καταδεικνύεται ότι οι περιοχές της Κερατέας, των Μεγάρων και
της Αναβύσσου έχουν καεί τις περισσότερες φορές απο το 2000 έως το 2021.''')


fire_counts = pd.read_excel('fire_counts.xlsx')
#fire_counts = pd.read_excel('/Users/Chris/Desktop/Python_lessons/Fire_map/fire_counts.xlsx')



fire_counts.columns = ['Περιοχή', 'Συχνότητα', 'intensity']

st.write(fire_counts.iloc[:,0:2].head(3))

st.write('''Ο συνολικός αριθμός των πυρκαγιών που ξέσπασαν στην Αττική απο το 2000
έως το 2021 ανέρχονται στις 1247. Η συχνότητα με την οποία έχουν καεί
ορισμένες περιοχές της Αττικής διαφέρουν.''')

# st.write(fire_counts[fire_counts['intensity'] < q0  ])
# st.write(fire_counts[ (fire_counts['intensity'] >= q0) & (fire_counts['intensity'] < q1) ])
# st.write(fire_counts[ (fire_counts['intensity'] >= q1) & (fire_counts['intensity'] < q3) ])
# st.write(fire_counts[ (fire_counts['intensity'] >= q3) & (fire_counts['intensity'] < q4) ])
# st.write(fire_counts[(fire_counts['intensity'] >= q4) ])

st.write('\
        Αν η περιοχή λαμβάνει το χρώμα μπλέ τότε ο αριθμός πυρκαγιών περιοχής είναι ίσος με 1. \
        \nΑν η περιοχή λαμβάνει το χρώμα κίτρινο τότε ο αριθμός πυρκαγιών περιοχής είναι μεταξύ του 2 και του 3 \
        \nΑν η περιοχή λαμβάνει το χρώμα πορτοκαλί τότε ο αριθμός πυρκαγιών περιοχής είναι μεταξύ του 4 και του 7. \
        \nΑν η περιοχή λαμβάνει το χρώμα κόκκινο τότε ο αριθμός πυρκαγιών περιοχής είναι μεταξύ του 8 και του 15. \
        \nΑν η περιοχή λαμβάνει το χρώμα σκούρο κόκκινο τότε ο αριθμός πυρκαγιών περιοχής είναι μεταξύ του 16 και του 142. ')
st_folium(m) # using st_folium to add the map to the streamlit app


#st.image('/Users/Chris/Desktop/Python_lessons/Fire_map/pie.png')
st.image('pie.png')

st.write('Παρατηρείται ότι η Κερατέα και τα Μέγαρα εμφανίζουν μεγαλύτερη διαφορά από όλες τις υπόλοιπες περιοχές με 142 και 41 πυρκαγίες αντίστοιχα. Ένω οι υπόλοιπες περιοχές σημειώνεται να έχουν παρόμοια συχνότητα πυρκαγιάς.')
st.markdown('#### Είδη καμένων εκτάσεων')

#st.image('/Users/Chris/Desktop/Python_lessons/Fire_map/landhist.png')
st.image('landhist.png')

st.write("1 ) " + '''Δάσος, σύμφωνα με τη παρ. 1 του άρθρου 3 ν. 998/79, αποτελεί το οργανικό
σύνολο άγριων φυτών με ξυλώδη κορμό πάνω στην αναγκαία επιφάνεια του
εδάφους, τα οποία, μαζί με την εκεί συνυπάρχουσα χλωρίδα και πανίδα,
αποτελούν μέσω της αμοιβαίας αλληλεξάρτησης και αλληλεπίδρασής τους,
ιδιαίτερη βιοκοινότητα (δασοβιοκοινότητα) και ιδιαίτερο φυσικό περιβάλλον
(δασογενές).''')

st.write('''2 ) Δασική έκταση, όπως ορίζεται στην παρ. 2 του ίδιου νόμου, υπάρχει όταν
στο παραπάνω (δάσος) σύνολο η άγρια ξυλώδης βλάστηση, υψηλή ή θαμνώδης,
είναι αραιά.''')

st.write('''3 ) Οι χορτολιβαδικές εκτάσεις βρίσκονται εννοιολογικά μεταξύ των δασικών
και γεωργικών εκτάσεων. Δεν καλλιεργούνται συστηματικά, έχουν μικρό
ποσοστό κάλυψης από άγρια ξυλώδη φυτά και δεν πληρούν τις προϋποθέσεις
για να χαρακτηριστούν δασική έκταση. Ωστόσο, οι ορεινές χορτολιβαδικές
εκτάσεις προστατεύονται από τη δασική νομοθεσία ως δασικές εκτάσεις.''')

st.write('''Ιδιαίτερο ενδιαφέρον παρουσιάζει και ο χρόνος κατάσβεσης των πυρκαγιών.
Καθώς κατά τους θερινούς μήνες οι φωτιές ευνοούνται από τις καιρικές
συνθήκες, ενώ τον χειμώνα καταπολεμούνται ευκολότερα. Μέσα από την
παρουσίαση του μέσου χρόνου κατάσβεσης μπορεί να αντιληφθεί ο κάθε
πολίτης πόσο γρήγορα σβήνονται οι φωτιές από το 2000 έως το 2021.''')


fire_time = pd.read_excel('fire_time.xlsx')
#fire_time = pd.read_excel('/Users/Chris/Desktop/Python_lessons/Fire_map/fire_time.xlsx')


mean_time = fire_time['Χρόνος κατάσβεσης(ώρες)'].mean()

fire_time = fire_time.iloc[:, 1::]

st.write(fire_time)

st.write('Ο μέσος χρόνος κατάσβεσης είναι : {} ώρες.'.format(round(mean_time,2)))


#st.image('/Users/Chris/Desktop/Python_lessons/Fire_map/extinguish_time.png')
st.image('extinguish_time.png')

st.write('''Ενδεικτικά στην περιοχή της Κερατέας στον Ιούνιο του 2013 η φωτιά σβήστηκε
σε μία ώρα και τριάντα λεπτά, ενώ στην ίδια περιοχή τον Ιούλιο του 2017 σβήστηκε
σε δύο ώρες.''')

