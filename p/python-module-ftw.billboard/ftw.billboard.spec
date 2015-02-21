%define mname ftw
%define oname %mname.billboard
Name: python-module-%oname
Version: 1.4.1
Release: alt1.dev0.git20150209
Summary: Simple market place addon for plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.billboard/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.billboard.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ftw.calendarwidget
BuildPreReq: python-module-ftw.colorbox
BuildPreReq: python-module-ftw.profilehook
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname ftw.calendarwidget ftw.colorbox ftw.profilehook
%py_requires ftw.upgrade plone.api plone.app.registry Products.CMFCore
%py_requires Products.Archetypes Products.validation plone.indexer
%py_requires Products.ATContentTypes Products.statusmessages plone.api
%py_requires plone.portlets plone.app.portlets plone.registry zope.i18n
%py_requires zope.i18nmessageid zope.component zope.interface
%py_requires zope.container

%description
ftw.billboard is a plone addon for providing a market place where users
can add ads.

The ads are addable within billboard categories and can contain images
and attachments.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing plone.app.testing ftw.builder.testing
%py_requires ftw.testbrowser zope.configuration

%description tests
ftw.billboard is a plone addon for providing a market place where users
can add ads.

The ads are addable within billboard categories and can contain images
and attachments.

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
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.dev0.git20150209
- Initial build for Sisyphus

