# -*- coding: utf-8 -*-

%define oname MySQLdb2
%def_without python3

Version: 1.3.0
Release: alt2.hg20110907
%setup_python_module %oname
Name: %packagename

Summary: Python interface to MySQL-3.23+
Summary(ru_RU.UTF-8): Интерфейс к MySQL-3.23+ для Python
License: GPLv2
Group: Development/Python
Url: http://sourceforge.net/projects/mysql-python
Packager: Python Development Team <python@packages.altlinux.org>

# hg clone http://mysql-python.hg.sourceforge.net:8000/hgroot/mysql-python/MySQLdb-2.0
Source: MySQL-python.tar

# Automatically added by buildreq on Fri Jul 13 2007
BuildRequires: libmysqlclient-devel python-module-setuptools zlib-devel
BuildPreReq: libssl-devel
Conflicts: python-module-MySQLdb
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

Obsoletes: MySQL-python <= 0.9.2-alt6

%description
MySQLdb is an interface to the popular MySQL database server for
Python.  The design goals are:

- Compliance with Python database API version 2.0

- Thread-safety

- Thread-friendliness (threads will not block each other)

MySQL-3.23 through 5.0 and Python-2.3 through 2.5 are currently
supported.

MySQLdb is Free Software.

%description -l ru_RU.UTF-8
MySQLdb - это интерфейс к популярной СУБД MySQL для Python.
При его создании преследовались следующие цели:

-    Соответствие API баз данных для Python версии 2.0

-    Совместимость с многопоточными средами

-    "Дружелюбие к потокам" (потоки не блокируют друг друга)

-    Совместимость с MySQL-3.23 и более поздними (вплоть до ветки 5.0)

MySQLdb - это свободное ПО.

%if_with python3
%package -n python3-module-%oname
Summary: Python3 interface to MySQL-3.23+
Group: Development/Python3
Conflicts: python3-module-MySQLdb

%description -n python3-module-%oname
MySQLdb is an interface to the popular MySQL database server for
Python.  The design goals are:

- Compliance with Python database API version 2.0

- Thread-safety

- Thread-friendliness (threads will not block each other)
%endif

