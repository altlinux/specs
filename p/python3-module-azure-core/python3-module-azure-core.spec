%define pypi_name azure-core

%def_without check

Name: python3-module-%pypi_name
Version: 1.32.0
Release: alt1

Summary: Microsoft Azure Core Library for Python
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/azure-core

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%python3_sitelibdir/azure/core
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 02 2025 Anton Vyatkin <toni@altlinux.org> 1.32.0-alt1
- Initial build for Sisyphus.
