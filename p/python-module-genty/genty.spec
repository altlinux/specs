%define oname genty

%def_with python3

Name: python-module-%oname
Version: 1.2.0
Release: alt1.git20150223
Summary: Allows you to run a test with multiple data sets
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/genty/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/box/genty.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-coveralls
BuildPreReq: python-module-mock python-tools-pep8
BuildPreReq: python-module-tox pylint
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-coveralls
BuildPreReq: python3-module-mock python3-tools-pep8
BuildPreReq: python3-module-tox pylint-py3
%endif

%py_provides %oname
%py_requires six

%description
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of
input.

%package -n python3-module-%oname
Summary: Allows you to run a test with multiple data sets
Group: Development/Python3
%py3_provides %oname
%py3_requires six

%description -n python3-module-%oname
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of
input.

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
* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150223
- Initial build for Sisyphus

