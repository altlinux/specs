%define oname pytest-allure-adaptor

%def_without python3

Name: python-module-%oname
Version: 1.5.2
Release: alt1.git20141112
Summary: Plugin for py.test to generate allure xml reports
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-allure-adaptor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/allure-framework/allure-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-lxml python-module-recordtype
BuildPreReq: python-module-enum34 python-module-hamcrest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-lxml python3-module-recordtype
BuildPreReq: python3-module-enum34 python3-module-hamcrest
BuildPreReq: python-tools-2to3
%endif

%py_provides allure

%description
This repository contains a plugin for py.test which automatically
prepares input data used to generate Allure Report. Note: this plugin
currently supports only Allure 1.4.x series.

%package -n python3-module-%oname
Summary: Plugin for py.test to generate allure xml reports
Group: Development/Python3
%py3_provides allure

%description -n python3-module-%oname
This repository contains a plugin for py.test which automatically
prepares input data used to generate Allure Report. Note: this plugin
currently supports only Allure 1.4.x series.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst demo
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst demo
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20141112
- Initial build for Sisyphus

