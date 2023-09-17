import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from browsermobproxy import Server

def generate_har_file(url, filename):
    server = Server()
    server.start()

    proxy = server.create_proxy()
    capabilities = {
        "browserName": "chrome",
        "proxy": {
            "proxyType": "manual",
            "httpProxy": proxy.proxy,
            "sslProxy": proxy.proxy
        }
    }

    driver = webdriver.Chrome(
        use_subprocess=True,
        executable_path=ChromeDriverManager().install(),
        desired_capabilities=capabilities
    )

    driver.get(url)

    # Perform any actions on the website that you want to capture in the HAR file.

    server.stop()

    with open(filename, "wb") as f:
        f.write(proxy.har)

if __name__ == "__main__":
    url = "https://www.youtube.com"
    filename = "youtube.har"

    generate_har_file(url, filename)
