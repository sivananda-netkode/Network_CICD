from pathlib import Path

from pybatfish.client.session import Session


def test_r1_interface():
    # Connect to Batfish
    bf = Session(host="localhost", port=9996)

    # Load the network configuration
    snapshot_path = Path("batfish_snapshot").resolve()

    bf.init_snapshot(
        str(snapshot_path),
        name="dhcp-lab",
        overwrite=True
    )

    # Get interface information
    interfaces = bf.q.interfaceProperties().answer().frame()

    # Find FastEthernet0/0
    r1_interface = interfaces[
        interfaces["Interface"].astype(str).str.endswith(
            "FastEthernet0/0]"
        )
    ]

    # Make sure the interface exists
    assert not r1_interface.empty

    # Get the interface row
    interface = r1_interface.iloc[0]

    # Verify interface state
    assert interface["Admin_Up"] is True
    assert interface["Active"] is True

    # Verify IP address
    assert str(interface["Primary_Address"]) == "192.168.10.1/24"
