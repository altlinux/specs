
%def_enable docs
%def_disable boo
%def_enable mtp
%def_enable appledevice
%def_enable daap
%def_enable podcast
%def_enable video
%def_disable moonlight
%def_enable webkit
%def_enable notify
%def_disable torrent
%def_enable nunit
%def_disable clutter
%def_enable youtube
%def_enable gio
%def_disable upnp

Name: banshee
Version: 2.3.5
Release: alt2
Summary: Easily import, manage, and play selections from your music collection
Group: Sound
License: MIT
Url: http://banshee.fm/

Source0: %name-%version.tar
Source2: hyena.tar
Patch0: %name-%version-%release.patch

# workaround for gnome-do-plugin-banshee
Provides: mono(Banshee.CollectionIndexer) = 2.3.0.0

BuildPreReq: lsb-core rpm-build-mono
# From configure.in and build/m4/banshee
BuildPreReq: intltool >= 0.35.0
BuildPreReq: libgtk+2-devel >= 2.22
BuildPreReq: gnome-doc-utils
BuildPreReq: libgnome-desktop-devel >= 2.28
BuildPreReq: gstreamer-devel >= 0.10.3
BuildPreReq: gst-plugins-devel >= 0.10.25.2
BuildPreReq: mono-devel >= 2.4.3
BuildPreReq: mono-data mono-data-sqlite
BuildPreReq: mono-web-devel
BuildPreReq: dbus-sharp-devel >= 0.7
BuildPreReq: dbus-sharp-glib-devel >= 0.5
BuildPreReq: mono-addins-devel >= 0.3.1
%{?_enable_boo:BuildPreReq: boo-devel >= 0.8.1}
%{?_enable_docs:BuildPreReq: monodoc-devel}
%{?_enable_nunit:BuildPreReq: mono-nunit-devel >= 2.4}
BuildPreReq: libtag-sharp-devel >= 2.0.3.7
BuildPreReq: libgtk-sharp2-devel >= 2.12
BuildPreReq: libgnome-sharp-devel >= 2.8
BuildPreReq: libsqlite3-devel >= 3.4
%{?_enable_mtp:BuildPreReq: libmtp-devel >= 0.2.0}
%{?_enable_appledevice:BuildPreReq: libgpod-sharp-devel >= 0.1}
%{?_enable_daap:BuildPreReq: mono-zeroconf-devel >= 0.7.3}
%{?_enable_moonlight:BuildPreReq: libmoon-sharp-devel >= 0.8}
%{?_enable_notify:BuildPreReq: libnotify-sharp-devel}
%{?_enable_torrent:BuildPreReq: monotorrent-devel >= 0.2}
%{?_enable_webkit:BuildPreReq: libwebkit-sharp-devel >= 0.2 libwebkitgtk2-devel >= 1.2.2 libsoup-devel >= 2.26 libsoup-gnome-devel >= 2.26}
%{?_enable_video:BuildPreReq: libXrandr-devel >= 1.1.1 libXxf86vm-devel >= 1.0.1}
%{?_enable_clutter:BuildPreReq: libclutter-devel >= 1.0.1}
%{?_enable_youtube:BuildPreReq: libgoogle-data-mono-devel >= 1.4}
%{?_enable_gio:BuildPreReq: libgtk-sharp-beans-devel >= 2.8 libgio-sharp-devel >= 2.22.3 libgudev-sharp-devel >= 0.1 libgkeyfile-sharp-devel >= 0.1}
%{?_enable_upnp:BuildPreReq: mono-upnp-devel >= 0.1}

BuildRequires: GConf libGConf-devel gcc-c++ mono-mcs perl-XML-Parser
BuildRequires: /proc
BuildPreReq: rpm-build-mono rpm-build-gnome desktop-file-utils
PreReq: desktop-file-utils

%description
Banshee allows you to import CDs, sync your music collection to an iPod,
play music directly from an iPod, create playlists with songs from your
library, and create audio and MP3 CDs from subsets of your library.

%package devel
Summary: Development files for Banshee
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for Banshee Media Player

%if_enabled docs
%package doc
Summary: Development documentation for %name
Group: Documentation
Provides: %name-monodoc = %version-%release
Obsoletes: %name-monodoc
BuildPreReq: monodoc
Requires: monodoc
BuildArch: noarch

%description doc
This package contains the API documentation for the %name in
Monodoc format.
%endif

%if_enabled appledevice
%package ipod
Group: Sound
Summary: Ipod support for Banshee
Requires: %name = %version-%release

%description ipod
Banshee allows you to import CDs, sync your music collection to an iPod,
play music directly from an iPod, create playlists with songs from your
library, and create audio and MP3 CDs from subsets of your library.

Install this package for iPod support in Banshee.
%endif

%if_enabled mtp
%package mtp
Group: Sound
Summary: MTP audio player support for Banshee
Requires: %name = %version-%release

%description mtp
Banshee allows you to import CDs, sync your music collection to an iPod,
play music directly from an iPod, create playlists with songs from your
library, and create audio and MP3 CDs from subsets of your library.

Install this package for MTP audio player support in Banshee.
%endif

