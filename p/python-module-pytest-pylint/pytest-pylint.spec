%define oname pytest-pylint

%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1.1
Summary: pytest plugin to check source code with pylint
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pytest-pylint/

# https://github.com/carsongee/pytest-pylint.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools pylint
BuildRequires: python-module-pytest-pep8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools pylint-py3
BuildRequires: python3-module-pytest-pep8
%endif

%py_provides pytest_pylint
%py_requires pytest pylint pytest_pep8

%description
Run pylint with pytest and have configurable rule types (i.e.
Convention, Warn, and Error) fail the build. You can also specify a
pylintrc file.

%if_with python3
%package -n python3-module-%oname
Summary: pytest plugin to check source code with pylint
Group: Development/Python3
%py3_provides pytest_pylint
%py3_requires pytest pylint pytest_pep8

%description -n python3-module-%oname
Run pylint with pytest and have configurable rule types (i.e.
Convention, Warn, and Error) fail the build. You can also specify a
pylintrc file.
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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst pylintrc
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst pylintrc
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt1
- Updated to upstream version 0.7.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20150423.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150423
- Initial build for Sisyphus

