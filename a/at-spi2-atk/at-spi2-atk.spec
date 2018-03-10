%def_disable snapshot

%define ver_major 2.26
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

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.32
%define core_ver 2.26.0
%define atk_ver 2.26.0

Requires: at-spi2-core >= %core_ver

BuildRequires: meson libdbus-devel libgio-devel >= %glib_ver libatk-devel >= %atk_ver
BuildRequires: libat-spi2-core-devel >= %core_ver libxml2-devel libX11-devel libICE-devel libSM-devel
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
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
#%%meson_test

%files -f %name.lang
%_libdir/libatk-bridge-%api_ver.so.*
%_libdir/gtk-2.0/modules/libatk-bridge.so
%_libdir/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
%doc AUTHORS README NEWS


%files devel
%dir %_includedir/%name
%dir %_includedir/%name/%api_ver
%_includedir/%name/%api_ver/atk-bridge.h
%_libdir/libatk-bridge-%api_ver.so
%_pkgconfigdir/atk-bridge-%api_ver.pc

%changelog
* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Tue Aug 30 2016 Yuri N. Sedunov <aris@altlinux.org> 2.21.91-alt1
- 2.21.91

* Tue Apr 12 2016 Yuri N. Sedunov <aris@altlinux.org> 2.20.1-alt1
- 2.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 2.18.1-alt1
- 2.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 2.18.0-alt1
- 2.18.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 2.14.1-alt1
- 2.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt1
- 2.14.0

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 2.12.1-alt1
- 2.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 2.12.0-alt1
- 2.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt1
- 2.10.2

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- 2.10.0

* Wed Apr 17 2013 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

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

