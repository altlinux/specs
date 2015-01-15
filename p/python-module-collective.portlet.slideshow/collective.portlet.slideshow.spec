%define mname collective.portlet
%define oname %mname.slideshow
Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20150114
Summary: A simple portlet that displays a slideshow
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.portlet.slideshow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/intk/collective.portlet.slideshow.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2
BuildPreReq: python-module-PasteScript
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.interface

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore plone.i18n plone.app.form
%py_requires plone.app.vocabularies plone.memoize plone.app.portlets
%py_requires plone.portlets zope.i18nmessageid zope.formlib zope.schema
%py_requires zope.component zope.interface

%description
A simple portlet that displays a slideshow.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A simple portlet that displays a slideshow.

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
%python_sitelibdir/collective/portlet/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/portlet/*/tests

%files tests
%python_sitelibdir/collective/portlet/*/tests

%changelog
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150114
- Initial build for Sisyphus

