%define rname yakuake

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Summary: Very powerful Quake style terminal emulator
License: GPL-2.0 or GPL-3.0
Group: Terminals
Url: http://yakuake.kde.org/

Requires: konsole

Provides: kde5-yakuake = %EVR
Obsoletes: kde5-yakuake < %EVR

# Download from https://download.kde.org/stable/release-service//$pkgver/src/yakuake-$pkgver.tar.xz
Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kauth-devel
BuildRequires: kf6-kbookmarks-devel
BuildRequires: kf6-kcodecs-devel
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kglobalaccel-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-kstatusnotifieritem-devel
BuildRequires: kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-purpose-devel
BuildRequires: kf6-solid-devel
BuildRequires: kf6-sonnet-devel
BuildRequires: plasma6-kwayland-devel plasma-wayland-protocols
BuildRequires: qt6-declarative-devel qt6-svg-devel
BuildRequires: libxcbutil-devel

%description
Yakuake is a drop-down terminal emulator based on KDE Konsole technology.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS README.md TODO LICENSES/*
%_K6bin/%rname
%_K6xdgapp/*%{rname}*.desktop
%_K6icon/*/*/apps/*%{rname}*
%_K6data/%rname
%_K6notif/%rname.notifyrc
%_K6dbus_srv/*%{rname}*.service
%_K6data/knsrcfiles/%rname.knsrc
%_datadir/metainfo/*%{rname}*.xml

%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Apr 21 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt2
- udpate packaging

* Mon Mar 09 2026 Andrey Cherepanov <cas@altlinux.org> 25.12.3-alt1
- New version.

* Tue Feb 10 2026 Andrey Cherepanov <cas@altlinux.org> 25.12.2-alt1
- New version.

* Sat Jan 10 2026 Andrey Cherepanov <cas@altlinux.org> 25.12.1-alt1
- New version.

* Sun Dec 14 2025 Andrey Cherepanov <cas@altlinux.org> 25.12.0-alt1
- New version.

* Wed Nov 12 2025 Andrey Cherepanov <cas@altlinux.org> 25.08.3-alt1
- New version.

* Sat Oct 11 2025 Andrey Cherepanov <cas@altlinux.org> 25.08.2-alt1
- New version.

* Sat Sep 13 2025 Andrey Cherepanov <cas@altlinux.org> 25.08.1-alt1
- New version.

* Sat Aug 16 2025 Andrey Cherepanov <cas@altlinux.org> 25.08.0-alt1
- New version.

* Tue Jul 08 2025 Andrey Cherepanov <cas@altlinux.org> 25.04.3-alt1
- New version.

* Sat Jun 21 2025 Andrey Cherepanov <cas@altlinux.org> 25.04.2-alt1
- New version.

* Mon May 26 2025 Andrey Cherepanov <cas@altlinux.org> 25.04.1-alt1
- New version.

* Mon Oct 28 2024 Andrey Cherepanov <cas@altlinux.org> 24.08.2-alt1
- New version (ALT #51843).
- Build for KF6.

* Sat Apr 27 2024 Andrey Cherepanov <cas@altlinux.org> 24.02.2-alt1
- New version.

* Wed Nov 15 2023 Andrey Cherepanov <cas@altlinux.org> 23.08.3-alt1
- New version.

* Mon Oct 16 2023 Andrey Cherepanov <cas@altlinux.org> 23.08.2-alt1
- New version.

* Mon Sep 18 2023 Andrey Cherepanov <cas@altlinux.org> 23.08.1-alt1
- New version.

* Mon Sep 04 2023 Andrey Cherepanov <cas@altlinux.org> 23.08.0-alt1
- New version.

* Mon Jul 10 2023 Andrey Cherepanov <cas@altlinux.org> 23.04.3-alt1
- New version.

* Tue Jun 13 2023 Andrey Cherepanov <cas@altlinux.org> 23.04.2-alt1
- New version.

* Mon May 15 2023 Andrey Cherepanov <cas@altlinux.org> 23.04.1-alt1
- New version.

* Thu Apr 27 2023 Andrey Cherepanov <cas@altlinux.org> 23.04.0-alt1
- New version.

* Sat Mar 04 2023 Andrey Cherepanov <cas@altlinux.org> 22.12.3-alt1
- New version.

* Fri Feb 03 2023 Andrey Cherepanov <cas@altlinux.org> 22.12.2-alt1
- New version.

* Tue Jan 10 2023 Andrey Cherepanov <cas@altlinux.org> 22.12.1-alt1
- New version.

* Sat Dec 10 2022 Andrey Cherepanov <cas@altlinux.org> 22.12.0-alt1
- New version.

* Sun Nov 06 2022 Andrey Cherepanov <cas@altlinux.org> 22.08.3-alt1
- New version.

* Mon Oct 17 2022 Andrey Cherepanov <cas@altlinux.org> 22.08.2-alt1
- New version.

* Wed Sep 14 2022 Andrey Cherepanov <cas@altlinux.org> 22.08.1-alt1
- New version.

* Sun Aug 21 2022 Andrey Cherepanov <cas@altlinux.org> 22.08.0-alt1
- New version.

* Fri Jul 15 2022 Andrey Cherepanov <cas@altlinux.org> 22.04.3-alt1
- New version.

* Wed Jun 15 2022 Andrey Cherepanov <cas@altlinux.org> 22.04.2-alt1
- New version.

* Sat May 28 2022 Andrey Cherepanov <cas@altlinux.org> 22.04.1-alt1
- New version.

* Mon Apr 25 2022 Andrey Cherepanov <cas@altlinux.org> 22.04.0-alt1
- New version.

* Mon Jan 03 2022 Andrey Cherepanov <cas@altlinux.org> 21.12.0-alt1
- New version.

* Tue Jul 13 2021 Andrey Cherepanov <cas@altlinux.org> 21.04.3-alt1
- New version.
- Rename to yakuake.

* Tue Jun 15 2021 Andrey Cherepanov <cas@altlinux.org> 21.04.2-alt1
- New version.

* Mon May 17 2021 Andrey Cherepanov <cas@altlinux.org> 21.04.1-alt1
- New version.

* Mon Apr 26 2021 Andrey Cherepanov <cas@altlinux.org> 21.04.0-alt1
- New version.

* Mon Mar 08 2021 Andrey Cherepanov <cas@altlinux.org> 20.12.3-alt1
- New version.

* Mon Feb 08 2021 Andrey Cherepanov <cas@altlinux.org> 20.12.2-alt1
- New version.

* Thu Jan 21 2021 Andrey Cherepanov <cas@altlinux.org> 20.12.1-alt1
- New version.

* Mon Nov 09 2020 Andrey Cherepanov <cas@altlinux.org> 20.08.2-alt1
- New version.

* Thu Oct 15 2020 Andrey Cherepanov <cas@altlinux.org> 20.08.1-alt1
- New version.

* Wed May 20 2020 Andrey Cherepanov <cas@altlinux.org> 20.04.1-alt1
- New version.

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 20.04.0-alt1
- New version.

* Tue Mar 10 2020 Andrey Cherepanov <cas@altlinux.org> 19.12.3-alt1
- New version.

* Fri Feb 14 2020 Andrey Cherepanov <cas@altlinux.org> 19.12.2-alt1
- New version.

* Fri Dec 20 2019 Andrey Cherepanov <cas@altlinux.org> 19.12.0-alt1
- New version.

* Mon Dec 02 2019 Andrey Cherepanov <cas@altlinux.org> 19.08.3-alt1
- New version.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 19.08.2-alt1
- New version.

* Sun Aug 25 2019 Andrey Cherepanov <cas@altlinux.org> 19.08.0-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.5-alt1
- New version.

* Sun Dec 10 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- New version.

* Thu Jun 30 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt2
- Rename package to kde5-yakuake (ALT #32098)

* Mon Jun 20 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version on KF5
- Place in standard directories
- Requires kde-konsole

* Thu Apr 04 2013 Andrey Cherepanov <cas@altlinux.org> 2.9.9-alt1
- New version 2.9.9

* Sat Jul 17 2010 Andrey Rahmatullin <wrar@altlinux.org> 2.9.7-alt1
- 2.9.7

* Tue Jun 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.6-alt2
- rename back to yakuake

* Fri May 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.6-alt1
- 2.9.6

* Tue May 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.5-alt1
- 2.9.5

* Mon Nov 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.4-alt3
- remove update_*/clean_* invocations

