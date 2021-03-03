import os
import requests

TEXT_FORMAT = "*{name}*: new version _{version}_ was released by {user}."
URL_FORMAT = "https://github.com/{repository}/releases/tag/{version}"


def main():
    slack_webhook_url = os.environ["INPUT_SLACK_WEBHOOK_URL"]

    github_repository = os.environ["GITHUB_REPOSITORY"]
    github_ref = os.environ["GITHUB_REF"]
    github_actor = os.environ["GITHUB_ACTOR"]

    project_name = github_repository.split("/")[-1]
    project_version = github_ref.split("/")[-1]

    requests.post(
        slack_webhook_url,
        json={
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": TEXT_FORMAT.format(
                            name=project_name.upper(),
                            version=project_version,
                            user=github_actor,
                        ),
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": f":github: {project_version}",
                            "emoji": True,
                        },
                        "value": "releases",
                        "url": URL_FORMAT.format(
                            repository=github_repository,
                            version=project_version,
                        ),
                        "action_id": "button-action",
                    },
                }
            ]
        },
    )


if __name__ == "__main__":
    main()
