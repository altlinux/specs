%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname libkscreen
Name: plasma6-%rname
Version: 6.7.2
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE Frameworks 6 display configuration library
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar
Patch1: gcc13.patch

BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: libvulkan-devel
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
Provides: plasma5-libkscreen-utils = %EVR
Obsoletes: plasma5-libkscreen-utils < %EVR
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
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_includedir \
    #

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
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Mon Apr 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt2
- add gcc-13 support

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

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

