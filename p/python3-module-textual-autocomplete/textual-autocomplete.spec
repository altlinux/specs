%define _unpackaged_files_terminate_build 1
%define pypi_name textual-autocomplete
%define mod_name textual_autocomplete

%def_with check

Name: python3-module-%pypi_name
Version: 4.0.6
Release: alt1

Summary: A simple autocomplete dropdown library for Textual Input widgets
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/textual-autocomplete/
Vcs: https://github.com/darrenburns/textual-autocomplete
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
%pyproject_builddeps_build
BuildRequires: rpm-build-pyproject
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A simple autocomplete dropdown library for Textual Input widgets.
Compatible with Textual 2.0 and above.

Core Features:
* Fuzzy matching - Find matches even with typos.
* Keyboard navigation - Arrow keys, Tab, Enter, and Escape.
* Rich styling options - Customizable highlighting and appearance.
* Dynamic content - Supply items as a list or from a callback function.
* Path completions - Built-in support for filesystem path completions.

%prep
%setup
%autopatch -p1
find ./tests/snapshots/__snapshots__/ -type f -name '*.svg' \
    -exec rename .svg .raw {} +
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.md LICENSE
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 10 2026 Andrey Kuzma <kuzmaav@altlinux.org> 4.0.6-alt1
- Initial build for Sisyphus.
