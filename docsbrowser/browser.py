from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder, Footer, Header, Markdown, Tree
from textual.binding import Binding

NAVIGATION = [
    {'item':'Home', 'doc':'/home'},
    {'item':'Tutorial', 'url':'/tutorial'},
    {'item':'How to', 'url':'/tutorial'},
    {'item':'Explanation', 'url':'/tutorial'},
    {'item':'Reference', 'url':'/tutorial'},
]

with open("k8s-docs/home.md",'r') as f:
        home = f.read();

tree: Tree[dict] = Tree("Home", id='nav')
tree.root.expand()
tut = tree.root.add("Tutorials")
tut.add_leaf("Get started")
how = tree.root.add("How To")
how.add_leaf("install")
how.add_leaf("configure")
how.add_leaf("upgrade")
how.add_leaf("uninstall")
exp = tree.root.add("Explanation")
exp.add_leaf("Overview")
ref = tree.root.add("Reference")
ref.add_leaf("Release notes")


class NavItem(Placeholder):
    DEFAULT_CSS = """
    Tweet {
        height: 3;
        width: 12;
    }
    """

class Nav(VerticalScroll):
    DEFAULT_CSS = """
    Nav {
        height: 1fr;
        width: 24;
        margin: 0 1;
    }
    """

    def compose(self) -> ComposeResult:
        for entry in NAVIGATION:
            yield NavItem(id=f"{entry['item']}")

class DocView(Markdown):
    DEFAULT_CSS = """
    Doc {
        height: 1fr;
        width: 60;
        max-width: 79;
        margin: 1 1 1 1;
    }
    """

class DocScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with HorizontalScroll():
            yield tree
            with VerticalScroll():
                yield DocView(markdown=home, id="maindoc")


class Documentation(App):
    CSS_PATH = "doc.tcss"
    BINDINGS = [
    Binding(key="q", action="quit", description="Quit"),
    Binding(
        key="question_mark",
        action="help",
        description="Show help screen",
        key_display="?",
    ),
    Binding(key="s", action="search", description="Search"),
    ]
    

    def on_ready(self) -> None:
        self.push_screen(DocScreen())

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path for docs")
    args = parser.parse_args()

    app = Documentation()
    app.run()