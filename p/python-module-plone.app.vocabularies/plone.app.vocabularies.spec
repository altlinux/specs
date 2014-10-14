%define oname plone.app.vocabularies

%def_disable check

Name: python-module-%oname
Version: 2.1.17
Release: alt1.dev0.git20140907
Summary: A bundle of generally useful vocabularies in Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.vocabularies/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.vocabularies.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.browser python-module-pytz
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.querystring
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.site Products.CMFCore plone.app.querystring
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.schema
%py_requires plone.app zope.browser zope.component zope.formlib

%description
A collection of generally useful vocabularies.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration zope.testing

%description tests
A collection of generally useful vocabularies.

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
%doc *.rst
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.17-alt1.dev0.git20140907
- Initial build for Sisyphus

