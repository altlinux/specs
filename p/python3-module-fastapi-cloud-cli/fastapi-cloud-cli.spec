%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi-cloud-cli
%define module_name fastapi_cloud_cli
%def_with check

Name: python3-module-%pypi_name
Version: 0.24.0
Release: alt1

Summary: Deploy and manage FastAPI Cloud apps from the command line
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi-cloud-cli/
Vcs: https://github.com/fastapilabs/fastapi-cloud-cli
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
BuildRequires: python3-module-coverage
BuildRequires: git
%endif

%description
%summary.

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
# Increase terminal line size, because
# test_create_token_human_output_does_not_print_token_value does not pass
# at narrow terminals: with no tty in the build environment Rich uses the
# default width of 80 and wraps the printed path inside the file name,
# failing the substring assertion.
export COLUMNS=135
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.24.0-alt1
- Initial build for ALT Sisyphus.
