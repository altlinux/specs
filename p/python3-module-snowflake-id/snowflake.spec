%define _unpackaged_files_terminate_build 1
%define pypi_name snowflake-id
%def_with check

Name: python3-module-%pypi_name
Version: 1.0.2
Release: alt1

Summary: The Snowflake generator done right
License: MIT
Group: Development/Python3
Url: https://github.com/vd2org/snowflake
Vcs: https://github.com/vd2org/snowflake.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject

%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
BuildRequires: /proc
%endif

%description
Generates 64-bit unique identifiers for distributed systems with low collision
probability. Supports configurable worker and datacenter ID settings.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/snowflake
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jan 16 2026 Grant Makyan <karonus@altlinux.org> 1.0.2-alt1
- First build for ALT.
