import matplotlib.pyplot as plt
import datetime
import yaml
import json
import requests
import schedule
import time
from discord_webhook import DiscordWebhook

with open('./settings.yml') as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)

try:
    graph_title = settings["graph-title"]

    api_key = settings['api-key']
    api = {"Authorization": f"Bearer {api_key}"}

    webhook_link = settings["webhook-url"]

    time = settings["time"]

    check_time = int(settings["check-time"])

    marker = settings["marker"]

except Exception as e:
    print(f'Error whilst loading settings: {e}')


def run():
    try:
        print('[+] Saving new users data')

        with open('./cache/data.json', 'r') as f:
            data = json.load(f)

        for i in data["account_list"]:

            r = requests.get(f'https://api.clashroyale.com/v1/players/%23{i["tag"]}', headers=api)
            playerData = r.json()

            if r.status_code != 200:
                print(f'   [X] Received status code {r.status_code} when getting data for {i["tag"]}')

            else:
                print(f'   [/] Saving data for {playerData["name"]}')
                expPoints = playerData["expPoints"]
                expLevel = playerData["expLevel"]

                with open('./cache/levels.json', 'r') as f:
                    expToAdd = json.load(f)[str(expLevel)]

                totalXP = expPoints + expToAdd

                i["data"]["xp"].append(totalXP)
                i["data"]["dates"].append(str(datetime.date.today()).replace('-', '/'))

                with open('./cache/data.json', 'w+') as f:
                    json.dump(data, f, indent=2)

                print(f'   [+] Successfully saved data for {playerData["name"]}')

    except Exception as e:
        print(f'   [X] An unknown error occurred: {e}')

    try:
        print(f'[/] Generating graph...')
        with open('./cache/data.json', 'r') as f:
            data = json.load(f)

        for i in data["account_list"]:
            display_name = i["display_name"]
            xp = i["data"]["xp"]
            dates = i["data"]["dates"]

            plt.plot(dates, xp, marker=marker, label=display_name)

        plt.title(graph_title)
        plt.xlabel('Date')
        plt.ylabel('Total XP')

        plt.legend()
        plt.savefig('./plot.png')

        print(f'   [/] Successfully generated graph, now posting to Discord...')

        webhook = DiscordWebhook(url=webhook_url)
        with open("./plot.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='unknown.png')
        webhook.execute()

        print(f'   [+] Successfully posted graph on discord')

    except Exception as e:
        print(f'   [X] An unknown error occurred: {e}')

    print(f'\n\nWaiting for next run...')


print(f'\nWaiting for next run...')

schedule.every().day.at(time).do(run)
while True:
    schedule.run_pending()
    time.sleep(check_time)
