%define _unpackaged_files_terminate_build 1
%define pypi_name covdefaults

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.2
Release: alt1

Summary: A coverage plugin to provide sensible default settings
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/covdefaults/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(coverage)
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
%tox_check_pyproject

%files
%doc LICENSE README.md
%python3_sitelibdir/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.2-alt1
- 2.2.0 -> 2.2.2

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- initial build for Sisyphus

