import random

def load_words_from_file(filename="kids_combined_word_list.txt"):
    """Load words from a text file and remove empty or duplicate words."""
    try:
        with open(filename, "r") as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith("#")]
        return words
    except FileNotFoundError:
        return ["default", "words", "list", "for", "testing", "only"]

def get_random_words(count):
    """Retrieve exactly 'count' number of random words from the word list."""
    words = load_words_from_file()

    # Remove duplicates and empty entries
    unique_words = list(set(filter(None, words)))

    # Ensure we only return exactly 'count' words
    if len(unique_words) >= count:
        selected_words = random.sample(unique_words, count)
    else:
        selected_words = unique_words  # If not enough words, return all available

    # Debugging output to verify word count
    print(f"Selected {len(selected_words)} words for the puzzle.")

    return selected_words
