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

create database hospital;
use hospital;

!sh mkdir /tmp/source
!sh mkdir /tmp/source/hospital
!sh cp ./datasource4/* /tmp/source/hospital

CREATE EXTERNAL TABLE IF NOT EXISTS hospital_ext(
 hospital_id STRING, name STRING, city STRING, type STRING)
 COMMENT 'hospitals'
 ROW FORMAT DELIMITED
 FIELDS TERMINATED BY ','
 STORED AS TEXTFILE
 location '/tmp/source/hospital';
