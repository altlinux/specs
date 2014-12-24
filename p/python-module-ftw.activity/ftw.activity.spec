%define mname ftw
%define oname %mname.activity
Name: python-module-%oname
Version: 1.1.4
Release: alt1.dev0.git20141219
Summary: An activity feed for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.activity/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.activity.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-openid
BuildPreReq: python-module-collective.lastmodifier
BuildPreReq: python-module-collective.prettydate
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Plone collective.lastmodifier collective.prettydate
%py_requires ftw.upgrade plone.api Products.CMFCore plone.uuid zope.i18n
%py_requires zope.interface zope.component zope.i18nmessageid

%description
ftw.activity provides a view with an activity stream for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.builder.testing ftw.testbrowser ftw.testing
%py_requires plone.app.testing plone.registry zope.configuration

%description tests
ftw.activity provides a view with an activity stream for Plone.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1.dev0.git20141219
- Initial build for Sisyphus

