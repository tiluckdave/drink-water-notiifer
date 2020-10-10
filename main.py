import time
import plyer
from plyer import notification


if __name__ == "__main__":
    while True:
        notification.notify(
            title="Time to Drink a Glass of Water!",
            message="Its been an Hour you haven't drunk a glass of Water. Consider drinking a glass of water.",
            app_icon="icon.ico",
            timeout=10
        )
        time.sleep(60*60)
