import random
import time
import nltk

def generate_text(num_sentences):
    categories = ['news', 'editorial', 'reviews', 'religion', 'hobbies']
    category = random.choice(categories)
    words = nltk.corpus.brown.words(categories=category)
    start_index = random.randint(0, len(words) - num_sentences*10)
    end_index = start_index + num_sentences*10
    sentence_list = words[start_index:end_index]
    text = ' '.join(sentence_list)
    return text

def typing_test(num_sentences):
    text = generate_text(2)
    print(text)
    input("Press Enter to start typing...")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    words_per_minute = words_typed / elapsed_time * 60
    accuracy = sum([1 if a == b else 0 for (a, b) in zip(text, user_input)]) / len(text) * 100
    print(f"Your typing speed is {words_per_minute:.2f} words per minute.")
    print(f"Your accuracy is {accuracy:.2f}%.")
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
        typing_test(num_sentences)

if __name__ == '__main__':
    num_sentences = 5
    typing_test(num_sentences)
