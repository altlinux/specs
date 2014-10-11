%define oname Products.PluginRegistry
Name: python-module-%oname
Version: 1.3
Release: alt1
Summary: Configure application plugins based on interfaces
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PluginRegistry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.GenericSetup python-module-docutils

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.GenericSetup

%description
Products.PluginRegistry offers a simple persistent registry which allows
the site manager to registe components for specific interfaces, and to
order them.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Products.PluginRegistry offers a simple persistent registry which allows
the site manager to registe components for specific interfaces, and to
order them.

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

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

