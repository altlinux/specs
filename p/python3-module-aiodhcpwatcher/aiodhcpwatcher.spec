Name: python3-module-aiodhcpwatcher
Version: 1.2.1
Release: alt2

Summary: Watch for DHCP packets with asyncio
License: GPLv3
Group: Development/Python
URL: https://pypi.org/project/aiodhcpwatcher
VCS: https://github.com/bdraco/aiodhcpwatcher

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
%pyproject_run_pytest -o=addopts= tests

%files
%python3_sitelibdir/aiodhcpwatcher
%python3_sitelibdir/aiodhcpwatcher-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.1-alt2
- revert unsolicited changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1.1
- Demodernized packaging.

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.1-alt1
- 1.2.1 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt1
- 1.0.0 released

* Fri Mar 15 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.0-alt1
- 0.8.0 released
