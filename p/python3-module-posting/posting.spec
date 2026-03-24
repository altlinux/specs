%define _unpackaged_files_terminate_build 1
%define pypi_name posting
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.9.2
Release: alt1

Summary: A powerful HTTP client that lives in your terminal
License: Apache-2.0
Group: Networking/Other
Url: https://posting.sh/
Vcs: https://github.com/darrenburns/posting
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
Posting is an HTTP client, not unlike Postman and Insomnia
As a TUI application, it can be used over SSH and enables efficient
keyboard-centric workflows. Your requests are stored locally in simple
YAML files, so they're easy to read and version control.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install
ln -sf %_licensedir/Apache-2.0 LICENSE

%check
%pyproject_run_pytest -vca \
    --ignore=tests/test_snapshots.py \
    ./tests
# test_snapshots.py is ignored because it requires internet
# and tree-sitter grammatics wich are not in sisyphus

%files
%doc --no-dereference LICENSE
%doc README.md
%_bindir/%mod_name
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 17 2026 Andrey Kuzma <kuzmaav@altlinux.org> 2.9.2-alt1
- Initial build for Sisyphus.
