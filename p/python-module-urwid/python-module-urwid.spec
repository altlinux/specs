%define rname urwid

%def_with python3

Name: python-module-urwid
Version: 1.2.1
Release: alt1

Summary: Urwid is a console user interface library for Python.
License: LGPL
Group: Development/Python
Url: http://excess.org/urwid

Source: %rname-%version.tar

Buildrequires: python-modules-curses python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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
Summary: Tests for %rname
Group: Development/Python
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

This package contains tests for %rname.

%package pickles
Summary: Pickles for %rname
Group: Development/Python

%description pickles
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

This package contains pickles for %rname.

%package docs
Summary: Documentation for %rname
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

This package contains documentation for %rname.

%package -n python3-module-%rname
Summary: Urwid is a console user interface library for Python
Group: Development/Python3
%py3_provides %rname

%description -n python3-module-%rname
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

%package -n python3-module-%rname-tests
Summary: Tests for %rname
Group: Development/Python3
Requires: python3-module-%rname = %EVR

%description -n python3-module-%rname-tests
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

This package contains tests for %rname.

%prep
%setup -n %rname-%version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_build_install --optimize=2 --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%rname/

%files -f INSTALLED_FILES
%doc *.rst examples
%python_sitelibdir/%rname/
%exclude %python_sitelibdir/%rname/pickle
%exclude %python_sitelibdir/%rname/tests
%python_sitelibdir/%rname-%version-py*.egg-info/

%files tests
%python_sitelibdir/%rname/tests

%files pickles
%python_sitelibdir/%rname/pickle

%files docs
%doc docs/examples docs/tutorial docs/build/html

%if_with python3
%files -n python3-module-%rname
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%rname/tests

%files -n python3-module-%rname-tests
%python3_sitelibdir/%rname/tests
%endif

%changelog
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

