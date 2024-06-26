%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname libkscreen
Name: plasma6-%rname
Version: 6.1.1
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE Frameworks 6 display configuration library
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-pnp-ids-path.patch

BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules
BuildRequires: qt6-tools-devel
BuildRequires: qt6-wayland-devel plasma-wayland-protocols
BuildRequires: kf6-kconfig-devel

%description
LibKScreen is a library that provides access to current configuration
of connected displays and ways to change the configuration.

%package utils
Group: Graphical desktop/KDE
Summary: %name utils
Requires: %name-common >= %EVR
%_K6if_ver_gteq %ubt_id M120
Conflicts: plasma5-libkscreen-utils
#Provides: plasma5-libkscreen-utils = %EVR
#Obsoletes: plasma5-libkscreen-utils < %EVR
%else
Conflicts: plasma5-libkscreen-utils
%endif
%description utils
%name utils.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6screen
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Requires: hwdatabase
%description -n libkf6screen
%name library

%package -n libkf6screendpms
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n libkf6screendpms
%name library

%prep
%setup -n %rname-%version
%patch1 -p1

%build
export PATH=%_qt6_bindir:$PATH
%K6build

%install
%K6install
%K6install_move data locale
%find_lang %name --all-name
%K6find_qtlang %name --append --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files utils
%_K6bin/*
%_K6exec/kscreen_backend_launcher
%_K6plug/kf6/kscreen/
%_K6dbus_srv/org.kde.kscreen.service
%_userunitdir/*.service
%_datadir/zsh/site-functions/_*

%files devel
%_K6inc/kscreen_version.h
%_K6inc/KScreen/
%_K6link/lib*.so
%_K6lib/cmake/KF6Screen
%_pkgconfigdir/*.pc

%files -n libkf6screen
%_K6lib/libKF6Screen.so.*

%files -n libkf6screendpms
%_K6lib/libKF6ScreenDpms.so.*


%changelog
* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

