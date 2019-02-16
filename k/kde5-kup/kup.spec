Name:     kde5-kup
Version:  0.7.3
Release:  alt1

Summary:  Kup is a KDE-based frontend for the very excellent bup backup software, that gives you easy and fast incremental backups!
License:  GPLv2+
Group:    Archiving/Backup
URL:      https://github.com/spersson/Kup

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   kup-%version.tar

ExclusiveArch: %ix86 x86_64

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libgit2-devel
BuildRequires: libhttp-parser-devel
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kidletime-devel
BuildRequires: kf5-kinit-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-plasma-framework-devel
BuildRequires: kf5-solid-devel

Provides: kde4-kup = %EVR
Obsoletes: kde4-kup < %EVR

Requires: bup

%description
Kup is a KDE-based frontend for the very excellent bup backup software,
that gives you easy and fast incremental backups!

%prep
%setup -n kup-%version

%build
#add_optflags -fPIC
%K5init no_altplace
%K5build -DQMAKE_EXECUTABLE=%_bindir/qmake-qt5

%install
%K5install
%find_lang --all %name

%files -f %name.lang
%doc README.md
%_bindir/kup-*
%_K5link/libgit24kup.so
%_K5start/kup-daemon.desktop
%_libdir/libgit24kup.so.*
%_libdir/libkdeinit5_kup-daemon.so
%_qt5_plugindir/*.so
%_qt5_plugindir/plasma/dataengine/*.so
%_K5data/plasma/plasmoids/org.kde.kupapplet
%_K5data/plasma/services/kupservice.operations
%_K5notif/kupdaemon.notifyrc
%_K5srv/*.protocol
%_K5srv/*.desktop
%_datadir/metainfo/*.appdata.xml
%_K5srv/kcm_kup.desktop
%_iconsdir/hicolor/scalable/apps/kup.svgz

%changelog
* Sat Feb 09 2019 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- New version.

* Wed Feb 15 2012 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- New version 0.2

* Sun Jan 29 2012 Andrey Cherepanov <cas@altlinux.org> 0.1-alt2
- Add requirement of bup

* Fri Jan 27 2012 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus

