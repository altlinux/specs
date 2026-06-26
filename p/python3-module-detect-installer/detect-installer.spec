%define _unpackaged_files_terminate_build 1
%define pypi_name detect-installer
%define module_name detect_installer
%def_with check

Name: python3-module-%pypi_name
Version: 0.1.0
Release: alt1.5.g47fdb25

Summary: Detect how a Python package was installed and get the correct upgrade command
License: 0BSD
Group: Development/Python3
Url: https://pypi.org/project/detect-installer/
Vcs: https://github.com/patrick91/detect-installer
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Detect how a Python package was installed and get the correct upgrade
command.

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
%pyproject_run_pytest --ignore=tests/e2e

%files
%doc README.md LICENSE
%_bindir/%pypi_name-test
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jun 26 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.1.0-alt1.5.g47fdb25
- Initial build for ALT Sisyphus.
