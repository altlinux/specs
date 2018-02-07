%define _unpackaged_files_terminate_build 1
%define oname pytest-diffeo

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.1
Summary: Common py.test support for Diffeo tests
License: MIT/X11
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-diffeo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/diffeo/pytest-diffeo.git
Source0: https://pypi.python.org/packages/e3/ee/25a3cab817e1ef69da019dbcfdbd8fa429f3c02dc6653c978262d3d9a83a/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-six
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
BuildRequires: python3-module-six
BuildRequires: python3-module-pytest
%endif

%py_provides pytest_diffeo

%description
If this package is installed, then you can run py.test with additional
command-line arguments --runperf, --runslow, -runload, or
-run-integration. Tests marked with @pytest.mark.performance,
@pytest.mark.slow, @pytest.mark.load, and pytest.mark.integration
respectively, will not be run unless the corresponding command-line
option is present.

This package also provides a redis_address fixture to get the location
of an external Redis installation. This must be provided via a
--redis-address command-line argument.

%package -n python3-module-%oname
Summary: Common py.test support for Diffeo tests
Group: Development/Python3
%py3_provides pytest_diffeo

%description -n python3-module-%oname
If this package is installed, then you can run py.test with additional
command-line arguments --runperf, --runslow, -runload, or
-run-integration. Tests marked with @pytest.mark.performance,
@pytest.mark.slow, @pytest.mark.load, and pytest.mark.integration
respectively, will not be run unless the corresponding command-line
option is present.

This package also provides a redis_address fixture to get the location
of an external Redis installation. This must be provided via a
--redis-address command-line argument.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|@VERSION@|%version|' setup.py

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt1.git20141106.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.git20141106
- Initial build for Sisyphus

