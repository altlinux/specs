%define oname repoze.depinj
Name: python-module-%oname
Version: 0.3
Release: alt1.1
Summary: Small dependency injection framework for unit testing
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.depinj/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze

%description
A dependency injection framework for unit testing.

%package tests
Summary: Tests for repoze.depinj
Group: Development/Python
Requires: %name = %version-%release

%description tests
A dependency injection framework for unit testing.

This package contains tests for repoze.depinj.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

