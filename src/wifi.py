import network


def connectWiFi(ssid,password):

    # Підключення до Wi-Fi
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(ssid, password)

    # Чекати на підключення
    while not wifi.isconnected():
        pass
    return wifi.ifconfig()


