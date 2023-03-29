%define _unpackaged_files_terminate_build 1
%define pypi_name apeye-core

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1

Summary: Core (offline) functionality for the apeye library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/apeye-core/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(hatchling)
BuildRequires: python3(hatch-requirements-txt)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(pytest-datadir)
BuildRequires: python3(coverage)
BuildRequires: python3(coverage-pyver-pragma)
BuildRequires: python3(tox)
BuildRequires: python3(tox-envlist)
BuildRequires: python3(coincidence)
BuildRequires: python3(idna)
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
%python3_sitelibdir/apeye_core/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.1-alt1
- New version.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt3
- add convenient 'python3(apeye-core)' provide

* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt2
- enable tests

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

