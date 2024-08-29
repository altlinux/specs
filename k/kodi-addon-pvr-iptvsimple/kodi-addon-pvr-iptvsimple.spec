Name: kodi-addon-pvr-iptvsimple
Version: 21.8.6
Release: alt1

Summary: IPTVSimple addon for Kodi
License: GPLv2
Group: Video
Url: https://github.com/kodi-pvr/pvr.iptvsimple/

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel
BuildRequires: libpugixml-devel liblzma-devel zlib-devel

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
%_libdir/kodi/addons/pvr.iptvsimple
%_datadir/kodi/addons/pvr.iptvsimple

%changelog
* Thu Aug 29 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.8.6-alt1
- 21.8.6 released

* Tue Jul 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.8.5-alt1
- 21.8.5 released

* Thu Apr 18 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.8.4-alt1
- 21.8.4 released

* Mon Apr 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.8.3-alt1
- 21.8.3 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.13.0-alt1
- 20.13.0 released

* Tue Oct 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.11.1-alt1
- 20.11.1 released

* Mon Aug 28 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.11.0-alt1
- 20.11.0 released

* Tue May 02 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.10.1-alt1
- 20.10.1 released

* Thu Apr 27 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.10.0-alt1
- 20.10.0 released

* Thu Mar 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.9.1-alt1
- 20.9.1 released

* Wed Mar 22 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.9.0-alt1
- 20.9.0 released

* Tue Feb 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.8.1-alt1
- 20.8.1 released

* Tue Feb 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.7.0-alt1
- 20.7.0 released

* Mon Jan 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.6.1-alt1
- 20.6.1 released

* Tue Nov 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.6.0-alt1
- 20.6.0 released

* Tue Jan 11 2022 Michael Shigorin <mike@altlinux.org> 19.0-alt6
- build on Elbrus as well

* Mon Oct 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt5
- 19.0-Matrix released

* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt4
- updated up to 7.4.2-Matrix

* Thu Nov 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt3
- updated up to 7.0.0-Matrix

* Fri Oct 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt2
- follow addon API changes

* Mon Aug 31 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt1
- updated for kodi 19.0 Matrix

* Fri Feb 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt1
- updated for Leia

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 17.0-alt2
- NMU: added URL

* Mon Feb 06 2017 Anton Farygin <rider@altlinux.ru> 17.0-alt1
- new version

* Mon Nov 28 2016 Anton Farygin <rider@altlinux.ru> 16.0-alt1
- initial build for ALT
