%define rname kgpg

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: File tools
Summary: Graphical frontend to GPG
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-kgpg = %EVR
Obsoletes: kde5-kgpg < %EVR
#Requires: xli

Source: %rname-%version.tar
Patch1: alt-gpg-bin.patch
Patch2: alt-revoke-fix-segfault.patch
Patch3: alt-remove-details-button.patch
Patch4: alt-gpg-home-args.patch
Patch5: alt-gpg-verify.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: boost-devel libgpgme-devel
BuildRequires: akonadi-contacts-devel akonadi-devel kf6-kcontacts-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-karchive-devel kf6-kcrash-devel kf6-kdbusaddons-devel  kf6-kdoctools-devel kf6-ktexttemplate-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel kf6-knotifications-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwindowsystem-devel

%description
Graphical GPG frontend.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%K6build

%install
%K6install
%K6install_move data kgpg kio
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kgpg
%_K6xdgapp/org.kde.kgpg.desktop
%_K6data/kio/servicemenus/*kgpg*.desktop
%_K6start/org.kde.kgpg.desktop
%_K6cfg/kgpg.kcfg
%_K6icon/*/*/apps/kgpg.*
%_K6icon/*/*/actions/*key*.*
%_K6icon/*/*/status/*key*.*
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml


%changelog
* Thu Jun 04 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Fri May 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Dec 03 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt2
- fix requires (closes: 57098)

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Mon Sep 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Thu Jul 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Tue Jun 10 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Mon May 12 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Apr 21 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.0-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Tue Feb 18 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Jan 20 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Wed Nov 13 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Oct 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

