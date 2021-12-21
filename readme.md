Creating a virtual envirnment and installing dependencies

```bash
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

Initial setup and start backend

```bash
cd tsp-backend/
export DJANGO_SETTINGS_MODULE=backend.settings
python3 manage.py runserver
python3 setupData.py
```

start frontend

```bash
cd tsp-frontend/
npm start
```
