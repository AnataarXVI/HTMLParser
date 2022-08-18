<a target="_blank" href="https://img.shields.io/badge/platform-linux-success.svg" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/platform-linux-success.svg">
</a>
<a target="_blank" href="https://img.shields.io/badge/platform-windows-success.svg" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/platform-windows-success.svg">
</a>
<a target="_blank" href="https://img.shields.io/badge/version-1.0.0-yellow" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/version-1.0.0-yellow">
</a>
<a href="https://www.python.org/" rel="nofollow">
    <img src="https://img.shields.io/badge/python-3.10-red">
</a>
<a href="https://github.com/msd0pe-1/cve-maker-master/blob/master/LICENSE" rel="nofollow">
    <img src="https://img.shields.io/badge/license-GPLv3-9cf.svg">
</a>

# HTMLParser
 This Tool can parse information in code source of a html page.Its role is to collect information quickly.

 Made by AnataarXVI

# How it works ?

HTMLParser will send a request to the indicated website and retrieve information depending on the option chosen.

# Installation

Download the project : `https://github.com/AnataarXVI/htmlparser.git`

## Complete parsing

![example_image1](/assets/2022-08-18_20-13.png)

## Parsing script tag
![2022-08-18_20-28](/assets/2022-08-18_20-28.png)

# Usage

```
Usage: python htmlparser.py [options] <url>

Options:
  --version      show program's version number and exit
  -h, --help     show this help message and exit
  -a, --all      Parse with all options (-c, -s, -f, -l)
  -c, --comment  Find all comments
  -s, --script   Find all scripts
  -f, --form     Find all forms
  -l, --link     Find all links

  Examples:
    python htmlparser.py -a <url>
    python htmlparser.py -c <url>
    python htmlparser.py -s <url>
    python htmlparser.py -f <url>
    python htmlparser.py -l <url>

This tool is used to analyze the source code of an html page by recovering tags and comments
```

# Contributing

If you liked the project do not hesitate to share it. I am free to any improvement proposal.