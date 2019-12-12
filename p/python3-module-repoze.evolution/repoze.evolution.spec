%define oname repoze.evolution

Name: python3-module-%oname
Version: 0.6
Release: alt3

Summary: Version-number-controlled evolution for database changes
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/repoze.evolution/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires repoze zope.interface


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
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires transaction sphinx

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
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.6-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

