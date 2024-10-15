import urllib.request
from uuid import uuid4

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

    send(PARAMS.slack_webhook_url, message)


def send(url: str, message: WebhookMessage):
    data = message.json().encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req) as response:
            status_code = response.getcode()

            if status_code != 200:
                response = response.read().decode("utf-8")

                raise Exception(f"Failed to send message to Slack > {status_code} {response}")
            else:
                print(f"Message was sent successfully > {message.text}")
    except urllib.error.HTTPError as e:
        raise Exception(f"Failed to send message to Slack > {e.code} {e.reason}")


if __name__ == "__main__":
    main()
