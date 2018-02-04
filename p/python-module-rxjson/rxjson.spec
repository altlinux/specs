%define oname rxjson

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.dev.git20130212.1.1
Summary: JSON RX Schema validation tool
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/rxjson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/spiral-project/rxjson.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-d2to1 python-modules-json
BuildPreReq: python-module-TAP python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-d2to1 python3-module-TAP python3-module-nose
%endif

%py_provides %oname

%description
rxjson is a python package that helps you validate your generated JSON
against a standardized json schema directly in your python app.

%package -n python3-module-%oname
Summary: JSON RX Schema validation tool
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
rxjson is a python package that helps you validate your generated JSON
against a standardized json schema directly in your python app.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
export PYTHONPATH=$PWD
pushd tests
nosetests
popd
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
pushd tests
nosetests3
popd
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.dev.git20130212.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.dev.git20130212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20130212
- Initial build for Sisyphus

