%define mname collective
%define oname %mname.dms.scanbehavior
Name: python-module-%oname
Version: 0.3.1
Release: alt1.dev0.git20141128
Summary: collective.dms.scanbehavior
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.dms.scanbehavior/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.dms.scanbehavior.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-rwproperty
BuildPreReq: python-module-plone.api python-module-openid
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-ecreall.helpers.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
%py_requires %mname.dms plone.api plone.behavior plone.directives.form
%py_requires zope.schema zope.interface zope.component zope.publisher
%py_requires zope.i18nmessageid

%description
collective.dms.scanbehavior.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ecreall.helpers.testing plone.app.testing
%py_requires plone.app.robotframework.testing

%description tests
collective.dms.scanbehavior.

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
%doc *.rst docs/*
%python_sitelibdir/%mname/dms/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/dms/*/test*
%exclude %python_sitelibdir/%mname/dms/*/*/test*

%files tests
%python_sitelibdir/%mname/dms/*/test*
%python_sitelibdir/%mname/dms/*/*/test*

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.dev0.git20141128
- Initial build for Sisyphus

