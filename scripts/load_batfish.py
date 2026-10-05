from pathlib import Path
from pybatfish.client.session import Session

# Connect to Batfish
bf = Session(host="localhost", port=9996)

# Get the absolute path of our Batfish snapshot
snapshot_path = Path("batfish_snapshot").resolve()

print(f"Loading snapshot from: {snapshot_path}")

# Load configuration into Batfish
bf.init_snapshot(
    str(snapshot_path),
    name="dhcp-lab",
    overwrite=True
)

print("Snapshot loaded successfully")

# Ask Batfish for the devices it knows about
nodes = bf.q.nodeProperties().answer().frame()

print("\nDevices detected by Batfish:")
print(nodes[["Node"]])
