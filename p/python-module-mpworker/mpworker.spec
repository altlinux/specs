%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname mpworker

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3
Release: alt1
Summary: Easy to use asyncio compatible package for stateful multiprocessing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mpworker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dustyrockpyle/mpworker.git
Source0: https://pypi.python.org/packages/91/56/4d5462a80b9b8b424b5833de8adabd51f88ad709a78739b7f695417c8b54/%{oname}-%{version}.zip
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
%setup -q -n %{oname}-%{version}

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
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*
%endif

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150205
- Initial build for Sisyphus

