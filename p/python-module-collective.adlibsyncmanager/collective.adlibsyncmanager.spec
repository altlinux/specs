%define mname collective
%define oname %mname.adlibsyncmanager
Name: python-module-%oname
Version: 0.1
Release: alt1.git20141114
Summary: Provides external methods to sync and create content from Adlib API
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.adlibsyncmanager/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.adlibsyncmanager.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-PasteScript python-module-PasteDeploy
BuildPreReq: python-module-collective.contentleadimage
BuildPreReq: python-module-collective.object
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.app.multilingual
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.multilingual
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.contentleadimage collective.object
%py_requires plone.namedfile plone.app.multilingual Products.CMFCore
%py_requires plone.registry plone.multilingual plone.i18n
%py_requires plone.dexterity plone.app.textfield zope.component

%description
Provides external methods to sync and create content from Adlib API.

Features:

* Creates Object content type in a Plone site based on Adlib API data.
* Synchronization of content from Adlib API with a Plone site.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Provides external methods to sync and create content from Adlib API.

This package contains tests for %oname.

%prep
%setup

rm -fR dist Paste* .svn

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
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141114
- Initial build for Sisyphus

