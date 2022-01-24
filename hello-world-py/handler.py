import time


def hello(event, context):
    time.sleep(4)
    print("hi !")
    return "hello-world"
