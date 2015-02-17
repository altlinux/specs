%define mname collective
%define oname %mname.elasticindex
Name: python-module-%oname
Version: 1.2.4
Release: alt1.dev0.git20150203
Summary: Index Plone content in Elastic Search
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.elasticindex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/infrae/collective.elasticindex.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Acquisition python-module-pyes
BuildPreReq: python-module-transaction python-module-mock
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
%py_requires %mname Acquisition Products.CMFCore Products.CMFPlone pyes
%py_requires Products.statusmessages plone.app.controlpanel transaction
%py_requires plone.app.portlets plone.portlets zope.component
%py_requires zope.formlib zope.i18nmessageid zope.interface zope.schema
%py_requires zope.traversing

%description
This extension index Plone content into ElasticSearch. This doesn't
replace the Plone catalog with ElasticSearch, nor interact with the
Plone catalog at all, it merely index content inside ElasticSearch when
it is modified or published.

In addition to this, it provides a simple search page called search.html
that queries ElasticSearch using Javascript (so Plone is not involved in
searching) and propose the same features than the default Plone search
page. A search portlet let you redirect people to this new search page
as well.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase mock

%description tests
This extension index Plone content into ElasticSearch. This doesn't
replace the Plone catalog with ElasticSearch, nor interact with the
Plone catalog at all, it merely index content inside ElasticSearch when
it is modified or published.

In addition to this, it provides a simple search page called search.html
that queries ElasticSearch using Javascript (so Plone is not involved in
searching) and propose the same features than the default Plone search
page. A search portlet let you redirect people to this new search page
as well.

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
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.dev0.git20150203
- Initial build for Sisyphus

