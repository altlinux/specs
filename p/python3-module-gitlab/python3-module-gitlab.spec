%define _unpackaged_files_terminate_build 1
%define module_name gitlab
%define pypi_name python-gitlab
%def_with check

Name: python3-module-%module_name
Version: 3.13.0
Release: alt1
Summary: A python wrapper for the GitLab API
License: LGPL-3.0
Group: Development/Python3
Url: https://github.com/python-gitlab/python-gitlab
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(responses)
BuildRequires: python3(requests)
BuildRequires: python3(requests_toolbelt)
%endif

%py3_provides %pypi_name

%description
Python package providing access to the GitLab server API.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%_bindir/%module_name
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Feb 08 2023 Alexander Makeenkov <amakeenk@altlinux.org> 3.13.0-alt1
- Updated to version 3.13.0

* Wed Jan 25 2023 Alexander Makeenkov <amakeenk@altlinux.org> 3.12.0-alt1
- Updated to version 3.12.0
- Enabled tests

* Tue Jul 26 2022 Alexander Makeenkov <amakeenk@altlinux.org> 3.6.0-alt1
- Initial build for ALT
