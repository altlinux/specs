%define _unpackaged_files_terminate_build 1
%define pypi_name rpmfile

# tests require share_network=1
%def_without check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: Read rmp archive files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rpmfile/
Vcs: https://github.com/srossross/rpmfile

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra zstd
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
%endif

%description
Tools for inspecting RPM files in python.
This module is modeled after the tarfile module.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Nov 17 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.0-alt1
- Built for ALT Sisyphus.

