%define rname calindori

%define sover 0
%define libcalindori libcalindori%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Summary: Calendar application for Plasma Mobile
License: GPL-3.0-only
Group: Office
Url: https://anongit.kde.org/calindori.git

Requires: kf6-kirigami
Provides:  kde5-calindori = %EVR
Obsoletes: kde5-calindori < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kdbusaddons-devel kf6-ki18n-devel kf6-kirigami-devel kf6-knotifications-devel
BuildRequires: kf6-kservice-devel kf6-kpeople-devel

%description
Calindori is a touch friendly calendar application. It has been designed for mobile devices but it can also run on desktop environments. It offers:
* Monthly agenda
* Multiple calendars
* Event management
* Task management
* Calendar import

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install

%find_lang --all-name --with-qt %name

%files -f %name.lang
%_K6bin/calind*
%_K6xdgapp/*calind*.desktop
%_K6start/*calind*.desktop
%_K6icon/*/*/apps/*calind*.*
%_K6notif/*calind*.notifyrc
%_K6dbus_srv/*calind*.service
%_datadir/metainfo/*.xml


%changelog
* Mon Jun 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Wed Sep 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Mon Jun 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Thu May 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Wed Mar 19 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Feb 03 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

