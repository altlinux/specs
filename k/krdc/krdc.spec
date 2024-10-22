%define rname krdc

%define sover 5
%define libkrdccore libkrdccore%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Networking/Remote access
Summary: Remote Desktop Client
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-krdc = %EVR
Obsoletes: kde5-krdc < %EVR
Requires: xfreerdp freerdp-plugins-standard

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvncserver-devel libssh-devel
BuildRequires: libfreerdp-devel xfreerdp freerdp-plugins-standard
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
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/krdc
%_K6plug/krdc/
%_K6xdgapp/org.kde.krdc.desktop
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
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

