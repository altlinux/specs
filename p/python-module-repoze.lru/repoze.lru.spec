%define oname repoze.lru

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.git20120324
Summary: Tiny LRU cache
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.lru
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.lru.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%py_requires repoze

%description
``repoze.lru`` is a LRU (least recently used) cache implementation.
Keys and values that are not used frequently will be evicted from the
cache faster than keys and values that are used frequently.

%if_with python3
%package -n python3-module-%oname
Summary: Tiny LRU cache (Python 3)
Group: Development/Python3
%py3_requires repoze

%description -n python3-module-%oname
``repoze.lru`` is a LRU (least recently used) cache implementation.
Keys and values that are not used frequently will be evicted from the
cache faster than keys and values that are used frequently.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.lru (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
``repoze.lru`` is a LRU (least recently used) cache implementation.
Keys and values that are not used frequently will be evicted from the
cache faster than keys and values that are used frequently.

This package contains tests for repoze.lru.
%endif

%package tests
Summary: Tests for repoze.lru
Group: Development/Python
Requires: %name = %version-%release

%description tests
``repoze.lru`` is a LRU (least recently used) cache implementation.
Keys and values that are not used frequently will be evicted from the
cache faster than keys and values that are used frequently.

This package contains tests for repoze.lru.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/__pycache__/tests*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/__pycache__/tests*
%endif

%changelog
* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20120324
- Version 0.5
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110904
- Version 0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110225.1
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110225
- Initial build for Sisyphus

