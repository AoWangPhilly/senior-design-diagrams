from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.programming.framework import FastAPI
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.client import Client, User, Users
from diagrams.programming.flowchart import Preparation

with Diagram("UID System", direction="LR"):
    user_validator = Custom("Validator", "pydantic.png")
    admin_validator = Custom("Validator", "pydantic.png")

    admin = User("Admin")
    users = Users("Users")
    admin_client = Client("Client")
    user_client = Client("Client")
    hashing = Preparation("Hash passwords")

    with Cluster("Routes"):
        delete = FastAPI("Delete")
        update = FastAPI("Update")
        signup = FastAPI("Signup")
        login = FastAPI("Login")
        logout = FastAPI("Logout")
        routes = [delete, update, signup, login, logout]

    with Cluster("Database"):
        accounts = PostgreSQL("Accounts")
        blacklist = PostgreSQL("Blacklist")
        tables = [accounts, blacklist]

    admin >> admin_client >> admin_validator
    admin_validator >> delete
    admin_validator >> update

    users >> user_client >> user_validator
    user_validator >> signup
    user_validator >> login
    user_validator >> logout

    delete >> accounts
    update >> hashing
    signup >> hashing
    hashing >> accounts

    hashing >> accounts
    login >> accounts
    logout >> Edge(label="Send expired token") >> blacklist
