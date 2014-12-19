%define mname eea
%define oname %mname.daviz
Name: python-module-%oname
Version: 9.1
Release: alt1
Summary: The first semantic web data visualization tool for Zope/Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.daviz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.daviz.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mock python-module-uuid
BuildPreReq: python-module-eea.app.visualization
BuildPreReq: python-module-eea.dataservice
BuildPreReq: python-module-eea.relations
BuildPreReq: python-module-eea.forms
BuildPreReq: python-module-eea.exhibit
BuildPreReq: python-module-eea.googlecharts
BuildPreReq: python-module-eea.cache
BuildPreReq: python-module-eea.depiction
BuildPreReq: python-module-zc.dict
BuildPreReq: python-module-Products.DataGridField
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-eea.sparql

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.app.visualization eea.dataservice eea.relations
%py_requires eea.forms eea.exhibit eea.googlecharts eea.cache zc.dict
%py_requires eea.depiction Products.DataGridField Products.Archetypes
%py_requires Products.ATContentTypes Products.CMFCore zope.container
%py_requires Products.validation Products.contentmigration zope.event
%py_requires zope.component zope.interface zope.schema zope.annotation
%py_requires zope.formlib zope.i18nmessageid eea.sparql

%description
EEA DaViz is a plone product which uses Exhibit and Google Charts API to
easily create data visualizations based on data from csv/tsv, JSON,
SPARQL endpoints and more.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
EEA DaViz is a plone product which uses Exhibit and Google Charts API to
easily create data visualizations based on data from csv/tsv, JSON,
SPARQL endpoints and more.

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
%doc *.md *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.1-alt1
- Initial build for Sisyphus

