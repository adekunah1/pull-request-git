import requests
from datetime import date, timedelta
from pprint import pprint
from prettytable import PrettyTable
import json

email_sender = "adekunah@gmail.com"
email_receiver = "xxx@yahoo.com"
subject = "Summary of pull requests for past few weeks"

print('From','-',email_sender)
print('To','-',email_receiver)
print('Subject','-',subject)

table = PrettyTable()
table.field_names = ["PR Title", "PR Number", "Created Date", "State"]

url = "https://api.github.com/repos/mastodon/mastodon-android/pulls"

pars = {
    "state": "all"
    
}
res=requests.get(url, params=pars)
repos=res.json()
while 'req' in res.links.keys():
  res=requests.get(res.links['req']['url'])
  repos.extend(res.json())

#timestamp
now = date.today()
previous_week =  now - timedelta(weeks=1)
previous_week= previous_week.strftime("%Y-%m-%dT%H:%M:%SZ")

for repo in repos:
    table.add_row([repo["title"], int(repo["number"]), repo["created_at"], repo["state"]])
print(table)
