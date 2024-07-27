%define pypi_name azure-keyvault-secrets

%def_without check

Name: python3-module-%pypi_name
Version: 4.8.0
Release: alt1

Summary: Microsoft Azure Key Vault Secrets Client Library for Python
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/azure-keyvault-secrets

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
%python3_sitelibdir/azure/keyvault/secrets/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jul 25 2024 Anton Vyatkin <toni@altlinux.org> 4.8.0-alt1
- Initial build for Sisyphus.
