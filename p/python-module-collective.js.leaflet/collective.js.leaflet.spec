%define mname collective
%define oname %mname.js.leaflet
Name: python-module-%oname
Version: 0.7.1
Release: alt1.dev0.git20141222
Summary: Leaflet maps integration for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.leaflet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.leaflet.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-openid
BuildPreReq: python-module-Plone python-module-Products.CMFPlone
BuildPreReq: python-module-z3c.autoinclude
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-plone.reload
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.traversing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname.js z3c.autoinclude Plone Products.ResourceRegistries
%py_requires Products.CMFPlone Products.CMFQuickInstallerTool
%py_requires plone.reload plone.theme zope.component zope.publisher
%py_requires zope.i18nmessageid zope.interface

%description
Enrich your Plone site with the power of Leaflet maps. Leaflet version
of this package is 0.7.3.

This addon registers the Leaflet base Javascript and CSS resources and
optionally some interesting Leaflet plugins.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.annotation zope.traversing

%description tests
Enrich your Plone site with the power of Leaflet maps. Leaflet version
of this package is 0.7.3.

This addon registers the Leaflet base Javascript and CSS resources and
optionally some interesting Leaflet plugins.

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
%python_sitelibdir/%mname/js/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/js/*/test*
%exclude %python_sitelibdir/%mname/js/*/*/*/*/*/tests
%exclude %python_sitelibdir/%mname/js/*/*/*/*/example*

%files tests
%python_sitelibdir/%mname/js/*/test*
%python_sitelibdir/%mname/js/*/*/*/*/*/tests
%python_sitelibdir/%mname/js/*/*/*/*/example*

%changelog
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.dev0.git20141222
- Initial build for Sisyphus

