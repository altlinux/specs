%def_disable snapshot

%define ver_major 0.3

%def_enable lua_factory

Name: grilo-plugins
Version: %ver_major.4
Release: alt1

Summary: Plugins for the Grilo framework
Group: Sound
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/Grilo

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: grilo-tools
Requires: tracker

BuildRequires: gnome-common intltool >= 0.40.0 gperf
BuildRequires: gtk-doc yelp-tools
BuildRequires: libgio-devel >= 2.36
BuildRequires: libgrilo-devel >= %ver_major.3
BuildRequires: libxml2-devel
BuildRequires: libgupnp-devel >= 0.13
BuildRequires: libgupnp-av-devel >= 0.5
BuildRequires: libgssdp-devel
BuildRequires: libsqlite3-devel
BuildRequires: libgdata-devel >= 0.9.1
BuildRequires: libgom-devel >= 0.3.2
BuildRequires: libsoup-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgmime-devel
BuildRequires: tracker-devel
BuildRequires: liboauth-devel
BuildRequires: libgnome-online-accounts-devel >= 3.18.0
BuildRequires: libtotem-pl-parser-devel >= 3.4.1
BuildRequires: libdmapsharing-devel >= 2.9.12
BuildRequires: libjson-glib-devel
BuildRequires: libavahi-gobject-devel libavahi-glib-devel libavahi-devel
BuildRequires: libmediaart2.0-devel
BuildRequires: librest-devel
BuildRequires: libarchive-devel
%{?_enable_lua_factory:BuildRequires: liblua5-devel >= 5.3}


%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Apple Trailers
- Bookmarks
- Filesystem
- Flickr
- Gravatar
- Jamendo
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Podcasts
- Shoutcast
- Tracker
- UPnP
- Vimeo
- Youtube

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_lua_factory:--enable-lua-factory}
%make_build

%install
%makeinstall_std

# Remove files that will not be packaged
rm -f %buildroot%_libdir/grilo-%ver_major/*.la

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%_libdir/grilo-%ver_major/*.so*
%if_enabled lua_factory
%dir %_datadir/%name/
%_datadir/%name/grl-lua-factory/
%endif

%changelog
* Tue Feb 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Sun Jan 29 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt3
- updated to 0.3.3-20-g063064b
- fixed buildreqs

* Thu Oct 06 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt2
- updated to 0.3.3-8-gcaf6541
- enbabled lua support

* Sat Sep 10 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Fri Jun 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Wed Feb 03 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Sun Dec 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.17-alt1
- 0.2.17

* Thu Sep 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.16-alt1
- 0.2.16

* Sat Sep 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.15-alt2
- rebuilt with goa-3.17.91

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.15-alt1
- 0.2.15

* Sun Aug 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.14-alt3
- rebuilt against libgdata.so.22

* Tue Apr 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.14-alt2
- fixed buildreqs

* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.14-alt1
- 0.2.14

* Wed Aug 27 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.13-alt1
- 0.2.13
- libarchive support enabled

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt2
- rebuilt against libgdata.so.19

* Thu Apr 03 2014 Alexey Shabalin <shaba@altlinux.ru> 0.2.12-alt1
- 0.2.12

* Thu Sep 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.9-alt2
- rebuild against libtotem-plparser.so.18

* Thu Aug 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.9-alt1
- 0.2.9

* Thu Jun 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.8-alt1
- 0.2.8

* Thu May 16 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.7-alt1
- 0.2.7

* Sun Mar 31 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6

* Tue Jan 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Tue Dec 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Mon Nov 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- 0.2.2
- add DMAP plugin
- add TMDb plugin

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri May 25 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.19-alt1
- 0.1.19

* Fri Mar 16 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.18-alt2.git9e007
- git snapshot 9e00790f40ee498a7359b00e0b11a7523fdd1b3e
- rebuild with tracker-0.14

* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.18-alt1
- 0.1.18

* Mon Oct 31 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.17-alt1
- 0.1.17

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.16-alt1
- 0.1.16

* Thu Jun 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt4
- rebuild with new libgupnp

* Wed Jun 01 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt3
- build with tracker plugin

* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt2
- rebuild with new libgdata

* Mon May 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.15-alt1
- initial build for ALT Linux Sisyphus
