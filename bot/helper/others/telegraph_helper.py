# Implement By - @VarnaX-279

from string import ascii_letters
from random import SystemRandom

from time import sleep
from bot import LOGGER
# from telegraph import Telegraph
# from telegraph.exceptions import RetryAfterError
from .telegraph.api import Telegraph
from .telegraph.exceptions import RetryAfterError


class TelegraphHelper:
    def __init__(self, author_name=None, author_url=None):
        self.api_url = "graph.org"  # ...
        self.telegraph = Telegraph(api_url=self.api_url)
        self.short_name = "".join(SystemRandom().choices(ascii_letters, k=8))
        self.access_token = None
        self.author_name = author_name
        self.author_url = author_url
        self.create_account()

    def create_account(self):
        self.telegraph.create_account(
            short_name=self.short_name,
            author_name=self.author_name,
            author_url=self.author_url,
        )
        self.access_token = self.telegraph.get_access_token()
        LOGGER.info(f"Creating TELEGRAPH Account using  '{self.short_name}' name")

    def create_page(self, title, content):
        try:
            return self.telegraph.create_page(
                title=title,
                author_name=self.author_name,
                author_url=self.author_url,
                html_content=content,
            )
        except RetryAfterError as st:
            LOGGER.warning(
                f"Telegraph Flood control exceeded. I will sleep for {st.retry_after} seconds."
            )
            sleep(st.retry_after)
            return self.create_page(title, content)

    def edit_page(self, path, title, content):
        try:
            return self.telegraph.edit_page(
                path=path,
                title=title,
                author_name=self.author_name,
                author_url=self.author_url,
                html_content=content,
            )
        except RetryAfterError as st:
            print(
                f"Telegraph Flood control exceeded. I will sleep for {st.retry_after} seconds."
            )
            sleep(st.retry_after)
        return self.edit_page(path, title, content)

    def edit_telegraph(self, path, telegraph_content):
        nxt_page = 1
        prev_page = 0
        num_of_path = len(path)
        for content in telegraph_content:
            if nxt_page == 1:
                content += (
                    f'<b><a href="https://{self.api_url}/{path[nxt_page]}">Next</a></b>'
                )
                nxt_page += 1
            else:
                if prev_page <= num_of_path:
                    content += f'<b><a href="https://{self.api_url}/{path[prev_page]}">Prev</a></b>'
                    prev_page += 1
                if nxt_page < num_of_path:
                    content += f'<b> | <a href="https://{self.api_url}/{path[nxt_page]}">Next</a></b>'
                    nxt_page += 1
            self.edit_page(
                path=path[prev_page], title="Sito-Cloud", content=content
            )
        return


telegraph = TelegraphHelper(
    "Sito-Cloud", "https://t.me/sito404"
)
