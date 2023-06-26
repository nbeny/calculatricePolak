#! /bin/bash
docker run -d --rm \
    --name prototype_db \
    -p 5432:5432 \
    -e POSTGRES_PASSWORD=alesio123442 \
    -e POSTGRES_USER=admin \
    -e POSTGRES_DB=prototype_db \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v /home/alesio/Documents/entretien/calculatricePolak/data:/var/lib/postgresql/data/pgdata \
    postgres:12