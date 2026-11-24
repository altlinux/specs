%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-playwright
%define mod_name pytest_playwright

# The tests launch browsers that "playwright install" downloads from the
# network, which is unavailable in hasher.
%def_without check

Name: python3-module-%pypi_name
Version: 0.10.0
Release: alt1

Summary: A pytest wrapper with fixtures for Playwright to automate web browsers
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-playwright
Vcs: https://github.com/microsoft/playwright-pytest
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject >= 0.3.0
%pyproject_configure_pypi_package
# Upstream made pytest-base-url optional: it is the base-url extra.
%pyproject_configure_pypi_subpackage base-url
%if_with check
BuildRequires: /dev/pts
BuildRequires: /dev/shm
%endif

%description
A pytest wrapper with fixtures for Playwright to automate web browsers.
This package provides synchronous (blocking) fixtures via the
pytest-playwright plugin, exposing browser, page, and context fixtures
for writing end-to-end browser tests with pytest.

%prep
%setup
# The upstream repository holds two projects, each in its own directory;
# setuptools-scm takes their version from the repository root.
%pyproject_scm_init
cd %pypi_name
%pyproject_setup_deps
cd -

%build
cd %pypi_name
%pyproject_build
cd -

%install
cd %pypi_name
%pyproject_install
cd -

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE %pypi_name/README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 12 2026 Andrey Kuzma <kuzmaav@altlinux.org> 0.10.0-alt1
- Initial build for ALT Sisyphus.
