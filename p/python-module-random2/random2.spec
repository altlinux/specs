%define oname random2

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.dev0.git20130315.1.1
Summary: Python 3 compatible Python 2 `random` Module
License: PSFL
Group: Development/Python
Url: https://pypi.python.org/pypi/random2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/strichter/random2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Python 3 compatible Python 2 `random` Module.

%package -n python3-module-%oname
Summary: Python 3 compatible Python 2 `random` Module
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python 3 compatible Python 2 `random` Module.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.dev0.git20130315.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.dev0.git20130315.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.dev0.git20130315
- Initial build for Sisyphus

