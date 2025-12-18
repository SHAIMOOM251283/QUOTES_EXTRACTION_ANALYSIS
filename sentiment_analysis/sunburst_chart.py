import json
import os
from collections import defaultdict
import plotly.express as px

class DataVisualization:

    def __init__(self):
        self.INPUT_JSON_PATH = "processed_quotes.json"
        self.quotes = self.load_json()
        self.plot_data = self.prepare_data()

    def load_json(self):
        if not os.path.exists(self.INPUT_JSON_PATH):
            print(f"Processed JSON file not found: {self.INPUT_JSON_PATH}")
            exit()

        with open(self.INPUT_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def prepare_data(self):
        agg_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

        for q in self.quotes:
            author = q.get("author", "Unknown")
            sentiment = q.get("sentiment", "Neutral")
            for tag in q.get("tags", []):
                agg_counts[author][tag][sentiment] += 1

        # Flatten for Plotly
        plot_data = []
        for author, tags in agg_counts.items():
            for tag, sentiments in tags.items():
                for sentiment, count in sentiments.items():
                    plot_data.append({
                        "author": author,
                        "tag": tag,
                        "sentiment": sentiment,
                        "count": count
                    })
        
        return plot_data

    def create_suburst_chart(self):
        fig = px.sunburst(
            self.plot_data,
            path=["author", "tag", "sentiment"],  # hierarchy
            values="count",
            color="sentiment",                     # sentiment colors
            color_discrete_map={
                "Positive": "green",
                "Neutral": "gray",
                "Negative": "red"
            },
            title="Sunburst Chart: Author → Tag → Sentiment"
        )

        fig.update_traces(textinfo="label+percent parent")

        output_dir = "../visualizations/exploratory_charts/"
        os.makedirs(output_dir, exist_ok=True)

        fig.write_html(os.path.join(output_dir, "sunburst_chart.html"))        
        print("Sunburst chart saved as HTML!")

if __name__ == '__main__':
    DataVisualization().create_suburst_chart()
