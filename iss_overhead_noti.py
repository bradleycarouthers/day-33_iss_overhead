import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 32.749901  # Your latitude
MY_LONG = -97.330338  # Your longitude
MY_EMAIL = "studious.estudent12345@gmail.com"
MY_PASSWORD = "8qA5Jt6e!K2S#kow"


def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    # iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude in range(int(MY_LAT - 5), int(MY_LAT + 5)):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="studious.estudent0@yahoo.com",
                msg="Subject:It is time\n\nLook up!!!"
            )
