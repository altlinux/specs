%define rname kdf

%define kdfprivate_sover 26
%define libkdfprivate libkdfprivate%kdfprivate_sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: File devices mount info
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-kdf = %EVR
Obsoletes: kde5-kdf < %EVR
Provides: kwikdisk = %EVR

Source: %rname-%version.tar
Patch1: alt-desktop.patch
Patch2: alt-mount.patch
Patch3: alt-fix-default-window-size.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kcmutils-devel kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-knotifications-devel
BuildRequires: kf6-kstatusnotifieritem-devel

%description
KDiskFree displays the available file devices (hard drive
partitions, floppy and CD-drives, USB sticks, etc) along with information on
their capacity, free space, type and mount point.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-kdf-common = %EVR
Obsoletes: kde5-kdf-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkdfprivate
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
Obsoletes: libkdfprivate23 < %EVR
%description -n %libkdfprivate
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/kdf
%_K6bin/kwikdisk
%_K6plug/plasma/kcms/systemsettings_qwidgets/*kdf*.so
%_K6xdgapp/*kdf*.desktop
%_K6xdgapp/*kwikdisk*.desktop
%_K6icon/*/*/apps/kdf.*
%_K6icon/*/*/apps/kwikdisk.*
%_K6icon/*/*/apps/kcmdf.*
%_datadir/metainfo/*kdf*.xml

%files -n %libkdfprivate
%_K6lib/libkdfprivate.so.%kdfprivate_sover
%_K6lib/libkdfprivate.so.*


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 18 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 26.04.1-alt2
- fix incorrect window size on first launch (closes: 49893)

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

