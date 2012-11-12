%define ver_major 2.6
%define api_ver 2.0
%define _libexecdir %_prefix/libexec
%def_enable introspection

Name: at-spi2-atk
Version: %ver_major.2
Release: alt1

Summary: A GTK+ module that bridges ATK to D-Bus at-spi
Group: Accessibility
License: LGPLv2+
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus

Source: ftp://ftp.gnome.org/pub/sources/%name/%ver_major/%name-%version.tar.xz

%define core_ver 2.5.91
%define atk_ver 2.5.91

Requires: at-spi2-core >= %core_ver

BuildRequires: libdbus-devel libgio-devel libatk-devel >= %atk_ver
BuildRequires: libat-spi2-core-devel >= %core_ver libX11-devel libICE-devel libSM-devel
BuildRequires: intltool

%description
at-spi allows assistive technologies to access GTK-based applications.
Essentially it exposes the internals of applications for automation, so
tools such as screen readers, magnifiers, or even scripting interfaces
can query and interact with GUI controls.

This version of at-spi is a major break from previous versions. It has
been completely rewritten to use D-Bus rather than ORBIT/CORBA for its
transport protocol.

This package includes a gtk-modules that bridges ATK to the new D-Bus
based at-spi.

%package devel
Summary: Development files for atk-bridge
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides development files for atk-bridge library.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_libdir/libatk-bridge-%api_ver.so.*
%_libdir/gtk-2.0/modules/libatk-bridge.so
%_datadir/glib-2.0/schemas/org.a11y.atspi.gschema.xml
%_libdir/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
%doc AUTHORS README NEWS

%exclude %_libdir/gtk-*/modules/libatk-bridge.la

%files devel
%dir %_includedir/%name
%dir %_includedir/%name/%api_ver
%_includedir/%name/%api_ver/atk-bridge.h
%_libdir/libatk-bridge-%api_ver.so
%_pkgconfigdir/atk-bridge-%api_ver.pc

%changelog
* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Nov 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Oct 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- first build for people/gnome

