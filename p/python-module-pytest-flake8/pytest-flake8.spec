%define _unpackaged_files_terminate_build 1
%define oname pytest-flake8

%def_with python3

Name: python-module-%oname
Version: 0.9.1
Release: alt1
Summary: pytest plugin to check FLAKE8 requirements
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pytest-isort

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python2.7(pytest) python2.7(flake8)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3(pytest) python3(flake8)
%endif

%description
pytest plugin to check FLAKE8 requirements

%if_with python3
%package -n python3-module-%oname
Summary: pytest plugin to check FLAKE8 requirements
Group: Development/Python3

%description -n python3-module-%oname
pytest plugin to check FLAKE8 requirements
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
PYTHONPATH=%buildroot%python_sitelibdir py.test -vv
%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir py.test3 -vv
popd
%endif

%files
%doc LICENSE CHANGELOG *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE CHANGELOG *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.1-alt1
- Initial build for ALT.
