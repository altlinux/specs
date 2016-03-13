%define oname repoze.tm

%def_with python3

Name: python-module-%oname
Version: 1.0a5
Release: alt4.1
Summary: Zope-like transaction manager via WSGI middleware
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.tm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze ZODB3
Conflicts: python-module-repoze.tm2

%description
Middleware which uses the ZODB transaction manager to wrap a call to its
pipeline children inside a transaction.

%package -n python3-module-%oname
Summary: Zope-like transaction manager via WSGI middleware
Group: Development/Python3
%py3_requires repoze ZODB3
Conflicts: python3-module-repoze.tm2

%description -n python3-module-%oname
Middleware which uses the ZODB transaction manager to wrap a call to its
pipeline children inside a transaction.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.tm
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Conflicts: python3-module-repoze.tm2-tests

%description -n python3-module-%oname-tests
Middleware which uses the ZODB transaction manager to wrap a call to its
pipeline children inside a transaction.

This package contains tests for repoze.tm.

%package tests
Summary: Tests for repoze.tm
Group: Development/Python
Requires: %name = %version-%release
Conflicts: python-module-repoze.tm2-tests

%description tests
Middleware which uses the ZODB transaction manager to wrap a call to its
pipeline children inside a transaction.

This package contains tests for repoze.tm.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0a5-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a5-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0a5-alt3.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a5-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a5-alt2
- Added explicit conflict with python-module-repoze.tm2

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a5-alt1
- Initial build for Sisyphus

