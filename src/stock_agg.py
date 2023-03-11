from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.client import Client, Users
from diagrams.programming.language import Python
from diagrams.generic.storage import Storage
from diagrams.programming.flowchart import PredefinedProcess


with Diagram("Stock Data Aggregation System", direction="TB"):
    users = Users("Users")
    user_client = Client("Client")

    with Cluster("Stock Search System"):
        nyse = Storage("NYSE")
        nasdaq = Storage("NASDAQ")
        search = Python("Ticker Symbol Search")
        [nyse, nasdaq] >> search

    yfinance = Custom("YFinance", "yfinance.png")
    stock_info_parser = Python("Stock Info. Parser")
    stock_data_aggregator = Python("Stock Data Aggregator")
    wishlist = PredefinedProcess("Wishlist")
    trending = PredefinedProcess("Trending")
    monte_carlo_simulator = PredefinedProcess("Monte Carlo Model")
    historical_stock_price_and_info = PredefinedProcess("Historical Stock Info")

    users >> user_client >> search >> yfinance >> stock_info_parser
    yfinance >> stock_data_aggregator >> monte_carlo_simulator
    stock_info_parser >> wishlist
    stock_info_parser >> trending
    stock_info_parser >> historical_stock_price_and_info
