import os
import requests


def main():
    url = os.environ["INPUT_SLACK_WEBHOOK_URL"]

    print(f"::set-output name=myOutput::{url[:5]}")


if __name__ == "__main__":
    main()