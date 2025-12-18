import json
import os
from collections import defaultdict
import plotly.graph_objects as go

class DataVisualization:

    def __init__(self):
        self.INPUT_JSON_PATH = "processed_quotes.json"
        self.quotes = self.load_json()
        self.nodes, self.authors, self.tags, self.source, self.target, self.value, self.source = self.prepare_data()

    def load_json(self):
        if not os.path.exists(self.INPUT_JSON_PATH):
            print(f"Processed JSON file not found: {self.INPUT_JSON_PATH}")
            exit()

        with open(self.INPUT_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)        
        return data

    def prepare_data(self):
        authors = sorted({q.get("author", "Unknown") for q in self.quotes})
        sentiments = ["Positive", "Neutral", "Negative"]
        tags = sorted({tag for q in self.quotes for tag in q.get("tags", [])})

        nodes = authors + sentiments + tags
        node_indices = {node: i for i, node in enumerate(nodes)}

        link_counts = defaultdict(int)

        for q in self.quotes:
            author = q.get("author", "Unknown")
            sentiment = q.get("sentiment", "Neutral")
            link_counts[(author, sentiment)] += 1

        for q in self.quotes:
            sentiment = q.get("sentiment", "Neutral")
            for tag in q.get("tags", []):
                link_counts[(sentiment, tag)] += 1

        source = []
        target = []
        value = []

        for (src, tgt), cnt in link_counts.items():
            source.append(node_indices[src])
            target.append(node_indices[tgt])
            value.append(cnt)
        
        return nodes, authors, tags, source, target, value, source

    def create_sankey_diagram(self):
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=self.nodes,
                color=["lightblue"]*len(self.authors) + ["gray"]*3 + ["lightgreen"]*len(self.tags)
            ),
            link=dict(
                source=self.source,
                target=self.target,
                value=self.value,
                color=["rgba(0,0,255,0.2)"]*len(self.source)  # semi-transparent links
            )
        )])

        fig.update_layout(
            title_text="Sankey Diagram: Author → Sentiment → Tag",
            font_size=12
        )

        output_dir = "../visualizations/exploratory_charts/"
        os.makedirs(output_dir, exist_ok=True)

        fig.write_html(os.path.join(output_dir, "sankey_diagram.html"))        
        print("Sankey diagram saved as HTML!")

if __name__ == '__main__':
    DataVisualization().create_sankey_diagram()
