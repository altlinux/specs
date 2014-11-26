%define mname ps.plone
%define oname %mname.fotorama
Name: python-module-%oname
Version: 4.6.3
Release: alt1.dev.git20141124
Summary: Fotorama slideshow for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ps.plone.fotorama
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/propertyshelf/ps.plone.fotorama.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-openid
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-robotframework-selenium2screenshots
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.api zope.i18nmessageid zope.interface

%description
Fotorama slideshow for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework.testing plone.app.testing
%py_requires plone.browserlayer zope.configuration

%description tests
Fotorama slideshow for Plone.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files for %mname
Group: Development/Python
%py_provides %mname
%py_requires ps

%description -n python-module-%mname
Core files for %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/ps/plone/__init__.py \
	%buildroot%python_sitelibdir/ps/plone/

%check
python setup.py test

%files
%doc *.rst docs/source/*.rst
%python_sitelibdir/ps/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ps/plone/*/test*
%exclude %python_sitelibdir/ps/plone/__init__.py*

%files tests
%python_sitelibdir/ps/plone/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/ps/plone
%python_sitelibdir/ps/plone/__init__.py*

%changelog
* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.3-alt1.dev.git20141124
- New snapshot

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6.3-alt1.dev.git20141121
- Initial build for Sisyphus

