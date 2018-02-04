%define oname pytest-quickcheck

%def_with python3

Name: python-module-%oname
Version: 0.8.1
Release: alt1.1.1
Summary: pytest plugin to generate random data inspired by QuickCheck
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-quickcheck/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-tox python-module-pytest-pep8
BuildPreReq: python-module-pytest-flakes python-module-virtualenv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-tox python3-module-pytest-pep8
BuildPreReq: python3-module-pytest-flakes python3-module-virtualenv
%endif

%py_provides pytest_quickcheck

%description
pytest plugin to generate random data inspired by QuickCheck.

Features:

* Provide pytest.mark.randomize function for generating random test data

%package -n python3-module-%oname
Summary: pytest plugin to generate random data inspired by QuickCheck
Group: Development/Python3
%py3_provides pytest_quickcheck

%description -n python3-module-%oname
pytest plugin to generate random data inspired by QuickCheck.

Features:

* Provide pytest.mark.randomize function for generating random test data

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus

