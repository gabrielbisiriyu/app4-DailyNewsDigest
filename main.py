import requests
from mail import send_email_now
api_key="a0aaa551c26b41b9b345daefd3f02a39"
news_topic="tesla"
url="https://newsapi.org/v2/everything?" \
    f"q={news_topic}" \
    "&from=2023-07-01" \
    "&sortBy=publishedAt" \
    "&apiKey=a0aaa551c26b41b9b345daefd3f02a39" \
    "&language=en" \


# Made a request
request=requests.get(url)

# Got a dictionary
content=request.json()

# Access articles,titles and description

body="Subject: Today's News" + '\n'

for article in content["articles"][:20]:

    body=body+article["title"]+ '\n' + article["description"] +'\n'+article["url"] + 2 * '\n'

body=body.encode("utf-8")
send_email_now(body)




