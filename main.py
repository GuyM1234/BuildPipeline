import requests



x = requests.post("http://localhost:5000/", data=config)
print(x)