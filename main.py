import time
import plyer
from plyer import notification
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Drink Water Notifier")
print(ascii_banner)
print("Developer Tilak dave")
time.sleep(2)
print("Starting Notification System...")
time.sleep(1)
print("Getting ready...")
time.sleep(2)

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Hydrate yourself on time..!",
            message="1 hour is too much , you haven't drunk water. Drink water immediately .",
            app_icon="icon.ico",
            timeout=15
        )
        time.sleep(60*60)
