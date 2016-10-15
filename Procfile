web: gunicorn config.wsgi:application
worker: celery worker --app=trip_brain.taskapp --loglevel=info
