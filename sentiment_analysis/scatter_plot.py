import json
import os
import plotly.express as px
import textwrap

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

    
    def wrap_text(self, text, width=80):
        return "<br>".join(textwrap.wrap(text, width=width))

    def prepare_data(self):
        plot_data = []

        for q in self.quotes:
            author = q.get("author", "Unknown")
            text = q.get("text", "")
            length = len(text)
            compound = q.get("compound", 0.0)
            sentiment = q.get("sentiment", "Neutral")

            wrapped = self.wrap_text(text, width=80)

            plot_data.append({
                "author": author,
                "length": length,
                "compound": compound,
                "sentiment": sentiment,
                "quote_wrapped": wrapped,  # formatted for tooltip
            })
        
        return plot_data

    def create_scatter_plot(self):
        fig = px.scatter(
            self.plot_data,
            x="length",
            y="compound",
            color="author",
            hover_data={"author": True, "quote_wrapped": True, "sentiment": True},
            title="Scatter Plot: Compound Sentiment Score vs Quote Length",
            labels={
                "length": "Quote Length (characters)",
                "compound": "Compound Sentiment Score"
            }
        )

        fig.update_traces(
            hovertemplate=
            "<b>Author:</b> %{customdata[0]}<br>" +   # 0 = author
            "<b>Length:</b> %{x}<br>"
            "<b>Compound Score:</b> %{y}<br>"
            "<b>Sentiment:</b> %{customdata[2]}<br><br>" +  # 2 = sentiment
            "<b>Quote:</b><br>%{customdata[1]}"              # 1 = wrapped quote
        )

        output_dir = "../visualizations/exploratory_charts/"
        os.makedirs(output_dir, exist_ok=True)

        fig.write_html(os.path.join(output_dir, "scatter_plot.html"))        
        print("Scatter plot saved as HTML!")

if __name__ == '__main__':
    DataVisualization().create_scatter_plot()