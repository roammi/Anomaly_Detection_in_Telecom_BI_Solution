docker command:

    docker run \
    -ti \
    -p 8080:8080 \
    -v ➥ /path/to/dag/download_rocket_launches.py:/opt/airflow/dags/
        download_rocket_launches.py \
    --entrypoint=/bin/bash \
    --name airflow \
    apache/airflow:2.0.0-python3.8 \
    -c '( \
    airflow db init && \
    ➥ airflow users create --username admin --password admin --firstname
        Anonymous --lastname Admin --role Admin --email admin@example.org \
    ); \
    airflow webserver & \
    airflow scheduler \
    '
