%define mname plone.mls
%define oname %mname.core
Name: python-module-%oname
Version: 0.6
Release: alt1.dev.git20140714
Summary: Plone support for the Propertyshelf MLS
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.mls.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/propertyshelf/plone.mls.core.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-httplib2 python-module-simplejson
BuildPreReq: python-module-plone.api python-module-openid
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.api plone.app.registry plone.directives.form
%py_requires Products.CMFPlone Products.CMFCore plone.registry
%py_requires plone.theme plone.browserlayer zope.component zope.schema
%py_requires zope.interface zope.annotation zope.globalrequest
%py_requires zope.i18nmessageid z3c.form

%description
Plone support for the Propertyshelf MLS.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
Plone support for the Propertyshelf MLS.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires plone

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/plone/mls/__init__.py \
	%buildroot%python_sitelibdir/plone/mls/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/plone/mls/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/mls/*/test*
%exclude %python_sitelibdir/plone/mls/__init__.py*

%files tests
%python_sitelibdir/plone/mls/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/plone/mls
%python_sitelibdir/plone/mls/__init__.py*

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.dev.git20140714
- Initial build for Sisyphus

