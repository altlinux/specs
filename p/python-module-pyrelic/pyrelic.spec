%define oname pyrelic

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt1.git20150520
Summary: Python API Wrapper for NewRelic API
License: MIT / GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pyrelic
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/andrewgross/pyrelic.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-requests
BuildPreReq: python-module-mock python-module-sure
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-httpretty
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-requests
BuildPreReq: python3-module-mock python3-module-sure
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-httpretty
%endif

%py_provides %oname
%py_requires six requests

%description
A New Relic client library written in Python.

%if_with python3
%package -n python3-module-%oname
Summary: Python API Wrapper for NewRelic API
Group: Development/Python3
%py3_provides %oname
%py3_requires six requests

%description -n python3-module-%oname
A New Relic client library written in Python.
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
python setup.py test -v
#make run_test suite=unit
%make run_test suite=fixtures
%if_with python3
pushd ../python3
python3 setup.py test -v
#make run_test suite=unit NOSETESTS=nosetests3
%make run_test suite=fixtures NOSETESTS=nosetests3
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20150520
- Initial build for Sisyphus

