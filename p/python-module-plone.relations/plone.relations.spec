%define oname plone.relations
Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20121127
Summary: Tools for defining and querying complex relationships between objects
License: GPL / ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.relations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.relations.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zc.relationship
BuildPreReq: python-module-five.intid
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.hookable
BuildPreReq: python-module-zope.untrustedpython
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-nose

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone zc.relationship five.intid zope.container zope.intid
%py_requires zope.lifecycleevent zope.site

%description
Tools for defining and querying complex relationships between objects.
This product builds on and requires zc.relationship and also five.intid.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing

%description tests
Tools for defining and querying complex relationships between objects.
This product builds on and requires zc.relationship and also five.intid.

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
%doc *.txt
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20121127
- Initial build for Sisyphus

