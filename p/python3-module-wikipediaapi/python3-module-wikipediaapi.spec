%define _unpackaged_files_terminate_build 1
%define mod_name %pypi_name
%define modulename wikipediaapi
%define pypi_name Wikipedia_API

%def_with check

Name: python3-module-%modulename
Version: 0.7.1
Release: alt1
Summary: wikipedia-api provide simple and easy to use API for retrieving informations from Wikipedia
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Wikipedia-API/
Vcs: https://github.com/martin-majlis/Wikipedia-API
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(sphinx)

%if_with check
BuildRequires: python3(yaml)
BuildRequires: python3(requests)
BuildRequires: python3(freezegun)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup

%build
%make_build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Nov 12 2024 Pavel Shilov <zerospirit@altlinux.org> 0.7.1-alt1
- initial build for Sisyphus
