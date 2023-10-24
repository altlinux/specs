%define pypi_name etcd3

%def_without check

Name:    python3-module-%pypi_name
Version: 0.12.0
Release: alt1

Summary: Python client for the etcd API v3
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/kragniz/python-etcd3

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pifpaf
BuildRequires: python3-module-xattr
BuildRequires: /proc
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus.
