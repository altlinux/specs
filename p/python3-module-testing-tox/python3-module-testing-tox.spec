%define _unpackaged_files_terminate_build 1
%define pypi_name testing-tox

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.0
Release: alt1.gitd1106cd5

Summary: Handy functions for testing tox plugins
License: MIT
Group: Development/Python3
Url: https://github.com/python-coincidence/testing-tox

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(whey)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox-envlist)
BuildRequires: python3(tox-pip-version)
BuildRequires: python3(domdf-python-tools)
BuildRequires: python3(importcheck)
%endif

BuildArch: noarch

%py3_provides %pypi_name

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
%python3_sitelibdir/testing_tox/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.0.0-alt1.gitd1106cd5
- initial build for Sisyphus

