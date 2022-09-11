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
    # def _tree_head(self):

    #     self._tree.append(f"{self._root_url}{os.sep}")
    #     self._tree.append(PIPE)

    # def _tree_body(self, directory, prefix=""):

    #     entries = directory.iterdir()
    #     entries = sorted(entries, key=lambda entry: entry.is_file())
    #     entries_count = len(entries)

    #     for index, entry in enumerate(entries):

    #         connector = ELBOW if index == entries_count - 1 else TEE
    #         if entry.is_dir():

    #             self._add_directory(
    #                 entry, index, entries_count, prefix, connector
    #             )
    #         else:

    #             self._add_file(entry, prefix, connector)

    # def _add_directory(

    #     self, directory, index, entries_count, prefix, connector

    # ):

    #     self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
    #     if index != entries_count - 1:

    #         prefix += PIPE_PREFIX
    #     else:

    #         prefix += SPACE_PREFIX
    #     self._tree_body(
    #         directory=directory,
    #         prefix=prefix,
    #     )
    #     self._tree.append(prefix.rstrip())


    # def _add_file(self, file, prefix, connector):

    #     self._tree.append(f"{prefix}{connector} {file.name}")
