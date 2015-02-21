%define mname ftw
%define oname %mname.poodle
Name: python-module-%oname
Version: 1.4.2
Release: alt1.dev0.git20150108
Summary: Provides a doodle like function in Plone
License: GPLv2+
Group: Development/Python
Url: https://github.com/4teamwork/ftw.poodle
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.poodle.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.DataGridField
BuildPreReq: python-module-Products.AutocompleteWidget
BuildPreReq: python-module-plone.principalsource
BuildPreReq: python-module-ftw.notification.email
BuildPreReq: python-module-ftw.notification.base
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.DataGridField Products.AutocompleteWidget
%py_requires plone.principalsource ftw.notification.email ftw.upgrade
%py_requires ftw.notification.base Products.CMFCore Products.Archetypes
%py_requires Products.ATContentTypes Products.statusmessages plone.i18n
%py_requires zope.i18nmessageid zope.component zope.schema zope.i18n
%py_requires zope.browserpage zope.publisher zope.interface zope.viewlet
%py_requires zope.annotation

%description
A product to make polls to find out when to have a meeting.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing ftw.testing Products.PloneTestCase
%py_requires zope.traversing zope.configuration

%description tests
A product to make polls to find out when to have a meeting.

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
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1.dev0.git20150108
- Initial build for Sisyphus

