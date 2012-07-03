%define _libexecdir %_prefix/libexec
%define ver_major 0.25

Name: libsocialweb
Version: %ver_major.20
Release: alt2

Summary: A social network data aggregator
Group: System/Libraries
License: LGPLv2
Url: http://www.gnome.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Source1: flickr
Source2: twitter
Source3: lastfm
Source4: twitpic
Source5: facebook
Source6: facebook.key

BuildRequires: libdbus-glib-devel libgeoclue-devel libgio-devel libGConf-devel
BuildRequires: libgnome-keyring-devel gobject-introspection-devel intltool
BuildRequires: libjson-glib-devel libsoup-gnome-devel libxslt-devel NetworkManager-glib-devel
BuildRequires: librest-devel libvala-devel vala-tools

Requires: %name-keys = %version-%release

%description
%name is a social data server which fetches data from the "social web",
such as your friend's blog posts and photos, upcoming events, recently played
tracks, and pending eBay* auctions. It also provides a service to update
your status on web services which support it, such as Twitter.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release
Requires: pkgconfig

%description devel
Files for development with %name.

%package devel-doc
Summary: Development documentation for the %name
Group: Development/C
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
%name is a convenience library making adding plug-ins support
to GTK+ and glib-based applications.

This package contains development documentation for the %name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/C
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name

%package vala
Summary: Vala Bindings for %name
Group: Development/C
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides Vala language bindings for %name  library

%package keys
Summary: API keys for %name
Group: Networking/Other
BuildArch: noarch

%description keys
Keys allowing access to various web services through libsocialweb.

%prep
%setup

chmod 644 examples/*.py

%build
%configure --with-gnome \
	--with-online=networkmanager \
	--disable-static \
	--enable-all-services \
	--enable-vala-bindings

%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot/%_datadir/libsocialweb/keys
cp %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %buildroot/%_datadir/libsocialweb/keys

%find_lang %name

%files -f %name.lang
%_libexecdir/%name-core

%_libdir/libsocialweb-client.so.*
%_libdir/libsocialweb-keyfob.so.*
%_libdir/libsocialweb-keystore.so.*
%_libdir/libsocialweb.so.*

%dir %_libdir/%name
%dir %_libdir/%name/services
%_libdir/%name/services/libfacebook.so
%_libdir/%name/services/libflickr.so
%_libdir/%name/services/liblastfm.so
%_libdir/%name/services/libmyspace.so
%_libdir/%name/services/libphotobucket.so
%_libdir/%name/services/libplurk.so
%_libdir/%name/services/libsina.so
%_libdir/%name/services/libsmugmug.so
%_libdir/%name/services/libtwitter.so
%_libdir/%name/services/libvimeo.so
%_libdir/%name/services/libyoutube.so

%dir %_datadir/%name/
%_datadir/%name/services/
%_datadir/dbus-1/services/%name.service
%doc AUTHORS COPYING TODO

%exclude %_libdir/%name/services/*.la

%files devel
%_includedir/%name
%_libdir/pkgconfig/libsocialweb-client.pc
%_libdir/pkgconfig/libsocialweb-keyfob.pc
%_libdir/pkgconfig/libsocialweb-keystore.pc
%_libdir/pkgconfig/libsocialweb-module.pc
%_libdir/*.so
%doc tests/*.c examples/*c examples/*.py

%files gir
%_typelibdir/SocialWebClient-0.25.typelib

%files gir-devel
%_girdir/SocialWebClient-0.25.gir

%files vala
%_datadir/vala/vapi/%name-client.deps
%_datadir/vala/vapi/%name-client.vapi

%files devel-doc
%_datadir/gtk-doc/html/%name
%_datadir/gtk-doc/html/%name-client
%_datadir/gtk-doc/html/%name-dbus

%files keys
%dir %_datadir/%name/keys
%_datadir/%name/keys/*

%changelog
* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.25.20-alt2
- keys subpackage

* Sat Nov 12 2011 Yuri N. Sedunov <aris@altlinux.org> 0.25.20-alt1
- 0.25.20

* Wed Aug 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.25.19-alt1
- first build for Sisyphus


