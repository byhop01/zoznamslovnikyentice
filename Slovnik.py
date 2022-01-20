my_dict = {
    "meno" : "Majo ",
    "priezvisko" : "Bicanik",
    "projazyk" : "ziaden",
    "adresa" : {
        "mesto" : "klubina",
        "cislodomu" : "155",
        "ulica" : "sniegon",

    }
}
for kluc, hodnota in list(my_dict.items()):
    print("Kluc je: ", kluc)
    print("Value je: ", hodnota)
