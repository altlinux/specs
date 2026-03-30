%def_with check

Name: python3-module-huawei-lte-api
Version: 1.11.0
Release: alt1.1

Summary: Python API For huawei LAN/WAN LTE Modems
License: LGPLv3
Group: Development/Python
Url: https://pypi.org/project/huawei-lte-api
VCS: https://github.com/salamek/huawei-lte-api

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pycryptodomex
BuildRequires: python3-module-requests
BuildRequires: python3-module-xmltodict
%endif

%description
%summary

%prep
%setup

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
