Name: kodi-addon-inputstream-adaptive
Version: 21.5.0
Release: alt1

Summary: Adaptive stream addon for Kodi
License: GPLv2
Group: Video
Url: https://github.com/peak3d/inputstream.adaptive/

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel rapidjson-devel
BuildRequires: libexpat-devel libgtest-devel libap4-devel-static libpugixml-devel

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
%_libdir/kodi/addons/*
%_datadir/kodi/addons/*

%changelog
* Wed Jul 31 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.5.0-alt1
- 21.5.0 released

* Tue Jun 25 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.4.10-alt1
- 21.4.10 released

* Fri May 31 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.4.9-alt1
- 21.4.9 released

* Mon May 20 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.4.8-alt1
- 21.4.8 released

* Mon May 13 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.4.7-alt1
- 21.4.7 released

* Fri May 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.4.6-alt1
- 21.4.6 released

* Mon Apr 15 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.4.5-alt1
- 21.4.5 released

* Mon Apr 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.4.4-alt1
- 21.4.4 released

* Sat Nov 11 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20.3.14-alt2
- NMU: fixed FTBFS on LoongArch

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.14-alt1
- 20.3.14 released

* Mon Sep 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.13-alt1
- 20.3.13 released

* Mon Aug 28 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.12-alt1
- 20.3.12 released

* Wed Jul 19 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.11-alt1
- 20.3.11 released

* Thu Jun 22 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.9-alt2
- rebuilt with gcc13

* Wed May 31 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.9-alt1
- 20.3.9 released

* Mon May 15 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.8-alt1
- 20.3.8 released

* Wed May 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.7-alt1
- 20.3.7 released

* Thu Apr 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.6-alt1
- 20.3.6 released

* Mon Mar 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.5-alt1
- 20.3.5 released

* Mon Feb 27 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.4-alt1
- 20.3.4 released

* Tue Feb 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.3-alt1
- 20.3.3 released

* Mon Jan 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.2-alt1
- 20.3.2 released

* Tue Nov 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.3.1-alt1
- 20.3.1 released

* Tue Jan 11 2022 Michael Shigorin <mike@altlinux.org> 19.0-alt5
- build on Elbrus as well (with a trivial patch)

* Mon Oct 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt4
- 19.0-Matrix released

* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt3
- updated up to 2.6.7-Matrix

* Thu Nov 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt2
- updated up to 2.6.4-Matrix

* Mon Aug 31 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 19.0-alt1
- updated for kodi 19.0 Matrix

* Mon Aug 05 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt3
- updated for Leia

* Thu Feb 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 18.0-alt2
- NMU: fixed build with gcc-8.

* Fri Feb 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt1
- updated for Leia

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 17.5-alt1.1
- NMU: added URL

* Sat Nov 11 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.5-alt1
- 2.0.19

* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- initial
