import json
import os
from wordcloud import WordCloud
import plotly.express as px
from PIL import Image
import numpy as np
from collections import defaultdict

class DataVisualization:

    def __init__(self):
        self.INPUT_JSON_PATH = "processed_quotes.json"
        self.quotes = self.load_json()
        self.sentiment_texts = self.prepare_data()

    def load_json(self):
        if not os.path.exists(self.INPUT_JSON_PATH):
            print(f"Processed JSON file not found: {self.INPUT_JSON_PATH}")
            exit()

        with open(self.INPUT_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def prepare_data(self):
        sentiment_texts = defaultdict(str)

        for q in self.quotes:
            sentiment = q.get("sentiment", "Neutral")
            text = q.get("text", "")
            sentiment_texts[sentiment] += " " + text
        
        return sentiment_texts

    def create_word_cloud(self):
        for sentiment, text in self.sentiment_texts.items():
            if not text.strip():
                continue

            # Generate word cloud using WordCloud library
            wc = WordCloud(width=800, height=400, background_color="white", colormap="tab10", max_words=200)
            wc.generate(text)

            # Convert to image array
            img_array = np.array(wc.to_image())

            # Plot using Plotly Express
            fig = px.imshow(img_array)
            fig.update_layout(
                title=f"Word Cloud: {sentiment}",
                xaxis_visible=False,
                yaxis_visible=False,
                margin=dict(l=0, r=0, t=40, b=0)
            )

            output_dir = os.path.join("..", "visualizations", "word_clouds")
            os.makedirs(output_dir, exist_ok=True)
            
            filename = f"word_cloud_2_{sentiment.lower()}.html"
            output_path = os.path.join(output_dir, filename)

            fig.write_html(output_path)
            print(f"Word Cloud saved: {sentiment}")

if __name__ == '__main__':
    DataVisualization().create_word_cloud()