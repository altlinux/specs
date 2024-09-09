Name: kodi-addon-pvr-hts
Version: 21.2.5
Release: alt1

Summary: PVR TVheadend addon for Kodi
License: GPLv2
Group: Video

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/kodi/addons/pvr.hts
%_datadir/kodi/addons/pvr.hts

%changelog
* Mon Sep 09 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.2.5-alt1
- 21.2.5 released

* Mon Jun 10 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.2.4-alt1
- 21.2.4 released

* Tue May 21 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.2.3-alt1
- 21.2.3 released

* Thu Apr 18 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.2.2-alt1
- 21.2.2 released

* Mon Apr 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.2.1-alt1
- 21.2.1 released

* Mon Mar 11 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.7.2-alt1
- 20.7.2 released

* Mon Feb 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.7.0-alt1
- 20.7.0 released

* Thu Oct 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.6.3-alt1
- 20.6.3 released

* Fri Mar 31 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.6.2-alt1
- 20.6.2 released

* Thu Feb 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.6.1-alt1
- 20.6.1 released

* Thu Jan 19 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.6.0-alt1
- 20.6.0 released

* Tue Jan 11 2022 Michael Shigorin <mike@altlinux.org> 19.0-alt6
- build on Elbrus as well

* Mon Oct 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt5
- 19.0-Matrix released

* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt4
- updated up to 8.2.2-Matrix

* Thu Nov 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt3
- updated up to 8.1.0-Matrix

* Fri Oct 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt2
- follow addon API changes

* Mon Aug 31 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt1
- updated for kodi 19.0 Matrix

* Tue Aug 06 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt2
- updated for Leia up to 4.4.18

* Thu Jan 31 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt1
- updated for Leia

* Thu Nov 29 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- initial
