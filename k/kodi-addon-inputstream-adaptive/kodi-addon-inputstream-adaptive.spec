Name: kodi-addon-inputstream-adaptive
Version: 20.3.3
Release: alt1

Summary: Adaptive stream addon for Kodi
License: GPLv2
Group: Video
Url: https://github.com/peak3d/inputstream.adaptive/

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel
BuildRequires: libexpat-devel libgtest-devel libap4-devel-static

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
