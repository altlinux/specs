%define oname plone.app.querystring

Name: python-module-%oname
Version: 1.2.3
Release: alt2.dev0.git20140823
Summary: Queryparser, querybuilder and extra helper tools, to parse stored queries to actual results
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.querystring/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.querystring.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-plone.batching
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.vocabularies

%py_provides %oname
%py_requires zope.i18nmessageid zope.interface zope.publisher
%py_requires zope.component zope.dottedname zope.globalrequest
%py_requires plone.app.upgrade plone.batching plone.registry
%py_requires plone.app Products.CMFCore plone.app.registry zope.i18n
%py_requires zope.schema
%py_requires Products.CMFPlone plone.app.contentlisting plone.app.layout
%py_requires plone.app.vocabularies

%description
This package provides an queryparser, querybuilder and extra helper
tools, to parse stored queries to actual results, used in new style
collections. It includes a registry reader which reads operators, values
and criteria from the Plone registry.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package provides an queryparser, querybuilder and extra helper
tools, to parse stored queries to actual results, used in new style
collections. It includes a registry reader which reads operators, values
and criteria from the Plone registry.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2.dev0.git20140823
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.dev0.git20140823
- Initial build for Sisyphus

