%define _unpackaged_files_terminate_build 1
%define module_name openqa-client
%define pypi_name openqa_client
%def_with check

Name: python3-module-%module_name
Version: 4.3.1
Release: alt1
Summary: Python API to access openQA server
License: GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/openqa-client
VCS: https://github.com/os-autoinst/openQA-python-client

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-yaml
BuildRequires: python3-module-requests
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-pytest
%endif

%py3_provides %pypi_name

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Nov 01 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.3.1-alt1
- Updated to version 4.3.1.

* Tue Jul 01 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.3.0-alt1
- Updated to version 4.3.0.

* Thu Feb 06 2025 Stanislav Levin <slev@altlinux.org> 4.2.3-alt1.1
- NMU: fixed FTBFS (tox 4).

* Tue Oct 10 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.2.3-alt1
- Updated to version 4.2.3.

* Fri Sep 15 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.2.2-alt1
- Updated to version 4.2.2.

* Fri Mar 10 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.2.1-alt1
- Initial build for ALT
