Name: python3-module-wakeonlan
Version: 3.1.0
Release: alt2

Summary: Python WOL implementation
License: MIT
Group: Development/Python
URL: https://pypi.org/project/wakeonlan
VCS: https://github.com/remcohaszing/pywakeonlan

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
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/wakeonlan
%python3_sitelibdir/wakeonlan-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.0-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1.1
- Demodernized packaging.

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.0-alt1
- 3.1.0 released

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 2.1.0-alt2
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1
- initial
