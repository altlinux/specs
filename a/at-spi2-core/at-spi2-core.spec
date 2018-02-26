%define ver_major 2.4
%define api_ver 2.0
%define _libexecdir %_prefix/libexec
%def_enable introspection

Name: at-spi2-core
Version: %ver_major.2
Release: alt1

Summary: Protocol definitions and daemon for D-Bus at-spi
Group: System/Libraries
License: LGPLv2+
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus

Source: ftp://ftp.gnome.org/pub/sources/%name/%ver_major/%name-%version.tar.xz
Patch: %name-2.2.0-alt-introspection.patch

Requires: lib%name = %version-%release
Requires: dbus-tools-gui

BuildRequires: libgio-devel >= 2.31.0
BuildRequires: libdbus-devel gobject-introspection-devel
BuildRequires: libXtst-devel libXext-devel libXi-devel
BuildRequires: libXevie-devel libICE-devel libSM-devel
BuildRequires: intltool gtk-doc

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT/CORBA for its transport protocol.

%package -n lib%name
Summary: Shared at-spi library
Group: System/Libraries

%description -n lib%name
This package contains shared library needed to run at-spi daemon.

%package -n lib%name-devel
Summary: Development files and headers for at-spi2-core
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package includes the header files and API documentation for
libatspi.

%package -n lib%name-gir
Summary: GObject introspection data for at-spi2-core
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for at-spi library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for at-spi2-core
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the at-spi library.

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
This package contains documentation for developing applications that use
%name library.

%prep
%setup
%patch

%build
%autoreconf
%configure \
    --with-dbus-daemondir=/bin \
    %{?_disable_introspection:--enable-introspection=no}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_libexecdir/at-spi2-registryd
%_libexecdir/at-spi-bus-launcher
%_datadir/dbus-1/services/org.a11y.atspi.Registry.service
%_datadir/dbus-1/services/org.a11y.Bus.service
%_sysconfdir/at-spi2
%_sysconfdir/xdg/autostart/at-spi-dbus-bus.desktop
%doc AUTHORS README NEWS

%files -n lib%name
%_libdir/libatspi.so.*

%files -n lib%name-devel
%_libdir/libatspi.so
%_includedir/at-spi-%api_ver
%_libdir/pkgconfig/atspi-2.pc

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Atspi-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Atspi-%api_ver.gir
%endif

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/libatspi

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Nov 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Tue Nov 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Oct 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- first build for people/gnome

