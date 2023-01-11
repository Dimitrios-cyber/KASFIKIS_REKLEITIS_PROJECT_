import streamlit as st # for the web app 
import folium # for the map 
import pandas as pd # for the dataframes 
import numpy as np # for the math calculations
from streamlit_folium import st_folium # for embedding the map to the streamlit app 


df = pd.read_excel('fires_coor.xlsx') # reading the fires_coor excel by the full path 

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
q0 = np.quantile(weight, 0.10)
q1 = np.quantile(weight, 0.25)
#q2 = np.quantile(weight, 0.50)
q3 = np.quantile(weight, 0.75)
q4 = np.quantile(weight, 0.90)

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

# writing the text and adding the images and dataframes that convey the information
st.write("# Η Ελλάδα καίγεται διαχρονικά.\n## H μελέτη περίπτωσης του νομού Αττικής" )
st.write("### Έρευνα – Ανάλυση και Οπτικοποίηση Δεδομένων του Κασφίκη Αλεξάνδρου και του Δημητρίου Ρεκλείτη.")
st.write('#### Εισαγωγή')
st.write('''Οι πυρκαγιές στην Ελλάδα, αποτελούν συχνό φαινόμενο. Όπως φαίνεται και από τα στοιχεία του [Πυροσβεστικού Σώματος](https://www.fireservice.gr/el/synola-dedomenon),
 πάνω  από 3556 πυρκαγίες έχουν προκληθεί. Ιδιαίτερο όμως ενδιαφέρον παρουσιάζει και  η συχνότητα με την οποία καίγονται κάποιες περιοχές.
  Στην Αττική έχουν καταγραφεί πάνω από 1247 πυρκαγιές. 
  Η περιοχή της Κερατέας έχει καεί 142 φορές. Ακολουθεί η περιοχή Μέγαρα και η περιοχή της Ανάβύσσου
''')

fire_counts = pd.read_excel('fire_counts.xlsx')



fire_counts.columns = ['Περιοχή', 'Συχνότητα']

st.write(fire_counts.head(3))


st.write('#### Είδη εκτάσεων που καίγονται ')

st.write('''Στο χρονικό διάστημα από το 2000-2021 έχουν καεί
   περισσότερα από 127952 στρέμματα δασικής έκτασης και
    773 δάση. Επίσης έχουν προκληθεί συνολικά 970 πυρκαγιές σε γεωργικές εκτάσεις στις οποίες έχουν καεί
    συνολικά 46486 στρέμματα.
      Μικρό υπόμνημα ότι μορφής θεωρείς καλύτερο
''')

st.image('forest_fire.png')

st.write(''' Σύμφωνα με τη παρ. 1 του άρθρου 3 ν. 998/79, Δάσος αποτελεί 
το οργανικό σύνολο άγριων φυτών με ξυλώδη κορμό πάνω στην αναγκαία επιφάνεια του εδάφους,
 τα οποία, μαζί με την εκεί συνυπάρχουσα χλωρίδα και πανίδα, αποτελούν μέσω της αμοιβαίας αλληλεξάρτησης 
 και αλληλεπίδρασης τους, ιδιαίτερη βιοκοινότητα (δασοβιοκοινότητα) και ιδιαίτερο φυσικό περιβάλλον (δασογενές).
''')

st.write('''Δασική έκταση, όπως ορίζεται στην παρ. 2 του ίδιου νόμου, υπάρχει όταν στο παραπάνω 
(δάσος) σύνολο η άγρια ξυλώδης βλάστηση, υψηλή ή θαμνώδης, είναι αραιά. 
''')

st.write('''Οι χορτολιβαδικές εκτάσεις βρίσκονται εννοιολογικά μεταξύ 
των δασικών και γεωργικών εκτάσεων. Δεν καλλιεργούνται συστηματικά, έχουν 
μικρό ποσοστό κάλυψης από άγρια ξυλώδη φυτά και δεν πληρούν τις προϋποθέσεις για να χαρακτηριστούν
 δασική έκταση. Ωστόσο, οι ορεινές χορτολιβαδικές εκτάσεις προστατεύονται
  από τη δασική νομοθεσία ως δασικές εκτάσεις. Οι γεωργικές εκτάσεις, είναι οι
   εκτάσεις που χρησιμοποιούνται αποκλειστικά για τη γεωργική παραγωγή.''')

