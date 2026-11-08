"""Мало Flask API за демонстрација на localhost, JSON и fetch()."""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Frontend-от работи на порт 5500, а ова API на порт 5000.
# CORS дозволува frontend-от да праќа барања до backend-от.
CORS(app)

# Ова ни е „лажна база“: обична Python листа со речници.
# Сите податоци се примерни, направени за час.
games = [
    {
        "id": 1,
        "name": "Minecraft",
        "category": "Creative",
        "platform": "PC / Console / Mobile",
        "year": 2011,
        "icon": "⛏️",
        "description": "Гради светови, истражувај и преживувај со пријателите.",
        "featured": True,
    },
    {
        "id": 2,
        "name": "Roblox",
        "category": "Creative",
        "platform": "PC / Console / Mobile",
        "year": 2006,
        "icon": "🧱",
        "description": "Истражувај игри и креации направени од други играчи.",
        "featured": False,
    },
    {
        "id": 3,
        "name": "Fortnite",
        "category": "Action",
        "platform": "PC / Console / Mobile",
        "year": 2017,
        "icon": "🎯",
        "description": "Брзи натпревари и тимски предизвици.",
        "featured": True,
    },
    {
        "id": 4,
        "name": "Rocket League",
        "category": "Sports",
        "platform": "PC / Console",
        "year": 2015,
        "icon": "🚗",
        "description": "Играј фудбал со автомобили и постигнувај голови.",
        "featured": True,
    },
    {
        "id": 5,
        "name": "Among Us",
        "category": "Party",
        "platform": "PC / Console / Mobile",
        "year": 2018,
        "icon": "🚀",
        "description": "Откриј кој се преправа дека е дел од екипажот.",
        "featured": False,
    },
    {
        "id": 6,
        "name": "Stardew Valley",
        "category": "Adventure",
        "platform": "PC / Console / Mobile",
        "year": 2016,
        "icon": "🌱",
        "description": "Одгледувај растенија и изгради сопствена фарма.",
        "featured": False,
    },
    {
        "id": 7,
        "name": "Mario Kart 8 Deluxe",
        "category": "Racing",
        "platform": "Nintendo Switch",
        "year": 2017,
        "icon": "🏎️",
        "description": "Тркај се низ забавни патеки со различни карактери.",
        "featured": True,
    },
    {
        "id": 8,
        "name": "EA Sports FC 26",
        "category": "Sports",
        "platform": "PC / Console",
        "year": 2025,
        "icon": "⚽",
        "description": "Одиграј фудбалски натпревар со омилениот тим.",
        "featured": False,
    },
]


@app.get("/")
def home():
    return jsonify({
        "message": "Welcome to Game Library API!",
        "try_these_routes": [
            "/api/games",
            "/api/games/1",
            "/api/games/featured",
            "/api/categories",
            "/api/games?category=Sports",
            "/api/games?search=mario",
            "/api/stats",
        ],
    })


@app.get("/api/games")
def get_games():
    """Сите игри. Опционални филтри: ?category= и ?search=."""
    category = request.args.get("category", "").strip().lower()
    search = request.args.get("search", "").strip().lower()

    results = games

    if category:
        results = [game for game in results if game["category"].lower() == category]

    if search:
        results = [game for game in results if search in game["name"].lower()]

    return jsonify(results)


@app.get("/api/games/featured")
def get_featured_games():
    return jsonify([game for game in games if game["featured"]])


@app.get("/api/games/<int:game_id>")
def get_game_by_id(game_id):
    for game in games:
        if game["id"] == game_id:
            return jsonify(game)

    # HTTP 404 = бараниот ресурс не постои.
    return jsonify({"error": "Играта не е пронајдена!"}), 404


@app.get("/api/categories")
def get_categories():
    categories = sorted({game["category"] for game in games})
    return jsonify(categories)


@app.get("/api/stats")
def get_stats():
    return jsonify({
        "total_games": len(games),
        "total_categories": len({game["category"] for game in games}),
        "featured_games": sum(1 for game in games if game["featured"]),
    })


if __name__ == "__main__":
    # Само за локален развој и за учење, не за production.
    app.run(host="127.0.0.1", port=5000, debug=True)
