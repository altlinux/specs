%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-watcher
%define module_name pytest_watcher
%def_with check

Name: python3-module-%pypi_name
Version: 0.4.3
Release: alt1

Summary: Automatically rerun your tests on file modification
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-watcher/
Vcs: https://github.com/olzhasar/pytest-watcher
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
pytest-watcher is a tool to automatically rerun tests (using pytest by
default) whenever your code changes.
Works on Unix (Linux, MacOS, BSD) and Windows.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%_bindir/ptw
%_bindir/pytest-watcher
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 10 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.4.3-alt1
- Initial build for ALT Sisyphus.

