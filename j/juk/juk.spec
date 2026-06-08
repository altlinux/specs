%define rname juk
%def_disable tunepimp

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Sound
Summary: Music Player
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-juk = %EVR
Obsoletes: kde5-juk < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-multimedia-devel
BuildRequires: libssl-devel taglib-devel
BuildRequires: kf6-kcrash-devel kf6-kdoctools-devel kf6-kglobalaccel-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-knotifications-devel kf6-ktextwidgets-devel kf6-kwallet-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kstatusnotifieritem-devel
%if_enabled tunepimp
BuildRequires: libtunepimp-devel
%endif

%description
Juk is a jukebox, tagger and music collection manager.

%prep
%setup -n %rname-%version
%if_disabled tunepimp
sed -i '/^find_package.*TunePimp/d' CMakeLists.txt
%endif

%build
%K6build

%install
%K6install
%K6install_move data juk kio
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6bin/juk
%_K6xdgapp/org.kde.juk.desktop
%_K6data/juk/
%_K6icon/*/*/apps/juk.*
%_K6data/kio/servicemenus/*juk*.desktop
%_K6notif/juk.notifyrc
%_datadir/metainfo/*.xml


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

