import prometheus_client as prom
import requests
import time

#here we have defined the gauge, it also has only one metric, which is to show the ms load time of websites
RESPONSE_TIME_GAUGE = prom.Gauge('sample_external_url_response_ms', 'Url response time in ms', ["url"])
URL_LIST = ["http://127.0.0.1:8000/", "http://127.0.0.1:8000/infoUsers"]  #here we have defined what sites we want our appliction to monitor 


#this function monitor’s how much time do the mentioned sites take to load
def get_response(url: str) -> dict:
    response = requests.get(url)
    response_time = response.elapsed.total_seconds()
    return response_time

#this function displays the results properly on the web page
def get_url_status():
    while True:
        for url_name in URL_LIST:
            response_time = get_response(url_name)
            RESPONSE_TIME_GAUGE.labels(url=url_name).set(response_time)
        time.sleep(5)  


if __name__ == '__main__':
    prom.start_http_server(8001)
    get_url_status()