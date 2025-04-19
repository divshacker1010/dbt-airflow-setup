#FROM apache/airflow:latest
#USER root
#RUN apt-get update && \
#    apt-get -y install git && \
#    apt-get clean
#USER airflow

FROM apache/airflow:2.5.0

USER root

RUN sudo apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    python3-distutils \
    libpython3.9-dev

USER airflow

COPY --chown=airflow . .

# RUN python -m pip install .

RUN pip install dbt-core==1.5.9 dbt-postgres==1.5.9

# RUN dbt deps --project-dir /opt/airflow/example_dbt_project