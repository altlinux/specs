%define pypi_name cli_base_utilities
%define modname cli_base

Name: python3-module-cli-base-utilities
Version: 0.33.0
Release: alt1

Summary: Helpers to build a CLI program

License: GPL-3.0-or-later
Group: Development/Python3
Url: https://github.com/jedie/cli-base-utilities
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)

%if_disabled check
%else
BuildRequires: python3(pytest)
BuildRequires: python3(bx_py_utils)
BuildRequires: python3(tyro)
BuildRequires: python3(rich)
BuildRequires: python3(tomlkit)
BuildRequires: python3(dateutil)
BuildRequires: python3(packaging)
BuildRequires: python3(typeguard)
BuildRequires: python3(pygments)
%endif

%description
Helpers to build a CLI program with tyro and rich:
TOML settings, git helpers, shell completion, systemd service setup
and test utilities.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# upstream development CLI and unit tests need manageprojects (not packaged)
rm -rv %buildroot%python3_sitelibdir/%modname/cli_dev/
find %buildroot%python3_sitelibdir/%modname -depth -type d -name tests -exec rm -rv {} +

%check
# tests of the upstream development tooling need manageprojects
# and pre-commit, import cli_dev (not packaged) or need a git checkout
%pyproject_run_pytest -v cli_base \
    --ignore=cli_base/cli_dev \
    --ignore=cli_base/cli_tools/tests/test_code_style.py \
    --ignore=cli_base/cli_tools/tests/test_dev_tools.py \
    --ignore=cli_base/cli_tools/tests/test_git_history.py \
    --ignore=cli_base/cli_tools/tests/test_git.py \
    --ignore=cli_base/cli_tools/tests/test_rich_click_test_utils.py \
    --ignore=cli_base/cli_tools/tests/test_rich_test_utils.py \
    --ignore=cli_base/cli_tools/tests/test_version_info.py \
    --ignore=cli_base/systemd/tests/test_api.py \
    --ignore=cli_base/tests/test_doctests.py \
    --ignore=cli_base/tests/test_pre_commit.py \
    --ignore=cli_base/tests/test_readme_history.py \
    --ignore=cli_base/tests/test_project_setup.py \
    --ignore=cli_base/tests/test_readme.py \
    --ignore=cli_base/tests/test_run_pip_audit.py \
    --ignore=cli_base/toml_settings/tests/test_sensible_editor.py

%files
%doc README.md LICENSE
%_bindir/%modname
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.33.0-alt1
- initial build for Sisyphus
