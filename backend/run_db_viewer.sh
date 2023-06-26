#! /bin/bash
docker run --rm -d --net=host \
    --name prototype_db_viewer \
    -e PGADMIN_DEFAULT_EMAIL=admin@pgadmin.fr \
    -e PGADMIN_DEFAULT_PASSWORD=alesio123442 \
    -e PGADMIN_LISTEN_PORT=5555 \
    dpage/pgadmin4:latest
