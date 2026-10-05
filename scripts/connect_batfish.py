from pybatfish.client.session import Session

bf = Session(host="localhost", port=9996)

print("Connected to Batfish")
print(bf)
