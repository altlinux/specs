%define mname collective
%define oname %mname.dexteritytextindexer
Name: python-module-%oname
Version: 2.0.2
Release: alt1.dev0.git20141107
Summary: Dynamic SearchableText index for dexterity content types
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.dexteritytextindexer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.dexteritytextindexer.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 python-module-elementtree
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.directives.form

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname ZODB3 zope.interface zope.schema zope.component
%py_requires zope.deferredimport z3c.form plone.indexer plone.behavior
%py_requires plone.dexterity plone.app.dexterity plone.supermodel
%py_requires plone.z3cform Products.CMFCore plone.namedfile

%description
collective.dexteritytextindexer provides a dynamic SearchableText
indexer for dexterity content types. It makes it possible to index
fields of multiple behaviors as SearchableText.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.configuration plone.testing plone.app.testing
%py_requires plone.autoform plone.directives.form

%description tests
collective.dexteritytextindexer provides a dynamic SearchableText
indexer for dexterity content types. It makes it possible to index
fields of multiple behaviors as SearchableText.

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
rm -fR build
py.test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.dev0.git20141107
- Initial build for Sisyphus

