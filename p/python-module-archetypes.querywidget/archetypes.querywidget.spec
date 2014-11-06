%define mname archetypes
%define oname %mname.querywidget
Name: python-module-%oname
Version: 1.1.3
Release: alt1.dev0.git20141105
Summary: Implements a widget for creating catalog queries for Archetypes
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/archetypes.querywidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/archetypes.querywidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.app.querystring
BuildPreReq: python-module-plone.app.jquery
BuildPreReq: python-module-plone.app.jquerytools
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.schema

%py_provides %oname
%py_requires %mname plone.app.querystring plone.app.jquery zope.site
%py_requires plone.app.jquerytools Products.Archetypes plone.registry
%py_requires zope.component zope.publisher zope.interface

%description
Archetypes.querywidget implements a widget for creating catalog queries
using an email-filtering-like interface, as found in GMail or Apple
Mail.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.collection plone.testing
%py_requires zope.configuration zope.schema

%description tests
Archetypes.querywidget implements a widget for creating catalog queries
using an email-filtering-like interface, as found in GMail or Apple
Mail.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/*/test*

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/test*

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.dev0.git20141105
- Initial build for Sisyphus

