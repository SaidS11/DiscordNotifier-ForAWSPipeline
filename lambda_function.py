from discord_webhook import DiscordWebhook, DiscordEmbed
import json

print('Loading function')


def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)

    webhook = DiscordWebhook(url="replace with your webhook url")
    embed = DiscordEmbed(
        title="AWS",
        description=message,
        color="00ff00")

    #Select an image if you want
    #embed.set_image(url="")

    webhook.add_embed(embed)
    webhook.execute()

    return message
