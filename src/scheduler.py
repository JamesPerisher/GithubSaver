import os
from handyhelpers import customthreading
from handyhelpers import config



start_config = config.Config.from_file("config.json")

start_config["python"] = start_config["python"] if start_config["python"] != None else "python" # default python enviroment 
start_config["interval"] = start_config["interval"] if start_config["interval"] != None else 5 * 60 # default interval between saves

def test(n):
    os.system("start call {} save.py".format(start_config["python"]))



customthreading.TimeLoopedThread(5, test).start()