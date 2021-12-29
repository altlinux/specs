
%define sover 1
%define libpackagekitqt5 libpackagekitqt5_%sover

Name: packagekit-qt
Version: 1.0.2
Release: alt1

Group: System/Libraries
Summary: Qt support library for PackageKit
License: LGPL-2.0-or-later
Url: http://www.packagekit.org/

# https://github.com/hughsie/PackageKit-Qt
Source: PackageKit-Qt-%version.tar

# Automatically added by buildreq on Thu Aug 02 2018 (-bi)
# optimized out: cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libqt5-core libqt5-dbus libstdc++-devel packagekit perl pkg-config python-base python-modules python3 python3-base qt5-base-common rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: cmake libssl-devel python3-dev qt5-base-devel rpm-build-ruby
BuildRequires: cmake libssl-devel qt5-base-devel
BuildRequires: libpackagekit-glib-devel

%description
PackageKit-Qt is a Qt support library for PackageKit

%package -n %libpackagekitqt5
Summary: %name library
Group: System/Libraries
#Requires: packagekit
Provides: PackageKit-Qt5 = %version-%release
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
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif

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
* Wed Dec 29 2021 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- new version

* Thu Aug 01 2019 Michael Shigorin <mike@altlinux.org> 1.0.1-alt4
- E2K: explicit -std=c++11

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3
- NMU: remove rpm-build-ubt from BR:

* Thu Dec 27 2018 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt2
- fix build requires

* Tue Aug 07 2018 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- initial build
