%define _unpackaged_files_terminate_build 1
%define pypi_name sqlite-migrate
%define mod_name sqlite_migrate

%def_with check

Name: python3-module-%pypi_name
Version: 0.1b1
Release: alt1

Summary: A simple database migration system for SQLite, based on sqlite-utils
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/sqlite-migrate/
Vcs: https://github.com/simonw/sqlite-migrate

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 06 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1b1-alt1
- Updated to 0.1b1.

* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.1b0-alt1.7.g2dc1485
- Built for ALT Sisyphus.
