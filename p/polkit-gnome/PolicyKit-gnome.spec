%define _libexecdir %_prefix/libexec/polkit-1
%define oldname PolicyKit-gnome

%def_enable introspection

Name: polkit-gnome
Version: 0.101
Release: alt1

Summary: polkit integration for the GNOME desktop
License: GPLv2+
Group: System/Libraries
Url: http://git.gnome.org/cgit/PolicyKit-gnome/

Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Requires: polkit
Requires: lib%name = %version-%release
Provides: %oldname = %version-%release
Obsoletes: %oldname < %version

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gnome-common gobject-introspection-devel gtk-doc intltool libdbus-glib-devel libgtk+2-devel
BuildRequires: libgtk+2-gir-devel libpango-gir-devel libpolkit-gir-devel libcairo-gobject-devel

%description
%name provides a GNOME integration library and tools for
polkit including an Authentication Agent that matches the look and
feel of the GNOME desktop.

%package demo
Summary: Demo application for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Provides: %oldname-demo = %version-%release
Obsoletes: %oldname-demo < %version

%description demo
%name-demo provides a sample application that demonstrates the
features of both polkit and %name. You normally don't
want to have this package installed

%package -n lib%name
License: LGPLv2+
Summary: %name libraries
Group: System/Libraries
Provides: lib%oldname = %version-%release
Obsoletes: lib%oldname < %version

%description -n lib%name
Libraries provided by %name

%package -n lib%name-devel
License: LGPLv2+
Summary: Headers, libraries and API docs for %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: lib%oldname-devel = %version-%release
Obsoletes: lib%oldname-devel < %version

%description -n lib%name-devel
This package provides headers, libraries and API docs for
%name

%package -n lib%name-gir
Summary: GObject introspection data for the PolkitGtk library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the PolkitGtk library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the PolkitGtk library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the PolkitGtk library

%prep
%setup -q
%patch -p1

%build
gnome-doc-prepare -f
%autoreconf
%configure  \
	%{subst_enable introspection} \
	--disable-static \
	--enable-gtk-doc
%make

%install
%make DESTDIR=%buildroot install

%find_lang %name-1

%files -f %name-1.lang
%doc README AUTHORS NEWS HACKING
%_sysconfdir/xdg/autostart/*.desktop
%_libexecdir/%name-authentication-agent-1

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/polkit-gtk-1

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*.gir
%endif

%changelog
* Tue Mar 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.101-alt1
- 0.101

* Tue Feb 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.100-alt1
- 0.100

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt1
- 0.99

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt3
- rebuild

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt2
- rebuild

* Sat Jan 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt1
- 0.96

* Sat Nov 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.95-alt2
- obsoletes PolicyKit-gnome

* Thu Nov 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.95-alt1
- 0.95

* Thu Aug 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.94-alt1
- 0.94

* Thu Jul 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt2
- fixes for dbus-glib-0.82

* Wed Jul 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Tue Apr 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt2
- apply a patch to fix applications using PolicyKit-gnome with widgets that only email clicked events

* Sun Aug 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.9-alt1
- release 0.9

* Mon Apr 21 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8-alt1
- release 0.8
- show the menu item in other desktops too
- fix i18n (fedora patch1)
- drop other patches(upsteam fixed)

* Thu Apr 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt2
- add requires PolicyKit (#15132, #15133)
- define dir libexecdir as %%_prefix/libexec/PolicyKit

* Mon Mar 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- initial build for ALTLinux

