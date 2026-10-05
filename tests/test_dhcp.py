def test_dhcp_pool_exists():

    with open("configs/router1_dhcp.cfg") as file:
        config = file.read()

    assert "ip dhcp pool LAN" in config


def test_dhcp_network():

    with open("configs/router1_dhcp.cfg") as file:
        config = file.read()

    assert "network 192.168.10.0 255.255.255.0" in config
def test_dhcp_default_gateway():

    with open("configs/router1_dhcp.cfg") as file:
        config = file.read()

    assert "default-router 192.168.10.1" in config
def test_dhcp_dns_server():

    with open("configs/router1_dhcp.cfg") as file:
        config = file.read()

    assert "dns-server 8.8.8.8" in config
