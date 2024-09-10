%define rname kded
%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif
%define service_name plasma-kded6

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE Frameworks 6 central daemon of KDE work spaces
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: %name-common

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: libsystemd-devel
BuildRequires: docbook-style-xsl extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools-devel kf6-kservice-devel

%description
KDED stands for KDE Daemon which isn't very descriptive.
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.

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
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6ded
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6ded
KF6 library

%prep
%setup -n %rname-%version

%build
%K6build \
    #

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name


%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files
%_bindir/kded6
%_K6bin/kded6
%_K6xdgapp/*.desktop
%_datadir/dbus-1/services/*.service
%_userunitdir/%service_name.service

%files devel
%_K6lib/cmake/KF6KDED/
%_K6dbus_iface/*.xml


%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

