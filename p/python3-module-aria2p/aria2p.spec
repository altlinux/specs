%define _unpackaged_files_terminate_build 1
%define pypi_name aria2p

# tests require the Internet connection, so they are disabled
%def_without check

Name: python3-module-%pypi_name
Version: 0.12.0
Release: alt2

Summary: Command-line tool and library to interact with an aria2c
License: ISC
Group: Networking/File transfer
Url: https://pypi.org/project/aria2p/
VCS: https://github.com/pawamoy/aria2p

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

Requires: aria2

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra tui
%pyproject_builddeps_check
BuildRequires: python3-modules-curses
%endif

%description
Command-line tool and Python library to interact
with an aria2c daemon process through JSON-RPC.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pdm tests
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Mar 10 2024 Alexey Volkov <qualimock@altlinux.org> 0.12.0-alt2
- Add aria2 to dependencies

* Mon Feb 14 2024 Alexey Volkov <qualimock@altlinux.org> 0.12.0-alt1
- Initial build for ALT
