%define _unpackaged_files_terminate_build 1
%define pypi_name dadata

%def_with check

Name: python3-module-%pypi_name
Version: 25.10.0
Release: alt1
Summary: Thin Python wrapper over Dadata API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dadata/
Vcs: https://github.com/hflabs/dadata-py.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Data cleansing, enrichment and suggestions via Dadata API.

%prep
%setup
%autopatch -p1
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
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Dec 05 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 25.10.0-alt1
- Initial build for ALT.
