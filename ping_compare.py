import subprocess
import re

def ping(host):
    # Ping the host
    result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print(f"Error pinging {host}: {result.stderr}")
        return None

    # Extract the average response time from the output
    times = re.findall(r'time=([\d.]+) ms', result.stdout)
    if times:
        times = [float(time) for time in times]
        average_response_time = sum(times) / len(times)
        return average_response_time
    else:
        print(f"Could not find the average time in ping output for {host}")
        return None


def compare_ping(host1, host2):
    time1 = ping(host1)
    time2 = ping(host2)

    if time1 is not None and time2 is not None:
        print(f"Average response time for {host1}: {time1} ms")
        print(f"Average response time for {host2}: {time2} ms")

        if time1 < time2:
            print(f"{host1} is faster by {time2 - time1} ms")
        else:
            print(f"{host2} is faster by {time1 - time2} ms")
    else:
        print("Could not compare the ping times due to an error.")


# Define the hosts
naver_host = '101.101.219.201'
aws_host = '13.209.126.190'

# Compare the ping times
compare_ping(naver_host, aws_host)
