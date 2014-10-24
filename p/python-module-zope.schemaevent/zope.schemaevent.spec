%define oname zope.schemaevent
Name: python-module-%oname
Version: 0.3
Release: alt1.dev0.git20140409
Summary: Event subscribers for zope.schema
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zope.schemaevent/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.schemaevent.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.schema-tests
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-unittest2

%py_provides %oname
%py_requires zope.component zope.schema

%description
Enable handler for event triggered on field by adding subscriber. We
make the configuration glue between zope.schema (which doesn't depend on
zope.component) and zope.component.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing plone.testing

%description tests
Enable handler for event triggered on field by adding subscriber. We
make the configuration glue between zope.schema (which doesn't depend on
zope.component) and zope.component.

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
%python_sitelibdir/zope/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zope/*/test*

%files tests
%python_sitelibdir/zope/*/test*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev0.git20140409
- Initial build for Sisyphus

