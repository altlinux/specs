%define oname aioawait

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 8
Release: alt1
Summary: Call asynchronous functions of asyncio infrastructure from synchronous code
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aioawait/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/carlopires/aioawait.git
Source0: https://pypi.python.org/packages/59/74/947%{version}068823434e5b2302a91e307f340d9fa7cfc79c76814506e9991301f7/%{oname}-8.tar.gz
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
# optimized out: python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python3-module-asyncio python3-module-setuptools-tests rpm-build-python3

%description
This package implements two primitives (await and spawn) on top of
asyncio infrastructure of Python 3. This two functions allow us to call
asynchronous functions from synchronous code.

%package -n python3-module-%oname
Summary: Call asynchronous functions of asyncio infrastructure from synchronous code
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
This package implements two primitives (await and spawn) on top of
asyncio infrastructure of Python 3. This two functions allow us to call
asynchronous functions from synchronous code.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
pushd ../python3
popd
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
python setup.py test
python -m unittest %oname
%endif
%if_with python3
pushd ../python3
python3 setup.py test
python3 -m unittest %oname
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
* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 7-alt1.git20140918.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 7-alt1.git20140918.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7-alt1.git20140918
- Initial build for Sisyphus

