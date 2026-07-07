%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-dotenv
%define mod_name pytest_dotenv

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.2
Release: alt1

Summary: This little plugin uses python-dotenv to load any environment variables from a .env file
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-dotenv/
Vcs: https://github.com/quiqua/pytest-dotenv
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
This little plugin uses python-dotenv to load any environment variables
from a .env file. Extra configuration can be defined in any pytest
config files, such as pytest.ini, tox.ini and so on.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
* Tue Jul 07 2026 Andrey Kuzma <kuzmaav@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus.
