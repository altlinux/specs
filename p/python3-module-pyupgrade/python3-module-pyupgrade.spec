%define _unpackaged_files_terminate_build 1
%define pypi_name pyupgrade

%def_with check

Name: python3-module-%pypi_name
Version: 3.2.2
Release: alt1

Summary: A tool (and pre-commit hook) to automatically upgrade syntax for newer versions of the language
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyupgrade/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(coverage)
BuildRequires: python3(covdefaults)
BuildRequires: python3(tokenize-rt)
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
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 15 2022 Anton Zhukharev <ancieg@altlinux.org> 3.2.2-alt1
- 2.38.2 -> 3.2.2

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 2.38.2-alt1
- initial build for Sisyphus

