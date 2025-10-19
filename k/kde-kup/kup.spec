Name:     kde-kup
Version:  0.10.0
Release:  alt1

Summary:  KDE-based frontend for bup backup software and incremental backups
License:  GPL-2.0+
Group:    Archiving/Backup

Url:      https://invent.kde.org/system/kup.git
Source:   kup-%version.tar

ExclusiveArch: %ix86 x86_64 %e2k

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libgit2-devel
BuildRequires: libhttp-parser-devel
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kidletime-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: plasma6-lib-devel
BuildRequires: plasma6-plasma5support-devel
BuildRequires: kf6-solid-devel
BuildRequires: kf6-kcmutils-devel

Provides: kde4-kup = %EVR
Obsoletes: kde4-kup < %EVR
Provides: kde5-kup = %EVR
Obsoletes: kde5-kup < %EVR

Requires: bup

%description
Kup is a KDE-based frontend for the very excellent bup backup software,
that gives you easy and fast incremental backups!

%prep
%setup -n kup-%version

%build
%K6init no_altplace
%K6build -Wno-dev -DQT_MAJOR_VERSION=6 -DQMAKE_EXECUTABLE=%_bindir/qmake-qt6

%install
%K6install
%find_lang --all %name

%files -f %name.lang
%doc README.md
%_K6bin/kup-*
%_K6start/kup-daemon.desktop
%_K6notif/kupdaemon.notifyrc
%_datadir/metainfo/*.appdata.xml
%_K6icon/hicolor/scalable/apps/kup.svg
%_qt6_plugindir/*
%_desktopdir/*.desktop
%_datadir/plasma/plasmoids/org.kde.kupapplet
%_datadir/plasma5support/services/*.operations
%_datadir/qlogging-categories6/kup.categories

%changelog
* Sun Oct 19 2025 Andrey Cherepanov <cas@altlinux.org> 0.10.0-alt1
- New version.
- Renamed to kde-kup.
- Built with KF6.

* Mon Oct 30 2023 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt2.1
- NMU: fix files location (closes: 48219)

* Thu Oct 26 2023 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt2
- FTBFS: fixed plasmoid and operations location.

* Mon Aug 16 2021 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1.1
- EA += %%e2k (builds just fine)
- minor spec cleanup

* Sat Jul 24 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- New version.
- New upstream URL.

* Sat Feb 09 2019 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- New version.

* Wed Feb 15 2012 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- New version 0.2

* Sun Jan 29 2012 Andrey Cherepanov <cas@altlinux.org> 0.1-alt2
- Add requirement of bup

* Fri Jan 27 2012 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus

