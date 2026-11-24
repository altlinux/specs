%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-base-url
%define mod_name pytest_base_url
%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1

Summary: pytest plugin for URL based testing
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-base-url/
Vcs: https://github.com/pytest-dev/pytest-base-url
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
pytest plugin for URL based testing.

Provides a base_url fixture and --base-url command-line option for
specifying the base URL of the application under test. The URL can
also be set via the PYTEST_BASE_URL environment variable.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 11 2026 Andrey Kuzma <kuzmaav@altlinux.org> 2.1.0-alt1
- Initial build for ALT Sisyphus.
