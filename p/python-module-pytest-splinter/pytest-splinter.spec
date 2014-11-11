%define oname pytest-splinter

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.2.4
Release: alt1.git20141019
Summary: Splinter plugin for pytest testing framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-splinter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pytest-dev/pytest-splinter.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tox python-module-splinter
BuildPreReq: python-module-detox python-module-mock
BuildPreReq: python-module-pytest-localserver
BuildPreReq: python-module-pytest-pep8 python-module-pytest-cov
BuildPreReq: python-module-virtualenv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tox python3-module-splinter
BuildPreReq: python3-module-detox python3-module-mock
BuildPreReq: python3-module-pytest-localserver
BuildPreReq: python3-module-pytest-pep8 python3-module-pytest-cov
BuildPreReq: python3-module-virtualenv
%endif

%py_provides pytest_splinter

%description
pytest spinter and selenium integration for anyone interested in browser
interaction in tests.

%package -n python3-module-%oname
Summary: Splinter plugin for pytest testing framework
Group: Development/Python3
%py3_provides pytest_splinter

%description -n python3-module-%oname
pytest spinter and selenium integration for anyone interested in browser
interaction in tests.

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
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.git20141019
- Initial build for Sisyphus

