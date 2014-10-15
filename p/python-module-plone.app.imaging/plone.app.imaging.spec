%define oname plone.app.imaging

Name: python-module-%oname
Version: 1.1.2
Release: alt2.dev0.git20140903
Summary: User-configurable, blob-aware image scaling for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.imaging/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.imaging.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.caching
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.scale
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.ATContentTypes

%py_provides %oname
Requires: python-module-plone.app = %EVR
Requires: python-module-Zope2
%py_requires z3c.caching five.globalrequest
%py_requires plone.app.controlpanel plone.scale Products.Archetypes

%description
This package tries to factor out and re-use the image scaling code from
Archetypes into a separate package in order to make it user-configurable
and add support for storing the image data into ZODB blobs.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.ATContentTypes

%description tests
This package tries to factor out and re-use the image scaling code from
Archetypes into a separate package in order to make it user-configurable
and add support for storing the image data into ZODB blobs.

This packag contains tests for %oname.

%package -n python-module-plone.app
Summary: Core files of plone.app
Group: Development/Python
%py_requires plone

%description -n python-module-plone.app
Core files of plone.app.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/plone/app/__init__.py \
	%buildroot%python_sitelibdir/plone/app/

%check
python setup.py test

%files
%doc *.txt *.rst docs/*
%python_sitelibdir/plone/app/*
%exclude %python_sitelibdir/plone/app/__init__.py*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%files -n python-module-plone.app
%dir %python_sitelibdir/plone/app
%python_sitelibdir/plone/app/__init__.py*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2.dev0.git20140903
- Added necessary requirements
- Enabled testing

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.dev0.git20140903
- Initial build for Sisyphus

