%define oname pytest-cov

%def_with python3

Name: python-module-%oname
Version: 1.8.1
Release: alt1.git20141125
Summary: py.test plugin for coverage reporting with support for centralised and distributed testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-cov/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/schlamar/pytest-cov.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage python-module-cov-core
BuildPreReq: python-module-virtualenv python-module-pytest-xdist
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage python3-module-cov-core
BuildPreReq: python3-module-virtualenv python3-module-pytest-xdist
%endif

%py_provides pytest_cov
%py_requires pytest cov_core

%description
This plugin produces coverage reports. It supports centralised testing
and distributed testing in both load and each modes. It also supports
coverage of subprocesses.

All features offered by the coverage package should be available, either
through pytest-cov or through coverage's config file.

%package -n python3-module-%oname
Summary: py.test plugin for coverage reporting with support for centralised and distributed testing
Group: Development/Python3
%py3_provides pytest_cov
%py3_requires pytest cov_core

%description -n python3-module-%oname
This plugin produces coverage reports. It supports centralised testing
and distributed testing in both load and each modes. It also supports
coverage of subprocesses.

All features offered by the coverage package should be available, either
through pytest-cov or through coverage's config file.

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
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.git20141125
- New snapshot

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.git20141106
- Version 1.8.1

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.git20140822
- Initial build for Sisyphus

