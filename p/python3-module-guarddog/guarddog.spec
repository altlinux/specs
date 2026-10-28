%define _unpackaged_files_terminate_build 1

Name: python3-module-guarddog

Version: 3.2.0
Release: alt1

Summary: GuardDog is a CLI tool to Identify malicious PyPI and npm packages
License: Apache-2.0
Group: Development/Tools
Url: https://pypi.org/project/guarddog
Vcs: https://github.com/DataDog/guarddog

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: guarddog-3.2.0-alt-user-cache-dir.patch
Patch1: guarddog-3.2.0-alt-sandbox-cert-symlink.patch

%add_pyproject_deps_runtime_filter 'configparser$'
%add_pyproject_deps_check_filter 'configparser$'
%add_pyproject_deps_check_filter 'python-tlsh$'

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
GuardDog is a CLI tool that identifies malicious PyPI and npm packages,
Go modules, Rust crates, RubyGems, GitHub actions, or VSCode extensions.
It runs static analysis on package source code (through YARA rules) and
analyzes package metadata to detect supply chain attacks.

%prep
%setup
%patch0 -p1
%patch1 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install --platlib

%check
# test_cd_size_zero*: fail with Python 3.14
# test_githubactions_find_requirements: needs a git repo
# others: need network
%pyproject_run_pytest \
    --ignore=tests/core/test_rubygems_package_scanner.py \
    --deselect tests/core/test_archives.py::test_cd_size_zero \
    --deselect tests/core/test_extension_scanner.py::test_download_and_get_package_info \
    --deselect tests/core/test_github_action_project_scanner.py::test_githubactions_find_requirements \
    --deselect tests/core/test_github_action_scanner.py::test_download_and_get_github_action_by_ \
    --deselect tests/core/test_go_package_scanner.py::test_download_and_get_package_info \
    --deselect tests/core/test_npm_package_scanner.py::test_download_and_get_package_info \
    --deselect tests/core/test_npm_package_scanner.py::test_metadata_mismatch_on_scoped_npm_package \
    --deselect tests/core/test_npm_requirements_scanner.py::test_npm_requirements_scanner \
    --deselect tests/core/test_pypi_requirements_scanner.py::test_requirements_scanner \
    tests

%files
%doc *.md LICENSE
%_bindir/guarddog
%python3_sitelibdir/guarddog
%python3_sitelibdir/%{pyproject_distinfo guarddog}

%changelog
* Tue Oct 27 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus.

