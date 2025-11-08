Program Hive (5)
Działając na wyniku zadania MapReduce (3) oraz zbiorze danych datasource4 (4) należy powiązać wizyty pacjentów z informacjami o szpitalach.

Na podstawie tych danych należy wyliczyć zestawienia na poziomie regionów i typów szpitali.

Dla każdego regionu i typu szpitala należy obliczyć:

łączną liczbę pacjentów obsłużonych w regionie w ramach danego typu szpitala,
średni wiek pacjentów obsłużonych w regionie w ramach danego typu szpitala.
Dodatkowo – w ramach każdego regionu – należy określić ranking typów szpitali według liczby obsłużonych pacjentów.

Wynik (6) powinien zawierać następujące atrybuty:

region – region,
hospital_type – typ szpitala (np. General, Specialist, Clinic),
total_patients – łączna liczba pacjentów w regionie dla danego typu szpitala,
avg_age – średni wiek pacjentów,
rank_in_region – pozycja typu szpitala w rankingu liczby obsłużonych pacjentów w ramach danego regionu.
Cyfry w nawiasach odnoszą się do cyfr wykorzystanych na graficznej reprezentacji projektu – patrz opis projektu na stronie kursu.

DROP TABLE IF EXISTS hospitals;
CREATE EXTERNAL TABLE hospitals(
  hospital_id STRING,
  name STRING,
  city STRING,
  country STRING,
  type STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '${hiveconf:input_dir4}';

DROP TABLE IF EXISTS stats;
CREATE EXTERNAL TABLE stats(
  hospital_id STRING,
  year INT,
  patient_count INT,
  avg_age DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '${hiveconf:input_dir3}';

DROP TABLE IF EXISTS final_stats;
CREATE EXTERNAL TABLE IF NOT EXISTS final_stats (
    region STRING,
    hospital_type STRING,
    total_patients INT,
    avg_age DOUBLE,
    rank_in_region INT
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS TEXTFILE
LOCATION '${output_dir6}';