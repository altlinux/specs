%define oname repoze.evolution

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt2.1
Summary: Version-number-controlled evolution for database changes
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.evolution/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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

%package -n python3-module-%oname
Summary: Version-number-controlled evolution for database changes
Group: Development/Python3
%py3_requires repoze zope.interface

%description -n python3-module-%oname
`repoze.evolution` is a package which allows you to keep
persistent data structures (data in a relational database, on the
filesystem, in a persistent object store, etc) in sync with changes
made to software.  It does so by allowing you to create and use a
package full of monotonically named ``evolve`` scripts which modify
the data; each script brings the data up to some standard of a
software version.  It includes a "manager" implementation for ZODB,
and an interface which allows you to implement different types of
managers for different persistent data stores.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.evolution
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires transaction sphinx

%description -n python3-module-%oname-tests
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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
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

