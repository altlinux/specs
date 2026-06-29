%define rname plasma-wayland-protocols

Name: kde5-%rname
Version: 1.21.0
Release: alt1
%K6init altplace no_appdata

Group: Development/KDE and QT
Summary: XML files of non-standard wayland protocols used in Plasma
License: LGPL-2.0-or-later
Url: https://invent.kde.org/libraries/plasma-wayland-protocols

BuildArch: noarch

Requires: wayland-protocols
Provides: %rname = %EVR
Provides: kde5-%rname = %EVR
Provides: kde6-%rname = %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel

%description
XML files of non-standard wayland protocols used in Plasma.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #
%install
%K6install

%files
%_datadir/cmake/PlasmaWaylandProtocols/
%_datadir/plasma-wayland-protocols/

%changelog
* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 1.21.0-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 1.20.0-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 1.19.0-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 1.18.0-alt1
- new version

* Mon Apr 21 2025 Sergey V Turchin <zerg@altlinux.org> 1.17.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 1.16.0-alt1
- new version

* Mon Dec 09 2024 Sergey V Turchin <zerg@altlinux.org> 1.15.0-alt1
- new version

* Fri Sep 13 2024 Sergey V Turchin <zerg@altlinux.org> 1.14.0-alt1
- new version

* Mon May 27 2024 Sergey V Turchin <zerg@altlinux.org> 1.13.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 1.11.1-alt2
- update provides

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 1.11.1-alt1
- new version

* Mon Mar 06 2023 Sergey V Turchin <zerg@altlinux.org> 1.10.0-alt2
- fix requires

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
