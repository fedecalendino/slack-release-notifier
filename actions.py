import os


class github:
    actor = os.environ["GITHUB_ACTOR"]
    ref = os.environ["GITHUB_REF"]
    repository = os.environ["GITHUB_REPOSITORY"]


class params:
    slack_webhook_url = os.environ["INPUT_SLACK_WEBHOOK_URL"]
    pypi_project_name = os.environ["INPUT_PYPI_PROJECT_NAME"]
