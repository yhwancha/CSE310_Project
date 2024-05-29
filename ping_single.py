import subprocess
import re

def ping_host(host):
    try:
        # Run the ping command and capture the output
        result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print(f"Error pinging {host}: {result.stderr}")
            return None

        # Extract all response times from the ping command output
        times = re.findall(r'time=([\d.]+) ms', result.stdout)
        if times:
            times = [float(time) for time in times]
            average_response_time = sum(times) / len(times)
            return average_response_time
        else:
            print(f"Could not find any response times in ping output for {host}")
            return None

    except Exception as e:
        print(f"An error occurred while pinging {host}: {str(e)}")
        return None

# Example usage
host = '223.130.160.225'
average_time = ping_host(host)
if average_time is not None:
    print(f"Average response time for {host}: {average_time:.2f} ms")
else:
    print(f"Failed to get average response time for {host}")