%if_enabled daap
%package daap
Group: Sound
Summary: DAAP audio player support for Banshee
Requires: %name = %version-%release

%description daap
Banshee allows you to import CDs, sync your music collection to an iPod,
play music directly from an iPod, create playlists with songs from your
library, and create audio and MP3 CDs from subsets of your library.

Install this package for DAAP support in Banshee.
%endif

%if_enabled boo
%package boo
Group: Sound
Summary: Boo support for Banshee
Requires: %name = %version-%release

%description boo
Banshee allows you to import CDs, sync your music collection to an iPod,
play music directly from an iPod, create playlists with songs from your
library, and create audio and MP3 CDs from subsets of your library.

Install this package for boo scripts support in Banshee.
%endif

%prep
%setup -q
%__tar -xf %SOURCE2 -C src/Hyena
%patch0 -p1

%build
intltoolize --force --copy
%__libtoolize --force --copy --automake
ACLOCAL="aclocal -I build/m4/banshee -I build/m4/shamrock -I build/m4/shave"  %autoreconf
%configure \
	--disable-static \
	%{subst_enable boo} \
	%{subst_enable mtp} \
	%{subst_enable appledevice} \
	%{subst_enable daap} \
	%{subst_enable moonlight} \
	%{subst_enable torrent} \
	%{subst_enable clutter} \
	%{subst_enable youtube} \
	%{subst_enable gio} \
	--disable-schemas-install \
	--enable-user-help \
	--enable-release \


# 	--with-vendor-build-id="`lsb_release -ds`"

# Non-parallel build
%make

%install
%make_install install DESTDIR=%buildroot

desktop-file-install --vendor gnome --delete-original		\
  --remove-category=X-Red-Hat-Base				\
  --remove-category=X-Novell-Main				\
  --remove-category=X-Ximian-Main				\
  --dir %buildroot%_desktopdir			\
%buildroot%_desktopdir/%name.desktop

%find_lang --with-gnome %name

%files -f %name.lang
%doc COPYING AUTHORS README NEWS
%_bindir/*
%_libdir/%name
%_desktopdir/*
%_datadir/dbus-1/services/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_datadir/mime/packages/*
%exclude %_libdir/%name/*.la
%exclude %_libdir/%name/*/*.la

%if_enabled appledevice
%exclude %_libdir/%name/Extensions/Banshee.Dap.AppleDevice.dll*
%endif
%if_enabled mtp
%exclude %_libdir/%name/Mtp.dll*
%endif
%if_enabled daap
%exclude %_libdir/%name/Extensions/Banshee.Dap.Mtp.dll*
%exclude %_libdir/%name/Extensions/Banshee.Daap.dll*
%endif
%if_enabled boo
%exclude %_libdir/%name/Extensions/Banshee.BooScript.dll*
%endif

%files devel
%_pkgconfigdir/*.pc

%if_enabled docs
%files doc
%_monodocdir/*-docs*
%endif

%if_enabled appledevice
%files ipod
%_libdir/%name/Extensions/Banshee.Dap.AppleDevice.dll*
%endif

%if_enabled mtp
%files mtp
%_libdir/%name/Mtp.dll*
%_libdir/%name/Extensions/Banshee.Dap.Mtp.dll*
%endif

%if_enabled daap
%files daap
%_libdir/%name/Extensions/Banshee.Daap.dll*
%endif

%if_enabled boo
%files boo
%_libdir/%name/Extensions/Banshee.BooScript.dll*
%endif

%changelog
* Tue Feb 21 2012 Alexey Shabalin <shaba@altlinux.ru> 2.3.5-alt2
- fixed manual provides  mono(Banshee.CollectionIndexer)

* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Wed Nov 02 2011 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon May 16 2011 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Fri Mar 11 2011 Alexey Shabalin <shaba@altlinux.ru> 1.9.5-alt1
- 1.9.5
- build without hal support
- build with gio,webkit support

* Wed Apr 07 2010 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 1.5.5-alt1
- 1.5.5
- build with support youtube

* Wed Mar 10 2010 Alexey Shabalin <shaba@altlinux.ru> 1.5.4-alt1
- 1.5.4
- build without clutter

* Fri Jan 29 2010 Alexey Shabalin <shaba@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Tue Dec 22 2009 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt2
- rebuild without  webkit-sharp

* Sat Nov 21 2009 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2 (1.6 beta3)
- disable builtin equalizer

* Thu Oct 15 2009 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt2
- release 1.5.1 (1.6 beta2)
- enable webkit support

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 1.5.1-alt1
- 1.5.1 (1.6 beta2)
- update buildreq

* Wed Jun 03 2009 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- update BuildRequires
- build with nunit
- cleanup spec for build from git source
- build without boo

* Sat Mar 14 2009 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Thu Jan 29 2009 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Nov 27 2008 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt2
- add libGConf-devel to BuildRequires
- enable support boo
- doc, ipod, mtp, daap, boo supbackages

* Thu Nov 20 2008 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1
- enable support daap and ipod
- add suport moonlight and mediaweb(webkit), but disabled
- build with notify support

* Sat Oct 25 2008 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt2
- rebuild with gnome-sharp-2.24

* Fri Aug 22 2008 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- initial build for ALTLinux

