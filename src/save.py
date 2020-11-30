import os
from datetime import datetime



date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

commands  = [
    "git add -A",
    "git commit -m \"{}\"".format(date),
    "git push --force"
]

for i in commands:
    try:
        os.system(i)
    except Exception as e:
        print("Error {}: {}".format(e.__class__.__name__, str(e)))
        break


# test