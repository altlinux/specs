%define rname ksystemlog

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Monitoring
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-ksystemlog = %EVR
Obsoletes: kde5-ksystemlog < %EVR

Source: %rname-%version.tar
Patch1: alt-modes.patch
Patch2: alt-open-empty-file.patch
Patch3: alt-postfix-mode.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libsystemd-devel libaudit-devel
BuildRequires: kf6-karchive-devel kf6-kdoctools-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-ktextwidgets-devel

%description
This program is developed for being used by beginner users,
which don't know how to find information about their Linux system,
and how the log files are in their computer.
But it is also designed for advanced users,
who want to quickly see problems occuring on their server.


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

%files -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/ksystemlog
%_K6xdgapp/org.kde.ksystemlog.desktop
%_datadir/metainfo/*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

