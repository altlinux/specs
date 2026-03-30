%def_with check

Name: python3-module-dbus-fast
Version: 4.0.0
Release: alt1.1

Summary: Python library for DBus
License: MIT
Group: Development/Python
Url: https://pypi.org/project/dbus-fast

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-poetry-core
BuildRequires: python3-module-cython
BuildRequires: /usr/bin/dbus-launch

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-codspeed
%endif

#%%python3_set_limited_api 3.12

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
dbus-launch sh -c '
%pyproject_run_pytest -o addopts=  tests'

%files
%python3_sitelibdir/dbus_fast
%python3_sitelibdir/dbus_fast-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1.1
- Demodernized packaging.

* Tue Feb 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.0.0-alt1
- 4.0.0 released

* Mon Nov 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.2-alt1
- 3.1.2 released

* Mon Nov 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.45.1-alt1
- 2.45.1 released

* Thu Oct 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.44.5-alt1
- 2.44.5 released

* Fri Sep 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.44.3-alt1
- 2.44.3 released

* Tue Jul 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.44.2-alt1
- 2.44.2 released

* Thu Jul 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.44.1-alt1
- 2.44.1 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.28.0-alt1
- 2.28.0 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.24.3-alt1
- 2.24.3 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.24.0-alt1
- 2.24.0 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.22.1-alt1
- 2.22.1 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.21.1-alt1
- 2.21.1 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.21.0-alt1
- 2.21.0 released

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.12.0-alt1
- 2.12.0 released

* Thu Sep 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.95.2-alt1
- 1.95.2 released

* Thu Sep 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.94.1-alt1
- 1.94.1 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.91.4-alt1
- 1.91.4 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.86.0-alt1
- 1.86.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.85.0-alt1
- 1.85.0 released

* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.84.1-alt1
- 1.84.1 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.82.0-alt1
- 1.82.0 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.61.1-alt1
- 1.61.1 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released
