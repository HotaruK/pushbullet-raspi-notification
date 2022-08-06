from settings import PUSHBULLET_WSS_URI, GPIO_RED_PIN, GPIO_BLUE_PIN, GPIO_GREEN_PIN
import asyncio
import websockets
import json
import logging
from LedGpioController import gpio_clean_up, Color, LEDGPIOController, light_normal_notify

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
)

gpio = LEDGPIOController(GPIO_RED_PIN, GPIO_BLUE_PIN, GPIO_GREEN_PIN)

services = {
    "Gmail": Color.RED,
    "LINE": Color.GREEN,
    "Twitter": Color.BLUE,
    "Slack": Color.TEAL,
    "other": Color.YELLOW,
}


async def process(msg):
    msg_dict = json.loads(msg)
    if msg_dict.get("type", "nop") == "nop":
        return

    p = msg_dict.get("push", {})
    if p.get("type", "dismissal") == "dismissal":
        return

    title = p.get("title")
    body = p.get("body")
    app_name = p.get("application_name")
    logging.debug(title, body, app_name)

    light_normal_notify(gpio, services.get(app_name, services["other"]))


async def __main():
    async for websocket in websockets.connect(PUSHBULLET_WSS_URI,
                                              logger=logging.getLogger("websockets.server")
                                              ):
        try:
            async for message in websocket:
                await process(message)
        except websockets.ConnectionClosed:
            continue


if __name__ == '__main__':
    try:
        asyncio.run(__main())
    except Exception as e:
        gpio_clean_up()
        print(e.args)
