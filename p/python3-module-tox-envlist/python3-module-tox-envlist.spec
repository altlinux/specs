%define _unpackaged_files_terminate_build 1
%define pypi_name tox-envlist

# due to circular dependecy
%def_without check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Additional utilities for click
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-envlist/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(whey)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(pytest-datadir)
BuildRequires: python3(coverage-pyver-pragma)
BuildRequires: python3(tox)
BuildRequires: python3(tox-pip-version)
BuildRequires: python3(domdf-python-tools)
BuildRequires: python3(coincidence)
BuildRequires: python3(braceexpand)
BuildRequires: python3(pluggy)
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
%python3_sitelibdir/tox_envlist/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- initial build for Sisyphus

