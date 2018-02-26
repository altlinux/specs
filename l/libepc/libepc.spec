%define ver_major 0.4

Name: libepc
Version: %ver_major.0
Release: alt1
Summary: Easy Publish and Consume library

Group: System/Libraries
License: LGPLv2+
URL: http://live.gnome.org/libepc
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

%define avahi_ver 0.6
%define soup_ver 2.3
%define gtk2_ver 2.10
%define glib2_ver 2.15.1
%define gnutls_ver 1.4
%define uuid_ver 1.36

BuildPreReq: rpm-build-gnome gnome-common
BuildPreReq: libavahi-devel >= %avahi_ver
BuildPreReq: libavahi-glib-devel >= %avahi_ver
BuildPreReq: libavahi-ui-gtk3-devel >= %avahi_ver
BuildPreReq: glib2-devel >= %glib2_ver
BuildPreReq: libgnutls-devel >= %gnutls_ver
BuildPreReq: libuuid-devel >= %uuid_ver
BuildPreReq: libgtk+2-devel >= %gtk2_ver
BuildPreReq: libsoup-devel >= %soup_ver
BuildPreReq: libgio-devel >= %glib2_ver

BuildRequires: intltool gtk-doc

%description
The Easy Publish and Consume library provides an easy method to:
* publish data per HTTPS
* announce that information via DNS-SD
* find that information
* and finally consume it

This library can be used as key/value store published to the
network, using encryption, authentication and service discovery.

%package ui
Summary: Widgets for %name
Group: System/Libraries

%description ui
The %name-ui package contains widget for use with %name.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: %name-ui = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package provides development documentation for %name.

%prep
%setup -q

%build
%configure --enable-static=no
%make_build

%check
# as minimum needs a running avahi daemon
#%%make check

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%_libdir/%name-1.0.so.*

%files ui
%_libdir/%name-ui-1.0.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0 (gtk+3 build)

* Mon May 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.3.11-alt1
- 0.3.11

* Wed Jan 07 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.8-alt1.1
- rebuild with gnutls-2.6
- removed obsolete *ldconfig from %%post{,un}

* Wed Oct 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.8-alt1
- initial build for ALTLinux

