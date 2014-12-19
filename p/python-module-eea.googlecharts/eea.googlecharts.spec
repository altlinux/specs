%define mname eea
%define oname %mname.googlecharts
Name: python-module-%oname
Version: 11.9
Release: alt1
Summary: Configurator for GoogleCharts
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.googlecharts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-lxml
BuildPreReq: python-module-eea.converter
BuildPreReq: python-module-eea.app.visualization
BuildPreReq: python-module-eea.icons
BuildPreReq: python-module-collective.js.underscore
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-eea.cache
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.converter eea.app.visualization eea.icons
%py_requires collective.js.underscore eea.cache Products.CMFCore
%py_requires zope.container zope.formlib zope.component zope.interface
%py_requires zope.schema zope.publisher zope.browserpage zope.event
%py_requires zope.security zope.i18nmessageid

%description
EEA Google Charts provides Google Charts framework integration for
eea.app.visualization. See eea.daviz package for more details.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
EEA Google Charts provides Google Charts framework integration for
eea.app.visualization. See eea.daviz package for more details.

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

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.9-alt1
- Initial build for Sisyphus

