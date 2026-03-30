%def_with check

Name: python3-module-onvif-zeep-async
Version: 4.0.4
Release: alt1.1

Summary: ONVIF Client Implementation in Python
License: MIT
Group: Development/Python
Url: https://pypi.org/project/onvif-zeep-async
VCS: https://github.com/hunterjm/python-onvif-zeep-async

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-zeep
BuildRequires: python3-module-aioresponses
BuildRequires: python3-module-httpx
BuildRequires: python3-module-ciso8601
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
%python3_sitelibdir/onvif
%python3_sitelibdir/onvif_zeep_async-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 4.0.4-alt1.1
- Demodernized packaging.

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.0.4-alt1
- 4.0.4 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.13-alt1
- 3.1.13 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.12-alt1
- 3.1.12 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.9-alt1
- 3.1.9 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial
