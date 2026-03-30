Name: python3-module-websockets
Version: 16.0
Release: alt2

Summary: Python WebSocket library
License: BSD-3-Clause
Group: Development/Python
URL: https://pypi.org/project/websockets
VCS: https://github.com/python-websockets/websockets

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_tox tox.ini testenv

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%_bindir/websockets
%python3_sitelibdir/websockets
%python3_sitelibdir/websockets-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 16.0-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 16.0-alt1.1
- Demodernized packaging.

* Wed Jan 14 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 16.0-alt1
- 16.0 released

* Thu Mar 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 15.0.1-alt1
- 15.0.1 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 14.1-alt1
- 14.1 released

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 14.0-alt1
- 14.0 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 12.0-alt1
- 12.0 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0.3-alt1
- 11.0.3 released

* Wed May 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.0.2-alt1
- 11.0.2 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.4-alt1
- 10.4 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 10.3-alt1
- initial
