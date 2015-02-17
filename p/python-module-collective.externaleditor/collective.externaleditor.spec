%define mname collective
%define oname %mname.externaleditor
Name: python-module-%oname
Version: 1.0.1
Release: alt1
Summary: Specific Plone layer for Products.ExternalEditor
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.externaleditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.ExternalEditor
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-plone.app.controlpanel-tests
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.ExternalEditor Products.CMFPlone
%py_requires Products.CMFDefault Products.CMFCore Products.PythonScripts
%py_requires Products.statusmessages plone.app.controlpanel zope.schema
%py_requires zope.i18nmessageid zope.interface zope.formlib
%py_requires zope.component

%description
This package add a Control Panel to enable or disable external editor
(ext_editor property in Plone seems to be unused) and to choose on which
content types action will be available.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase plone.app.controlpanel.tests

%description tests
This package add a Control Panel to enable or disable external editor
(ext_editor property in Plone seems to be unused) and to choose on which
content types action will be available.

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
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

