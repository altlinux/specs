%define oname repoze.zodbconn
Name: python-module-%oname
Version: 0.13
Release: alt1.git20110722
Summary: Open databases from URI specifications
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.zodbconn
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.zodbconn.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze ZODB3 ZConfig

%description
A library which allows ZODB databases to be constructed from URI
specifications.

%package tests
Summary: Tests for repoze.zodbconn
Group: Development/Python
Requires: %name = %version-%release

%description tests
A library which allows ZODB databases to be constructed from URI
specifications.

This package contains tests for repoze.zodbconn.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110722
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13-alt1.git20110604.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110604.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20110604
- Initial build for Sisyphus

