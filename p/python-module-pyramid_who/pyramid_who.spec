%define oname pyramid_who
Name: python-module-%oname
Version: 0.3
Release: alt1
Summary: Pyramid authentication policies based on repoze.who
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_who/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid repoze.who

%description
pyramid_who is an extension for the pyramid web framework, providing an
authentication policy based on the "new" repoze.who API, as found in
version 2.0 and greater.

%package tests
Summary: Tests for pyramid_who
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyramid_who is an extension for the pyramid web framework, providing an
authentication policy based on the "new" repoze.who API, as found in
version 2.0 and greater.

This package contains tests for pyramid_who.

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
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

