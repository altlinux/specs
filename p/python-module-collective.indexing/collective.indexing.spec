%define mname collective
%define oname %mname.indexing
Name: python-module-%oname
Version: 2.0
Release: alt1.dev.git20130216
Summary: Abstract framework for queueing, optimizing and dispatching index operations
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.indexing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/collective.indexing.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.ATContentTypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.container zope.event zope.lifecycleevent
%py_requires zope.publisher Products.CMFCore Products.Archetypes
%py_requires Products.CMFPlone

%description
collective.indexing is an approach to provide an abstract framework for
queuing and optimizing index operations in Plone as well as dispatching
them to various backends. The default implementation aims to replace the
standard indexing mechanism of CMF to allow index operations to be
handled asynchronously in a backwards-compatible way.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing unittest2 Products.ATContentTypes

%description tests
collective.indexing is an approach to provide an abstract framework for
queuing and optimizing index operations in Plone as well as dispatching
them to various backends. The default implementation aims to replace the
standard indexing mechanism of CMF to allow index operations to be
handled asynchronously in a backwards-compatible way.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/%mname
cp -fR src/collective/indexing %buildroot%python_sitelibdir/%mname/
cp -fR src/*.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.txt *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.dev.git20130216
- Initial build for Sisyphus

