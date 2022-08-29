#Development

## Minio setup
1) To run MinIO on 64-bit Windows hosts, download the MinIO executable from the following URL:
    https://dl.min.io/server/minio/release/windows-amd64/minio.exe
2) run in CLI:
    minio.exe server D:\  
> Replace D:\ with the path to the drive or directory in which you want MinIO to store data   

## Spark setup
Either:
1) pip install pyspark
2) docker run -it apache/spark-py /opt/spark/bin/pyspark

## Reference
https://github.com/arezamoosavi/AcidOnSpark-ETL
