%define _name gnome-media-profiles
%define ver_major 3.0
%define api_ver 3.0

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: GNOME Media Profiles library
Group: System/Libraries
License: LGPLv2+
Url: http://git.gnome.org/browse/libgnome-media-profiles
Source: ftp://ftp.gnome.org/sources/%name/%ver_major/%name-%version.tar.bz2

BuildRequires: libgtk+3-devel libgio-devel libGConf-devel
BuildRequires: gstreamer-devel gst-plugins-devel
BuildRequires: intltool gnome-doc-utils

Requires(post,preun): GConf

%description
The GNOME Media Profiles library provides prebuilt GStreamer pipelines
for applications aiming to support different sound formats.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files
for developing applications that use %name.

%prep
%setup -q

%build
%configure --disable-static \
	--disable-schemas-install \
	--disable-scrollkeeper

%make_build

%install
%make DESTDIR=%buildroot install
find %buildroot -name '*.la' -exec rm -f {} ';'

%find_lang --with-gnome --output=%name.lang %_name gnome-audio-profiles

%post
%gconf2_install %_name

%preun
%gconf2_uninstall %_name

%files -f %name.lang
%_bindir/gnome-audio-profiles-properties
%_libdir/*.so.*
%_datadir/%name
%config %_sysconfdir/gconf/schemas/%_name.schemas
%doc README NEWS

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/%name-%api_ver.pc

%changelog
* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Feb 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.2-alt1
- first build for Sisyphus

