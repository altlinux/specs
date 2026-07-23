%define _unpackaged_files_terminate_build 1
%define pypi_name rpmfile
%define mod_name rpmfile

# tests require share_network=1
%def_without check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1

Summary: Read rmp archive files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rpmfile/
Vcs: https://github.com/srossross/rpmfile

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
Conflicts: qa-robot
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
%autopatch -p1
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
%_bindir/rpmfile
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jul 23 2026 Anton Zhukharev <ancieg@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1.

* Thu Jul 25 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0.

* Thu Apr 04 2024 Anton Zhukharev <ancieg@altlinux.org> 2.0.0-alt2
- Set conflict with qa-robot package (due to /usr/bin/rpmfile path).

* Fri Nov 17 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.0-alt1
- Built for ALT Sisyphus.
