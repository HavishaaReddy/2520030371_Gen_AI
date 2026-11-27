
import random

# Training text
text = """
the student studied hard
the student studied well
the student passed examination
the student worked hard
the teacher taught students
the teacher explained concepts
students studied hard and passed
"""

# Tokenization
words = text.lower().split()

# Build next-word probability dictionary
model = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in model:
        model[current_word] = []

    model[current_word].append(next_word)


# Autoregressive generation
def generate_text(start_word, max_words=10):

    current_word = start_word
    generated = [current_word]

    for _ in range(max_words):

        if current_word not in model:
            break

        # Predict the next word
        next_word = random.choice(model[current_word])

        # Append predicted word
        generated.append(next_word)

        # Use predicted word as next input
        current_word = next_word

    return " ".join(generated)


# Generate text
result = generate_text("the", 10)

print("Generated Text:")
print(result)
