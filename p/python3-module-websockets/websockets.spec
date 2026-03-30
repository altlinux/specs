%def_with check

Name: python3-module-websockets
Version: 16.0
Release: alt1.1

Summary: Python WebSocket library
License: BSD-3-Clause
Group: Development/Python
Url: https://github.com/python-websockets/websockets

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-werkzeug
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
%pyproject_run_unittest

%files
%_bindir/websockets
%python3_sitelibdir/websockets
%python3_sitelibdir/websockets-%version.dist-info

%changelog
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
