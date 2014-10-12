%define oname Products.statusmessages
Name: python-module-%oname
Version: 4.0.1
Release: alt1.git20120103
Summary: statusmessages for Plone
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.statusmessages/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.statusmessages.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.component

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.annotation zope.i18n zope.interface

%description
statusmessages provides an easy way of handling internationalized status
messages managed via an BrowserRequest adapter storing status messages
in client-side cookies.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component

%description tests
statusmessages provides an easy way of handling internationalized status
messages managed via an BrowserRequest adapter storing status messages
in client-side cookies.

This package contains tests for %oname.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20120103
- Initial build for Sisyphus

