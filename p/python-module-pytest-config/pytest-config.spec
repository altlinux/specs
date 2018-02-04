%define oname pytest-config

%def_with python3

Name: python-module-%oname
Version: 0.0.11
Release: alt1.1.1
Summary: A plugin for pytest to aid setup and configuration
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-config/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pytest-django python-module-pytest-cov
BuildPreReq: python-module-pytest-cache python-tools-pep8
BuildPreReq: python-module-pytest-pep8 python-module-pytest-random
BuildPreReq: python-module-pytest-pythonpath
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pytest-django python3-module-pytest-cov
BuildPreReq: python3-module-pytest-cache python3-tools-pep8
BuildPreReq: python3-module-pytest-pep8 python3-module-pytest-random
BuildPreReq: python3-module-pytest-pythonpath
BuildPreReq: python-tools-2to3
%endif

%py_provides pytest_config
Requires: %oname-common = %EVR

%description
Base configurations and utilities for developing your Python project
test suite with pytest.

%package -n python3-module-%oname
Summary: A plugin for pytest to aid setup and configuration
Group: Development/Python3
%py3_provides pytest_config
Requires: %oname-common = %EVR

%description -n python3-module-%oname
Base configurations and utilities for developing your Python project
test suite with pytest.

%package -n %oname-common
Summary: Configure files for %oname
Group: System/Configuration/Other

%description -n %oname-common
Base configurations and utilities for developing your Python project
test suite with pytest.

This package contains configure files for %oname.

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

%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

%python_install
install -d %buildroot%_sysconfdir
mv %buildroot/usr/src/.pytest_config \
	%buildroot%_sysconfdir/pytest_config

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files -n %oname-common
%_sysconfdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.11-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.11-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.11-alt1
- Initial build for Sisyphus

