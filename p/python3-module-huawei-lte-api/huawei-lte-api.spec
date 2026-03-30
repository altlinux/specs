Name: python3-module-huawei-lte-api
Version: 1.11.0
Release: alt2

Summary: Python API For huawei LAN/WAN LTE Modems
License: LGPLv3
Group: Development/Python
URL: https://pypi.org/project/huawei-lte-api
VCS: https://github.com/salamek/huawei-lte-api

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

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/huawei_lte_api
%python3_sitelibdir/huawei_lte_api-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.11.0-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.11.0-alt1.1
- Demodernized packaging.

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.11.0-alt1
- 1.11.0 released

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.1-alt1.1
- NMU: updated build dependencies

* Wed Jul 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.4-alt1
- 1.5.4 released

* Tue Jun 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.18-alt1
- 1.4.18 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.17-alt1
- 1.4.17 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.12-alt1
- 1.4.12 released

* Tue Jan 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.7-alt1
- 1.4.7 released
