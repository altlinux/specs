%define oname repoze.filesafe
Name: python-module-%oname
Version: 2.0b2
Release: alt1.gi20110831
Summary: Transaction-aware file creation
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.filesafe
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.filesafe.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze transaction

%description
repoze.filesafe provides utilities methods to handle creation
of files on the filesystem safely by integrating with the ZODB package's
transaction manager.  It can be used in combination with repoze.tm (or
repoze.tm2) for use in WSGI environments.

%package tests
Summary: Tests for repoze.filesafe
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.filesafe provides utilities methods to handle creation
of files on the filesystem safely by integrating with the ZODB package's
transaction manager.  It can be used in combination with repoze.tm (or
repoze.tm2) for use in WSGI environments.

This package contains tests for repoze.filesafe.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0b2-alt1.gi20110831
- Version 2.0b2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.gi20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.gi20110322.1
- Added necessary requirements
- Excluded *.pth

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.gi20110322
- Initial build for Sisyphus

