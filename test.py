import subprocess

interface = "wlp4s0"  # Replace with your WiFi interface name

# Use iwlist to scan for available networks
output = subprocess.check_output(["sudo", "iwlist", interface, "scan"]).decode()

# Parse the output to extract the RSSI values for each channel
rssi_values = {}
current_channel = None
isFiveG = False
for line in output.split("\n"):
    line = line.strip()
    if line.startswith("Channel"):
        current_channel = int(line.split(":")[1])
    elif line.startswith("Frequency:"):
        isFiveG = int(line.split(":")[1].split(".")[0]) == 2
    elif line.startswith("Quality="):
        if isFiveG:
            rssi = int(line.split("=")[2].split()[0])
            rssi_values[current_channel] = rssi
print(len(rssi_values))
# Print the RSSI values for each channel
for channel, rssi in rssi_values.items():
    print(f"Channel {channel}: {rssi} dBm")