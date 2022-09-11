#!/usr/bin/python3

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

class URLTree:
    def __init__(self, root_url, url_links):
        self._generator = _TreeGenerator(root_url, url_links)

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)


class _TreeGenerator:

    def __init__(self, root_url, url_links):

        self._root_url = root_url
        self._url_links = url_links
        self._tree = []


    def build_tree(self):

        self._tree_head()
        self._tree_body(self._url_links)

        return self._tree

    def _tree_head(self):

        self._tree.append(f"{self._root_url}")
        self._tree.append(PIPE)

    def _tree_body(self, all_links):

        links = [] ## Contain all filtered links 
        for element in all_links:
            if element[:4] != "http" and element[:1] != "#":
                links.append(element)
        links_count = len(links)

        for index, link in enumerate(links):

            connector = ELBOW if index == links_count - 1 else TEE

            self._add_link(link, connector)

    def _add_link(self, link, connector):

        self._tree.append(f"{connector} {link}")
    