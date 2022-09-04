from slackhooks.blocks.accessory import ButtonAccessory
from slackhooks.blocks.context import Context
from slackhooks.blocks.element import ImageElement, PlainTextElement
from slackhooks.blocks.section import Section
from slackhooks.blocks.text import MarkdownText, PlainText
from slackhooks.client import Message

from actions import github, params


class Project:
    def __init__(
        self,
        github_repository: str,
        github_ref: str,
        github_user: str,
        pypi_project: str = None,
    ):
        self.user = github_user
        self.name = github_repository.split("/")[-1]
        self.pypi_project = pypi_project
        self.repository = github_repository
        self.version = github_ref.split("/")[-1]

    @property
    def title_markdown(self):
        return f"*{self.name.upper()}*: new version _{self.version}_ was released!"

    @property
    def title_plain_text(self):
        return f"{self.name.upper()}: new version {self.version} was released by {self.user}!"

    @property
    def emoji(self):
        if self.pypi_project:
            return "pypi"

        return "github"

    @property
    def user_image_url(self):
        return f"https://github.com/{self.user}.png"

    @property
    def url(self):
        if self.pypi_project:
            return f"https://pypi.org/project/{self.pypi_project}/"

        return f"https://github.com/{self.repository}/releases/tag/{self.version}"


def main():
    project = Project(
        github_repository=github.repository,
        github_ref=github.ref,
        github_user=github.actor,
        pypi_project=params.pypi_project_name,
    )

    message = Message(
        text=project.title_plain_text,
        blocks=[
            Section(
                text=MarkdownText(
                    text=project.title_markdown,
                ),
                accessory=ButtonAccessory(
                    text=PlainText(
                        text=f":{project.emoji}: {project.version}",
                    ),
                    value="releases",
                    action_id="button-action",
                    url=project.url,
                ),
            ),
            Context(
                elements=[
                    ImageElement(
                        image_url=project.user_image_url,
                    ),
                    PlainTextElement(
                        text=f"by {project.user}",
                    ),
                ]
            ),
        ],
    )

    message.send(params.slack_webhook_url)


if __name__ == "__main__":
    main()
