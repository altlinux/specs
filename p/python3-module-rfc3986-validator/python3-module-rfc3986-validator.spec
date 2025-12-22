%define _unpackaged_files_terminate_build 1
%define pypi_name rfc3986-validator
%define module_name rfc3986_validator

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.1
Release: alt1

Summary: A pure python RFC3986 validator
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/rfc3986-validator/
Vcs: https://github.com/naimetti/rfc3986-validator

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-rfc3987
BuildRequires: python3-module-hypothesis
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vca

%files
%doc README.md LICENSE
%python3_sitelibdir_noarch/__pycache__/%module_name.*
%python3_sitelibdir_noarch/%module_name.py
%python3_sitelibdir_noarch/%{pyproject_distinfo %module_name}/

%changelog
* Tue Dec 16 2025 Andrey Kuzma <kuzmaav@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
