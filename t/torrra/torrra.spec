%define _unpackaged_files_terminate_build 1

%define pypi_name torrra
%def_with check

Name: %pypi_name
Version: 2.0.7
Release: alt1

Summary: A Python tool that lets you search and download torrents without leaving your CLI
Group: Networking/File transfer
License: MIT
Url: https://torrra.readthedocs.io/
VCS: https://github.com/stabldev/torrra.git

BuildArch: noarch

# Source-url: https://github.com/stabldev/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%add_pyproject_deps_runtime_filter libtorrent
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter libtorrent
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-libtorrent-rasterbar
BuildRequires: python3-module-respx
BuildRequires: python3-module-pytest-asyncio
%endif

%description
Torrra provides a streamlined command-line interface for torrent search
and downloads, powered by Jackett/Prowlarr and Libtorrent. Built with
Textual, it offers a beautiful TUI with pause/resume support - all
without leaving your terminal.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -k "\
not test_home_screen_snapshot \
and not test_welcome_screen_snapshot \
and not test_theme_selector_screen_snapshot"

%files
%doc README.md docs/configuration.md docs/usage.md
%_bindir/%name
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}

%changelog
* Fri Apr 10 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.0.7-alt1
- initial build for ALT Linux
