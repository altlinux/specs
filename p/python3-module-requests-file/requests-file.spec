Name: python3-module-requests-file
Version: 3.0.1
Release: alt2

Summary: Local filesystem access for Requests module
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/requests-file
VCS: https://codeberg.org/dashea/requests-file

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_tox tox.ini testenv
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/requests_file
%python3_sitelibdir/requests_file-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.1-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1.1
- Demodernized packaging.

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.1-alt1
- 3.0.1 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- initial
