%define ver_major 0.1

Name: grilo-plugins
Version: %ver_major.19
Release: alt1
Summary: Plugins for the Grilo framework
Group: Sound
License: LGPLv2+
Url: https://live.gnome.org/Grilo

Source: %name-%version.tar

BuildRequires: gnome-common
BuildRequires: glib2-devel >= 2.28 libgio-devel
BuildRequires: libgrilo-devel = %version
BuildRequires: libxml2-devel
BuildRequires: libgupnp-devel >= 0.13
BuildRequires: libgupnp-av-devel >= 0.5
BuildRequires: libsqlite3-devel
BuildRequires: libgdata-devel >= 0.7.0
BuildRequires: libquvi-devel >= 0.4.0
BuildRequires: libsoup-devel
BuildRequires: librest-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgmime-devel
BuildRequires: tracker-devel
BuildRequires: libtotem-pl-parser-devel >= 3.4.1

Requires: grilo-tools >= %version
Requires: tracker

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
NOCONFIGURE=1 ./autogen.sh
%configure		\
	--disable-static

%make_build

%install
%make_install DESTDIR=%buildroot install

# Remove files that will not be packaged
rm -f %buildroot%_libdir/grilo-%ver_major/*.la

%files
%doc AUTHORS COPYING NEWS README
%_libdir/grilo-%ver_major/*.so*
%_libdir/grilo-%ver_major/*.xml

%changelog
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
