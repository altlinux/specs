
%define sover 1
%define libpackagekitqt5 libpackagekitqt5_%sover

Name: packagekit-qt
Version: 1.0.1
Release: alt2

Group: System/Libraries
Summary: Qt support library for PackageKit
License: LGPLv2+
Url: http://www.packagekit.org/

Requires: packagekit
Provides: PackageKit-Qt = %version-%release
Provides: PackageKit-Qt5 = %version-%release

# https://github.com/hughsie/PackageKit-Qt
Source: PackageKit-Qt-%version.tar

# Automatically added by buildreq on Thu Aug 02 2018 (-bi)
# optimized out: cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libqt5-core libqt5-dbus libstdc++-devel packagekit perl pkg-config python-base python-modules python3 python3-base qt5-base-common rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: cmake libssl-devel python3-dev qt5-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake libssl-devel qt5-base-devel
BuildRequires: libpackagekit-glib-devel

%description
PackageKit-Qt is a Qt support library for PackageKit

%package -n %libpackagekitqt5
Summary: %name library
Group: System/Libraries
%description -n %libpackagekitqt5
%name library.

%package devel
Group: Development/KDE and QT
Summary: Development files for PackageKit-Qt
Provides: PackageKit-Qt5-devel = %version-%release
%description devel
%summary.

%prep
%setup -qn PackageKit-Qt-%version

%build
%cmake

%cmake_build

%install
%cmakeinstall_std


%files -n %libpackagekitqt5
%doc AUTHORS NEWS COPYING
%_libdir/libpackagekitqt5.so.%sover
%_libdir/libpackagekitqt5.so.*

%files devel
%_libdir/lib*.so
%_libdir/pkgconfig/packagekitqt5.pc
%_includedir/packagekitqt5/
%_libdir/cmake/packagekitqt5/

%changelog
* Thu Dec 27 2018 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt2
- fix build requires

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1%ubt
- initial build
