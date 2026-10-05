from netmiko import ConnectHandler

CONFIG_FILE = "configs/router1_dhcp.cfg"

router = {
    "device_type": "cisco_ios",
    "host": "192.168.10.1",
    "username": "netkode",
    "password": "netkode",
}

print("Reading configuration file...")

with open(CONFIG_FILE, "r") as file:
    commands = [
        line.strip()
        for line in file
        if line.strip()
    ]

print("Configuration to be deployed:")
for command in commands:
    print(f"  {command}")

print("\nConnecting to R1...")

connection = ConnectHandler(**router)

print("Connected to R1")

print("\nPushing configuration to R1...")

output = connection.send_config_set(commands)

print("\n=== R1 Configuration Output ===")
print(output)

connection.save_config()

connection.disconnect()

print("\nConfiguration deployed successfully")
print("Disconnected from R1")
