%define mname collective.portlet
%define oname %mname.embed
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20131227
Summary: Embed an html snippet in a Plone portlet
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.portlet.embed/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.portlet.embed.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-selenium
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.portlet
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore plone.app.portlets plone.portlets
%py_requires plone.portlet plone.i18n zope.component zope.formlib
%py_requires zope.schema zope.interface zope.i18nmessageid z3c.form

%description
This addon provide a new portlet: Embed portlet.

This portlet let you copy / paste HTML code from services like facebook,
twitter, youtube and display the result in a portlet.

The portlet is based on the static portlet, so you have the same
options: omit borders, more url, ...

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework.testing selenium

%description tests
This addon provide a new portlet: Embed portlet.

This portlet let you copy / paste HTML code from services like facebook,
twitter, youtube and display the result in a portlet.

The portlet is based on the static portlet, so you have the same
options: omit borders, more url, ...

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
%python_sitelibdir/collective/portlet/embed
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/portlet/embed/test*

%files tests
%python_sitelibdir/collective/portlet/embed/test*

%changelog
* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20131227
- Initial build for Sisyphus

