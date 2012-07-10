%define lib_major 2

Name: dbusmenu-qt
Version: 0.9.2
Release: alt1

Group: System/Libraries
Summary: A Qt implementation of the DBusMenu protocol
License: LGPLv2+
URL: http://gitorious.org/dbusmenu/

Source: libdbusmenu-qt-%{version}.tar

# Automatically added by buildreq on Tue Jan 18 2011 (-bi)
#BuildRequires: cmake gcc-c++ libqt3-devel qjson-devel qt4-designer
BuildRequires: cmake gcc-c++ libqt4-devel kde-common-devel qjson-devel doxygen

%description
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%package -n libdbusmenu-qt%lib_major
Group: System/Libraries
Summary: A Qt implementation of the DBusMenu protocol
%description -n libdbusmenu-qt%lib_major
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%package -n libdbusmenu-qt-devel
Summary: Development files for %{name}
Group: Development/KDE and QT
Requires: libdbusmenu-qt%lib_major = %{version}-%{release}
%description -n libdbusmenu-qt-devel
Development files for %{name}

%prep
%setup -qn lib%name-%version


%build
%Kbuild

%install
%Kinstall

%files -n libdbusmenu-qt%lib_major
%doc COPYING README
%_libdir/libdbusmenu-qt.so.%lib_major
%_libdir/libdbusmenu-qt.so.%lib_major.*

%files -n libdbusmenu-qt-devel
%_includedir/dbusmenu-qt/
%_libdir/libdbusmenu-qt.so
%_pkgconfigdir/dbusmenu-qt.pc

%changelog
* Tue Jul 10 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt1
- new version

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt0.M60P.1
- built for M60P

* Sat Jan 28 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.5-alt2
- fix to build

* Tue Jan 18 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.5-alt1
- new version

* Tue Aug 10 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.2-alt1
- new version

* Wed Jul 21 2010 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- initial specfile

