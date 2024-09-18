# slack-release-notifier

Simple action to notify a slack channel after a new version of a project has been released.

### Requirements

To be able to send the notification, a webhook url needs to be provided. You can get one by installing the app [Incoming WebHooks](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks) into your slack workspace.


## Default Usage

![default configuration](/img/custom.png)

workflow.yml
```yml
name: Release

on:
  release:
    types:
      - created

jobs:
  publish:
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
    - name: Notify Slack
      id: slack
      with:
        slack_webhook_url: ${{ secrets.SLACK_WEBHOOK_URL }}
      uses: fedecalendino/slack-release-notifier@v3.0.2
```

## Custom Usage

![custom configuration](/img/custom.png)

workflow.yml
```yml
name: Release

on:
  release:
    types:
      - created

jobs:
  publish:
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
    - name: Notify Slack
      id: slack
      with:
        slack_webhook_url: ${{ secrets.SLACK_WEBHOOK_URL }}
        button_text: "open in pypi"
        button_url: "https://pypi.com"
        button_emoji: ":pypi:"
      uses: fedecalendino/slack-release-notifier@v3.0.2
```


