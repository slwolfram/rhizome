import functools
from collections import namedtuple

import MySQLdb as mySql

get_db = lambda: mySql.connect(
    host='localhost', user='root', passwd='dbadmin', db='rhizome')
