"""Generate a list of my publications from arXiv."""
import requests

AUTHOR_ID = "2282538977"
FIELDS = "papers.title,papers.venue,papers.publicationVenue,papers.year,papers.authors,papers.journal," \
    "papers.externalIds,papers.openAccessPdf"
AUTHOR_URL = f"https://api.semanticscholar.org/graph/v1/author/{AUTHOR_ID}?fields={FIELDS}"
EXTERNAL_IDS = {
    'ArXiv': 'https://arxiv.org/abs/{}'
}
NO_PUB = ['arXiv.org']
NAME_MAP = {
    "Filip Uradnik": "Filip Úradník",
    "Filip 'Uradn'ik": "Filip Úradník",
    "David Sychrovsk'y": "David Sychrovský",
    "Martin vCern'y": "Martin Černý",
    "Jakub vCern'y": "Jakub Černý",
}


def generate_publications() -> str:
    """Generate publications."""
    search = requests.get(AUTHOR_URL).json()["papers"]
    return "\n".join([
        render_result(result) for result in search])


PUBLICATION_FORMAT = "* {authors} ({year}): _{title}_{publication} {links}"


def render_result(result: dict) -> str:
    """Render the result."""
    authors = ", ".join(NAME_MAP.get(author["name"], author["name"]) for author in result["authors"])
    title = result["title"]
    year = result["year"]
    publication = generate_publication_venue(result["publicationVenue"])
    links = generate_links(result["openAccessPdf"], result["externalIds"])
    return PUBLICATION_FORMAT.format(title=title, authors=authors, year=year, links=links,
                                     publication=publication)


def generate_publication_venue(publication: dict | None) -> str:
    """Generate an 'In: ...', if present."""
    if publication is None or publication["name"] in NO_PUB:
        return ""
    name = publication['name']
    if 'url' in publication:
        name = f"[{name}]({publication['url']})"
    return f" In: _{name}_"


def generate_links(pdf: dict | None, external: dict) -> str:
    """Generate links for other sites."""
    if pdf is not None:
        external["pdf"] = pdf["url"]

    results = []
    for name, link in external.items():
        link = str(link)
        if "http" not in link:
            if name not in EXTERNAL_IDS:
                continue
            link = EXTERNAL_IDS[name].format(link)
        results.append(f"[{name}]({link})")
    if not results:
        return ""
    return f'({", ".join(results)})'
