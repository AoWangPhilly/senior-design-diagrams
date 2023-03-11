from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.programming.framework import FastAPI
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.client import Client, Users
from diagrams.programming.language import Python

with Diagram("Wishlist System", direction="LR"):
    users = Users("Users")
    user_client = Client("Client")
    user_validator = Custom("Validator", "pydantic.png")

    wishlist = PostgreSQL("Wishlist")

    with Cluster("Routes"):
        create = FastAPI("Create")
        delete = FastAPI("Delete")
        rename = FastAPI("Rename")
        add_stock = FastAPI("Add Stock")
        remove_stock = FastAPI("Remove Stock")
        routes = [create, delete, rename, add_stock, remove_stock]

    (users >> user_client >> user_validator >> routes >> wishlist)

    with Cluster("Stock Reccomendator"):
        stock_reccomendator = Python("Stock Reccomendator")
        stock_notifier = Python("Stock Notifier")
        wishlist >> stock_reccomendator >> stock_notifier >> users
