# Project 3 — Movie Recommendation CLI

## What this does
This is a terminal-based movie recommender. You type a mood or vibe like "dark thriller suspense" and it gives you five movies ranked by how well they match. No internet, no AI model — just math.

## How it works
The app has three pieces that work together.

First, there's `catalog.py`. It's just a list of 18 movies, each with a `title` and a `tags` string stuffed with descriptive keywords — genre, mood, themes, director. The tags are the whole game. Generic tags produce garbage scores, so I made them rich and specific.

Second, `engine.py` is the brain. When the app starts, it feeds all 18 tag strings into scikit-learn's `TfidfVectorizer`, which converts every word into a weighted number. Words that show up everywhere (like "drama") get downweighted. Rare, specific words (like "Tarantino" or "cyberpunk") get boosted. This produces a matrix — 18 rows of movies, each column a word, each cell a number representing importance. That build happens once at startup.

When you type your mood, `engine.py` runs your words through the same vectorizer and computes cosine similarity — basically measuring the angle between your vector and every movie's vector. A score of 1.0 means identical, 0.0 means unrelated. The top 5 get returned sorted by score.

Third, `recommender.py` is the CLI. It shows a welcome banner, asks what you're in the mood for, calls the engine, and prints a numbered list with scores rounded to two decimals. If you type nothing it re-prompts instead of crashing. After showing results it asks if you want to try again — loops until you say no.

## How to run it
```bash
cd project3
pip install -r requirements.txt
python recommender.py
```

```bash
git add project3/
git commit -m "feat: recommendation system - DecodeLabs Project 3"
git push origin main
```

## What I actually learned
The TF-IDF vectorizer clicked once I saw it in action — feeding it 18 strings and getting back a matrix where you could literally see which words carried weight was way more satisfying than reading about it in theory.

The biggest surprise was how hard tag quality hits the results. I started with lazy tags like "good movie action" and the scores were flat zeros across the board. Once I rewrote every tag to include mood, themes, director names, and specific genre keywords, the recommendations suddenly made sense. Typing "scary horror" actually returned The Conjuring at 0.66.

Empty input handling seemed trivial but the first version crashed on a blank line. A real user will absolutely hit Enter by accident, so the re-prompt loop matters more than it looks.
