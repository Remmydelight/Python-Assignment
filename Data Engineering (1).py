import re

def letter_score(letter):
    common_uncommon_scores = {'Q': 1, 'Z': 1, 'J': 3, 'X': 3, 'K': 6, 'F': 7, 'H': 7, 'V': 7, 'W': 7, 'Y': 7,
                              'B': 8, 'C': 8, 'M': 8, 'P': 8, 'D': 9, 'G': 9, 'L': 15, 'N': 15, 'R': 15, 'S': 15,
                              'T': 15, 'O': 20, 'U': 20, 'A': 25, 'I': 25, 'E': 35}

    return common_uncommon_scores.get(letter, 0)

def calculate_score(word):
    scores = [letter_score(word[i]) if i == 0 else
              (20 if word[i] == 'E' else 5 if i == len(word) - 1 else
               (1 if i == 1 else 2 if i == 2 else 3) + letter_score(word[i]))
              for i in range(len(word))]
    
    return sum(scores[1:])  # Exclude the score for the first letter

def clean_word(word):
    return ''.join(char.upper() if char.isalpha() else '' for char in word)

def generate_abbreviations(word):
    return [word[:3], word[:2] + word[-1], word[0] + word[-2:]]

def pick_best_abbreviation(word, abbreviations):
    return min(abbreviations, key=calculate_score)

def abbreviate_single_word(word):
    cleaned_word = clean_word(word)
    abbreviation_options = generate_abbreviations(cleaned_word)
    best_abbreviation = pick_best_abbreviation(cleaned_word, abbreviation_options)
    return f"{word}: {best_abbreviation}"

def abbreviate_two_words(words):
    combined_words = ' '.join(words)
    cleaned_combined_words = ''.join(char.upper() if char.isalpha() else ' ' for char in combined_words)
    abbreviation_options = generate_abbreviations(cleaned_combined_words)
    best_abbreviation = pick_best_abbreviation(cleaned_combined_words, abbreviation_options)
    return f"{' '.join(words)}: {best_abbreviation[:3]}"

def abbreviate_three_words(words):
    cleaned_words = [clean_word(word) for word in words]
    abbreviation = ''.join(word[0] for word in cleaned_words if word)
    return f"{' '.join(words)}: {abbreviation}"

def main():
    input_file_name = input("Enter the file name (without extension): ")
    surname = input("Enter your surname: ")

    with open(f"{input_file_name}.txt", "r") as file:
        words = [line.strip() for line in file.readlines()]

    output_file_name = f"{surname}_{input_file_name}.txt"

    with open(output_file_name, "w") as output_file:
        output_file.write("Abbreviations:\n")

        for word in words:
            word_list = re.split(r'\s+', word)
            num_words = len(word_list)

            if num_words == 1:
                result = abbreviate_single_word(word_list[0])
            elif num_words == 2:
                result = abbreviate_two_words(word_list)
            elif num_words >= 3:
                result = abbreviate_three_words(word_list)

            output_file.write(result + "\n")

    print(f"Results written to: {output_file_name}")

if __name__ == "__main__":
    main()
