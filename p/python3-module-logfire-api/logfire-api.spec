%define _unpackaged_files_terminate_build 1
%define pypi_name logfire-api
%define module_name logfire_api

Name: python3-module-logfire-api
Version: 5.1.1
Release: alt1

Summary: Shim for the Logfire SDK which does nothing unless Logfire is installed
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/logfire-api/
VCS: https://github.com/pydantic/logfire
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary.

%prep
%setup
%autopatch -p1
cd logfire-api
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
cd -

%build
cd logfire-api
%pyproject_build
cd -

%install
cd logfire-api
%pyproject_install
cd -

%files
%doc logfire-api/README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 5.1.1-alt1
- Initial build for ALT Sisyphus.
