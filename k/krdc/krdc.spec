%define rname krdc

%define sover 5
%define libkrdccore libkrdccore%sover

Name: %rname
Version: 26.04.1
Release: alt1
%K6init

Group: Networking/Remote access
Summary: Remote Desktop Client
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-krdc = %EVR
Obsoletes: kde5-krdc < %EVR
#Requires: /usr/bin/winpr-makecert

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-wayland-devel
BuildRequires: libvncserver-devel libssh-devel libfuse3-devel
BuildRequires: libfreerdp3-devel /usr/bin/winpr-makecert
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcompletion-devel kf6-kdnssd-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-knotifications-devel
BuildRequires: kf6-kservice-devel kf6-kwallet-devel kf6-kxmlgui-devel kf6-knotifyconfig-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kio-devel kf6-kstatusnotifieritem-devel
BuildRequires: plasma6-activities-devel

%description
Remote Desktop Client.
is a client application that allows you to view or even control
the desktop session on another machine that is running a compatible server.
VNC and RDP is supported.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-krdc-common = %EVR
Obsoletes: kde5-krdc-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkrdccore
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkrdccore
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data krdc kio

mv %buildroot/%_datadir/mime/packages/org.kde.krdc{,6}-mime.xml

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_datadir/mime/packages/*krdc*.xml

%files
%_K6bin/krdc
%_K6plug/krdc/
%_K6xdgapp/org.kde.krdc.desktop
%_K6icon/*/*/apps/*krdc*
%_K6cfg/krdc.kcfg
#%_K6data/kio/servicemenus/*rdc*.desktop
%_datadir/metainfo/*.xml

%files devel
%_K6inc/krdccore_export.h
%_K6inc/krdc/
%_K6link/lib*.so

%files -n %libkrdccore
%_K6lib/libkrdccore.so.%sover
%_K6lib/libkrdccore.so.*


%changelog
* Fri May 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

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

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt2
- update requires

* Wed Nov 13 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Oct 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

