%def_without doc

%def_with gtk
%def_with urwid
%def_without curtsies

%def_with python3
%def_without python3_gtk
%def_without python3_urwid
%def_without python3_curtsies

Name: bpython
Version: 0.13.2
Release: alt1

Summary: Fancy curses interface to the Python 2 interactive interpreter
License: MIT
Group: Development/Python
Url: http://bpython-interpreter.org/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Mon Sep 08 2014 (-bb)
# optimized out: python-base python-devel python-module-BeautifulSoup python-module-PyStemmer python-module-Pygments python-module-docutils python-module-genshi python-module-jinja2 python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-setuptools
BuildRequires: python-module-babel python-module-html5lib python-module-jinja2-tests python-module-mock python-module-setuptools-tests python-module-sphinx python-module-requests

%if_with doc
BuildPreReq: python-module-objects.inv time
BuildPreReq: python-module-sphinx-devel
%endif

%if_with python3
BuildPreReq: python3-module-pytest rpm-build-python3
%endif

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

%package gtk
Group: Development/Python
Summary: GTK front-end for bpython
Requires: %name = %version-%release

%description gtk
GTK front-end for bpython

%package urwid
Group: Development/Python
Summary: Urwid front-end for bpython
Requires: %name = %version-%release

%description urwid
Urwid front-end for bpython

%package curtsies
Group: Development/Python
Summary: Curtsies front-end for bpython
Requires: %name = %version-%release

%description curtsies
Curtsies front-end for bpython

%package -n bpython3
Summary: Fancy curses interface to the Python 3 interactive interpreter
Group: Development/Python

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

%package -n bpython3-gtk
Group: Development/Python
Summary: GTK front-end for bpython3
Requires: bpython3 = %version-%release

%description -n bpython3-gtk
GTK front-end for bpython3

%package -n bpython3-urwid
Group: Development/Python
Summary: Urwid front-end for bpython3
Requires: bpython3 = %version-%release

%description -n bpython3-urwid
Urwid front-end for bpython3

%package -n bpython3-curtsies
Group: Development/Python
Summary: Curtsies front-end for bpython3
Requires: bpython3 = %version-%release

%description -n bpython3-curtsies
Curtsies front-end for bpython3

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
mv %buildroot/%_bindir/%name-gtk %buildroot/%_bindir/bpython3-gtk
mv %buildroot/%_bindir/%name-curtsies %buildroot/%_bindir/bpython3-curtsies
%endif

%python_install
mv %buildroot%python_sitelibdir/%name/urwid.py %buildroot%python_sitelibdir/%name/urwid_.py

%check
python setup.py test

%files
%_bindir/%name
%python_sitelibdir/%name/
%exclude %python_sitelibdir/%name/gtk_.py
%exclude %python_sitelibdir/%name/urwid_.py
%exclude %python_sitelibdir/%name/curtsies.py
%exclude %python_sitelibdir/%name/curtsiesfrontend
%exclude %python_sitelibdir/%name/test
%python_sitelibdir/bpdb/
%python_sitelibdir/%name-%version-py%_python_version.egg-info
%_desktopdir/%name.desktop
%_man1dir/*
%_man5dir/*

%if_without gtk
%exclude %_bindir/%{name}-gtk
%endif
%if_without urwid
%exclude %_bindir/%{name}-urwid
%endif
%if_without curtsies
%exclude %_bindir/%{name}-curtsies
%endif

%if_with doc
%files doc
%doc doc/sphinx/source/html
%endif

%if_with gtk
%files gtk
%_bindir/%name-gtk
%python_sitelibdir/%name/gtk_.py
%endif

%if_with urwid
%files urwid
%_bindir/%name-urwid
%python_sitelibdir/%name/urwid_.py
%endif

%if_with curtsies
%files curtsies
%_bindir/%name-curtsies
%python_sitelibdir/%name/curtsies.py
%python_sitelibdir/%name/curtsiesfrontend
%endif

%if_with python3
%files -n bpython3
%_bindir/%{name}3
%python3_sitelibdir/%name/
%exclude %python3_sitelibdir/%name/gtk_.py
%exclude %python3_sitelibdir/%name/urwid_.py
%exclude %python3_sitelibdir/%name/curtsies.py
%exclude %python3_sitelibdir/%name/curtsiesfrontend
%exclude %python3_sitelibdir/%name/test
%python3_sitelibdir/bpdb/
%python3_sitelibdir/%name-%version-py%_python3_version.egg-info

%if_without python3_gtk
%exclude %_bindir/%{name}3-gtk
%endif
%if_without python3_urwid
%exclude %_bindir/%{name}3-urwid
%endif
%if_without python3_curtsies
%exclude %_bindir/%{name}3-curtsies
%endif

%if_with python3_gtk
%files -n bpython3-gtk
%_bindir/%{name}3-gtk
%python3_sitelibdir/%name/gtk_.py
%endif

%if_with python3_urwid
%files -n bpython3-urwid
%_bindir/%{name}3-urwid
%python3_sitelibdir/%name/urwid_.py
%endif

%if_with python3_curtsies
%files -n bpython3-curtsies
%_bindir/%{name}3-curtsies
%python3_sitelibdir/%name/curtsies.py
%python3_sitelibdir/%name/curtsiesfrontend
%endif
%endif

%changelog
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

