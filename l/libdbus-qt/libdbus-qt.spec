Name: libdbus-qt
Version: 0.62
Release: alt9.1.1
Summary: QT3/KDE bindings for D-Bus
URL: http://dbus.freedesktop.org/
License: GPL or Academic Free License
Group: System/Libraries

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: dbus-qt3-%version.tar.bz2

Patch0: dbus-qt3-compile-fix-thoenig-01.patch
Patch1: dbus-qt3-do-not-close-shared-connection-thoenig-01.patch
Patch2: dbus-qt3-0.62-alt-new-autotools.patch
Patch3: dbus-qt3-0.62-fix-autoconf-2.64.patch

# Automatically added by buildreq on Mon Dec 18 2006
BuildRequires: gcc-c++ libXext-devel libXt-devel libdbus-devel libjpeg-devel libpng-devel libqt3-devel

%description
QT3/KDE bindings for D-Bus.

%package devel
Summary: Developer package for QT3/KDE bindings for D-Bus
Requires: %name = %version-%release
Requires: libdbus-devel >= 0.94
Requires: libqt3-devel
Group: Development/C++

%description devel
Developer package for QT3/KDE bindings for D-Bus.

%prep
%setup -q -n dbus-qt3-%version
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build

%make -f admin/Makefile.common cvs
%configure \
	--disable-static
%make

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/dbus-1.0/dbus/*.h
%_libdir/*.so

%changelog
* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.62-alt9.1.1
- rebuild (with the help of girar-nmu utility)

* Sat May 22 2010 Motsyo Gennadi <drool@altlinux.ru> 0.62-alt9.1
- fix build with autoconf-2.64

* Wed Aug 26 2009 Ilya Mashkin <oddity@altlinux.ru> 0.62-alt9
- Rebuild with automake 1.10

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.62-alt8
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Jan 03 2008 Igor Zubkov <icesik@altlinux.org> 0.62-alt7
- fix rebuild with new autotools

* Sun Dec 24 2006 Igor Zubkov <icesik@altlinux.org> 0.62-alt6
- add libdbus-devel >= 0.94 to buildprereq

* Mon Dec 18 2006 Igor Zubkov <icesik@altlinux.org> 0.62-alt5
- buildreq

* Tue Dec 05 2006 Igor Zubkov <icesik@altlinux.org> 0.62-alt4
- bump version

* Tue Dec 05 2006 Igor Zubkov <icesik@altlinux.org> 0.62-alt1
- Initial build for Sisyphus

