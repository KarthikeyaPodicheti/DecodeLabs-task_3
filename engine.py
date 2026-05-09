from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_tfidf_matrix(catalog):
    """Fit a TF-IDF vectorizer on all item tags from the catalog.

    Args:
        catalog (list): List of dicts with a 'tags' key containing
            space-separated keyword strings.

    Returns:
        tuple: (fitted TfidfVectorizer, TF-IDF matrix as sparse array)
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    tag_texts = [item["tags"] for item in catalog]
    tfidf_matrix = vectorizer.fit_transform(tag_texts)
    return vectorizer, tfidf_matrix


def get_recommendations(user_input, vectorizer, tfidf_matrix, catalog, top_n=5):
    """Score every catalog item against the user's mood input using
    TF-IDF + cosine similarity and return the top matches.

    Args:
        user_input (str): User's free-text mood or preference string.
        vectorizer (TfidfVectorizer): Pre-fitted TfidfVectorizer instance.
        tfidf_matrix (sparse matrix): TF-IDF vectors for all catalog items.
        catalog (list): List of catalog dicts with 'title' and 'tags'.
        top_n (int): Number of top recommendations to return.

    Returns:
        list: Top-N dicts, each with keys 'title', 'score', 'tags',
            sorted by descending similarity score.
    """
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
    ranked_indices = similarities.argsort()[::-1]

    results = []
    for idx in ranked_indices[:top_n]:
        results.append({
            "title": catalog[idx]["title"],
            "score": round(float(similarities[idx]), 2),
            "tags": catalog[idx]["tags"],
        })
    return results
