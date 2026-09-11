from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.labels, self.links, self.stack = path, [], [], [], []
        self.headings = self.mains = self.current = 0
        self.feed(path.read_text(encoding='utf-8-sig'))
        assert not self.stack, (path, self.stack)
        assert len(self.ids) == len(set(self.ids)), path
        assert all(label in self.ids for label in self.labels), path
        assert self.headings == self.mains == self.current == 1, path
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'label': self.labels.append(a['for'])
        if tag == 'h1': self.headings += 1
        if tag == 'main': self.mains += 1
        if a.get('aria-current') == 'page': self.current += 1
        if tag == 'img': assert a.get('alt'), self.path
        if tag in ('a', 'button'): assert not any(t in ('a', 'button') for t in self.stack)
        if self.path.name == 'contact.html' and tag in ('input', 'textarea'): assert 'disabled' in a
        for key in ('href', 'src'):
            if key in a: self.links.append(a[key])
        if tag not in ('meta', 'link', 'img', 'input', 'hr', 'br'): self.stack.append(tag)
    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, (self.path, tag, self.stack)
        self.stack.pop()
pages = {path.name: Page(path) for path in ROOT.glob('*.html')}
for name, page in pages.items():
    for link in page.links:
        assert '\\' not in link, link
        url = urlsplit(link)
        if url.scheme: continue
        target = ROOT / (url.path or name)
        assert target.is_file(), link
        if url.fragment: assert url.fragment in pages[target.name].ids, link
    print(f'PASS {name}: structure, links/assets/fragments, labels, alt text, main heading, active navigation')
