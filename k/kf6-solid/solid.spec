%define rname solid

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 desktop hardware abstraction
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: upower udisks2 media-player-info

Source: %rname-%version.tar

Patch1: alt-hack-repeat-unmount.patch

# Automatically added by buildreq on Mon Jan 19 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt6-concurrent libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-qml libqt6-test libqt6-widgets libqt6-xml libstdc++-devel python-base qt6-base-devel qt6-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules flex gcc-c++ libudev-devel media-player-info python-module-google qt6-declarative-devel qt6-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: libplist-devel libimobiledevice-devel libusbmuxd-devel libmount-devel
BuildRequires: extra-cmake-modules flex bison libudev-devel qt6-declarative-devel qt6-tools-devel

%description
Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.

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

%package -n libkf6solid
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
Requires: media-player-info
%description -n libkf6solid
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p2

%build
%K6build ||:
# hack against ALTBUG#32378
sed -i '/num_to_alloc.*\/\//s|//\(.*\)|/* \1 */|' BUILD/src/solid/predicate_lexer.c ||:
%K6make

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files
%_bindir/solid-hardware6
%_K6bin/solid-hardware6
#%_K6bin/solid-power
#%_K6qml/org/kde/solid/

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/solid_version.h
%_K6inc/Solid/
%_K6link/lib*.so
%_K6lib/cmake/KF6Solid

%files -n libkf6solid
%_K6lib/libKF6Solid.so.*


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

