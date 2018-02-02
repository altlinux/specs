%def_without doc

%def_with curses
%def_with urwid

%def_with python3
%def_with python3_curses
%def_with python3_urwid

Name: bpython
Version: 0.14.1
Release: alt1.1.1

Summary: Fancy curses interface to the Python 2 interactive interpreter
License: MIT
Group: Development/Python
Url: http://bpython-interpreter.org/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Mon Mar 16 2015 (-bb)
# optimized out: python-base python-devel python-module-BeautifulSoup python-module-OpenSSL python-module-PyStemmer python-module-SQLAlchemy python-module-backports python-module-backports.ssl_match_hostname python-module-blessings python-module-cffi python-module-chardet python-module-cryptography python-module-docutils python-module-enum34 python-module-genshi python-module-google python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-markupsafe python-module-ndg python-module-ndg-httpsclient python-module-ntlm python-module-py python-module-pyasn1 python-module-pycparser python-module-pytest python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-urllib3 python-module-whoosh python-module-xapian python-modules python-modules-bsddb python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-Pygments python-module-babel python-module-cssselect python-module-curtsies python-module-greenlet python-module-html5lib python-module-mock python-module-nose python-module-requests python-module-setuptools python3-module-pytest rpm-build-python3

%if_with doc
BuildPreReq: python-module-objects.inv time
BuildPreReq: python-module-sphinx-devel
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-pytest rpm-build-python3
%endif

%py_requires curtsies

# no gtk frontend anymore
Obsoletes: bpython-gtk < %EVR

%description
bpython is a fancy interface to the Python interpreter for
Unix-like operating systems.

It has the following features:
 - In-line syntax highlighting.
 - Readline-like autocomplete with suggestions displayed as you type.
 - Expected parameter list for any Python function.
 - "Rewind" function to pop the last line of code from memory and
   re-evaluate.
 - Send the code you've entered off to a pastebin.
 - Save the code you've entered to a file.
 - Auto-indentation

%package doc
Group: Development/Python
Summary: Documentation for bpython

%description doc
Documentation for bpython

%package urwid
Group: Development/Python
Summary: Urwid front-end for bpython
Requires: %name = %version-%release

%description urwid
Urwid front-end for bpython

%package curses
Group: Development/Python
Summary: Curses front-end for bpython
Requires: %name = %version-%release

%description curses
Curses front-end for bpython

%package -n bpython3
Summary: Fancy curses interface to the Python 3 interactive interpreter
Group: Development/Python
# no gtk frontend anymore
Obsoletes: bpython3-gtk < %EVR
%py3_requires curtsies

%description -n bpython3
bpython is a fancy interface to the Python interpreter for
Unix-like operating systems.

It has the following features:
 - In-line syntax highlighting.
 - Readline-like autocomplete with suggestions displayed as you type.
 - Expected parameter list for any Python function.
 - "Rewind" function to pop the last line of code from memory and
   re-evaluate.
 - Send the code you've entered off to a pastebin.
 - Save the code you've entered to a file.
 - Auto-indentation

This is the Python 3 build of bpython

%package -n bpython3-urwid
Group: Development/Python
Summary: Urwid front-end for bpython3
Requires: bpython3 = %version-%release

%description -n bpython3-urwid
Urwid front-end for bpython3

%package -n bpython3-curses
Group: Development/Python
Summary: Curses front-end for bpython3
Requires: bpython3 = %version-%release

%description -n bpython3-curses
curses front-end for bpython3

%prep
%setup
%patch -p1
%if_with python3
cp -a . ../python3
%endif

%if_with doc
%prepare_sphinx doc/sphinx
ln -s ../objects.inv doc/sphinx/source/
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%if_with doc
pushd doc/sphinx/source
sphinx-build -b html -d build/doctrees . html
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%python3_sitelibdir/%name/urwid.py %buildroot%python3_sitelibdir/%name/urwid_.py
mv %buildroot/%_bindir/%name %buildroot/%_bindir/%{name}3
mv %buildroot/%_bindir/%name-urwid %buildroot/%_bindir/bpython3-urwid
rm -f %buildroot%_datadir/applications/%name.desktop
mv %buildroot/%_bindir/%name-curses %buildroot/%_bindir/bpython3-curses
%endif

%python_install
mv %buildroot%python_sitelibdir/%name/urwid.py %buildroot%python_sitelibdir/%name/urwid_.py

%check
python setup.py test ||:

%files
%_bindir/%name
%_bindir/bpbd
%python_sitelibdir/%name/
%exclude %python_sitelibdir/%name/urwid_.py
%exclude %python_sitelibdir/%name/cli.py
%exclude %python_sitelibdir/%name/test
%python_sitelibdir/bpdb/
%python_sitelibdir/%name-%version-py%_python_version.egg-info
%_desktopdir/%name.desktop
%_datadir/appdata/bpython.appdata.xml
%_pixmapsdir/%name.png

%_man1dir/*
%_man5dir/*

%if_without urwid
%exclude %_bindir/%{name}-urwid
%endif
%if_without curses
%exclude %_bindir/%{name}-curses
%endif

%if_with doc
%files doc
%doc doc/sphinx/source/html
%endif

%if_with urwid
%files urwid
%_bindir/%name-urwid
%python_sitelibdir/%name/urwid_.py
%endif

%if_with curses
%files curses
%_bindir/%name-curses
%python_sitelibdir/%name/cli.py
%endif

%if_with python3
%files -n bpython3
%_bindir/%{name}3
%python3_sitelibdir/%name/
%exclude %python3_sitelibdir/%name/urwid_.py
%exclude %python3_sitelibdir/%name/cli.py
%exclude %python3_sitelibdir/%name/test
%python3_sitelibdir/bpdb/
%python3_sitelibdir/%name-%version-py%_python3_version.egg-info
%_datadir/appdata/bpython.appdata.xml
%_pixmapsdir/%name.png


%if_without python3_urwid
%exclude %_bindir/%{name}3-urwid
%endif
%if_without python3_curses
%exclude %_bindir/%{name}3-curses
%endif

%if_with python3_urwid
%files -n bpython3-urwid
%_bindir/%{name}3-urwid
%python3_sitelibdir/%name/urwid_.py
%endif

%if_with python3_curses
%files -n bpython3-curses
%_bindir/%{name}3-curses
%python3_sitelibdir/%name/cli.py
%endif
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.14.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.14.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.14.1-alt1
- Updated to 0.14.1.

* Wed Jan 28 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.13.2-alt1
- Updated to 0.13.2.

* Mon Sep 08 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.13.1-alt2
- Fix bpython-urwid.
- Introduced bpython3 subpackage.
- Moved documentation to separate subpackage.

* Thu Aug 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1
- Version 0.13.1
- Packaged documentation.

* Fri Sep 13 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.12-alt1
- New version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7.1-alt1.1
- Rebuild with Python-2.7

* Tue Aug 24 2010 Alexey Morsov <swi@altlinux.ru> 0.9.7.1-alt1
- new version

* Sat Jan 23 2010 Alexey Morsov <swi@altlinux.ru> 0.9.6.2-alt2
- fix python requires
- fix requires

* Tue Jan 19 2010 Alexey Morsov <swi@altlinux.ru> 0.9.6.2-alt1
- initial build

