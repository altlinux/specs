%define mname eea
%define oname %mname.sparql
Name: python-module-%oname
Version: 3.8
Release: alt2
Summary: Wrapper for Products.ZSPARQLMethod
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.sparql/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mock python-module-uuid
BuildPreReq: python-module-Products.ZSPARQLMethod
BuildPreReq: python-module-Products.DataGridField
BuildPreReq: python-module-eea.versions
BuildPreReq: python-module-plone.app.async
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-eea.cache
BuildPreReq: python-module-eea.app.visualization
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-eea.daviz

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.ZSPARQLMethod Products.DataGridField
%py_requires eea.versions plone.app.async eea.cache Products.CMFCore
%py_requires eea.app.visualization Products.Archetypes zope.component
%py_requires Products.CMFEditions Products.ATContentTypes zope.interface
%py_requires zope.event zope.i18nmessageid
%py_requires eea.daviz

%description
EEA Sparql is a plone product for fetching data from Linked open data
servers (sparql endpoints).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.PloneTestCase

%description tests
EEA Sparql is a plone product for fetching data from Linked open data
servers (sparql endpoints).

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
%doc *.md *.rst *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/*/test*

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/test*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt2
- Added necessary requirements

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8-alt1
- Initial build for Sisyphus

