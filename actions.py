import os


class GITHUB:
    actor = os.getenv("GITHUB_ACTOR")
    assert actor, "GITHUB_ACTOR is not set"

    ref = os.getenv("GITHUB_REF")
    assert ref, "GITHUB_REF is not set"

    repository = os.getenv("GITHUB_REPOSITORY")
    assert repository, "GITHUB_REPOSITORY is not set"

    name = repository.split("/")[-1]
    version = ref.split("/")[-1]
    url = f"https://github.com/{repository}/releases/tag/{version}"

    user_name = actor
    user_image_url = f"https://github.com/{user_name}.png"


class PARAMS:
    slack_webhook_url = os.getenv("INPUT_SLACK_WEBHOOK_URL")
    assert slack_webhook_url, "SLACK_WEBHOOK_URL is not set"

    button_text = os.getenv(
        "INPUT_SLACK_BUTTON_TEXT",
        default=GITHUB.version,
    )

    button_url = os.getenv(
        "INPUT_SLACK_BUTTON_URL",
        default=GITHUB.url,
    )

    button_emoji = (
        os.getenv(
            "INPUT_SLACK_BUTTON_EMOJI",
            default="github",
        )
        .strip()
        .lower()
        .replace(":", "")
    )
