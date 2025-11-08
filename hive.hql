DROP TABLE IF EXISTS stats;
DROP TABLE IF EXISTS hospitals;
DROP TABLE IF EXISTS final_stats;

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

CREATE TABLE final_stats(
    region STRING,
    hospital_type STRING,
    total_patients BIGINT,   
    avg_age DOUBLE,
    rank_in_region INT
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS TEXTFILE;

INSERT OVERWRITE DIRECTORY '${hiveconf:output_dir6}'
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
SELECT
    h.country AS region,
    h.type AS hospital_type,
    SUM(s.patient_count) AS total_patients,
    AVG(s.avg_age) AS avg_age,
    RANK() OVER (PARTITION BY h.country ORDER BY SUM(s.patient_count) DESC) AS rank_in_region
FROM stats s
JOIN hospitals h
  ON s.hospital_id = h.hospital_id
GROUP BY h.country, h.type;