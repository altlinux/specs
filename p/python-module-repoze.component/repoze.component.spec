%define oname repoze.component
Name: python-module-%oname
Version: 0.4
Release: alt1.git20110222.1.1
Summary: A Python component system
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.component
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.component.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze repoze.lru

%description
``repoze.component`` is a package that software developers can use to
provide configurability and pluggability to their applications.
``repoze.component`` provides a generalized indirection mechanism
which can be used to provide plugin points to integrators or other
developers who may wish to provide alternate implementations of
application logic or configuration values.

%package tests
Summary: Tests for repoze.component
Group: Development/Python
Requires: %name = %version-%release

%description tests
``repoze.component`` is a package that software developers can use to
provide configurability and pluggability to their applications.
``repoze.component`` provides a generalized indirection mechanism
which can be used to provide plugin points to integrators or other
developers who may wish to provide alternate implementations of
application logic or configuration values.

This package contains tests for repoze.component.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110222
- Initial build for Sisyphus

