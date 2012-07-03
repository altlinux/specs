%define oname z3c.traverser
Name: python-module-%oname
Version: 0.3.0
Release: alt2.1
Summary: Pluggable Traversers And URL handling utilities
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.traverser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.contentprovider zope.interface
%py_requires zope.publisher zope.traversing zope.viewlet

%description
This package provides the pluggable traverser mechanism allowing
developers to add new traversers to an object without altering the
original traversal implementation.

In addition to the pluggable traversers, this package contains two more
subpackages:

* viewlet - provides a way to traverse to viewlets using namespaces
* stackinfo - provides a way to consume parts of url and store them as
  attributes of the "consumer" object. Useful for urls like:
  /blog/2009/02/02/hello-world

%package tests
Summary: Tests for Pluggable Traversers And URL handling utilities
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy
%py_requires zope.app.zcmlfiles zope.testbrowser

%description tests
This package provides the pluggable traverser mechanism allowing
developers to add new traversers to an object without altering the
original traversal implementation.

This package contains tests for Pluggable Traversers And URL handling
utilities.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

