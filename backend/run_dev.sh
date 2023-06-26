#! /bin/bash
export FLASK_ENV=development
export DATABASE_URI=postgresql://admin:alesio123442@prototype_db:5432/prototype_db

flask db migrate
flask db upgrade
gunicorn run:app --worker-class gevent --bind 127.0.0.1:5000
