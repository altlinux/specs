%define mname eea
%define oname %mname.exhibit
Name: python-module-%oname
Version: 7.7
Release: alt1
Summary: EEA Exhibit provides Simile Widgets Exhibit JS libraries as Zope 3 resources
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.exhibit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-rdflib python-module-SPARQLWrapper
BuildPreReq: python-module-eea.app.visualization
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.app.visualization Products.CMFCore zope.formlib
%py_requires zope.interface zope.schema zope.component
%py_requires zope.i18nmessageid

%description
EEA Exhibit provides Simile Widgets Exhibit framework integration for
eea.app.visualization. See eea.daviz package for more details.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.PloneTestCase

%description tests
EEA Exhibit provides Simile Widgets Exhibit framework integration for
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
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.7-alt1
- Initial build for Sisyphus

