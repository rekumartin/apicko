# moj_prvy_backend

Jednoduchý Flask backend API so zoznamom študentov.

## Routes

| URL | Popis |
|-----|-------|
| `/` | Privítacia stránka |
| `/api` | Vráti všetkých 10 študentov ako JSON |
| `/api/student/<id>` | Vráti jedného študenta podľa ID |

## Spustenie lokálne

```bash
pip install -r requirements.txt
python app.py
```

Server beží na `http://localhost:5000`

## GitHub Pages (statické JSON)

- `docs/students.json` – všetci študenti
- `docs/student/1.json` až `docs/student/10.json` – jednotliví študenti
