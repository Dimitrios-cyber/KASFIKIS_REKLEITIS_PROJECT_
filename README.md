# KASFIKIS_REKLEITIS_PROJECT_
Ο φάκελος code περιέχει τον κώδικα, που γράφτηκε για το project. Τρια  επιμέρους αρχεία υπάρχουν σε αυτόν. Πρώτο το Attica_fires.ipynb περιέχει το pitch της εργασίας. (Ανανεωμένο pitch υπάρχει ως ξεχωριστό αρχείο). Το αρχείο coor περιέχει τον κώδικα, που γράφτηκε από την επεξεργασία των δεδομένων από τον ιστότοπο του πυροσβεστκού σώματος. Το αρχείο  make_map περιέχει τον κώδικα, που γράφτηκε για την κατασκευή του χάρτη στην τελική έκδοση του project.
Ο φάκελος Data περιέχει όλα τα αρχεία xls, που προέκυψαν από την συγγραφή του κώδικα.
Ο φάκελος Explanatory files, περιέχει το αρχείο documentation σε μορφή .md που επεξηγεί τα dataset. Το αρχείο methodology σε μορφή .md, που περιέχει τα αναλυτικά βήματα, που ακολουθήσαμε για τη δημιουργία του project. Ένα αρχείο readme, που επεξηγεί, πώς θα ανοιχθούν τα αρχεία για την παρουσίαση του project.
Το αρχείο pictures περιέχει τις εικόνες, του τελικού project.
Το αρχείο site needed files, που περιέχουν τα αρχεία που χρειάστηκαν για την κατασκευή του ιστοτόπου της εργασίας.
Στο repository αυτό υπάρχει το αρχείο zip  fire_map (2). Αυτό το αρχείο περιέχει ότι χρειάζεται για να δημιουργηθεί ο πίνακας και πώς θα άνοιγε η εργασία αν δεν δημιουργούσαμε ιστότοπο για την προβολή του project. Ταυτόχρονα για τρέξουν τα αρχεία ΑΝΕΞΑΡΤΗΤΩΣ του ιστοτόπου ( για τρέξει το project) πρέπει να ακολουθηθούν τα εξής ΑΠΑΡΑΊΤΗΤΑ βήματα: Αρχικά πρέπει να εγκατασταθούν οι εξής βιβλιοθήκες: geopy, streamlit,folium, pandas, numpy, streamlit_folium. Στη συνέχεια 1) να τρέξει το Attica_fires.ipynb αρχείο και θα σωθούν τα αρχεία xlsx.  2) Θα ανοιχθεί με κάποιο περιβάλλον πχ  vs code θα τρέξουμε το αρχείο coor.py το οποίο χρησιμοποιείται έτσι ώστε να παρθουν οι συντεταγμένες τις κάθε περιοχής. Αυτό θα παράξει το αρχείο fires_coor.xlsx (αυτό το αρχείο υπάρχει στο τελικό φάκελο) 3) Πριν τρέξει το τελικό αρχείο make_map.py κάνε copy paste το full path του κάθε αρχείου, που χρησιμοποιείται μέσα στο πρόγραμμα. 
Το url για το τελικό site που παράξαμε είναι http://atticafires.herokuapp.com/
