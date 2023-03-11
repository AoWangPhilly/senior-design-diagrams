from diagrams import Diagram, Cluster
from diagrams.programming.framework import FastAPI
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.client import Client, Users
from diagrams.programming.language import Python
from diagrams.programming.flowchart import PredefinedProcess

with Diagram("Monte Carlo Simulation Model", direction="LR"):
    users = Users("Users")
    user_client = Client("Client")
    search = Python("Ticker Symbol Search")
    monte_carlo_simulator = PredefinedProcess("Monte Carlo Model")
    stock_data_aggregator = Python("Stock Data Aggregator")
    wellness_calculator = Python("Wellness Calculator")

    with Cluster("Routes"):
        save = FastAPI("Save Results")
        get = FastAPI("Get Results")

        routes = [save, get]
    predictor_model = PostgreSQL("Predictor Model Results")

    (
        users
        >> user_client
        >> search
        >> stock_data_aggregator
        >> monte_carlo_simulator
        >> routes
    )
    save >> predictor_model
    get >> wellness_calculator
