# Game Library — Python API + Frontend (localhost)

Мал проект за час: **Python Flask backend** враќа JSON со игри, а **HTML/CSS/JavaScript frontend** ги прикажува преку `fetch()`.

Не користи база на податоци. Игрите се запишани во Python листа од речници.

## 1. Структура

```text
game-library-localhost-demo/
├── backend/
│   ├── app.py
│   └── requirements.txt
└── README.md
```

## 2. Стартувај го backend-от (прв терминал)

Во терминал, отвори ја папката `backend`:

```powershell
cd backend
python -m venv .venv
cd .venv/Scripts
activate
cd ../..
python -m pip install -r requirements.txt
python app.py
```

Ако командата `python` не работи на Windows, пробај со `py` наместо `python`.

Backend-от ќе работи на **http://127.0.0.1:5000**.

Отвори во browser:

- http://127.0.0.1:5000/api/games
- http://127.0.0.1:5000/api/games/1
- http://127.0.0.1:5000/api/categories


## 4. Рути од backend-от

| Method | URL | Што враќа? |
|---|---|---|
| GET | `/` | Порака и листа со API рути |
| GET | `/api/games` | Сите игри (JSON array) |
| GET | `/api/games/1` | Една игра според ID (JSON object) |
| GET | `/api/games/999` | Грешка со статус 404 |
| GET | `/api/games/featured` | Само препорачани игри |
| GET | `/api/categories` | Листа со категории |
| GET | `/api/games?category=Sports` | Игри од Sports |
| GET | `/api/games?search=mine` | Игри со „mine“ во името |
| GET | `/api/stats` | Статистика за игрите |

## 5. Што да покажеш на час?

1. Покажи ја Python листата `games` во `app.py`.
2. Отвори `http://127.0.0.1:5000/api/games` и покажи го JSON одговорот.
3. Кликни „Сите игри“, „Препорачани“ и „Детали“.
4. Во browser притисни **F12 → Network → Fetch/XHR** и забележи ги URL, методот **GET**, статус **200** и JSON одговорот.
5. Отвори `/api/games/999` директно и покажи го статусот **404** во Network табот.
6. Затвори го backend-от со **Ctrl+C** и види што ќе се случи на frontend-от при пребарување. Потоа стартувај го повторно.

### Што е што?

- **localhost / 127.0.0.1** — нашиот компјутер.
- **порт 5000** — Python backend серверот.
- **порт 5500** — серверот кој го прикажува frontend-от.
- **API** — правила и адреси преку кои frontend-от бара податоци.
- **JSON** — формат за испраќање податоци.
- **fetch()** — JavaScript функција која праќа HTTP барање.
- **CORS** — дозвола веб-страница од еден origin да го прочита одговорот од друг origin.

## 6. Задачи

**Задача 1 — Повеќе информации (лесна):** Во `frontend/script.js`, во `showGameDetails()`, прикажи ја и годината на издавање.
