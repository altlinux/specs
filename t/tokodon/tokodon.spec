%define rname tokodon

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Networking/Chat
Summary: Mastodon client
Url: http://www.kde.org
License:  GPL-3.0-only


Requires: kf6-kirigami kf6-kirigami-addons
Provides:  kde5-tokodon = %EVR
Obsoletes: kde5-tokodon < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: mpvqt6-devel
BuildRequires: qt6-multimedia-devel qt6-declarative-devel qt6-svg-devel qt6-websockets-devel
%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel qt6-webview-devel
%endif
BuildRequires: qcoro6-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kirigami-addons-devel kf6-kirigami-devel
BuildRequires: kf6-knotifications-devel kf6-qqc2-desktop-style-devel kf6-purpose-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kirigami-addons-devel

%description
A modern Mastodon client.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/tokodon
%_K6xdgapp/*tokodon*.desktop
%_K6icon/*/*/apps/*tokodon*
%_K6notif/*tokodon*.notifyrc
%_K6plug/kf?/purpose/*tokodon*.so
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*tokodon*.xml

%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

