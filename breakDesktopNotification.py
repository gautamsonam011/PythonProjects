# How to create take a break desktop notification system in python. 
# pip install plyer 

from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="***Rest API***",
            message="A REST API is an API that conforms to the design principles of the REST, or representational state transfer architectural style.",
            app_icon="",
            timeout=5)
        time.sleep(10)