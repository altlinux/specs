%define rname solid

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 desktop hardware abstraction
Url: http://www.kde.org
License: LGPL-2.1-or-later

Requires: upower udisks2 media-player-info

Source: %name-%version.tar

Patch1: alt-hack-repeat-unmount.patch

# Automatically added by buildreq on Mon Jan 19 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt6-concurrent libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-qml libqt6-test libqt6-widgets libqt6-xml libstdc++-devel python-base qt6-base-devel qt6-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules flex gcc-c++ libudev-devel media-player-info python-module-google qt6-declarative-devel qt6-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-dkf6
BuildRequires: libplist-devel libimobiledevice-devel libusbmuxd-devel libmount-devel
BuildRequires: deepin-extra-cmake-modules flex bison libudev-devel dqt6-declarative-devel dqt6-tools-devel
BuildRequires: vulkan-headers libdqt6-xml libdqt6-gui

# find libraries
%add_findprov_lib_path %_DK6lib

%description
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
# Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libdkf6solid
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
Requires: media-player-info
%description -n libdkf6solid
KF6 library


%prep
%setup -n %name-%version
%patch1 -p2 -b .reunmount

%build
%DK6build ||:
# hack against ALTBUG#32378
sed -i '/num_to_alloc.*\/\//s|//\(.*\)|/* \1 */|' BUILD/src/solid/predicate_lexer.c ||:
%DK6make

%install
%DK6install
%find_lang %name --all-name
%DK6find_qtlang %name --all-name

%files
%exclude %_bindir/solid-hardware6
%_DK6bin/solid-hardware6
#%_DK6bin/solid-power
#%_DK6qml/org/kde/solid/

%files common -f %name.lang
%doc LICENSES/* README.md
%_DK6data/qlogging-categories6/*.*categories

%files devel
#%_DK6inc/solid_version.h
%_DK6inc/Solid/
%_DK6link/lib*.so
%_DK6lib/cmake/KF6Solid

%files -n libdkf6solid
%_DK6lib/libKF6Solid.so.*


%changelog
* Thu Aug 20 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
- fork for independent deepin build

* Tue Jul 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.28.0-alt1
- new version

* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

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

