# Game Library — Python API + Frontend (localhost)

Мал проект за час: **Python Flask backend** враќа JSON со игри, а **HTML/CSS/JavaScript frontend** ги прикажува преку `fetch()`.

Не користи база на податоци. Игрите се запишани во Python листа од речници.

## 1. Структура

```text
game-library-localhost-demo/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
```

## 2. Стартувај го backend-от (прв терминал)

Во терминал, отвори ја папката `backend`:

```powershell
cd backend
python -m pip install -r requirements.txt
python app.py
```

Ако командата `python` не работи на Windows, пробај со `py` наместо `python`.

Backend-от ќе работи на **http://127.0.0.1:5000**.

Отвори во browser:

- http://127.0.0.1:5000/api/games
- http://127.0.0.1:5000/api/games/1
- http://127.0.0.1:5000/api/categories

Не го затворај овој терминал.

## 3. Стартувај го frontend-от (втор терминал)

Отвори **нов терминал** во папката `frontend`:

```powershell
cd frontend
python -m http.server 5500
```

Ако `python` не работи, пробај `py -m http.server 5500`.

Отвори во browser: **http://localhost:5500**.

**Важно:** отвори го frontend-от преку `http://localhost:5500`, а не со двоен клик на `index.html`. Ако користиш VS Code Live Server, постави го да работи на порт **5500**.

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
3. Отвори `http://localhost:5500` и објасни дека ова е друга апликација на друг порт.
4. Кликни „Сите игри“, „Препорачани“ и „Детали“.
5. Во browser притисни **F12 → Network → Fetch/XHR** и забележи ги URL, методот **GET**, статус **200** и JSON одговорот.
6. Отвори `/api/games/999` директно и покажи го статусот **404** во Network табот.
7. Затвори го backend-от со **Ctrl+C** и види што ќе се случи на frontend-от при пребарување. Потоа стартувај го повторно.

### Што е што?

- **localhost / 127.0.0.1** — нашиот компјутер.
- **порт 5000** — Python backend серверот.
- **порт 5500** — серверот кој го прикажува frontend-от.
- **API** — правила и адреси преку кои frontend-от бара податоци.
- **JSON** — формат за испраќање податоци.
- **fetch()** — JavaScript функција која праќа HTTP барање.
- **CORS** — дозвола веб-страница од еден origin да го прочита одговорот од друг origin.

## 6. Задачи за учениците

**Задача 1 — Нова игра (лесна):** Додај нов речник во листата `games` во `backend/app.py`, со ново `id`. Рефреширај ја страницата и види дали се прикажува.

**Задача 2 — Повеќе информации (лесна):** Во `frontend/script.js`, во `showGameDetails()`, прикажи ја и годината на издавање.

**Задача 3 — Нова категорија (средна):** Додај игра со нова категорија, на пример `Puzzle`. Провери дали автоматски се појавува во филтерот.

**Задача 4 — Нова рута (потешка):** Во Flask додај `GET /api/games/free` или `GET /api/games/latest` и враќај филтрирана листа. Потоа додади копче на frontend-от што ја повикува оваа рута. (За `free` прво додади поле `is_free` кај игрите.)

## Забелешки

- При промена на `app.py`, Flask debug режимот автоматски го рестартира backend-от.
- За тестирање користиме локален Flask **debug режим**, не за објавување на интернет.
- Ако друг процес го користи портот 5000 или 5500, прекини го тој процес. Ако менуваш портови, ажурирај ги и `API_URL` во `script.js` и CORS дозволите во `app.py`.
- Ако backend-от не е стартуван, `fetch()` не може да добие одговор.
