%define oname nose-allure-plugin

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.alpha2.git20150215
Summary: Nose plugin for allure framework
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-allure-plugin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sergeychipiga/nose-allure-plugin.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-pytest-allure-adaptor
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-pytest-allure-adaptor
%endif

%py_provides nose_allure
%py_requires nose allure.pytest_plugin

%description
It is a port of pytest-allure-adaptor for nose framework.

%package -n python3-module-%oname
Summary: Nose plugin for allure framework
Group: Development/Python3
%py3_provides nose_allure
%py3_requires nose allure.pytest_plugin

%description -n python3-module-%oname
It is a port of pytest-allure-adaptor for nose framework.

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
* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.alpha2.git20150215
- Initial build for Sisyphus

