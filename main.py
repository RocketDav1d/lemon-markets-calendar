# sending emails via python
from calendar import c
from curses.ascii import EM
from email.mime import image
import os
import smtplib
from email.message import EmailMessage
from positions import aktien, count, total_investment

# EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
# EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")
EMAIL_ADDRESS = "david.korn@code.berlin"
EMAIL_PASSWORD = "wkcoonhqvonmvccr"


contents = []


msg = EmailMessage()
msg["Subject"] = "Your daily portfolio update"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "dkorn941@gmail.com"


html = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Dispatch</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  </head>
"""

for aktie in aktien:
    isin = aktie.isin
    isin_title = aktie.isin_title
    quantity = aktie.quantity
    buy_price_avg =  aktie.buy_price_avg
    estimated_price = aktie.estimated_price
    estimated_price_total = aktie.estimated_price_total


    buy_price_avg = str(buy_price_avg)
    buy_price_avg = "€" + buy_price_avg[:3] + "," + buy_price_avg[3:]

    estimated_price = str(estimated_price)
    estimated_price = "€" + estimated_price[:3] + "," + estimated_price[3:]

    estimated_price_total = str(estimated_price_total)
    estimated_price_total = "€" + estimated_price_total[:3] + "," + estimated_price_total[3:]

    html += f"""\
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Dispatch</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    </head>
    <body style="font-family: 'Space Grotesk'; sans-serif;">
        <h1 style="color:#FDDC35;">&#127819; {isin_title}</h1>
        <h2 style="color:black;">{isin}</h2>
        <p style="color:black;">quantity: {quantity}</p>
        <p style="color:black;">buy price average: {buy_price_avg}</p>
        <p style="color:black;">estimated price: {estimated_price}</p>
        <p style="color:black;">estimated price total: {estimated_price_total}</p>
        <hr width="40%" color="black" align="left" />
    </body>
    </html>
    """

lemon_url = f"https://www.lemon.markets/de-de"

html += f"""
<h1>total portfolio worth: {total_investment}</h1>

<a href="{lemon_url}"
          ><button
            style="
              margin-top: 1em;
              margin-left: 50px;
              width: 30%;
              height: 40px;
              cursor: pointer;
              font-size: 20px;
              outline: none;
              background: none;
              border: none;
              border-radius: 15px;
              color: white;
              text-align: center;
              background: linear-gradient(
                to right,
                rgb(23, 158, 136),
                rgb(20, 102, 98),
                rgb(23, 158, 136)
              );
            "
          >
            check out lemon markets
          </button></a
        >
"""

msg.add_alternative(html, subtype="html")


def send_mail():
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


if __name__ == "__main__":
    send_mail()

















    # print(content)
    # msg.set_content(f"How about {content[0]} dinner at 6pm this Saturday?")
    # msg.set_content(f"this is a isin: {isin}")

# msg.set_content(str)






# print(contents)


# str = ""
# for content in contents:
#     str+= " "+content
# msg.set_content(str)


# msg.add_alternative(f"""\
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <h1></h1>
# </body>
# </html>
# """, subtype="html")





# def send_mail():
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()

#     # with open("password.txt", "r") as x:
#     #     password = x.read()

#     server.login("david.korn@code.berlin", "wkcoonhqvonmvccr")

#     subject = "Good Morning David. This is your portfolio"
#     with open("body.txt", "r") as n:
#         body = n.read()
#     msg = f"subject: {subject} \n\n\n {body}"


#     server.sendmail(
#         "david.korn@code.berlin",
#         "dkorn941@gmail.com",
#         msg
#     )
#     # 16:35 Corey Schafer Video

# if __name__ == "__main__":
#     send_mail()