import datetime

# Hónapok szöveges reprezentációja
honapok = {
    'január': 1, 'február': 2, 'március': 3,
    'április': 4, 'május': 5, 'június': 6,
    'július': 7, 'augusztus': 8, 'szeptember': 9,
    'október': 10, 'november': 11, 'december': 12
}

# Szoba osztály (absztrakt)
class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    def __str__(self):
        return f"Szoba száma: {self.szobaszam}, Ár: {self.ar} Ft"

# EgyágyasSzoba osztály
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

# KétágyasSzoba osztály
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 25000)

# Szálloda osztály
class Szalloda:
    def __init__(self):
        self.szobak = {}
        self.foglalasok = []

    def szoba_felvetel(self, szoba):
        self.szobak[szoba.szobaszam] = szoba

    def foglalas_hozzaadasa(self, szobaszam, datum):
        if datum < datetime.date.today():
            raise ValueError("A foglalás dátuma nem lehet a múltban!")
        if szobaszam in self.szobak and not any(f.szobaszam == szobaszam and f.datum == datum for f in self.foglalasok):
            self.foglalasok.append(Foglalas(self.szobak[szobaszam], datum))
        else:
            raise ValueError("A szoba ezen a napon már foglalt vagy nem létezik!")

    def foglalas_torlese(self, szobaszam, datum):
        foglalas = next((f for f in self.foglalasok if f.szobaszam == szobaszam and f.datum == datum), None)
        if foglalas:
            self.foglalasok.remove(foglalas)
        else:
            raise ValueError("Nincs ilyen foglalás!")

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "Nincs aktív szobafoglalás"
        return "\n".join(str(f) for f in self.foglalasok)

# Foglalás osztály
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Foglalás: {self.szoba}, Dátum: {self.datum}"

# Felhasználói interfész funkciók
def datum_beker():
    ev = int(input("Év: "))
    ho = input("Hónap (szövegesen): ").lower()
    if ho not in honapok:
        raise ValueError("Érvénytelen hónap név")
    ho = honapok[ho]
    nap = int(input("Nap: "))
    return datetime.date(ev, ho, nap)

def menu():
    while True:
        print("\nSzálloda Menü")
        print("1 - Szoba Foglalás")
        print("2 - Foglalás Lemondása")
        print("3 - Foglalások Listázása")
        print("4 - Kilépés")
        valasztas = input("Kérlek válassz egy opciót: ")

        if valasztas == "1":
            szobaszam = int(input("Szoba száma: "))
            try:
                datum = datum_beker()
                szalloda.foglalas_hozzaadasa(szobaszam, datum)
                print("Foglalás sikeresen létrehozva.")
            except Exception as e:
                print(e)

        elif valasztas == "2":
            szobaszam = int(input("Szoba száma: "))
            try:
                datum = datum_beker()
                szalloda.foglalas_torlese(szobaszam, datum)
                print("Foglalás sikeresen törölve.")
            except Exception as e:
                print(e)

        elif valasztas == "3":
            print("Aktuális foglalások:")
            print(szalloda.foglalasok_listazasa())

        elif valasztas == "4":
            print("Kilépés a programból.")
            break

        else:
            print("Érvénytelen választás, próbáld újra.")

# Példányosítjuk a szállodát és hozzáadunk néhány szobát
szalloda = Szalloda()
szalloda.szoba_felvetel(EgyagyasSzoba(101))
szalloda.szoba_felvetel(KetagyasSzoba(102))

# Menü indítása
menu()
