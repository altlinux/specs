%define _unpackaged_files_terminate_build 1
%define pypi_name posting
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.9.2
Release: alt1.1

Summary: A powerful HTTP client that lives in your terminal
License: Apache-2.0
Group: Networking/Other
Url: https://posting.sh/
Vcs: https://github.com/darrenburns/posting
BuildArch: noarch

Source0: %name-%version.tar

Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-textual-snapshot
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-syrupy

BuildRequires: python3-module-click
BuildRequires: python3-module-click-default-group
BuildRequires: python3-module-httpx
BuildRequires: python3-module-openapi-pydantic
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-pydantic-settings
BuildRequires: python3-module-pyperclip
BuildRequires: python3-module-python-dotenv
BuildRequires: python3-module-pyyaml
BuildRequires: python3-module-textual
BuildRequires: python3-module-textual-autocomplete
BuildRequires: python3-module-watchfiles
BuildRequires: python3-module-xdg-base-dirs
%endif

%description
Posting is an HTTP client, not unlike Postman and Insomnia
As a TUI application, it can be used over SSH and enables efficient
keyboard-centric workflows. Your requests are stored locally in simple
YAML files, so they're easy to read and version control.

%prep
%setup
%autopatch -p1

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
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.9.2-alt1.1
- Demodernized packaging.

* Tue Mar 17 2026 Andrey Kuzma <kuzmaav@altlinux.org> 2.9.2-alt1
- Initial build for Sisyphus.
