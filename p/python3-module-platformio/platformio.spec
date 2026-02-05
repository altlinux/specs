Name: python3-module-platformio
Version: 6.1.19
Release: alt1

Summary: PlatformIO Core
License: Apache-2.0
Group: Development/Other
URL: https://platformio.org/
VCS: https://github.com/platformio/platformio-core

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

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

%files
%_bindir/pio
%_bindir/platformio
%_bindir/piodebuggdb
%python3_sitelibdir/platformio
%python3_sitelibdir/platformio-%version.dist-info

%changelog
* Thu Feb 05 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 6.1.19-alt1
- 6.1.19 released

* Thu Mar 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 6.1.18-alt1
- 6.1.18 released

* Fri Feb 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 6.1.17-alt1
- 6.1.17 released

* Mon Sep 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.1.16-alt1
- 6.1.16 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.1.15-alt1
- 6.1.15 released

* Wed Mar 27 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.1.14-alt1
- 6.1.14 released

* Mon Jan 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.13-alt2
- dropped check section, most of actual tests are online anyway

* Tue Jan 23 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.13-alt1
- 6.1.13 released

* Mon Sep 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.11-alt1
- 6.1.11 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.9-alt1
- 6.1.9 released

* Thu Jul 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.8-alt1
- 6.1.8 released

* Thu Jun 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.7-alt3
- build deps fixed

* Tue May 30 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.7-alt2
- rebuilt with starlette version bump

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.7-alt1
- 6.1.7 released

* Wed Jan 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.6-alt1
- 6.1.6 released

* Tue Nov 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.5-alt1
- 6.1.5 released

* Thu Jul 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.3-alt1
- 6.1.3 released

* Tue May 24 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.1-alt1
- 6.0.1 released

* Mon Feb 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.5-alt1
- 5.2.5 released

* Wed Oct 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.2.1-alt1
- 5.2.1 released

* Mon Mar 22 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.1-alt1
- 5.1.1 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.1.0-alt1
- initial
