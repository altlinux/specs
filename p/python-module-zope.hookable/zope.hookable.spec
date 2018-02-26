%define oname zope.hookable
Name: python-module-%oname
Version: 3.4.1
Release: alt2.1.1
Summary: Hookable object support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.hookable/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope

%description
Support the efficient creation of hookable objects, which are callable
objects that are meant to be replaced by other callables, at least
optionally.

The idea is you create a function that does some default thing and make
it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation.  All users of the
function, including those that imported it, will see the change.

%package tests
Summary: Tests for zope.hookable
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Support the efficient creation of hookable objects, which are callable
objects that are meant to be replaced by other callables, at least
optionally.

The idea is you create a function that does some default thing and make
it hookable. Later, someone can modify what it does by calling its
sethook method and changing its implementation.  All users of the
function, including those that imported it, will see the change.

This package contains tests for zope.hookable.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus

