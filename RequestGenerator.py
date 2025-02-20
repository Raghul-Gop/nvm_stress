import time
import requests
import concurrent.futures

urls = []  # input URLs/IPs array
responses = []  # output content of each request as string in an array
total_connections=0
total_iterations=0

def send(url):
    responses.append(requests.get(url).content)

def generate_tcp_traffic(connections_per_second, iterations):
    global total_iterations
    global total_connections
    total_iterations=iterations
    total_connections=connections_per_second
    requests.packages.urllib3.util.connection.HAS_IPV6 = False
    for y in range(connections_per_second):
        #print("second for loop")
        urls.append("http://172.16.120.16")
    for _ in range(iterations):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
            futures = []
            for url in urls:
                futures.append(executor.submit(send, url))

start = int(time.time())  # get time before the requests are sent

#Change the connections per second value here to set the number of records that needs to be sent
generate_tcp_traffic(connections_per_second=1000, iterations=5)

end = int(time.time())  # get time after the requests are finished
print(f"total_connections : {total_connections},total_iterations : {total_iterations}")
print("Total time taken for the script to run : "+ str(end-start)+ " seconds")
print(str((total_connections*total_iterations)/(end-start)) + "/sec")  # get average requests per second
