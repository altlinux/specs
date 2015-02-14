%define mname ftw
%define oname %mname.testbrowser
Name: python-module-%oname
Version: 1.14.6
Release: alt1.dev0.git20150130
Summary: A test browser for Zope and Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.testbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.testbrowser.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-lxml
BuildPreReq: python-module-mechanize python-module-requests
BuildPreReq: python-module-unittest2 python-module-cssselect
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-ftw.builder
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.formwidget.autocomplete
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formwidget.query
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.testbrowser

%py_provides %oname
%py_requires %mname plone.testing zope.component zope.deprecation
%py_requires zope.interface plone.app.testing zope.testbrowser.testing

%description
ftw.testbrowser is a browser library for testing Plone web sites and
applications. It integrations directly into Plone / Zope and uses lxml
for parsing and querying pages. It supports all the basic features such
as filling forms.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.CMFCore Products.statusmessages ftw.builder
%py_requires plone.app.contenttypes plone.formwidget.autocomplete
%py_requires plone.formwidget.contenttree plone.z3cform z3c.form
%py_requires z3c.formwidget.query zope.configuration zope.publisher
%py_requires zope.schema

%description tests
ftw.testbrowser is a browser library for testing Plone web sites and
applications. It integrations directly into Plone / Zope and uses lxml
for parsing and querying pages. It supports all the basic features such
as filling forms.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
ftw.testbrowser is a browser library for testing Plone web sites and
applications. It integrations directly into Plone / Zope and uses lxml
for parsing and querying pages. It supports all the basic features such
as filling forms.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
ftw.testbrowser is a browser library for testing Plone web sites and
applications. It integrations directly into Plone / Zope and uses lxml
for parsing and querying pages. It supports all the basic features such
as filling forms.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export PYTHONPATH=$PWD
%make pickle
%make html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.rst docs/*.txt
%dir %python_sitelibdir/%oname
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/html/*

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.6-alt1.dev0.git20150130
- Version 1.14.6.dev0

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.5-alt1.dev0.git20141107
- Initial build for Sisyphus

