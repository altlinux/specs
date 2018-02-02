%define oname pytest-capturelog

%def_with python3

Name: python-module-%oname
Version: 0.7
Release: alt1.1.1
Summary: py.test plugin to capture log messages
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-capturelog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-py
%endif

%py_provides pytest_capturelog
%py_requires pytest

%description
py.test plugin to capture log messages.

%package -n python3-module-%oname
Summary: py.test plugin to capture log messages
Group: Development/Python3
%py3_provides pytest_capturelog
%py3_requires pytest

%description -n python3-module-%oname
py.test plugin to capture log messages.

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
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

