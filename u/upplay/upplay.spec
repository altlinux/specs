Name: upplay
Version: 1.9.11
Release: alt1

Summary: UPnP/OpenHome audio Control Point
License: GPLv2
Group: Sound
URL: http://www.lesbonscomptes.com/upplay/
VCS: https://framagit.org/medoc92/upplay

ExcludeArch: i586

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: jsoncpp-devel libcurl-devel libexpat-devel libupnpp-devel
BuildRequires: qt6-base-devel qt6-webengine-devel libambermpris-devel

%description
Upplay is a simple Qt-based UPnP/OpenHome audio Control Point.
It supports gapless transitions using either AVTransport _setNextUri_ or
OpenHome _Playlist_, depending on what the device supports (OpenHome is
chosen if available).

%prep
%setup

%build
%qmake_qt6
%make_build

%install
make install INSTALL_ROOT=%buildroot

%files
%_bindir/upplay
%_datadir/upplay
%_desktopdir/upplay.desktop
%_liconsdir/upplay.png
%_pixmapsdir/upplay.png

%changelog
* Wed Jun 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.11-alt1
- 1.9.11 released

* Thu Feb 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.10-alt1
- 1.9.10 released

* Tue Jan 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.9-alt1
- 1.9.9 released

* Tue Dec 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.8-alt1
- 1.9.8 released

* Wed Jun 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.7-alt1
- 1.9.7 released

* Wed Apr 30 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.6-alt1
- 1.9.6 released

* Mon Apr 07 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.1-alt1
- 1.9.1 released

* Tue Jan 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.1-alt1
- 1.8.1 released

* Thu Jan 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.0-alt1
- 1.8.0 released

* Mon Nov 18 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.8-alt1
- 1.7.8 released

* Wed Oct 16 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.7-alt1
- 1.7.7 released

* Mon May 20 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.3-alt1
- 1.7.3 released

* Mon Dec 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.2-alt1
- 1.7.2 released

* Tue Dec 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released

* Mon Aug 28 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.6-alt1
- 1.6.6 released

* Mon Aug 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt1
- 1.6.3 released

* Tue Apr 26 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Tue Sep 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.10-alt1
- 1.4.10 released

* Wed Feb 03 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.8-alt1
- 1.4.8 released

* Wed Dec 25 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.9-alt1
- initial
