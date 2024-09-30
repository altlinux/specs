Name: python3-module-platformio
Version: 6.1.16
Release: alt1

Summary: PlatformIO Core
License: Apache-2.0
Group: Development/Other
Url: https://platformio.org/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# lemme cite requests/packages.py:
# "I don't like it either. Just look the other way."
%add_python3_req_skip requests.packages.urllib3.util.retry
# can't happen
%add_python3_req_skip msvcrt

%set_python3_req_method strict

%files
%_bindir/pio
%_bindir/platformio
%_bindir/piodebuggdb
%python3_sitelibdir/platformio
%python3_sitelibdir/platformio-%version.dist-info

%changelog
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
