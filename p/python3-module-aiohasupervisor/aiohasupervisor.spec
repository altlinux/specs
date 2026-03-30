%def_with check

Name: python3-module-aiohasupervisor
Version: 0.3.3
Release: alt1.1

Summary: Client Library for Home Assistant Supervisor
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/propcache/
VCS: https://github.com/home-assistant-libs/python-supervisor-client

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-aioresponses
BuildRequires: python3-module-mashumaro
BuildRequires: python3-module-orjson
%endif

%description
%summary

%prep
%setup
sed -ri '/^version\s+=/ s,"[^"]+","%version",' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o=addopts= tests

%files
%python3_sitelibdir/aiohasupervisor
%python3_sitelibdir/aiohasupervisor-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.3.3-alt1.1
- Demodernized packaging.

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.3-alt1
- 0.3.3 released

* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.2-alt1
- 0.2.2 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released
