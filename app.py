from flask import Flask, render_template_string, request

app = Flask(__name__)

EVENTS = [
    {
        "year": 1945,
        "title": "End of World War II",
        "category": "World War II",
        "summary": "World War II ended in 1945 with the surrender of Germany and Japan. After the war, the United States and the Soviet Union became the two main superpowers, helping set up the Cold War."
    },
    {
        "year": 1947,
        "title": "Truman Doctrine",
        "category": "Cold War",
        "summary": "The Truman Doctrine was a U.S. policy announced by President Harry S. Truman. It promised support to countries resisting communism and became an important part of Cold War containment."
    },
    {
        "year": 1948,
        "title": "Berlin Blockade and Airlift",
        "category": "Cold War",
        "summary": "The Soviet Union blocked access to West Berlin, and the United States and its allies responded by flying supplies into the city. This became one of the first major crises of the Cold War."
    },
    {
        "year": 1955,
        "title": "Vietnam War Begins",
        "category": "Cold War",
        "summary": "The Vietnam War was fought between communist North Vietnam and anti-communist South Vietnam, with the United States supporting South Vietnam. It became one of the biggest Cold War conflicts."
    },
    {
        "year": 1961,
        "title": "Berlin Wall Built",
        "category": "Cold War",
        "summary": "East Germany built the Berlin Wall to stop people from leaving East Berlin for West Berlin. The wall became a major symbol of the division between communism and democracy."
    },
    {
        "year": 1969,
        "title": "Apollo 11 Moon Landing",
        "category": "Space Race",
        "summary": "Apollo 11 landed the first humans on the Moon. This was a major victory for the United States during the Space Race against the Soviet Union."
    },
    {
        "year": 1979,
        "title": "Soviet-Afghan War",
        "category": "Cold War",
        "summary": "The Soviet Union invaded Afghanistan in 1979. The United States supported Afghan fighters, making the war another major Cold War proxy conflict."
    },
    {
        "year": 1989,
        "title": "Fall of the Berlin Wall",
        "category": "Cold War",
        "summary": "The Berlin Wall fell in 1989, allowing East and West Berlin to reconnect. This event showed that communist control in Eastern Europe was weakening."
    },
    {
        "year": 1991,
        "title": "Dissolution of the Soviet Union",
        "category": "Cold War",
        "summary": "The Soviet Union collapsed in 1991, creating 15 independent republics. This marked the end of the Cold War and changed global politics."
    }
]

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>History Timeline Explorer</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #111827;
            color: white;
            padding: 30px;
        }

        h1 {
            text-align: center;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            color: #d1d5db;
            margin-bottom: 30px;
        }

        form {
            text-align: center;
            margin-bottom: 30px;
        }

        input {
            padding: 12px;
            width: 320px;
            max-width: 80%;
            border-radius: 8px;
            border: none;
            font-size: 16px;
        }

        button {
            padding: 12px 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            margin-left: 5px;
        }

        .event {
            background: #1f2937;
            padding: 20px;
            margin: 15px auto;
            border-left: 5px solid #60a5fa;
            border-radius: 10px;
            max-width: 750px;
        }

        .year {
            color: #93c5fd;
            font-weight: bold;
            font-size: 18px;
        }

        .category {
            color: #facc15;
            font-weight: bold;
        }

        .empty {
            text-align: center;
            color: #d1d5db;
        }
    </style>
</head>
<body>
    <h1>History Timeline Explorer</h1>
    <p class="subtitle">Search major Cold War and modern history events.</p>

    <form method="GET">
        <input name="search" placeholder="Search Cold War, Vietnam, Berlin, 1991..." value="{{ search }}">
        <button type="submit">Search</button>
    </form>

    {% if results %}
        {% for event in results %}
            <div class="event">
                <div class="year">{{ event.year }}</div>
                <h2>{{ event.title }}</h2>
                <p class="category">{{ event.category }}</p>
                <p>{{ event.summary }}</p>
            </div>
        {% endfor %}
    {% else %}
        <p class="empty">No events found. Try searching for Cold War, Vietnam, Berlin, or 1991.</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    search = request.args.get("search", "").strip().lower()

    if search:
        results = [
            event for event in EVENTS
            if search in event["title"].lower()
            or search in event["category"].lower()
            or search in event["summary"].lower()
            or search in str(event["year"])
        ]
    else:
        results = EVENTS

    results = sorted(results, key=lambda event: event["year"])
    return render_template_string(HTML, results=results, search=search)

if __name__ == "__main__":
    app.run(debug=True)
