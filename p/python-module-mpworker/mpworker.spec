%define oname mpworker

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2
Release: alt1.git20150205.1
Summary: Easy to use asyncio compatible package for stateful multiprocessing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mpworker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dustyrockpyle/mpworker.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio
#BuildPreReq: python-modules-multiprocessing
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio multiprocessing

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base
BuildRequires: rpm-build-python3 python3-module-pytest

%description
Easy to use stateful multiprocessing. Asyncio compatible.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Easy to use stateful multiprocessing. Asyncio compatible.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Easy to use asyncio compatible package for stateful multiprocessing
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio multiprocessing

%description -n python3-module-%oname
Easy to use stateful multiprocessing. Asyncio compatible.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Easy to use stateful multiprocessing. Asyncio compatible.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
py.test -vv mpworker/*.py
%endif
%if_with python3
pushd ../python3
py.test-%_python3_version -vv mpworker/*.py
popd
%endif

%if_with python2
%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150205
- Initial build for Sisyphus

