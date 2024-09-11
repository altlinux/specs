%define rname plasma-thunderbolt

%define sover 6
%define libkbolt libkbolt%sover

Name: %rname
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma 6
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-thunderbolt = %EVR
Obsoletes: plasma5-thunderbolt < %EVR
Requires: bolt

Source: %rname-%version.tar
Patch1: alt-soversion.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-wayland-devel
BuildRequires: kf6-kcmutils-devel kf6-kconfigwidgets-devel kf6-kdbusaddons-devel kf6-kdeclarative-devel
BuildRequires: kf6-ki18n-devel kf6-knotifications-devel kf6-kpackage-devel kf6-kservice-devel

%description
This package contains a Plasma Sytem Settings module and a KDED module to
handle authorization of Thunderbolt devices connected to the computer. There's
also a shared library (libkbolt) that implements common interface between the
modules and the system-wide bolt daemon, which does the actual hard work of
talking to the kernel.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-thunderbolt-common = %EVR
Obsoletes: plasma5-thunderbolt-common < %EVR
%description common
%name common package

%package -n %libkbolt
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkbolt
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data kpackage
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6plug/plasma/kcms/systemsettings/kcm_bolt.so
%_K6plug/kf6/kded/*bolt*.so
%_K6notif/*bolt*.notifyrc
%_K6xdgapp/*bolt*.desktop

%files -n %libkbolt
%_K6lib/libkbolt.so.%sover
%_K6lib/libkbolt.so.*


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