st.write('#### Κατασκευή Χάρτη')
st.write('Χρησιμοποιώντας την βιβλιοθήκη folium της python δημιουργήθηκε ένας χάρτης. \
    Στον χάρτη απεικονίζονται οι καμένες περιοχές στις οποίες κωδικοποιήθηκε η συχνότητα πυρκαγιών\
        με την εξής λογική :  ')
st.write('Στο εύρος 1 εως 142 εάν ο αριθμός των φορών που έχει καεί μία περιοχή είναι μικρότερος του 10ου ποσοστιμορίου του τότε \
    η περιοχή λαμβάνει το χρώμα μπλέ. \
        \nΆν είναι μεταξύ του 10ου και του 25 ποσοστιμορίου, τότε λαμβάνει το χρώμα κίτρινο \
        \nΆν είναι μεταξύ του 25ου και του 75ου ποσοστιμορίου, τότε λαμβάνει το χρώμα πορτοκαλί\
        \nΆν είναι μεταξύ του 75οθ και του 90ου ποσοστιμορίου, τότε λαμβάνει το χρώμα κόκκινο \n \
        Αν είναι μεταξύ του 90ου και 100ου ποσοστιμορίου, τότε λαμβάνει το χρώμα σκούρο κόκκινο.')
st_folium(m) # using st_folium to add the map to the streamlit app

st.write('''Πολλές φορές η αιτία πρόκλησης των πυρκαγιών ποικίλει, 
όπως δείχνουν οι ενημερωτικές αφίσες του υπουργείου Πολιτικής Προστασίας. 
Από την απόθεση σκουπιδιών, το άναμμα υπαίθριων ψησταριών
''')

st.image(['im1.png','im2.png'])

st.write('''μέχρι και τις εμπρηστικές απόπειρες, που ανάγονται σε αξιόποινη πράξη με την ισχύ 
του νέου ποινικού κώδικα  Νόμος (4619/2019). Όποιος με πρόθεση προξενεί πυρκαγιά τιμωρείται: α)
 με φυλάκιση τουλάχιστον δύο ετών, αν από την πράξη μπορεί να προκύψει κοινός κίνδυνος σε ξένα
 πράγματα· β) με κάθειρξη, αν από την πράξη μπορεί να προκύψει κίνδυνος για άνθρωπο· γ) με κάθειρξη
  ισόβια ή πρόσκαιρη τουλάχιστον δέκα ετών, αν στην περίπτωση του στοιχ. β' επήλθε θάνατος.
''')

st.markdown("Για αυτούς τους λόγους ιδιαίτερη μνεία πρέπει να δοθεί στην ετοιμότητα της πυροσβεστικής και στον **χρόνο κατάσβεσης των πυρκαγιών**.")

st.write('#### Χρόνος κατάσβεσης')
st.write('Στον παρακάτω πίνακα παρουσιάζονται οι ημερομηνίες καθώς και οι ώρες έναρξης και κατάσβεσης της φωτιάς. Χρησιμοποιώντνας αυτές τις στήλες\
    έγινε υπολογισμός του χρόνου κατάσβεσης της φωτιάς για κάθε συμβάν.')

    

fire_time = pd.read_excel('fire_time.xlsx')


mean_time = fire_time['Χρόνος κατάσβεσης(ώρες)'].mean()
mode_time = fire_time['Χρόνος κατάσβεσης(ώρες)'].min()

fire_time = fire_time.iloc[:, 1::]

st.write(fire_time)

st.write('Όπου ο μέσος χρόνος κατάσβεσης είναι : {} ώρες.'.format(round(mean_time,2)))





st.write('''
Ο συνολικός αριθμός των πυρκαγιών στην Αττική  από το 2000-2021 ανάγεται στις 1247. Το ερώτημα είναι αν και πότε 
θα υιοθετηθεί ένα ευρύτερο μοντέλο επιχειρησιακής ετοιμότητας και αντιμετώπισης του φαινομένου των πυρκαγιών 
''')


