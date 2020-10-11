import time
import plyer
from plyer import notification
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Drink Water Notifier")
print(ascii_banner)
print("Developer Tilak dave")
time.sleep(2)
print("Starting Notification ystem...")
time.sleep(1)
print("Getting ready...")
time.sleep(2)

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Time to Drink a Glass of Water!",
            message="Its been an Hour you haven't drunk a glass of Water. Consider drinking a glass of water.",
            app_icon="icon.ico",
            timeout=10
        )
        time.sleep(60*60)
