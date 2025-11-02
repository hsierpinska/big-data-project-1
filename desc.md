datasource1 – wizyty pacjentów (visits)
Dane mają format CSV, pliki posiadają nagłówek.
Każdy zestaw zawiera 10 000 wierszy, a plików jest 100.

# Pola w pliku:

- visit_id – unikalny identyfikator wizyty (UUID)
- hospital_id – identyfikator szpitala (hospital_id ze słownika szpitali)
- patient_name – imię i nazwisko pacjenta
- disease – kod choroby (ICD-10, z biblioteki Faker)
- medication – nazwa leku
- date – data i godzina wizyty (yyyy-MM-dd'T'HH:mm), losowo z ostatnich 5 lat, w godzinach 8:00–18:45
- age – wiek pacjenta (0–100)
- gender – płeć pacjenta (Male, Female, Other)
- datasource4 – informacje o szpitalach (hospitals)
Dane mają format CSV, plik posiada nagłówek.

# Pola w pliku:

- hospital_id – unikalny identyfikator szpitala (UUID)
- name – nazwa szpitala (np. Acme Corp Hospital)
- city – miasto
- country – kraj
- type – typ szpitala (General, Specialist, Clinic)

# Program MapReduce (2)
Działając na zbiorze datasource1 (1) należy wyznaczyć podstawowe statystyki wizyt pacjentów w poszczególnych szpitalach.

# Dane powinny zostać pogrupowane według:

identyfikatora szpitala (hospital_id),
roku wizyty (year).
W ramach każdej grupy należy obliczyć dwie miary:

- total_patients – liczba wizyt pacjentów w danym roku i szpitalu,
- avg_age – średni wiek pacjentów w danym roku i szpitalu.
W wynikowym zbiorze (3) powinny znaleźć się cztery atrybuty:

hospital_id – identyfikator szpitala,
year – kod choroby (YYYY),
total_patients – liczba wizyt pacjentów w danej grupie,
avg_age – średni wiek pacjentów w danej grupie.