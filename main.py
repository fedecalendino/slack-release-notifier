import os
import requests

SUMMARY_FORMAT = "{name}: new version {version} was released by {user}."
TEXT_FORMAT = "*{name}*: new version _{version}_ was released by {user}."

GITHUB_URL_FORMAT = "https://github.com/{repository}/releases/tag/{version}"
PYPI_URL_FORMAT = "https://pypi.org/project/{project_name}/"
    

def main():
    slack_webhook_url = os.environ["INPUT_SLACK_WEBHOOK_URL"]
    pypi_project_name = os.environ["INPUT_PYPI_PROJECT_NAME"]
    
    github_repository = os.environ["GITHUB_REPOSITORY"]
    github_ref = os.environ["GITHUB_REF"]
    github_actor = os.environ["GITHUB_ACTOR"]

    project_name = github_repository.split("/")[-1]
    project_version = github_ref.split("/")[-1]

    summary = SUMMARY_FORMAT.format(
        name=project_name.upper(), 
        version=project_version, 
        user=github_actor,
    )
    
    text = TEXT_FORMAT.format(
        name=project_name.upper(), 
        version=project_version, 
        user=github_actor,
    )
    
    if pypi_project_name:
        emoji = "pypi"
        url = PYPI_URL_FORMAT.format(
            project_name=pypi_project_name,
        )
    else:
        emoji = "github"
        url = GITHUB_URL_FORMAT.format(
            repository=github_repository, 
            version=project_version,
        )
    
    requests.post(
        slack_webhook_url,
        json={
            "text": summary,
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": text,
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": f":{emoji}: {project_version}",
                            "emoji": True,
                        },
                        "value": "releases",
                        "url": url,
                        "action_id": "button-action",
                    },
                }
            ]
        },
    )


if __name__ == "__main__":
    main()
