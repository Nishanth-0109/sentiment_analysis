

from textblob import TextBlob

def analyze(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        mood = "Positive 😊"
    elif polarity < -0.1:
        mood = "Negative 😞"
    else:
        mood = "Neutral 😐"
    print(f"  Sentiment : {mood}  (score: {polarity:+.2f})\n")

# --- Demo ---
samples = [
    "I love this! It's absolutely amazing.",
    "This is terrible. Very disappointed.",
    "The item arrived on time.",
]

print("=== Sentiment Analyser ===\n")
for text in samples:
    print(f"  Text: {text!r}")
    analyze(text)

# --- Interactive ---
print("Try it yourself (type 'quit' to exit):\n")
while True:
    text = input("Enter text: ").strip()
    if text.lower() in ("quit", "q"):
        break
    analyze(text)