%define oname vstat

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20150101.1.1
Summary: Implementation of the v-statistic
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/vstat/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dostodabsi/vstat.py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-scipy python-module-nose
BuildPreReq: python-module-repoze.lru
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-scipy python3-module-nose
BuildPreReq: python3-module-repoze.lru
%endif

%py_provides %oname

%description
Implements the v-statistic, a measure that compares the estimation
accuracy of the ordinary least squares estimator against a random
benchmark.

%package -n python3-module-%oname
Summary: Implementation of the v-statistic
Group: Development/Python
%py3_provides %oname

%description -n python3-module-%oname
Implements the v-statistic, a measure that compares the estimation
accuracy of the ordinary least squares estimator against a random
benchmark.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.git20150101.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20150101.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150101
- Version 0.3

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20150101
- Initial build for Sisyphus

