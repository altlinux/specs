%define ver_major 2.32

Name: glib-networking
Version: %ver_major.3
Release: alt1

Summary: Networking support for GIO
Group: System/Libraries
License: LGPLv2+
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/sources/gnome/%name/%ver_major/%name-%version.tar.xz

Requires: ca-certificates gsettings-desktop-schemas >= 3.2.0

%define glib_ver 2.31.20
%define gnutls_ver 2.12.8

BuildRequires: intltool libgio-devel >= %glib_ver libproxy-devel
BuildRequires: libgnutls-devel >= %gnutls_ver libgcrypt-devel
BuildRequires: libp11-kit-devel ca-certificates gsettings-desktop-schemas-devel

%description
This package contains modules that extend the networking support in GIO.
In particular, it contains a libproxy-based GProxyResolver implementation
and a gnutls-based GTlsConnection implementation.

%define _libexecdir %_prefix/libexec

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-libproxy \
	--with-ca-certificates=%_datadir/ca-certificates/ca-bundle.crt

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_libexecdir/glib-pacrunner
%_libdir/gio/modules/libgiolibproxy.so
%_libdir/gio/modules/libgiognutls.so
%_libdir/gio/modules/libgiognomeproxy.so
%_datadir/dbus-1/services/org.gtk.GLib.PACRunner.service
%doc NEWS README

%exclude %_libdir/gio/modules/*.la

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Jan 04 2012 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 3.2.0

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.7-alt1
- 2.28.7

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6.1-alt1
- 2.28.6.1

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt1
- 2.28.6

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4

* Tue Mar 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- updated buildrqs

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- first build for Sisyphus

