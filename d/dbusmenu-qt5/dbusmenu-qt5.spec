%define sover 2

Name: dbusmenu-qt5
Version: 0.9.3
Release: alt0.3

Group: System/Libraries
Summary: A Qt implementation of the DBusMenu protocol
License: LGPLv2+
URL: http://gitorious.org/dbusmenu/

Source: libdbusmenu-qt5-%{version}.tar

# Automatically added by buildreq on Wed Mar 04 2015 (-bi)
# optimized out: cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt4-core libqt5-core libqt5-dbus libqt5-gui libqt5-widgets libstdc++-devel pkg-config python-base ruby ruby-stdlibs
#BuildRequires: cmake doxygen gcc-c++ qjson-devel qt5-base-devel rpm-build-ruby
BuildRequires: kde-common-devel
BuildRequires: cmake doxygen gcc-c++ qt5-base-devel

%description
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%package -n libdbusmenu-qt5%sover
Group: System/Libraries
Summary: A Qt implementation of the DBusMenu protocol
%description -n libdbusmenu-qt5%sover
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%package -n libdbusmenu-qt5-devel
Summary: Development files for %{name}
Group: Development/KDE and QT
%description -n libdbusmenu-qt5-devel
Development files for %{name}

%prep
%setup -qn lib%name-%version


%build
%Kbuild \
    -DUSE_QT4:BOOL=FALSE \
    -DUSE_QT5:BOOL=TRUE \
    #

%install
%Kinstall

%files -n libdbusmenu-qt5%sover
%doc COPYING README
%_libdir/libdbusmenu-qt5.so.%sover
%_libdir/libdbusmenu-qt5.so.%sover.*

%files -n libdbusmenu-qt5-devel
%_includedir/dbusmenu-qt5/
%_libdir/libdbusmenu-qt5.so
%_libdir/cmake/dbusmenu-qt5/
%_pkgconfigdir/dbusmenu-qt5.pc

%changelog
* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt0.3
- update to 20160218 snapshot

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt0.2
- rebuild

* Fri Oct 02 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt0.1
- use 0.9.3 snapshot 15.10.2015

* Wed Mar 04 2015 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt1
- initial build

