%define mname ftw
%define oname %mname.task

%def_disable check

Name: python-module-%oname
Version: 2.4.8
Release: alt1.dev0.git20141107
Summary: A simple task content type for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.task/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.task.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 python-module-mocker
BuildPreReq: python-module-transaction
BuildPreReq: python-module-ftw.pdfgenerator
BuildPreReq: python-module-ftw.workspace
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATReferenceBrowserWidget
BuildPreReq: python-module-plone.principalsource
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-ftw.calendarwidget
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-ftw.tabbedview
BuildPreReq: python-module-ftw.table

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname ftw.pdfgenerator ftw.workspace zope.app.component
%py_requires zope.component zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.schema Products.ATContentTypes Products.Archetypes
%py_requires Products.CMFCore Products.ATReferenceBrowserWidget
%py_requires plone.principalsource plone.app.contentmenu plone.portlets
%py_requires plone.app.portlets ftw.calendarwidget ftw.upgrade
%py_requires Products.GenericSetup ftw.tabbedview ftw.table

%description
ftw.task provides a simple task content type for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires unittest2 mocker transaction ftw.testing plone.testing
%py_requires plone.app.testing ftw.builder.testing ftw.testbrowser
%py_requires zope.configuration zope.traversing Products.CMFPlone

%description tests
ftw.task provides a simple task content type for Plone.

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
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.8-alt1.dev0.git20141107
- Initial build for Sisyphus

