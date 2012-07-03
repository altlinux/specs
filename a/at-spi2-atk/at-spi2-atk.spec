%define ver_major 2.4
%define api_ver 2.0
%define _libexecdir %_prefix/libexec
%def_enable introspection

Name: at-spi2-atk
Version: %ver_major.0
Release: alt1

Summary: A GTK+ module that bridges ATK to D-Bus at-spi
Group: Accessibility
License: LGPLv2+
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus

Source: ftp://ftp.gnome.org/pub/sources/%name/%ver_major/%name-%version.tar.xz

%define core_ver 2.3.90

Requires: at-spi2-core >= %core_ver

BuildRequires: libdbus-devel libgio-devel libatk-devel libat-spi2-core-devel >= %core_ver
BuildRequires: libX11-devel libICE-devel libSM-devel
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

%prep
%setup

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_libdir/gtk-2.0/modules/libatk-bridge.so
%_libdir/gtk-3.0/modules/libatk-bridge.so
%_datadir/glib-2.0/schemas/org.a11y.atspi.gschema.xml
%_libdir/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
%doc AUTHORS README NEWS

%exclude %_libdir/gtk-*/modules/libatk-bridge.la

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Nov 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Oct 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- first build for people/gnome

