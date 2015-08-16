%define oname urllib3-mock

%def_with python3

Name: python-module-%oname
Version: 0.3.3
Release: alt1.git20150417
Summary: A utility library for mocking out the `urllib3` Python library
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/urllib3-mock
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/florentx/urllib3-mock.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-module-pytest-cov
BuildPreReq: python-module-flake8 python-module-requests
BuildPreReq: python-module-urllib3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-pytest-cov
BuildPreReq: python3-module-flake8 python3-module-requests
BuildPreReq: python3-module-urllib3
%endif

%py_provides urllib3_mock
%py_requires urllib3

%description
A utility library for mocking out the urllib3 Python library.

%if_with python3
%package -n python3-module-%oname
Summary: A utility library for mocking out the `urllib3` Python library
Group: Development/Python3
%py3_provides urllib3_mock
%py3_requires urllib3

%description -n python3-module-%oname
A utility library for mocking out the urllib3 Python library.
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
py.test -vv . --cov urllib3_mock --cov-report term-missing
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv . --cov urllib3_mock \
	--cov-report term-missing
popd
%endif

%files
%doc CHANGES *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20150417
- Initial build for Sisyphus

