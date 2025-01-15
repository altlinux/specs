%define _unpackaged_files_terminate_build 1
%define pypi_name rich-toolkit
%define mod_name rich_toolkit

%def_with check

Name: python3-module-%pypi_name
Version: 0.13.2
Release: alt1

Summary: Opinionated components for Rich
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rich-toolkit/
Vcs: https://github.com/patrick91/rich-toolkit

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter pdbpp
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This is a very opinionated set of components for building CLI
applications. It is based on Rich.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -q -Wignore tests

%files
%doc README.* LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jan 15 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.13.2-alt1
- Updated to 0.13.2.

* Sat Dec 28 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.12.0-alt1
- Initial build for ALT Sisyphus.

