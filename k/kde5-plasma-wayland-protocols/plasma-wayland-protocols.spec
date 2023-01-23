%define rname plasma-wayland-protocols

Name: kde5-%rname
Version: 1.10.0
Release: alt1
%K5init altplace no_appdata

Group: Development/KDE and QT
Summary: XML files of non-standard wayland protocols used in Plasma
License: LGPL-2.0-or-later
Url: https://invent.kde.org/libraries/plasma-wayland-protocols

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel

%description
XML files of non-standard wayland protocols used in Plasma.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install

%files
%_libdir/cmake/PlasmaWaylandProtocols/
%_datadir/plasma-wayland-protocols/

%changelog
* Mon Jan 23 2023 Sergey V Turchin <zerg@altlinux.org> 1.10.0-alt1
- new version

* Thu Oct 13 2022 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt1
- new version

* Tue May 17 2022 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt1
- new version

* Fri Jan 14 2022 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt1
- new version

* Wed Dec 29 2021 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt1
- new version

* Mon Sep 13 2021 Sergey V Turchin <zerg@altlinux.org> 1.4.0-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Mon Apr 12 2021 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Tue Aug 11 2020 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- initial build
