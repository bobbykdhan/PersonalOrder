from fastapi import Request

from dotenv import load_dotenv
from fastapi import FastAPI

from image import upload_screenshot
from webdriver_handler import *

load_dotenv()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/order/{selection}")
async def say_hello(selection: str):
    orderFood(selection)

@app.get("/testScreenshot")
async def testScreenshot():
    driver = create_driver()
    driver.get("https://www.youtube.com")
    time.sleep(5)

    return {"message": "Screenshot is at: " + upload_screenshot(driver, True, True)}

def orderFood(selection):
    # Initialize the Selenium WebDriver and the Wait object.

    # Navigate to the website.
    if selection == "breakfast1":
        print("pizza")
    elif selection == "breakfast2":
        print("burger")
    elif selection == "commonsBurger":
        print("burger")
    elif selection == "crossroadsBurger":
        print("burger")
    elif selection == "pasta1":
        print("pasta")
    elif selection == "pasta2":
        print()


#TODO make this work

# @app.get('/sms')
# @app.post("/sms")
# async def root(request: Request):
#     """Respond to incoming calls with a simple text message."""
#     # Start our TwiML response
#     # resp = MessagingResponse()
#     #
#     # # Add a message
#     # resp.message("The Robots are coming! Head for the hills!")
#     #
#     # print(str(resp))


