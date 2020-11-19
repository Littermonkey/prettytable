import os
from pkg_resources import get_distribution, DistributionNotFound

from .prettytable import (
    ALL,
    DEFAULT,
    FRAME,
    HEADER,
    MARKDOWN,
    MSWORD_FRIENDLY,
    NONE,
    ORGMODE,
    PLAIN_COLUMNS,
    RANDOM,
    PrettyTable,
    TableHandler,
    from_csv,
    from_db_cursor,
    from_html,
    from_html_one,
    from_json,
)

__all__ = [
    "ALL",
    "DEFAULT",
    "FRAME",
    "HEADER",
    "MARKDOWN",
    "MSWORD_FRIENDLY",
    "NONE",
    "ORGMODE",
    "PLAIN_COLUMNS",
    "RANDOM",
    "PrettyTable",
    "TableHandler",
    "from_csv",
    "from_db_cursor",
    "from_html",
    "from_html_one",
    "from_json",
]


try:
    _dist = get_distribution('prettytable')
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'prettytable')):
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Please install this project with setup.py'
else:
    __version__ = _dist.version

