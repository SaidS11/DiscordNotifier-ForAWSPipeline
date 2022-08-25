from discord_webhook import DiscordWebhook, DiscordEmbed
import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)
    message_str=str(message)
    if "New" in message:
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1011442516266066000/ewLbjHcrp0AmpwYthQh-K4EiBtz3WEdiRr6_ZIlihuvSPH4IQSX3FG9bo2Puq363OcFg")
        embed = DiscordEmbed(
            title="AWS",
            description=message,
            color="00ff00")
        
        #embed.set_image(url="")
        webhook.add_embed(embed)
        webhook.execute()
    else:
        pass
    return message
