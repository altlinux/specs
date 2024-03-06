%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-html
%define mod_name pytest_html

%def_with check

Name: python3-module-%pypi_name
Version: 4.1.1
Release: alt1
Summary: pytest plugin for generating HTML reports
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-html
Vcs: https://github.com/pytest-dev/pytest-html
BuildArch: noarch
Source: %name-%version.tar
# to update nodejs modules cache run:
# NODE_ENV= ./alt/update-vendor-nodejs.sh .
Source1: vendor_nodejs.tar
Source2: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: npm
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup -a1
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
export SKIP_NPM_CI=yes
%pyproject_build

%install
%pyproject_install

%check
# TODO: check integration tests
%pyproject_run_pytest -ra testing/test_unit.py

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 05 2024 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- Initial build for Sisyphus.
