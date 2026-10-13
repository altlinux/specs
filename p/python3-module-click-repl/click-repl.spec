%define _unpackaged_files_terminate_build 1
%define pypi_name click-repl
%define mod_name click_repl

%def_with check

Name: python3-module-click-repl
Version: 0.4.1
Release: alt1
Summary: REPL plugin for Click
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/click-repl/
Vcs: https://github.com/click-contrib/click-repl
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
REPL plugin for Click.

%prep
%setup
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
# see .github/workflows/tests.yml and tox.ini
%pyproject_run_pytest -vra -o=addopts=''

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 13 2026 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.3.0 -> 0.4.1

* Tue Oct 08 2024 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2
- migrated from removed setuptools' test command (#51666).

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Sisyphus
