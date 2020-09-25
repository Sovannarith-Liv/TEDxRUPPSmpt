from tedxemail import send_email
from threading import Thread
import pandas as pd

df = pd.read_csv("./static/audience.csv")
emails = df["email"].values
images = ["./static/qrcode/" + name + ".jpg" for name in df["name"].values]

for i in range(len(emails)):
    thread = Thread(target=send_email, args=[images[i], emails[i]])
    thread.start()
