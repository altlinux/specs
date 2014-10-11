%define oname Products.PluggableAuthService
Name: python-module-%oname
Version: 1.10.0
Release: alt1
Summary: Pluggable Zope2 authentication / authorization framework
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PluggableAuthService/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PluginRegistry
BuildPreReq: python-module-docutils

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.GenericSetup Products.PluginRegistry

%description
This product defines a fully-pluggable user folder, intended for use in
all Zope2 sites.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This product defines a fully-pluggable user folder, intended for use in
all Zope2 sites.

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
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/*/*/tests

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/*/tests

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt1
- Initial build for Sisyphus

