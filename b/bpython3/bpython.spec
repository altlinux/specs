%define _unpackaged_files_terminate_build 1
%define oname bpython
%def_with doc
%def_without check

%def_with curses
%def_with urwid

Name: bpython3
Version: 0.24
Release: alt1

Summary: Fancy curses interface to the Python 3 interactive interpreter

License: MIT
Group: Development/Python3
Url: https://bpython-interpreter.org/
VCS: https://github.com/bpython/bpython.git

BuildArch: noarch

# Source-url: https://github.com/bpython/bpython/archive/refs/tags/%version-release.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
%if_with check
BuildRequires: /dev/pts
BuildRequires: python3-module-pyxdg
BuildRequires: python3-module-curtsies
BuildRequires: python3-module-greenlet
BuildRequires: python3-module-typing_extensions
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
Group: Development/Python3
Summary: Documentation for bpython

%description doc
Documentation for bpython

%package urwid
Group: Development/Python3
Summary: Urwid front-end for bpython
Requires: %name = %EVR

%description urwid
Urwid front-end for bpython

%package curses
Group: Development/Python
Summary: Curses front-end for bpython
Requires: %name = %EVR

%description curses
Curses front-end for bpython

%prep
%setup
echo "__version__ = '%version'" > bpython/_version.py

%if_with doc
%prepare_sphinx3 doc/sphinx
ln -s ../objects.inv doc/sphinx/source/
%endif

%build
%python3_build

%if_with doc
pushd doc/sphinx/source
sphinx-build-3 -b html -d build/doctrees . html
popd
%endif

%install
%python3_install
mv %buildroot%python3_sitelibdir/%oname/urwid.py %buildroot%python3_sitelibdir/%oname/urwid_.py
mv %buildroot/%_bindir/%oname %buildroot/%_bindir/%name
mv %buildroot/%_bindir/%oname-urwid %buildroot/%_bindir/%name-urwid
mv %buildroot/%_bindir/%oname-curses %buildroot/%_bindir/%name-curses

subst "s|bpython|bpython3|" %buildroot%_datadir/applications/*
mv %buildroot%_pixmapsdir/%oname.png %buildroot%_pixmapsdir/%name.png

%check
python3 setup.py test

%files
%_bindir/bpdb
%_bindir/%name
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/urwid_.py
%exclude %python3_sitelibdir/%oname/cli.py
%exclude %python3_sitelibdir/%oname/test
%python3_sitelibdir/bpdb/
%python3_sitelibdir/*.egg-info
%_datadir/metainfo/*
%_datadir/applications/*
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
%_bindir/%{name}-urwid
%python3_sitelibdir/%oname/urwid_.py
%endif

%if_with curses
%files curses
%_bindir/%{name}-curses
%python3_sitelibdir/%oname/cli.py
%endif

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 0.24-alt1
- new version 0.24 (with rpmrb script)

* Fri Sep 09 2022 Danil Shein <dshein@altlinux.org> 0.23-alt1
- NMU: new version 0.23

* Mon Apr 18 2022 Danil Shein <dshein@altlinux.org> 0.22.1-alt1
- NMU: new version 0.22.1
- NMU: cleanup spec, fix FTBFS

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 0.20.1-alt2
- NMU: add sphinx module for man generation
- NMU: enable build doc subpackage

* Wed Aug 04 2021 Vitaly Lipatov <lav@altlinux.ru> 0.20.1-alt1
- NMU: cleanup spec, build bpython3 separately, switch to build from tarball

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

