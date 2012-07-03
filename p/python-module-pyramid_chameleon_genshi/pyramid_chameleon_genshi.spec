%define oname pyramid_chameleon_genshi
Name: python-module-%oname
Version: 0.6
Release: alt1.1
Summary: chameleon.genshi template bindings for the Pyramid web framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_chameleon_genshi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid chameleon

%description
Bindings for Chameleon Genshi-style templating support under Pyramid.

%package tests
Summary: Tests for pyramid_chameleon_genshi
Group: Development/Python
Requires: %name = %version-%release

%description tests
Bindings for Chameleon Genshi-style templating support under Pyramid.

This package contains tests for pyramid_chameleon_genshi.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

