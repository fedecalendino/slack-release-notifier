from uuid import uuid4

import requests
from slackblocks import (
    WebhookMessage,
    SectionBlock,
    Button,
    ContextBlock,
    Image,
    Text,
    ResponseType,
)

from actions import GITHUB, PARAMS


def main():
    title = f"*{GITHUB.name.upper()}*: new version _<{GITHUB.url}|{GITHUB.version}>_ was released!"
    preview = f"{GITHUB.name.upper()}: new version {GITHUB.version} was released by {GITHUB.user_name}!"

    message = WebhookMessage(
        response_type=ResponseType.IN_CHANNEL,
        text=preview,
        blocks=[
            SectionBlock(
                text=title,
                accessory=Button(
                    text=f":{PARAMS.button_emoji}: {PARAMS.button_text}",
                    url=PARAMS.button_url,
                    action_id=str(uuid4()),
                ),
            ),
            ContextBlock(
                elements=[
                    Image(
                        image_url=GITHUB.user_image_url,
                    ),
                    Text(
                        text=f"by {GITHUB.user_name}",
                    ),
                ]
            ),
        ],
    )

    response = requests.post(
        url=PARAMS.slack_webhook_url,
        data=message.json(),
    )

    if response.status_code != 200:
        raise Exception(
            f"Failed to send message to Slack > {response.status_code} {response.text}"
        )
    else:
        print(f"Message was sent successfully > {title}")


if __name__ == "__main__":
    main()
