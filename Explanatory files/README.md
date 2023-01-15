θα πρέπει να γίνει χρήση των αρχείων, έτσι ώστε να τρέξει το πρόγραμμα, ως εξής: 
Αρχικά πρέπει να κατεβούν οι εξής βιβλιοθήκες python : 
geopy, streamlit, folium, pandas, numpy, streamlit_folium
1) Έπειτα να τρέξει το attica_fires.ipynb αρχείο και θα σωθούν τα αρχεία xlsx. (Αυτά βρίσκονται ήδη στον φάκελο)
2) Μετά πρέπει να ανοιχθεί με κάποιο περιβάλλον (π.χ. vs code) και να τρέξει το αρχείο coor.py το οποίο χρησιμοποιείται έτσι ώστε να παρθούν οι συντεταγμένες (latitude, longitude) της κάθε περιοχής. Αυτό θα παράξει το αρχείο fires_coor.xlsx ( Αυτό το αρχείο θα χρειαστεί για το τελικό πρόγραμμα, υπάρχει ήδη στον φάκελο) 
3) Πριν τρέξει το τελικό αρχείο make_map.py πρέπει να γίνει copy paste το full path κάθε αρχείου που χρησιμοποιείται μέσα στο πρόγραμμα ( αυτό πρέπει να γίνει γιατί το full path για ένα αρχείο στον κάθε υπολογιστή είναι διαφορετικό. Είναι προτεινόμενο να τρέξει το αρχείο με την χρήση του anaconda.
Μόλις τρέξει το make_map.py
Θα πρέπει να πληκτρολογηθεί στο terminal :  "streamlit run (εδώ το path που οδηγεί στο αρχείο make_map.py)" 