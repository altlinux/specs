%define oname repoze.evolution
Name: python-module-%oname
Version: 0.3
Release: alt2.1
Summary: Version-number-controlled evolution for database changes
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.evolution/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze zope.interface

%description
`repoze.evolution` is a package which allows you to keep
persistent data structures (data in a relational database, on the
filesystem, in a persistent object store, etc) in sync with changes
made to software.  It does so by allowing you to create and use a
package full of monotonically named ``evolve`` scripts which modify
the data; each script brings the data up to some standard of a
software version.  It includes a "manager" implementation for ZODB,
and an interface which allows you to implement different types of
managers for different persistent data stores.

%package tests
Summary: Tests for repoze.evolution
Group: Development/Python
Requires: %name = %version-%release
%py_requires transaction sphinx

%description tests
`repoze.evolution` is a package which allows you to keep
persistent data structures (data in a relational database, on the
filesystem, in a persistent object store, etc) in sync with changes
made to software.  It does so by allowing you to create and use a
package full of monotonically named ``evolve`` scripts which modify
the data; each script brings the data up to some standard of a
software version.  It includes a "manager" implementation for ZODB,
and an interface which allows you to implement different types of
managers for different persistent data stores.

This package contains tests for repoze.evolution.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

