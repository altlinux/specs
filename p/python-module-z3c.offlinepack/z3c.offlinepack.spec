%define oname z3c.offlinepack

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.1
Summary: Pack ZODB databases without running Zope or ZEO
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.offlinepack/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires ZODB3 zope.dottedname

%description
Pack a ZODB storage without running any part of the Zope application
server. Only an appropriate version of ZODB3 for the ZODB storage is
required. Apply only to copies of ZODB storages, not ZODB storages
currently in use.

%package -n python3-module-%oname
Summary: Pack ZODB databases without running Zope or ZEO
Group: Development/Python3
%py3_requires ZODB3 zope.dottedname

%description -n python3-module-%oname
Pack a ZODB storage without running any part of the Zope application
server. Only an appropriate version of ZODB3 for the ZODB storage is
required. Apply only to copies of ZODB storages, not ZODB storages
currently in use.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.offlinepack
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zc.buildout zc.recipe.egg

%description -n python3-module-%oname-tests
Pack a ZODB storage without running any part of the Zope application
server. Only an appropriate version of ZODB3 for the ZODB storage is
required. Apply only to copies of ZODB storages, not ZODB storages
currently in use.

This package contains tests for z3c.offlinepack.

%package tests
Summary: Tests for z3c.offlinepack
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.buildout zc.recipe.egg

%description tests
Pack a ZODB storage without running any part of the Zope application
server. Only an appropriate version of ZODB3 for the ZODB storage is
required. Apply only to copies of ZODB storages, not ZODB storages
currently in use.

This package contains tests for z3c.offlinepack.

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
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

