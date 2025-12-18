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
        author_counts = defaultdict(int)
        for q in self.quotes:
            author = q.get("author", "Unknown")
            author_counts[author] += 1

        plot_data = [{"author": author, "count": count} for author, count in author_counts.items()]
        return plot_data 

    def create_treemap(self):
        fig = px.treemap(
            self.plot_data,
            path=["author"],      # each author = one rectangle
            values="count",       # size of rectangle = number of quotes
            color="count",        # optional: color intensity by count
            color_continuous_scale="Blues",
            title="Treemap: Number of Quotes per Author"
        )

        output_dir = "../visualizations/exploratory_charts/"
        os.makedirs(output_dir, exist_ok=True)

        fig.write_html(os.path.join(output_dir, "treemap.html"))        
        print("Treemap saved as HTML!")

if __name__ == '__main__':
    DataVisualization().create_treemap()

