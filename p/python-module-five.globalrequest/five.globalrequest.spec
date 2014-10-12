%define oname five.globalrequest
Name: python-module-%oname
Version: 1.1
Release: alt1.dev.git20140409
Summary: Zope 2 integration for zope.globalrequest
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/five.globalrequest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/five.globalrequest.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-docutils

%py_provides %oname
Requires: python-module-Zope2
%py_requires five zope.globalrequest

%description
This package integrates zope.globalrequest with Zope 2.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package integrates zope.globalrequest with Zope 2.

This package contains tests for %oname

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/five/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/five/*/tests.*

%files tests
%python_sitelibdir/five/*/tests.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev.git20140409
- Initial build for Sisyphus

