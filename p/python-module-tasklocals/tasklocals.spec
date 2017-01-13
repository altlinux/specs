%define _unpackaged_files_terminate_build 1
%define oname tasklocals

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1
Summary: Task locals support for tulip/asyncio
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tasklocals/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vkryachko/tasklocals.git
Source0: https://pypi.python.org/packages/06/38/c228770a8c8cfab3b99ec3d9b8d84dc9f0736c2e18a6642000789767a968/%{oname}-%{version}.tar.gz
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio-tests python-module-nose
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio-tests python3-module-nose
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-asyncio python3-module-pytest python3-module-setuptools
BuildRequires: python3-module-asyncio-tests python3-module-nose python3-module-setuptools-tests rpm-build-python3

%description
It provides Task local storage similar to python's threading.local
but for Tasks in asyncio.

%package -n python3-module-%oname
Summary: Task locals support for tulip/asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
It provides Task local storage similar to python's threading.local
but for Tasks in asyncio.

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
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20131205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20131205.1
- NMU: Use buildreq for BR.

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20131205
- Initial build for Sisyphus

