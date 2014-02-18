%define ver_major 3.10

Name: evolution-ews
Version: 3.10.4
Release: alt1

Group: Networking/Mail
Summary: Evolution extension for Exchange Web Services
License: LGPLv2
Url: http://projects.gnome.org/evolution
Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar


%define ver_base 3.10
%define evo_ver_base %ver_base

%define evolution_ver 3.10.0
# from configure.in.
%define eds_ver 3.10.0
%define libmspack_ver 0.4


Requires: evolution >= %evolution_ver
Requires: evolution-data-server >= %eds_ver
Requires: libmspack >= %libmspack_ver

BuildPreReq: gnome-common rpm-build-gnome gtk-doc
BuildPreReq: evolution-data-server-devel >= %eds_ver
BuildPreReq: evolution-devel >= %evolution_ver
BuildPreReq: libmspack-devel >= %libmspack_ver
BuildPreReq: libkrb5-devel

BuildPreReq: intltool
BuildRequires: glib2-devel >= 2.32
BuildRequires: libgtk+3-devel >= 3.0
BuildRequires: gcc-c++

%description
This package allows Evolution to interact with Microsoft Exchange servers,
versions 2007 and later, through its Exchange Web Services (EWS) interface.

%prep
%setup

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--with-krb5 \
	--with-krb5-includes=/usr/include/krb5

%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name '*.la' -exec rm {} \;
rm -f %buildroot%_libdir/evolution-data-server/*.so

%find_lang %name

%files -f %name.lang
%doc COPYING NEWS README
%_libdir/evolution-data-server/*.so.*
%_libdir/evolution-data-server/camel-providers/*
%_libdir/evolution-data-server/addressbook-backends/*.so
%_libdir/evolution-data-server/calendar-backends/*.so
%_libdir/evolution-data-server/registry-modules/*.so
%_libdir/evolution/%evo_ver_base/modules/*.so
%_datadir/evolution/%evo_ver_base/errors/*.error

%changelog
* Tue Feb 18 2014 Alexey Shabalin <shaba@altlinux.ru> 3.10.4-alt1
- initial build
