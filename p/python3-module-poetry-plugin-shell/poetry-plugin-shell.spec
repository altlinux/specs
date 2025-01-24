%define _unpackaged_files_terminate_build 1
%def_with check

%define pypi_name poetry-plugin-shell
%define mod_name poetry_plugin_shell

Name: python3-module-%pypi_name
Version: 1.0.1
Release: alt1

Summary: This package is a plugin that runs a subshell with virtual environment activated
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/poetry-plugin-shell/
Vcs: https://github.com/python-poetry/poetry-plugin-shell

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This package is a plugin that runs a subshell with virtual environment
activated.
This plugin replaces the same feature as the shell command previously
available in Poetry.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev
%if_with check
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
export SHELL="bash"
%pyproject_run_pytest -q -Wignore tests

%files
%doc README.* LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jan 24 2025 Alexandr Shashkin <dutyrok@altlinux.org> 1.0.1-alt1
- Initial build for ALT Sisyphus.

