%define oname chameleon
Name: python-module-%oname.genshi
Version: 1.0.b4
Release: alt1.bzr20090728.1
Summary: Genshi template engine based on Chameleon
License: BSD
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:chameleon.genshi
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
This package provides a fast Genshi template implementation based on
the Chameleon template compiler. It's largely compatible with
``genshi.template``.

%package tests
Summary: Tests for Genshi template engine based on Chameleon
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a fast Genshi template implementation based on
the Chameleon template compiler. It's largely compatible with
``genshi.template``.

This package contains tests for Genshi template engine based on
Chameleon.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/*/tests

%files tests
%python_sitelibdir/%oname/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.b4-alt1.bzr20090728.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.b4-alt1.bzr20090728
- Initial build for Sisyphus

