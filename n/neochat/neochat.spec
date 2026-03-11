%define rname neochat

Name: %rname
Version: 25.12.3
Release: alt1
%K6init

Group: Networking/Chat
Summary: Matrix client
Url: http://www.kde.org
License: GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND BSD-3-Clause

Requires: qml6(QtLocation)
Requires: qml6(QtTextToSpeech)
Requires: qml6(org.kde.desktop)
Requires: kf6-kirigami kf6-purpose kf6-kquickcharts kf6-kconfig
Requires: libkf6prison libkf6prisonscanner
Requires: kf6-kirigami-addons
Requires: kde6-kquickimageeditor
Requires: kunifiedpush

Source: %rname-%version.tar
Patch1: alt-hide-location.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: libquotient-qt6-devel libolm-devel
BuildRequires: cmark-devel cmark
BuildRequires: qcoro6-devel libqtkeychain-qt6-devel
BuildRequires: qt6-multimedia-devel qt6-declarative-devel qt6-location-devel qt6-speech-devel
# qt6-positioning-devel
%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel qt6-webview-devel
%endif
BuildRequires: kf6-kio-devel kf6-qqc2-desktop-style-devel kf6-kcrash-devel kf6-purpose-devel
BuildRequires: kf6-kirigami-devel kf6-ki18n-devel kf6-knotifications-devel kf6-sonnet-devel
BuildRequires: kf6-kitemmodels-devel kf6-kiconthemes-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-syntax-highlighting-devel
BuildRequires: kf6-kirigami-addons-devel kde6-kquickimageeditor-devel
BuildRequires: kunifiedpush-devel

%description
NeoChat is a client for [Matrix](https://matrix.org), the decentralized
communication protocol for instant messaging. It is a fork of Spectral.

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/neochat
%_K6plug/kf?/purpose/*neochat*.so
%_K6xdgapp/*neochat*.desktop
%_K6icon/*/*/apps/*neochat*
%_K6data/krunner/dbusplugins/*neochat*.desktop
%_K6notif/*neochat*.notifyrc
%_K6dbus_srv/*neochat*.service
%_datadir/qlogging-categories6/*neochat*.*categories
%_datadir/metainfo/*neochat*.xml

%changelog
* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt3
- hide location browser

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt2
- hide send location button

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Wed Oct 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt2
- fix requires (closes: 56553)

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt2
- fix requires (closes: 55474)

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Mon Jun 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt2
- fix requires

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Thu Apr 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.0-alt1
- initial build
