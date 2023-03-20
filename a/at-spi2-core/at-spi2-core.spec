%define _name at-spi2
%define ver_major 2.48
%define api_ver_major 2
%define api_ver 2.0
%define atk_api_ver 1.0

%define _libexecdir %_prefix/libexec
%def_enable introspection
%def_enable x11
%def_disable xevie
%def_enable doc
%def_disable check

Name: %_name-core
Version: %ver_major.0
Release: alt1

Summary: Protocol definitions and daemon for D-Bus at-spi
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/Accessibility

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: lib%name = %version-%release
Requires: dbus-tools-gui

%define meson_ver 0.63
%define glib_ver 2.67.4
%define dbus_ver 1.5

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-xdg
BuildRequires: meson >= %meson_ver libgio-devel >= %glib_ver libdbus-devel >= %dbus_ver
BuildRequires: libxml2-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_x11:BuildRequires: libXtst-devel libXext-devel libXi-devel libICE-devel libSM-devel}
%{?_enable_xevie:BuildRequires: libXevie-devel}
%{?_enable_doc:BuildRequires: /usr/bin/sphinx-build-3 python3-module-sphinx_rtd_theme gi-docgen}

%description
The Access Technology Service Provider Interface (AT-SPI) is a set of
interfaces that allow access technologies such as screen readers to
programmatically determine what is being displayed on the screen and
simulate keyboard and mouse events. It can also be used for automated
testing.

The at-spi2-core module contains the D-Bus specification, the registry
daemon, and a C library for use by access technologies that provides a
convenient wrapper around the DBus interfaces.

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

%package -n libatk
Summary: Shared ATK library
Group: System/Libraries

%description -n libatk
ATK is a library providing interface definitions that are consumed by
toolkits that wish to integrate with the GNOME accessibility
infrastructure.

This package provides shared ATK library.

%package -n libatk-devel
Summary: Development environment for ATK
Group: Development/C
Requires: libatk = %EVR

%description -n libatk-devel
ATK is a library providing interface definitions that are consumed by
toolkits that wish to integrate with the GNOME accessibility
infrastructure.

This package contains the necessary components to develop for ATK.

%package -n libatk-devel-doc
Summary: Development documentation for ATK
Group: Development/C
BuildArch: noarch
Conflicts: libatk < %version-%release

%description -n libatk-devel-doc
ATK is a library providing interface definitions that are consumed by
toolkits that wish to integrate with the GNOME accessibility
infrastructure.

This package contains development documentation for ATK.

%package -n libatk-gir
Summary: GObject introspection data for the Atk library
Group: System/Libraries
Requires: libatk = %EVR

%description -n libatk-gir
GObject introspection data for the Atk library

%package -n libatk-gir-devel
Summary: GObject introspection devel data for the Atk library
Group: Development/Other
BuildArch: noarch
Requires: libatk-devel = %EVR
Requires: libatk-gir = %EVR

%description -n libatk-gir-devel
GObject introspection devel data for the Atk library.

%package -n %_name-atk
Summary: Shared at-spi library
Group: System/Libraries
Requires: libatk = %EVR
Requires: lib%name = %EVR

%description -n %_name-atk
at-spi2-atk is the library used to bridge ATK to AT-SPI, allowing
applications exposing information via ATK to interface with clients that
use AT-SPI. This module provides the necessary inter-process
communication to allow accessibility-oriented software to operate.

This package contains shared library needed to run at-spi daemon.

%package -n %_name-atk-devel
Summary: Development files for atk-bridge
Group: Development/C
Requires: %_name-atk = %EVR
Requires: lib%name-devel = %EVR

%description -n %_name-atk-devel
This package provides development files for atk-bridge library.

%prep
%setup
sed -i 's/\(sphinx-build\)/\1-3/' devel-docs/meson.build

%build
%meson \
    -Ddbus_daemon=/bin/dbus-daemon \
    %{?_disable_x11:-Dx11=disabled} \
    %{?_disable_introspection:-Dintrospection=disabled} \
    %{?_enable_doc:-Ddocs=true}
%nil
%meson_build
%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_xdgconfigdir/Xwayland-session.d/00-at-spi
%_libexecdir/at-spi2-registryd
%_libexecdir/at-spi-bus-launcher
%_datadir/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
%_datadir/dbus-1/services/org.a11y.Bus.service
%_datadir/defaults/at-spi2/accessibility.conf
%_sysconfdir/xdg/autostart/at-spi-dbus-bus.desktop
%_prefix/lib/systemd/user/at-spi-dbus-bus.service
%doc README* MAINTAINERS NEWS

%files -n lib%name
%_libdir/libatspi.so.*

%files -n lib%name-devel
%_libdir/libatspi.so
%_includedir/at-spi-%api_ver/
%_pkgconfigdir/atspi-%api_ver_major.pc

%files -n libatk
%_libdir/libatk-%atk_api_ver.so.*

%files -n libatk-devel
%_includedir/atk-%atk_api_ver/
%_libdir/libatk-%atk_api_ver.so
%_pkgconfigdir/atk.pc

%files -n %_name-atk
%_libdir/libatk-bridge-%api_ver.so.*
%_libdir/gtk-2.0/modules/libatk-bridge.so
%_libdir/gnome-settings-daemon-3.0/gtk-modules/%_name-atk.desktop

%files -n %_name-atk-devel
%_includedir/%_name-atk/
%_libdir/libatk-bridge-%api_ver.so
%_pkgconfigdir/atk-bridge-%api_ver.pc

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Atspi-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Atspi-%api_ver.gir

%files -n libatk-gir
%_typelibdir/Atk-%atk_api_ver.typelib

%files -n libatk-gir-devel
%_girdir/Atk-%atk_api_ver.gir
%endif

%if_enabled doc
%files -n lib%name-devel-doc
%_datadir/doc/libatspi/

%files -n libatk-devel-doc
%_datadir/doc/atk/
%endif

%changelog
* Sun Mar 19 2023 Yuri N. Sedunov <aris@altlinux.org> 2.48.0-alt1
- 2.48.0

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 2.46.0-alt1
- 2.46.0 (merged with ATK and ati-spi2-atk)

* Fri Apr 22 2022 Yuri N. Sedunov <aris@altlinux.org> 2.44.1-alt1
- 2.44.1

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 2.44.0-alt1
- 2.44.0

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt1
- 2.42.0

* Fri Jul 09 2021 Yuri N. Sedunov <aris@altlinux.org> 2.40.3-alt1
- 2.40.3

* Sat Jun 05 2021 Yuri N. Sedunov <aris@altlinux.org> 2.40.2-alt1
- 2.40.2

* Sat May 01 2021 Yuri N. Sedunov <aris@altlinux.org> 2.40.1-alt1
- 2.40.1

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1
- 2.40.0

* Sun Sep 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt1
- 2.38.0

* Sat Sep 05 2020 Yuri N. Sedunov <aris@altlinux.org> 2.36.1-alt1
- 2.36.1

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1.1
- fixed build without docs

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Mon Mar 04 2019 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sun Dec 31 2017 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt2
- fixed dbus-daemon path

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

