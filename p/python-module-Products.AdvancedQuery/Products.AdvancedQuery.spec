%define oname Products.AdvancedQuery
Name: python-module-%oname
Version: 3.0.3
Release: alt1
Summary: Flexible high level search construction and execution
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.AdvancedQuery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.ZCatalog Products.CMFCore

%description
AdvancedQuery is a Zope product aimed to overcome several limitations
and bugs of ZCatalog's native search function.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
AdvancedQuery is a Zope product aimed to overcome several limitations
and bugs of ZCatalog's native search function.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Initial build for Sisyphus

