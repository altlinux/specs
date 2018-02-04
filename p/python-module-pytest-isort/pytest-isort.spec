%define _unpackaged_files_terminate_build 1
%define oname pytest-isort

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.1
Summary: pytest plugin to perform isort checks (import ordering)
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pytest-isort

Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(pytest)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(pytest)
%endif

%py_requires pytest_cache

%description
pytest plugin to perform isort checks (import ordering)

%if_with python3
%package -n python3-module-%oname
Summary: pytest plugin to perform isort checks (import ordering)
Group: Development/Python3
%py3_requires pytest_cache

%description -n python3-module-%oname
pytest plugin to perform isort checks (import ordering)
%endif

%prep
%setup -n %oname-%version

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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt1
- Initial build for ALT.
