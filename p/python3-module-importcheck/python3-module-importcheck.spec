%define _unpackaged_files_terminate_build 1
%define pypi_name importcheck

# check disabled due to hard-coded test-data in the package
%def_without check

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: A tool to check all modules can be correctly imported
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/importcheck/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(whey)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(pytest-datadir)
BuildRequires: python3(tox)
BuildRequires: python3(tox-envlist)
BuildRequires: python3(tox-pip-version)
BuildRequires: python3(coverage-pyver-pragma)
BuildRequires: python3(deprecation)
BuildRequires: python3(click)
BuildRequires: python3(consolekit)
BuildRequires: python3(coincidence)
BuildRequires: python3(dom-toml)
BuildRequires: python3(domdf-python-tools)
BuildRequires: python3(packaging)
BuildRequires: python3(typing_extensions)
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
%doc LICENSE README.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- initial build for Sisyphus

