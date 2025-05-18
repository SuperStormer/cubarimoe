import os
import subprocess

if __name__ == "__main__":
    os.system("python manage.py makemigrations")
    result = subprocess.check_output("python manage.py migrate", shell=True, text=True)

    os.system("python -u manage.py runserver 0.0.0.0:8000")
