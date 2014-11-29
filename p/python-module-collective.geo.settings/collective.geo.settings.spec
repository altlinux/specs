%define mname collective
%define oname %mname.geo.settings
Name: python-module-%oname
Version: 3.1
Release: alt1.dev0.git20141110
Summary: Provides some utility to store settings of collective.geo packages
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geo.settings/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geo.settings.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.publisher

%py_provides %oname
Requires: python-module-%mname.geo = %EVR
%py_requires Products.CMFCore plone.app.registry plone.app.z3cform
%py_requires plone.app.controlpanel plone.registry plone.dexterity
%py_requires plone.app.vocabularies zope.interface zope.component
%py_requires zope.schema zope.i18nmessageid zope.site zope.i18n
%py_requires z3c.form

%description
collective.geo.settings provides some utility to store settings of
collective.geo packages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.publisher

%description tests
collective.geo.settings provides some utility to store settings of
collective.geo packages.

This package contains tests for %oname.

%package -n python-module-%mname.geo
Summary: Core files of %mname.geo
Group: Development/Python
%py_provides %mname.geo
%py_requires %mname

%description -n python-module-%mname.geo
Core files of %mname.geo.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/%mname/geo/__init__.py \
	%buildroot%python_sitelibdir/%mname/geo/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/geo/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/geo/*/test*
%exclude %python_sitelibdir/%mname/geo/__init__.py*

%files tests
%python_sitelibdir/%mname/geo/*/test*

%files -n python-module-%mname.geo
%dir %python_sitelibdir/%mname/geo
%python_sitelibdir/%mname/geo/__init__.py*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1.dev0.git20141110
- Initial build for Sisyphus

