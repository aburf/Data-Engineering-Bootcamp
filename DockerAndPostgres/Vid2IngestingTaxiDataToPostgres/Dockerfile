services:
    postgres:
        image: postgres:13
        environment:
            POSTGRES_USER: airflow
            POSTGRES_password: airflow
            POSTGRES_DB: airflow
        volumes:
            -postgres-db-volume:/var/lib/postgresql/data
        HEALTHCHECK:
            test: ["CMD", "pg_isready", "-U", "airflow"]
            intervals: 5s
            retries: 5
        restart: always

docker run -it \
    -e POSTGRES_USER: "root" \
    -e POSTGRES_password: "root" \
    -e POSTGRES_DB: "ny_taxi"  \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \   
    -p 5432:5432 \
    postgres:13 