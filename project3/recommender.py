from catalog import CATALOG
from engine import build_tfidf_matrix, get_recommendations


def main():
    vectorizer, tfidf_matrix = build_tfidf_matrix(CATALOG)

    print("=" * 47)
    print("DecodeLabs Project 3 — Movie Recommender")
    print("=" * 47)
    print("Tell me what kind of movie you're in the mood for.")
    print('Examples: "action hero adventure", "sad romantic drama", '
          '"funny lighthearted family"')
    print()

    while True:
        try:
            user_input = input("What are you in the mood for? > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! Happy watching :)")
            break

        if not user_input:
            print("Please type at least one word describing your mood.")
            print()
            continue

        recommendations = get_recommendations(
            user_input, vectorizer, tfidf_matrix, CATALOG
        )

        print()
        print("Top 5 Picks For You:")
        for i, rec in enumerate(recommendations, start=1):
            print(f"{i}. {rec['title']} (score: {rec['score']})")
        print()

        try:
            again = input("Try again with different preferences? (yes/no) > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! Happy watching :)")
            break

        if again != "yes":
            print("\nGoodbye! Happy watching :)")
            break
        print()


if __name__ == "__main__":
    main()