* Wed Oct 29 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.4-alt2
- Sisyphus build
- rename to kde4-yakuake, enable __kde4_alternate_placement

* Sat Sep 06 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.4-alt1
- 2.9.4

* Sat Aug 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.3-alt2
- rebuild

* Mon Jun 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.3-alt1
- 2.9.3

* Sat May 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.2-alt1
- 2.9.2
- use %%K4find_lang

* Sun Mar 30 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Mon Mar 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.9-alt1
- 2.9 (KDE4 version)
- Daedalus build

* Sun Feb 10 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Nov 20 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.8-alt2
- spec cleanup
- enable _unpackaged_files_terminate_build
- fix packaging of icons (#10173, php-coder@)

* Sat Oct 13 2007 Nick S. Grechukh <gns@altlinux.org> 2.8-alt1
- new version (wrar@ reminded ;)

* Thu May 04 2006 Nick S. Grechukh <gns@altlinux.org> 2.7.5-alt1
- new version. fixed Url and Source. i18n removed (fixed in upstream)

* Mon Feb 13 2006 Nick S. Grechukh <gns@altlinux.org> 2.7.3-alt5
- removed kdedesktop2mdkmenu

* Sun Nov 13 2005 Nick S. Grechukh <gns@altlinux.ru> 2.7.3-alt4
- new version with i18n patch from Albert Valiev

* Mon Oct 24 2005 Nick S. Grechukh <gns@altlinux.org> 2.7.2-alt1
- new version

* Thu Oct 13 2005 Nick S. Grechukh <gns@altlinux.org> 2.6-alt1
- initial build
