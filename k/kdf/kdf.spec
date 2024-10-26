%define rname kdf

%define kdfprivate_sover 24
%define libkdfprivate libkdfprivate%kdfprivate_sover

Name: %rname
Version: 24.08.2
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
* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

