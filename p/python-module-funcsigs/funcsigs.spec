%define _unpackaged_files_terminate_build 1
%define oname funcsigs

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.1
Summary: Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/funcsigs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aliles/funcsigs.git
Source0: https://pypi.python.org/packages/94/4a/db842e7a0545de1cdb0439bb80e6e42dfe82aaeaadd4072f2263a4fbed23/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-unittest2 python-module-coverage
BuildPreReq: python-module-flake8 python-module-wheel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-unittest2 python3-module-coverage
BuildPreReq: python3-module-flake8 python3-module-wheel
%endif

%py_provides %oname

%description
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6,
2.7 as well as 3.2 and up.

%package -n python3-module-%oname
Summary: Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6,
2.7 as well as 3.2 and up.

%prep
%setup -q -n %{oname}-%{version}

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
flake8 --exit-zero funcsigs tests
%if_with python3
pushd ../python3
python3 setup.py test
python3-flake8 --exit-zero funcsigs tests
popd
%endif

%files
%doc CHANGELOG *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20131220.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20131220
- Initial build for Sisyphus

