python3 -m venv env
. env/bin/activate

<!-- deactivate -->

<!-- pip install -upgrade pip -->

pip install django
Django
Pillow
django-crispy-forms
crispy-bootstrap4
pytz
pip freeze

<!-- pip freeze > requirements.txt -->
<!-- pip install -r requirements.txt -->

django-admin
django-admin startproject pjt1
cd pjt1
python manage.py runserver 8080 (originally 8000)
python manage.py startapp app1

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

    <hr>
    名前 / ニックネーム
    <br>{{ form.skater }}<br>
    <hr>
    曲名
    <br>{{ form.title }}<br>
    <hr>
    曲の分数
    <br>{{ form.length }}<br>
    <hr>
    曲のアップロード
    <br>{{ form.music }}
    <hr>
