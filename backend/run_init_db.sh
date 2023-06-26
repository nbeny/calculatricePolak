#!/bin/bash
export FLASK_ENV=development
export DATABASE_URI=postgres://admin:alesio123442@prototype_db:5432/prototype_db

flask db init