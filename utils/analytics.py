import plotly.express as px

def volume_by_category(df):
    fig = px.bar(
        df,
        x="category",
        y="volume",
        title="Trading Volume by Category",
        text_auto=True
    )
    return fig

def yes_price_distribution(df):
    fig = px.histogram(
        df,
        x="yes_price",
        nbins=10,
        title="YES Price Distribution"
    )
    return fig

def top_markets(df):
    return df.sort_values("volume", ascending=False).head(5)
