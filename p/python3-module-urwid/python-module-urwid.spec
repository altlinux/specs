%define _unpackaged_files_terminate_build 1
%define oname urwid

Name: python3-module-urwid
Version: 2.1.2
Release: alt1

Summary: Urwid is a console user interface library for Python.

License: LGPL
Group: Development/Python3
Url: http://excess.org/urwid

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.1.3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%py3_provides %oname

%description
Urwid is a console user interface library for Python. Urwid is released
under the GNU Lesser General Public License and it includes many features
useful for text console application developers:

 * Fluid interface resizing (xterm window resizing / fbset on Linux console)
 * Web application display mode using Apache and CGI [ Live Demo ]
 * Support for UTF-8, simple 8-bit and CJK encodings
 * Multiple text alignment and wrapping modes built-in
 * Ability create user-defined text layout classes
 * Simple markup for setting text attributes
 * Powerful list box that handles scrolling between different widget types
 * List box contents may be managed with a user-defined class
 * Flexible edit box for editing many different types of text
 * Buttons, check boxes and radio boxes
 * Customizable layout for all widgets
 * Easy interface for creating HTML screen shots

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Urwid is a console user interface library for Python. Urwid is released
under the GNU Lesser General Public License and it includes many features
useful for text console application developers:

 * Fluid interface resizing (xterm window resizing / fbset on Linux console)
 * Web application display mode using Apache and CGI [ Live Demo ]
 * Support for UTF-8, simple 8-bit and CJK encodings
 * Multiple text alignment and wrapping modes built-in
 * Ability create user-defined text layout classes
 * Simple markup for setting text attributes
 * Powerful list box that handles scrolling between different widget types
 * List box contents may be managed with a user-defined class
 * Flexible edit box for editing many different types of text
 * Buttons, check boxes and radio boxes
 * Customizable layout for all widgets
 * Easy interface for creating HTML screen shots

This package contains tests for %oname.


%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Urwid is a console user interface library for Python. Urwid is released
under the GNU Lesser General Public License and it includes many features
useful for text console application developers:

 * Fluid interface resizing (xterm window resizing / fbset on Linux console)
 * Web application display mode using Apache and CGI [ Live Demo ]
 * Support for UTF-8, simple 8-bit and CJK encodings
 * Multiple text alignment and wrapping modes built-in
 * Ability create user-defined text layout classes
 * Simple markup for setting text attributes
 * Powerful list box that handles scrolling between different widget types
 * List box contents may be managed with a user-defined class
 * Flexible edit box for editing many different types of text
 * Buttons, check boxes and radio boxes
 * Customizable layout for all widgets
 * Easy interface for creating HTML screen shots

This package contains documentation for %oname.


%prep
%setup

#%prepare_sphinx .
#ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

#export PYTHONPATH=%buildroot%python_sitelibdir
#pushd docs
#sphinx-build -b pickle -d build/doctrees . build/pickle
#sphinx-build -b html -d build/doctrees . build/html
#popd

#cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

#%files docs
#%doc docs/examples docs/tutorial docs/build/html

%files
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- new version 2.1.2 (with rpmrb script)

* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- build python3 module only

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.1-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1
- Added module for Python 3

* Mon Sep 16 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.1-alt1
- New version

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.1.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.1
- Rebuilt for debuginfo

* Sat Jan 23 2010 Alexey Morsov <swi@altlinux.ru> 0.9.9-alt1
- new version

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.4-alt2
- Rebuilt with python 2.6

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 0.9.8.4-alt1
- new version

* Thu Dec 13 2007 Alexey Morsov <swi@altlinux.ru> 0.9.8.1-alt1
- initial build

