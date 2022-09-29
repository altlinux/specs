%define _unpackaged_files_terminate_build 1
%define pypi_name braceexpand

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.7
Release: alt1

Summary: Bash-style brace expansion for Python 
License: MIT
Group: Development/Python3
Url: https://pypi.org/projects/braceexpand/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
%summary

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
%doc LICENSE README.md CHANGELOG.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.7-alt1
- initial build for Sisyphus

