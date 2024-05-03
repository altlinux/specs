
%define sover 1
%define libpackagekitqt6 libpackagekitqt6_%sover

Name: packagekit-qt6
Version: 1.1.1
Release: alt1

Group: System/Libraries
Summary: Qt support library for PackageKit
License: LGPL-2.0-or-later
Url: https://www.freedesktop.org/software/PackageKit/

# https://github.com/PackageKit/PackageKit-Qt
Source: PackageKit-Qt-%version.tar
# SuSE
Patch1: 0001-Fix-PackageKit-not-emitting-network-state-changed-signal.patch

BuildRequires: cmake libssl-devel qt6-base-devel
BuildRequires: libpackagekit-glib-devel

%description
PackageKit-Qt is a Qt support library for PackageKit

%package -n %libpackagekitqt6
Summary: %name library
Group: System/Libraries
#Requires: packagekit
Provides: PackageKit-Qt6 = %version-%release
%description -n %libpackagekitqt6
%name library.

%package devel
Group: Development/KDE and QT
Summary: Development files for PackageKit-Qt
Provides: PackageKit-Qt6-devel = %version-%release
%description devel
%summary.

%prep
%setup -qn PackageKit-Qt-%version
%patch1 -p1

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif

%cmake \
    -DBUILD_WITH_QT6:BOOL=ON \
    #
%cmake_build

%install
%cmakeinstall_std


%files -n %libpackagekitqt6
%doc AUTHORS NEWS COPYING
%_libdir/libpackagekitqt6.so.%sover
%_libdir/libpackagekitqt6.so.*

%files devel
%_libdir/lib*.so
%_libdir/pkgconfig/packagekitqt6.pc
%_includedir/packagekitqt6/
%_libdir/cmake/packagekitqt6/

%changelog
* Fri May 03 2024 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- initial build
