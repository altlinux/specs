%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname kglobalacceld

%define sover 0
%define libkglobalacceld libkglobalacceld%sover

Name: plasma6-%rname
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Global Shortcuts Server
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kf5-kglobalaccel = %EVR
Obsoletes: kf5-kglobalaccel < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libxcb-devel libxcbutil-keysyms-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kglobalaccel-devel kf6-kservice-devel kf6-kio-devel kf6-kjobwidgets-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common >= %EVR
Requires: %libkglobalacceld
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkglobalacceld
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkglobalacceld
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
#%_datadir/qlogging-categories6/*.*categories

%files
%_K6libexecdir/kglobalacceld
%_K6plug/org.kde.kglobalacceld.platforms/*.so
%_K6start/kglobalacceld.desktop
%_userunitdir/*.service

%files -n %libkglobalacceld
%_K6lib/libKGlobalAccelD.so.%sover
%_K6lib/libKGlobalAccelD.so.*

%files devel
%_K6inc/KGlobalAccelD/
#%_K6link/lib*.so
%_K6lib/cmake/KGlobalAccelD/

%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