%prep
%setup -n MySQL-python
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --optimize=2 --record=INSTALLED_FILES
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc README HISTORY doc/*
%python_sitelibdir/MySQLdb

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Thu May 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.hg20110907
- Renamed MySQLdb -> MySQLdb2 (ALT #27288)

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.hg20110907
- Version 1.3.0

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt3.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt3
- Rebuilt for debuginfo

* Wed Sep 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2
- Rebuilt with libmysqlclient.so.16

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1
- Version 1.2.3

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.1.1
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.2.2-alt1.1
- Rebuilt with python-2.5.

* Fri Jul 13 2007 Ivan Fedorov <ns@altlinux.org> 1.2.2-alt1
- 1.2.2

* Mon Mar 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt0.1
- NMU: new version (build with MySQL 5.x)
- add packager, add URL in Source, remove Prefix, Vendor
- 

* Mon Mar 07 2005 Andrey Orlov <cray@altlinux.ru> 1.0.1-alt3
- Rebuild with python 2.4

* Tue Jan 11 2005 Andrey Orlov <cray@altlinux.ru> 1.0.1-alt2
- Some dependencies fixed

* Mon Jan 10 2005 Alexey Morozov <morozov@altlinux.org> 1.0.1-alt1
- New release (1.0.1). Not actually tested yet ;-)
- python_req_hier macro is used.
- Spec cleanup
- Russian translation in spec.

* Thu Aug 19 2004 Alexey Morozov <morozov@altlinux.org> 1.0.0-alt1
- 1.0.0 release

* Mon May 31 2004 Alexey Morozov <morozov@altlinux.org> 1.0.0-alt0c2
- New version (1.0.0c2 prerelease)

* Wed May 19 2004 Andrey Orlov <cray@altlinux.ru> 0.9.2-alt9
- Fix obsoletes ;(

* Wed May 19 2004 Andrey Orlov <cray@altlinux.ru> 0.9.2-alt8
- Obsoletes on previous package added

* Mon May 17 2004 Andrey Orlov <cray@altlinux.ru> 0.9.2-alt7
- Conditional packaging excluded
- Obsoletes previouse package added

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 0.9.2-alt6.d
- Rebuild with new rpm release

* Fri Mar 26 2004 Andrey Orlov <cray@altlinux.ru> 0.9.2-alt5.d
- Fix new python policy compatibility

* Thu Dec 04 2003 Andrey Orlov <cray@altlinux.ru> 0.9.2-alt2
- Rebuild with python23

* Sat Oct 19 2002 Andrey Orlov <cray@altlinux.ru> 0.9.2-alt1
  New Version from digicoool
  0.9.2
  + BUG: When using Python 1.5.2, if the connect fails, Python seems
  to eventually crash with a segfault. In my case, this seems to
  only happen on exit. I just have not been able to track this one
  down.  I still want to support Python 1.5.2, and I'm probably just
  missing something very subtle. There's no problem with either
  Python 2.1.3 or 2.2.1; I have not tested with 1.6 through 2.1.2
  nor 2.2, nor do I plan to, but there should be no issues with
  other versions, except for the above issue with 1.5.2.
  + Memory API updates. The GC memory allocator is used when Python
  2.2 or newer is used.
  + Minor RPM packaging cleanups.
  + cursor.execute(query) with no args leaves the original query string
  alone; it no longer tries to do query %% (). This is to maintain
  backwards compatibility. The only time this is an issue is if your
  query has percent signs (%%) in it, as in the SQL wildcard used for
  LIKE comparisions. I strongly recommend passing any string literals
  as parameters to avoid this issue.
  0.9.2c3
  + Did some more setup cleanups. Apparently on non-server versions of
  MacOSX, the MySQL stuff installs in /sw instead of /usr/local.
  + There's now a cursor._execute(), used by execute() and executemany(),
  when does NOT clear cursor.messages. Internal use only. This is so
  all messages can be kept with executemany().
  + Fixed a memory leak (cursor+traceback) I introduced when reworking
  the errorhandler code.
  + If both conv and unicode options were given to connect, things
  broke. (Skip Montanaro)
  + Since MySQL uses the same internal FIELD_TYPE for both BLOB and
  TEXT columns, reverting the 0.9.2c1 change that returned them
  as array objects; they are now strings again. Array objects passed
  as parameters are still converted correctly into string literals.
  + Replaced cursor iterator implementation with something not dumb.
  The old one worked, but the new one makes use of the iter()
  function. StoreResultMixIn has it's own implementation which is
  fast but doesn't update the rownumber, which should not be a real
  problem in practice.
  0.9.2c2
  + errorhandler cleanups (Rob Steele)
  0.9.2c1
  + If using Python 2.2 or newer, the _mysql connection object is
  now usable as a base class, and MySQLdb.Connection uses it as
  it's base class. If you have an older Python, everything still
  works as if it were a subclass, due to some clever __getattr__.
  + Internal documentation with _mysql is greatly expanded and
  improved.
  + BLOBs are now converted to Python array objects (from the array
  module). If you are expecting them to be strings, sorry. This
  is actually the preferred representation for DB-API.
  [Reverted in 0.9.2c3]
  + MySQL converts array objects passed as parameters into a correct
  string representation (presumably for BLOB columns).
  + The unicode=charset option to connect causes CHAR and VARCHAR
  columns to be returned as unicode options using the specified
  character set. XXX This needs more testing as I really don't
  do anything with unicode.
  + cursor.executemany() would only work with INSERT and REPLACE,
  when it ought to work with any statement. Now fixed, though
  still optimized to do multi-row INSERT/REPLACE.
  + cursor.executemany() also didn't work if you passed it a
  zero-length list. Whoops. Although zero is not many...
  + Use name of the python interpreter as part of the package name.
  On Red Hat Linux (7.2 and earlier), the standard python package
  is 1.5.2. The www.python.org RPM package for Python-2.2.1 is
  python2, and their 2.1.3 package is python2.1. This is so you can
  install all three at once; RPM considers them different packages.
  With this packaging change, you'll now get:
  python setup.py bdist_rpm # MySQL-python for python-1.5.2
  python2.1 setup.py bdist_rpm # MySQL-python2.1 for python 2.1.x
  python2 setup.py bdist_rpm # MySQL-python2 for python 2.2.x
  (You probably need to use the --python=x option where x is the
  name of the Python executable so that the RPM build uses the right
  version of python.)
  Once Python 2.3 comes out, that will probably become the python2
  package, and the Python 2.2.x version will become the python2.2
  package, or at least that's what the progression seems to be.
  Note that in the current Red Hat beta (skipjack), the python
  package is still 1.5.2 and python2 is 2.2. Skipjack already
  comes with MySQL-python-0.9.1, but I don't know what version of
  Python it's compiled against. Who knows if Red Hat will follow
  python.org's naming convention, but in any case, this change
  shouldn't hurt anything.
  + Plug: I will be at OScon2002 giving a tutorial session on the
  Python DB-API, mostly using MySQLdb.
  http://conferences.oreillynet.com/os2002/

* Thu May 30 2002 Andrey Orlov <cray@altlinux.ru> 0.9.2b2-alt1
  New Version from digicoool
  0.9.2b2
  + Avoid memory leak when using dictionary-based cursors
  + Avoid crash when using fetchall on SSCursors (mysql_use_result)
  0.9.2b1
  + Minor build updates
  + Avoid memory leak on connection failure
  + Avoid potential leak on cursor close.

* Wed Feb 20 2002 Uzorin Pavel <pitch@altlinux.ru> 0.9.2a2-alt3
  Initial changelog
  0.9.2a2
  + Reworked platform configuration some more. cygwin is now (sorta)
  supported (to the extent that Windows is supported at all).
  + Use PyObject_Del() to dealloc objects, if we have Python 2.0 or newer.
  + Fixed broken CursorStoreResultMixIn.fetchmany().
- 0.9.2a1
  + Added a number of DB-API extensions.
  + Unicode instances can now be used as parameters to cursor.execute().
  It attempts to use whatever character set MySQL is using. If that
  can't be determined, then latin1 is used.
  + Mac OS X configuration linkage fix (Dan Grassi)
  + netbsd configuration (Tage Stabell-Kuloe)
- 0.9.1
  + The Set class wasn't being imported into MySQLdb, so
  "from MySQLdb import +" didn't work (not that I recommend you do
  this).
  + Tested a bit with MySQL-4.0.0. Seems to be okay. Embedded support
  is forthcoming.
- 0.9.1c2
  + Exceptions on connect() were not handled correctly.
  + Added CHANGELOG to MANIFEST.in. (John Bowe)
- 0.9.1c1
  + Added ER_PARSE_ERROR as a ProgrammingError, because
  ER_SYNTAX_ERROR doesn't get the job done.
  + In Python < 2.0.1, PyArgs_ParseTupleAndKeywords() returns a new
  reference when the O format is used. In 2.0.1 and later, it
  returns a borrowed reference. Since it's not actually documented
  either way that I can tell, I must assume this is some sort of
  bugfix. However, it does mean that you need to test against the
  Python version, and Py_INCREF() if it is 2.0.1 or later. If you
  Py_INCREF() all the time, you get a memory leak in earlier
  version; and if you never Py_INCREF(), it works fine in earlier
  versions but crashes later versions. If you're an end-user, don't
  worry about this...
  + In Python 2.2, the internal _PyTuple_Resize() dropped the (unused)
  third argument, so we have to test against the Python version here
  as well to maintain backwards compatibility.
  + Some deprecated MySQL API functions were removed.
  + A literal() method was added to the database connection. It takes
  a single argument and converts it into an SQL literal. If the
  argument is a non-string sequence, the sequence items are
  converted to SQL literals, and the sequence of converted items is
  returned as a list. This was previously done internally by Cursor
  objects. You don't normally need to use it, but it might be useful
  for debugging.
  + Return DECIMAL/NUMERIC columns as floats.
  + A number of documentation updates.
- 0.9.0
  Too many changes from 0.3.5 to go into much detail.
  + MySQLdb was turned into a true Python package.
  + _mysql didn't change all that much. Constants were moved out into
  the MySQLdb package structure. Exceptions were moved to
  _mysql_exceptions.py, but these are imported into _mysql. This
  makes the binary (and source) significantly smaller.
  + Reduced threadsafety to 1 (from 2), and ripped out a lot of the
  crap that attempts to let you safely share a connection between
  threads. If you are using transactions, you can only hand off the
  connection from one thread to another after a commit or
  rollback. Sharing a connection will hurt your performance anyway,
  so give each thread it's own connection.
  + A Set class was added for use with SET columns.
  + Loads of docstrings were added to take advantage of pydoc.
  + Operationally, there's not much difference.
