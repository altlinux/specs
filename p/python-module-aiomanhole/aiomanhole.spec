%define oname aiomanhole

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: Python module to provide a manhole in asyncio applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiomanhole/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nathan-hoad/aiomanhole.git
Source0: https://pypi.python.org/packages/21/da/fc81b74d5e7dda932dd2742b5cb595a9cf34708524c9261b993353795cdc/aiomanhole-%{version}.tar.gz
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python3-module-asyncio python3-module-pytest rpm-build-python3 time

%description
Manhole for accessing asyncio applications. This is useful for debugging
application state in situations where you have access to the process,
but need to access internal application state.

%package -n python3-module-%oname
Summary: Python module to provide a manhole in asyncio applications
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
Manhole for accessing asyncio applications. This is useful for debugging
application state in situations where you have access to the process,
but need to access internal application state.

%prep
%setup -q -n aiomanhole-%{version}

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
py.test -vv
%endif
%if_with python3
pushd ../python3
py.test-%_python3_version -vv
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20140914.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1.git20140914.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140914
- Initial build for Sisyphus

