from catalog import CATALOG
from engine import build_tfidf_matrix, get_recommendations


def main():
    # build the tfidf stuff once at startup — don't rebuild on every loop
    vec, matrix = build_tfidf_matrix(CATALOG)

    # welcome message
    print("===============================================")
    print("  DecodeLabs Project 3 - Movie Recommender")
    print("===============================================")
    print()
    print("Tell me what kind of movie you're in the mood for.")
    print('For example: "action adventure" or "sad romance"')
    print()

    while True:

        # get the user's mood
        mood = input("What are you in the mood for? > ").strip()

        # if they hit enter without typing anything
        if mood == "":
            print("Oops, you gotta type something! Try again.")
            print()
            continue

        # run the recommendations
        recs = get_recommendations(mood, vec, matrix, CATALOG)

        # display results
        print()
        print("Top 5 Picks For You:")
        for num, movie in enumerate(recs, start=1):
            print(f"{num}. {movie['title']} (score: {movie['score']})")
        print()

        # ask if they wanna go again
        again = input("Try again with different preferences? (yes/no) > ").strip().lower()

        if again == "yes":
            print()
            continue
        else:
            print()
            print("Cool, hope you found something good! :)")
            break


if __name__ == "__main__":
    main()
