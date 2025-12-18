import json
import os
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm  

class ProcessSentiment:

    def __init__(self):
        self.INPUT_JSON_PATH = "../data_extraction/quotes.json"
        self.OUTPUT_JSON_PATH = "processed_quotes.json"

    def load_json(self, path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def analyze_sentiment(self, quotes):
        sia = SentimentIntensityAnalyzer()
        processed = []

        for q in tqdm(quotes, desc="Analyzing Sentiment"):
            text = q.get("text", "")
            author = q.get("author", "")
            tags = q.get("tags", [])

            scores = sia.polarity_scores(text)
            compound = scores["compound"]

            # Determine sentiment label
            if compound >= 0.05:
                sentiment = "Positive"
            elif compound <= -0.05:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            # Store processed record
            processed.append({
                "text": text,
                "author": author,
                "tags": tags,
                "compound": compound,
                "sentiment": sentiment,
                "scores": scores
            })

        return processed

    def save_json(self, data, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def run(self):
        if not os.path.exists(self.INPUT_JSON_PATH):
            print(f"Input JSON file not found: {self.INPUT_JSON_PATH}")
            return

        quotes = self.load_json(self.INPUT_JSON_PATH)
        print(f"Loaded {len(quotes)} quotes.")

        processed_quotes = self.analyze_sentiment(quotes)
        self.save_json(processed_quotes, self.OUTPUT_JSON_PATH)

        print(f"Processed quotes saved to: {self.OUTPUT_JSON_PATH}")

if __name__ == "__main__":
    ProcessSentiment().run()
