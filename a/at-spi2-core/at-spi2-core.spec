%define ver_major 2.26
%define api_ver 2.0
%define _libexecdir %_prefix/libexec
%def_enable introspection
%def_enable x11
%def_disable xevie
%def_enable docs
%def_disable check

Name: at-spi2-core
Version: %ver_major.2
Release: alt1

Summary: Protocol definitions and daemon for D-Bus at-spi
Group: System/Libraries
License: LGPLv2+
Url: http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: lib%name = %version-%release
Requires: dbus-tools-gui

BuildRequires(pre): meson
BuildRequires: libgio-devel >= 2.36.0 libdbus-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_x11:BuildRequires: libXtst-devel libXext-devel libXi-devel libICE-devel libSM-devel}
%{?_enable_xevie:BuildRequires: libXevie-devel}
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

%build
%meson \
    -Ddbus_daemon=/bin \
    %{?_disable_x11:-Denable-x11=false} \
    %{?_disable_introspection:-Denable-introspection=false} \
    %{?_enable_docs:-Denable_docs=true}

%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%_libexecdir/at-spi2-registryd
%_libexecdir/at-spi-bus-launcher
%_datadir/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
%_datadir/dbus-1/services/org.a11y.Bus.service
%_datadir/defaults/at-spi2/accessibility.conf
%_sysconfdir/xdg/autostart/at-spi-dbus-bus.desktop
%_prefix/lib/systemd/user/at-spi-dbus-bus.service
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
* Fri Dec 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- 2.22.1

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Wed Jul 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt1
- 2.21.4

* Mon May 30 2016 Yuri N. Sedunov <aris@altlinux.org> 2.20.2-alt1
- 2.20.2

* Tue Apr 12 2016 Yuri N. Sedunov <aris@altlinux.org> 2.20.1-alt1
- 2.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Wed Nov 11 2015 Yuri N. Sedunov <aris@altlinux.org> 2.18.3-alt1
- 2.18.3

* Sun Nov 08 2015 Yuri N. Sedunov <aris@altlinux.org> 2.18.2-alt1
- 2.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 2.18.1-alt1
- 2.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 2.18.0-alt1
- 2.18.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 2.14.1-alt1
- 2.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt1
- 2.14.0

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.12.0-alt1
- 2.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt1
- 2.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- 2.10.0

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Dec 11 2012 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- 2.6.3

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

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

