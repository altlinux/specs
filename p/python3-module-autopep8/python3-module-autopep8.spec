%define _unpackaged_files_terminate_build 1
%define pypi_name autopep8

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.2
Release: alt1

Summary: A tool that automatically formats Python code to conform to the PEP 8 style guide
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/autopep8/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pycodestyle)
BuildRequires: python3(toml)
%endif

BuildArch: noarch

%description
autopep8 automatically formats Python code to conform to the PEP 8
style guide. It uses the pycodestyle utility to determine what parts
of the code needs to be formatted. autopep8 is capable of fixing most
of the formatting issues that can be reported by pycodestyle.

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
%doc LICENSE README.rst AUTHORS.rst
%_bindir/%pypi_name
%python3_sitelibdir/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Mar 25 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.2-alt1
- New version.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.1-alt1
- 1.7.0 -> 2.0.1

* Sun Oct 02 2022 Anton Zhukharev <ancieg@altlinux.org> 1.7.0-alt1
- initial build for Sisyphus

