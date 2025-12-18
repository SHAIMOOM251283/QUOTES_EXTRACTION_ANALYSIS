import json
import plotly.express as px
from collections import defaultdict
import os

class DataVisualizationTags:

    def __init__(self):
        self.INPUT_JSON_PATH = "processed_quotes.json"
        self.quotes = self.load_json()
        self.records = self.prepare_data()

        # Consistent color scheme for all charts
        self.color_map = {
            "Positive": "#2ecc71",  # green
            "Neutral":  "#3498db",  # blue
            "Negative": "#e74c3c"   # red
        }

    def load_json(self):
        if not os.path.exists(self.INPUT_JSON_PATH):
            print(f"Processed JSON file not found: {self.INPUT_JSON_PATH}")
            exit()

        with open(self.INPUT_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def prepare_data(self):
        tag_sentiment = defaultdict(lambda: {"Positive": 0, "Neutral": 0, "Negative": 0})

        for q in self.quotes:
            sentiment = q.get("sentiment", "Neutral")
            for tag in q.get("tags", []):
                tag_sentiment[tag][sentiment] += 1

        records = []
        for tag, sent_counts in tag_sentiment.items():
            for sentiment, count in sent_counts.items():
                records.append({
                    "tag": tag,
                    "sentiment": sentiment,
                    "count": count
                })

        return records

    def create_bar_chart(self):
        # Sorting tags alphabetically for consistent chart ordering
        sorted_tags = sorted({r["tag"] for r in self.records})

        fig = px.bar(
            self.records,
            x="tag",
            y="count",
            color="sentiment",
            color_discrete_map=self.color_map,  # SAME COLORS for all charts
            title="Sentiment Distribution by Tag",
            barmode="stack",
            text="count",
            category_orders={"tag": sorted_tags}
        )

        fig.update_layout(
            xaxis_tickangle=-45,
            template="plotly_white"
        )

        output_dir = "../visualizations/bar_charts/"
        os.makedirs(output_dir, exist_ok=True)

        fig.write_html(os.path.join(output_dir, "bar_chart_tags.html"))
        print("Bar chart saved as HTML!")

if __name__ == '__main__':
    DataVisualizationTags().create_bar_chart()
