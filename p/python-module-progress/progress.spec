%define oname progress

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt1.git20131128.1.1
Summary: Easy to use progress bars
License: ISC
Group: Development/Python
Url: https://pypi.python.org/pypi/progress
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/verigak/progress.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Easy progress reporting for Python.

There are 6 progress bars to choose from:
* Bar
* ChargingBar
* FillingSquaresBar
* FillingCirclesBar
* IncrementalBar
* ShadyBar

%if_with python3
%package -n python3-module-%oname
Summary: Easy to use progress bars
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Easy progress reporting for Python.

There are 6 progress bars to choose from:
* Bar
* ChargingBar
* FillingSquaresBar
* FillingCirclesBar
* IncrementalBar
* ShadyBar
%endif

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
export LC_ALL=en_US.UTF-8
python setup.py test -v
python test_progress.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 test_progress.py -v
popd
%endif

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2-alt1.git20131128.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt1.git20131128.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20131128
- Initial build for Sisyphus

