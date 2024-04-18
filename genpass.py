import random

# Palabras para usar en la contraseña
words = [
    "apple", "banana", "orange", "grape", "pineapple", "watermelon", "strawberry", "kiwi",
    "carrot", "potato", "tomato", "broccoli", "cucumber", "lettuce", "pepper", "onion",
    "dog", "cat", "bird", "rabbit", "hamster", "fish", "turtle", "guinea pig",
    "car", "bicycle", "motorcycle", "bus", "train", "airplane", "boat", "truck",
    "house", "apartment", "cabin", "castle", "tent", "igloo", "mansion", "hut",
    "sun", "moon", "star", "cloud", "rain", "snow", "wind", "storm",
    "beach", "mountain", "forest", "desert", "valley", "island", "cave", "canyon",
    "book", "pen", "pencil", "notebook", "computer", "phone", "tablet", "camera",
    "music", "movie", "art", "dance", "theater", "poetry", "painting", "photography"
    # Agrega más palabras según lo desees
]

# Años del calendario gregoriano
years = list(range(1300, 2025))

def generate_password():
    # Seleccionar una palabra aleatoria
    word = random.choice(words)
    # Seleccionar un año aleatorio
    year = random.choice(years)
    # Combinar la palabra y el año para formar la contraseña
    password = f"{word}{year}"
    return password

# Generar una contraseña
password = generate_password()
print("Tu contraseña generada es:", password)
