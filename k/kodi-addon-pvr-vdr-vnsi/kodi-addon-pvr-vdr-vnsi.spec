Name: kodi-addon-pvr-vdr-vnsi
Version: 20.4.1
Release: alt1

Summary: PVR VDR addon for Kodi
License: GPLv2
Group: Video
Url: https://github.com/kodi-pvr/pvr.vdr.vnsi

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel
BuildRequires: libGL-devel libGLES-devel

%description
%summary

%prep
%setup

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix -DCMAKE_INSTALL_LIBDIR=%_libdir/kodi
%make_build

%install
%makeinstall_std

%files
%_libdir/kodi/addons/pvr.vdr.vnsi
%_datadir/kodi/addons/pvr.vdr.vnsi

%changelog
* Fri Mar 31 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.4.1-alt1
- 20.4.1 released

* Thu Jan 19 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20.4.0-alt1
- 20.4.0 released

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

* Thu Jan 31 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 18.0-alt1
- updated for Leia

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 17.0-alt1.1
- NMU: added URL

* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- updated for Krypton

* Wed Feb 24 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.0-alt1
- updated for Jarvis

* Wed Jul 29 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.0-alt1
- initial
