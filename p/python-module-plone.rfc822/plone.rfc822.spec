%define oname plone.rfc822
Name: python-module-%oname
Version: 1.1.1
Release: alt1.dev0.git20140620
Summary: RFC822 marshalling for zope.schema fields
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.rfc822/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.rfc822.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.schema python-module-dateutil
#BuildPreReq: python-module-plone.supermodel

%py_provides %oname
%py_requires plone zope.schema zope.component zope.interface
#py_requires plone.supermodel

%description
This package provides primitives for turning content objects described
by zope.schema fields into RFC (2)822 style messages, as managed by the
Python standard library's email module.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides primitives for turning content objects described
by zope.schema fields into RFC (2)822 style messages, as managed by the
Python standard library's email module.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.dev0.git20140620
- Initial build for Sisyphus

