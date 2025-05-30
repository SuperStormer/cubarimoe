import os
import subprocess

if __name__ == "__main__":
    os.system("python manage.py makemigrations")
    result = subprocess.check_output("python manage.py migrate", shell=True, text=True)

    os.system("gunicorn -c docker/gunicorn_config.py cubarimoe.wsgi:application")
