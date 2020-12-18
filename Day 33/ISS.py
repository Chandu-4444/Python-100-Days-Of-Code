import requests
import datetime as dt
import smtplib
import time


parameters = {
        "lat": 16.066500,
        "lng": 80.551399,
        "formatted": 0,
    }

def is_iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)


    if parameters["lat"]-5<=latitude<= parameters["lng"]+5 and parameters["lng"]-5<=longitude<=parameters["lng"]+5:
        return True

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters )
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    if time_now>=sunset or time_now<=sunset:
        return True


# Send an email
while True:
    time.sleep(60)
    if is_iss_near() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login("chanduguntur4444@gmail.com","Chandu@4444")
        connection.sendmail(
            from_addr="chanduguntur4444@gmail.com",
            to_addrs="chanduguntur4444@gmail.com",
            msg="Subject:Look Up\n\nThs ISS is above you in the sky"
        )
