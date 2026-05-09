from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_tfidf_matrix(catalog):
    """
    Takes the catalog and builds a TF-IDF matrix from the tags.
    Returns the fitted vectorizer and the matrix so we can reuse them.
    """
    # grab all the tag strings from the catalog
    tag_list = [movie["tags"] for movie in catalog]

    # fit the vectorizer — stop_words removes stuff like "the", "a", etc.
    vec = TfidfVectorizer(stop_words="english")
    matrix = vec.fit_transform(tag_list)

    return vec, matrix


def get_recommendations(user_text, vec, tfidf_matrix, catalog, top_n=5):
    """
    Turns the user's text into a vector, compares it against every
    movie using cosine similarity, and returns the top_n matches.
    """
    # vectorize the user's input using the SAME vectorizer
    user_vec = vec.transform([user_text])

    # compute similarity between user and ALL movies at once
    scores = cosine_similarity(user_vec, tfidf_matrix).flatten()

    # argsort gives us indices from lowest to highest,
    # so [::-1] reverses it to get highest first
    ranked = scores.argsort()[::-1]

    # build the result list
    results = []
    for i in ranked[:top_n]:
        results.append({
            "title": catalog[i]["title"],
            "score": round(float(scores[i]), 2),
            "tags": catalog[i]["tags"],
        })

    return results
