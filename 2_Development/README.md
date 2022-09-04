# Development

## Minio setup
1) To run MinIO on 64-bit Windows hosts, download the MinIO executable from the following URL:
    https://dl.min.io/server/minio/release/windows-amd64/minio.exe
2) run in CLI:
    minio.exe server D:\  
> Replace D:\ with the path to the drive or directory in which you want MinIO to store data   

## Spark setup
1) use dockerfile and docker compose files in spark folder and run: 
> docker-compose up   
2) py -m pip install pyspark

## Connection between minio and spark 
JARS needed
- wget --no-verbose https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar
- wget --no-verbose https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.2/hadoop-aws-3.2.2.jar

## Reference
- https://github.com/arezamoosavi/AcidOnSpark-ETL
- https://blog.min.io/delta-lake-minio-multi-cloud/
- https://github.com/UBC-UrbanDataLab/Anomaly-Detection-MDS2021#code
