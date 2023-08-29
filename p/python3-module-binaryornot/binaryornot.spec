%define _unpackaged_files_terminate_build 1

%define pypi_name binaryornot

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.4
Release: alt1.gitac4f56e

Summary: Ultra-lightweight pure Python package to check if a file is binary or text
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/binaryornot
Vcs: https://github.com/binaryornot/binaryornot

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- tests/test_check.py

%files
%_bindir/%pypi_name
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Aug 26 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.4.4-alt1.gitac4f56e
- Initial build for ALT Sisyphus

