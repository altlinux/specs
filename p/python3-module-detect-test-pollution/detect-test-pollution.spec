%define _unpackaged_files_terminate_build 1
%define pypi_name detect-test-pollution
%define mod_name detect_test_pollution

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1
Summary: A tool to detect test pollution
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/detect-test-pollution
Vcs: https://github.com/asottile/detect-test-pollution
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.*
%_bindir/detect-test-pollution
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Apr 27 2024 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
