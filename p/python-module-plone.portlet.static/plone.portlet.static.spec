%define mname plone.portlet
%define oname %mname.static

Name: python-module-%oname
Version: 3.0.1
Release: alt2.dev0.git20141009
Summary: A simple static HTML portlet for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.portlet.static/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.portlet.static.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.portlets plone.app.portlets plone.i18n
%py_requires plone.app.textfield zope.component zope.i18nmessageid
%py_requires zope.interface zope.schema

%description
A simple static HTML portlet for Plone 3 and up.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
A simple static HTML portlet for Plone 3 and up.

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
%python_sitelibdir/plone/portlet/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/portlet/*/test*

%files tests
%python_sitelibdir/plone/portlet/*/test*

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt2.dev0.git20141009
- Enabled testing

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.dev0.git20141009
- Initial build for Sisyphus

