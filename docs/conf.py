# Configuration file for the Sphinx documentation builder.

import os
import datetime

# -- Print Versions

import sys
print ('python version: ' + str(sys.version))

from sphinx import __version__ as sphinx_version
print ('sphinx version: ' + str(sphinx_version))

from sphinx_ifelse import __version__ as sphinx_ifelse_version
print ('sphinx_ifelse version: ' + str(sphinx_ifelse_version))

from sphinx_needs import __version__ as sphinx_needs_version
print ('sphinx-needs version: ' + str(sphinx_needs_version))

sys.path.append(os.path.abspath('.'))


# -- Project information

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

project = 'Playground'
copyright = f'2025 - {date.year}, PhilipPartsch'
author = 'PhilipPartsch'

release = '1.0'
version = '1.0.0'

# -- General configuration
on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.doctest',
    'sphinx_needs',
    'sphinxcontrib.plantuml',
    #'sphinxcontrib.test_reports',
    #'sphinxcontrib.collections',
    'sphinxcontrib.jquery', # https://github.com/sphinx-contrib/jquery
    'sphinx_preview',
    #'sphinx_immaterial',
    'sphinx_ifelse'
]

templates_path = ['_templates']

exclude_patterns = ['_tools/*',]

# to use numref see https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-numfig
numfig = True

# -- intersphinx

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']


# -- Sphinx-Preview

# The config for the preview features, which allows to "sneak" into a link.
# Docs: https://sphinx-preview.readthedocs.io/en/latest/#configuration
preview_config = {
    # Add a preview icon only for this type of links
    # This is very theme and HTML specific. In this case "div-mo-content" is the content area
    # and we handle all links there.
    #"selector": "div.md-content a",
    "selector": "div.main a",
    # A list of selectors, where no preview icon shall be added, because it makes often no sense.
    # For instance the own ID of a need object, or the link on an image to open the image.
    "not_selector": "div.needs_head a, h1 a, h2 a, a.headerlink, a.md-content__button, a.image-reference, em.sig-param a, a.paginate_button",
    #"not_selector": "div.needs_head a, h1 a, h2 a",
    "set_icon": True,
    "icon_only": True,
    "icon_click": True,
    "icon": "🔎",
    #"icon": "icon:search",
    "width": 600,
    "height": 400,
    "offset": {
        "left": 0,
        "top": 0
    },
    "timeout": 0,
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
#html_theme = 'sphinx_immaterial'

html_css_files = ['custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- extension configuration: ifelse

ifelse_variants = {
   'ifelse_OS': 'ifelse_Linux',
}

# --  sphinxcontrib.plantuml configuration
local_plantuml_path = os.path.join(os.path.dirname(__file__), "_tools", "plantuml.jar")

if on_rtd:
    plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
else:
    plantuml = f"java -jar {local_plantuml_path}"

print('plantuml path: ' + str(plantuml))

plantuml_output_format = 'svg'

# -- Sphinx-Needs

needs_from_toml = "ubproject.toml"

from sphinx_needs.api import add_dynamic_function

def getUnits(app, need, needs, *args, **kwargs):
    # Do magic here
    need_file = need["docname"] + need["doctype"]
    linked_needs = []

    for n in needs:
        current_file = n["docname"] + n["doctype"]
        if current_file == need_file and n["type"] == "unit":
            linked_needs.append(n["id"])

    return linked_needs

from sphinx_needs.config import NeedsSphinxConfig
from sphinx_needs.filter_common import filter_needs_and_parts

def copyall(
    app: Sphinx,
    need: NeedItem | NeedPartItem | None,
    needs: NeedsMutable | NeedsView,
    option: str,
    need_id: str | None = None,
    lower: bool = False,
    upper: bool = False,
    filter: str | None = None,
) -> Any:
    """
    Copies the value of needs option to another need.
    """
    if need_id:
        need = needs[need_id]

    if filter:
        location = (
            (need["docname"], need["lineno"]) if need and need["docname"] else None
        )
        result = filter_needs_and_parts(
            needs.values(),
            NeedsSphinxConfig(app.config),
            filter,
            need,
            location=location,
        )

    if 0 == len(result):
        raise ValueError("Needs not found")

    if option not in result[0]:
        raise ValueError(f"Option {option} not found in needs config.")

    values = []

    for r in result:
        value = r[option]
        if upper:
            values.append(str(value).upper())
        elif lower:
            values.append(str(value).lower())
        else:
            values.append(value)

    return values

def setup(app):
    add_dynamic_function(app, copyall)

