%define oname repoze.filecat
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: A file catalog with an HTTP frontend
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.filecat/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze repoze.bfg xappy lxml ore.xapian jsonlib docutils

%description
This package provides application support for indexing and serving
content in a file system.

An HTTP API is available for querying operations.

%package tests
Summary: Tests for repoze.filecat
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides application support for indexing and serving
content in a file system.

An HTTP API is available for querying operations.

This package contains tests for repoze.filecat.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

