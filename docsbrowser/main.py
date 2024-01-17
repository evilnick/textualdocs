from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder, Footer
from textual.binding import Binding


class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """


class DocFooter(Footer):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

    def compose(self) -> ComposeResult:
        yield Footer()


class Tweet(Placeholder):
    DEFAULT_CSS = """
    Tweet {
        height: 5;
        width: 1fr;
        border: tall $background;
    }
    """


class Column(VerticalScroll):
    DEFAULT_CSS = """
    Column {
        height: 1fr;
        width: 32;
        margin: 0 2;
    }
    """

    def compose(self) -> ComposeResult:
        for tweet_no in range(1, 20):
            yield Tweet(id=f"Tweet{tweet_no}")

class DocView(Placeholder):
    DEFAULT_CSS = """
    Doc {
        height: 1fr;
        width: 79;
        margin: 1 1 1 1;
    }
    """

class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer()
        with HorizontalScroll():
            yield Column()
            yield DocView()
        



class LayoutApp(App):
    NAVIGATION = [
        {'item':'Home', 'url':'/home'},
        {'item':'Tutorial', 'url':'/tutorial'},

    ]
    BINDINGS = [
    Binding(key="q", action="quit", description="Quit"),
    Binding(
        key="question_mark",
        action="help",
        description="Show help screen",
        key_display="?",
    ),
    Binding(key="s", action="search", description="Search"),
    Binding(key="j", action="down", description="Scroll down", show=False),
    ]
    def on_ready(self) -> None:
        self.push_screen(TweetScreen())


if __name__ == "__main__":
    app = LayoutApp()
    app.run()
