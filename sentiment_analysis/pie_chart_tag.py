import json
import plotly.graph_objects as go
from collections import defaultdict
import os
import re

class DataVisualizationTags:

    def __init__(self):
        self.INPUT_JSON_PATH = "processed_quotes.json"
        self.quotes = self.load_json()

        # Consistent color map
        self.color_map = {
            "Positive": "#2ecc71",
            "Neutral": "#3498db",
            "Negative": "#e74c3c"
        }

    def clean_filename(self, name):
        """Remove invalid filename characters."""
        return re.sub(r'[\\/*?:"<>|]', "_", name)

    def load_json(self):
        if not os.path.exists(self.INPUT_JSON_PATH):
            print(f"Processed JSON file not found: {self.INPUT_JSON_PATH}")
            exit()

        with open(self.INPUT_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def prepare_all_tags(self):
        tag_sentiment_counts = defaultdict(lambda: {"Positive": 0, "Neutral": 0, "Negative": 0})

        for q in self.quotes:
            sentiment = q.get("sentiment", "Neutral")
            for tag in q.get("tags", []):
                tag_sentiment_counts[tag][sentiment] += 1

        return tag_sentiment_counts
    
    def make_safe_filename(self, name):
        name = name.replace(" ", "_")
        name = re.sub(r"[^A-Za-z0-9_-]", "_", name)
        return name

    def create_pie_chart(self, tag, sentiment_dict):

        labels = ["Positive", "Neutral", "Negative"]
        values = [sentiment_dict[label] for label in labels]
        colors = [self.color_map[label] for label in labels]

        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.4,
            marker=dict(colors=colors, line=dict(color='white', width=3)),
            pull=[0.05, 0.02, 0.05]
        )])

        fig.update_traces(textinfo='percent+label')
        fig.update_layout(title_text=f"Sentiment Distribution for Tag: '{tag}'")

        output_dir = "../visualizations/pie_chart_tags/"
        os.makedirs(output_dir, exist_ok=True)

        safe_name = self.make_safe_filename(tag)
        fig.write_html(os.path.join(output_dir, f"{safe_name}.html"))

    def generate_all_charts(self):
        tag_data = self.prepare_all_tags()
        print("Generating charts for all tags...\n")

        for tag, counts in tag_data.items():
            print(f"Creating chart for tag: {tag}")
            self.create_pie_chart(tag, counts)

        print("\nAll tag charts generated successfully!")

if __name__ == '__main__':
    DataVisualizationTags().generate_all_charts()
