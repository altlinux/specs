%define oname plone.alterego
Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20140826
Summary: Low level support for dynamic modules
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.alterego/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.alterego.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
%py_requires plone

%description
This package defines a dynamic module type that lets you create objects
in the dynamic module on demand.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package defines a dynamic module type that lets you create objects
in the dynamic module on demand.

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
%doc *.txt docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20140826
- Initial build for Sisyphus

