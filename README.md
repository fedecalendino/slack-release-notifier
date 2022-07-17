# slack-release-notifier

Simple action to notify a slack channel after a new version of a project has been released.


### Usage

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
      uses: fedecalendino/slack-release-notifier@v1.2.1
```


### SetUp

To be able to send the notification, a webhook url needs to be provided. You can get one by installing the app [Incoming WebHooks](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks) into your slack workspace.


### Result

![Slack Notificator](/img/screenshot.png)

