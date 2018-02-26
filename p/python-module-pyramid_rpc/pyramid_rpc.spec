%define oname pyramid_rpc
Name: python-module-%oname
Version: 0.3
Release: alt1
Summary: RPC support for the Pyramid web framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_rpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid

%description
pyramid_rpc is a package of RPC related add-on's to make it easier to
create RPC services.

%package tests
Summary: Tests for pyramid_rpc
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyramid_rpc is a package of RPC related add-on's to make it easier to
create RPC services.

This package contains tests for pyramid_rpc.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

