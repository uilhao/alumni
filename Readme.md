## Alumni

In progress

## Python environment

Create and start the python environment before performing other operations.

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Local development

#### Database:

Postgres is used.

#### Django app:

Run the Django app in debug mode and auto-load on save:

```bash
python manage.py runserver
```

python manage.py runscript bulk_create --dir-policy none
