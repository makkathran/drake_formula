import numpy as np
import matplotlib.pyplot as plt

# Csillagok száma a Tejútrendszerben
# Becsüljük meg, hogy kb. 400 milliárd csillag van a galaxisunkban.
csillagok_szama = np.array(400e9)

# Csillagok százaléka, amelyeknek bolygói vannak
# A legújabb kutatások szerint szinte minden csillagnak van legalább egy bolygója. 
# Tegyük fel, hogy ez az arány 99%.
bolygo_arany = np.array(0.99)

# Lakható zónában lévő bolygók átlagos száma egy csillagon
# Nem minden bolygó lakható. Tegyük fel, hogy átlagosan minden századik bolygó lehet lakható.
lakható_bolygók = np.array(0.01)

# Az élet kialakulásának valószínűsége egy lakható bolygón
# Az élet kialakulása bonyolult folyamat. Becsüljük, hogy 5% esély van rá egy lakható bolygón.
elet_valoszinusege = np.array(0.05)

# Az intelligens élet kialakulásának valószínűsége
# Még ritkább, hogy az élet intelligenssé fejlődjön. Tegyük fel, ez az esély csak 1%.
intelligens_elet = np.array(0.01)

# Az intelligens civilizációk százaléka, amelyek képesek a kommunikációra
# Nem minden intelligens életfejlődés vezet kommunikációs képességekhez. Tegyük fel, ez 1%.
kommunikacio = np.array(0.01)

# A Drake-egyenlet egyszerűsített változatának kiszámítása
civilizaciok_szama = csillagok_szama * bolygo_arany * lakható_bolygók * elet_valoszinusege * intelligens_elet * kommunikacio

# Eredmény kiírása
eredmeny = f"A Tejútrendszerben a kommunikáló civilizációk becsült száma: {civilizaciok_szama:.0f}"
print(eredmeny)

# Vizuális megjelenítés
plt.figure(figsize=(10, 6))
labels = ['Csillagok száma x4', 'Bolygók aránya', 'Lakható bolygók', 'Élet valószínűsége', 'Intelligens élet', 'Kommunikáció', 'Civilizáció élettartam']
values = np.array([csillagok_szama, bolygo_arany, lakható_bolygók, elet_valoszinusege, intelligens_elet, kommunikacio, 10000 / 10000])

# Logaritmikus skála alkalmazása
plt.yscale('log')
plt.bar(labels, values, color=['blue', 'green', 'red', 'purple', 'orange', 'pink', 'yellow'])
plt.xlabel('Faktorok')
plt.ylabel('Értékek (logaritmikus skála)')
plt.title('A Drake-egyenlet faktorai és becsült értékei')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Az eredmény kiírása a grafikonon
plt.text(3, csillagok_szama / 10, eredmeny, fontsize=12, ha='center', va='bottom')

plt.show()
