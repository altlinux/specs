%define _unpackaged_files_terminate_build 1
%define module_name openqa-client
%define pypi_name openqa_client
%def_with check

Name: python3-module-%module_name
Version: 4.2.1
Release: alt1
Summary: Python API to access openQA server
License: GPL-2.0
Group: Development/Python3
Url: https://github.com/os-autoinst/openQA-python-client
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(yaml)
BuildRequires: python3(requests)
BuildRequires: python3(freezegun)
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
* Fri Mar 10 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.2.1-alt1
- Initial build for ALT

