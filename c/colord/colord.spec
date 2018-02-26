%def_enable sane
%def_enable reverse
%def_enable introspection
%def_enable vala

%define _libexecdir %_prefix/libexec

Name: colord
Version: 0.1.22
Release: alt1

Summary: Color daemon
License: GPLv2+
Group: Graphics

URL: http://www.freedesktop.org/software/%name/
Source: http://www.freedesktop.org/software/%name/releases/colord-%version.tar.xz
Patch1: %name-0.1.18-alt-localstatedir.patch

%define colord_group %name
%define colord_user %name
%define glib_ver 2.31
%define lcms_ver 2.2

Requires: lib%name = %version-%release
Requires: shared-color-profiles

BuildRequires: glib2-devel >= %glib_ver
BuildRequires: docbook-utils gtk-doc intltool libdbus-devel libgudev-devel
BuildRequires: liblcms2-devel >= %lcms_ver libpolkit-devel >= 0.103 libsane-devel
BuildRequires: libsqlite3-devel libusb-devel libgusb-devel systemd-devel
%{?_enable_sane:BuildRequires: libsane-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools}

%description
colord is a low level system activated daemon that maps color devices to color
profiles in the system context.

%package -n lib%name
Summary: Colord shared library
Group: System/Libraries

%description -n lib%name
This package provides shared library for Colord to work.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C
Obsoletes: %name-devel
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
colord is a low level system activated daemon that maps color devices to color
profiles in the system context.

This package provides development files for Colord library.

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package -n lib%name-vala
Summary: Vala Bindings for lib%name
Group: Development/C
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-vala
This package provides Vala language bindings for %name library


%prep
%setup
%patch1 -p1 -b .var

%build
%autoreconf
%configure --disable-static \
	--disable-rpath \
	%{subst_enable reverse} \
	%{subst_enable sane} \
	--with-daemon-user=%colord_user

%make_build

%install
%makeinstall_std

# databases
touch %buildroot%_localstatedir/%name/mapping.db
touch %buildroot%_localstatedir/%name/storage.db

mkdir -p %buildroot%_localstatedir/{%name,color}/icc

%find_lang %name

%pre
%_sbindir/groupadd -r -f %colord_group 2>/dev/null ||:
%_sbindir/useradd -r -n -g %colord_group -d %_localstatedir/%name \
	-s /dev/null -c "User for colord" %colord_user 2>/dev/null ||:

%files -f %name.lang
%_bindir/*
%config %_sysconfdir/%name.conf
%_libexecdir/%name
%_libexecdir/%name-sane
%_sysconfdir/dbus-1/system.d/org.freedesktop.ColorManager.conf
%_sysconfdir/dbus-1/system.d/org.freedesktop.colord-sane.conf
%_datadir/dbus-1/interfaces/org.freedesktop.colord.sane.xml
%_datadir/dbus-1/interfaces/org.freedesktop.ColorManager*.xml
%_datadir/dbus-1/system-services/org.freedesktop.colord-sane.service
%_datadir/dbus-1/system-services/org.freedesktop.ColorManager.service
%_datadir/polkit-1/actions/org.freedesktop.color.policy
/lib/udev/rules.d/*.rules
%dir %_libdir/colord-sensors
%_libdir/colord-sensors/libcolord_sensor_dummy.so
%_libdir/colord-sensors/libcolord_sensor_huey.so
%_libdir/colord-sensors/libcolord_sensor_colorhug.so
%dir %_datadir/color/icc/colord
%_datadir/color/icc/%name/x11-colors.icc
%_datadir/color/icc/%name/crayons.icc
%_man1dir/cd-create-profile.1.*
%_man1dir/colormgr.*
%_man1dir/cd-fix-profile.*
%attr(775,root,%colord_group) %dir %_localstatedir/%name
%dir %_localstatedir/%name/icc
%dir %_localstatedir/color
%dir %_localstatedir/color/icc
%ghost %_localstatedir/%name/*.db
%systemd_unitdir/*.service

%_sysconfdir/bash_completion.d/colormgr-completion.bash

%exclude %_libdir/%name-sensors/*.la

%files -n lib%name
%_libdir/libcolord.so.*

%files -n lib%name-devel
%_includedir/colord-1/
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Colord-1.0.typelib

%files -n lib%name-gir-devel
%_girdir/Colord-1.0.gir
%endif

%if_enabled vala
%files -n lib%name-vala
%_datadir/vala/vapi/%name.vapi
%endif


%changelog
* Sun Jul 01 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.22-alt1
- 0.1.22

* Wed May 23 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.21-alt1
- 0.1.21

* Sun May 13 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.20-alt1
- 0.1.20

* Wed Apr 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.19-alt1
- 0.1.19

* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.18-alt1
- 0.1.18

* Mon Feb 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.17-alt1
- 0.1.17

* Thu Feb 23 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.16-alt2
- fixed permission for %%_localstatedir/colord (ALT #26978)

* Wed Jan 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.16-alt1
- 0.1.16

* Sun Nov 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.15-alt1
- 0.1.15

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.14-alt1
- 0.1.14

* Thu Oct 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.13-alt2
- fixed databases location
- packaged %%_localstatedir/colord/*.db as %%ghost
- added shared-color-profiles to rqs

* Sat Oct 08 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.13-alt1
- 0.1.13

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.12-alt1
- 0.1.12
- new lib%name-{gir,gir-devel,vala} subpackages

* Tue Aug 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt1
- 0.1.10

* Thu Apr 14 2011 Victor Forsiuk <force@altlinux.org> 0.1.5-alt1
- Initial build.
