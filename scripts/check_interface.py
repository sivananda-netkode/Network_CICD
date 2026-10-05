from pathlib import Path
from pybatfish.client.session import Session

# Connect to Batfish
bf = Session(host="localhost", port=9996)

# Load the configuration snapshot
snapshot_path = Path("batfish_snapshot").resolve()

bf.init_snapshot(
    str(snapshot_path),
    name="dhcp-lab",
    overwrite=True
)

# Ask Batfish for interface information
interfaces = bf.q.interfaceProperties().answer().frame()

print("=== Columns returned by Batfish ===")
print(interfaces.columns.tolist())

print("\n=== Complete interface information ===")
print(interfaces)
