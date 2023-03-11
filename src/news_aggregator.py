from diagrams import Diagram, Cluster
from diagrams.programming.framework import FastAPI
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.client import Client, Users
from diagrams.programming.language import Python
from diagrams.programming.flowchart import PredefinedProcess
from diagrams.custom import Custom

with Diagram("News Aggregator", direction="LR"):
    news_api = Custom("News API", "news-api.png")
    with Cluster("News Processor"):
        news_aggregator = Python("News Aggregator")
        sentiment_analyzer = Python("Sentiment Analyzer")
        reccomender_article_engine = Python("Recommender Article Engine")
        news_aggregator >> sentiment_analyzer >> reccomender_article_engine
        proccess = [news_aggregator, sentiment_analyzer, reccomender_article_engine]

    wishlist = PredefinedProcess("Wishlist")
    notifier = PredefinedProcess("Notifier")
    recommeded_articles = PostgreSQL("Recommended Articles")
    users = Users("Users")

    news_api >> news_aggregator
    wishlist >> reccomender_article_engine
    reccomender_article_engine >> recommeded_articles
    reccomender_article_engine >> notifier >> users
