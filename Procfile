release: python manage.py migrate
web: gunicorn rasagula.wsgi:application --bind 0.0.0.0:8080
