from src import sign

if __name__ == "__main__":
    sign = sign.Sign("test", "127.0.0.1", 8080)
    sign.connect()
    sign.send("Hello World")
    sign.send("Test")
    sign.disconnect(10)
