%define oname plone.app.i18n
Name: python-module-%oname
Version: 2.0.3
Release: alt1.dev0.git20140823
Summary: Plone specific i18n extensions
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.i18n/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.i18n.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires plone.app

%description
Plone integration, views and persistence of plone.i18n.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
Plone integration, views and persistence of plone.i18n.

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
%exclude %python_sitelibdir/plone/app/*/*/tests
%exclude %python_sitelibdir/plone/app/*/*/*/tests.*

%files tests
%python_sitelibdir/plone/app/*/*/tests
%python_sitelibdir/plone/app/*/*/*/tests.*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.dev0.git20140823
- Initial build for Sisyphus

