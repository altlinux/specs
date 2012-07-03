%define gst_plugins gst-plugins
%define ver_major 0.10

%define _gst_datadir %_datadir/gstreamer-%ver_major
%define _gst_libdir %_libdir/gstreamer-%ver_major
%define _gtk_docdir %_datadir/gtk-doc/html

Name: %gst_plugins-good
Version: %ver_major.31
Release: alt1
Summary: A set of GStreamer plugins considered good
Group: System/Libraries
License: LGPL
URL: http://gstreamer.freedesktop.org/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq(post): GConf
Conflicts: %gst_plugins-bad < %ver_major.22
Provides: %name-audio-formats = %version-%release
Provides: %name-container-formats = %version-%release
Provides: %name-tags = %version-%release
Provides: %name-video-filters = %version-%release
Provides: %gst_plugins-flac = %version-%release
Provides: %gst_plugins-gconf = %version-%release
Obsoletes: %gst_plugins-gconf < %version

Source: %name-%version.tar
Source1: common.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): libGConf-devel
BuildRequires: GConf bzlib-devel gcc-c++ gst-plugins-devel gtk-doc intltool libSM-devel libXdamage-devel libXext-devel
BuildRequires: libXv-devel libavc1394-devel libcairo-devel libdv-devel libflac-devel libiec61883-devel libjpeg-devel
BuildRequires: liboil-devel libpulseaudio-devel libshout2-devel libsoup-devel libtag-devel libv4l-devel libwavpack-devel
BuildRequires: python-module-PyXML python-modules-email python-modules-encodings liborc-devel orc libgdk-pixbuf-devel
BuildRequires: libjack-devel libpng-devel libcairo-gobject-devel libgudev-devel libspeex-devel zlib-devel

%description
GStreamer Good Plug-ins is is a set of plug-ins that the developers consider
to have good quality code, correct functionality, and their preferred license
(LGPL for the plug-in code, LGPL or LGPL-compatible for the supporting
library).

%package devel-doc
Summary: Development documentation for GStreamer Good plugins
Group: Development/C
BuildArch: noarch

%description devel-doc
This package contains development documentation for GStreamer Good Plugins

%prep
%setup -q -a1
%patch -p1

touch ABOUT-NLS config.rpath

%build
%autoreconf
%configure \
	--enable-experimental \
	--disable-examples \
	--disable-valgrind \
	--disable-oss \
	--disable-oss4 \
	--enable-gtk-doc \
	--disable-debug \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name-%ver_major

%post
%gconf2_install gstreamer-0.10

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall gstreamer-0.10
fi

%files -f %name-%ver_major.lang
%doc AUTHORS NEWS README RELEASE
%_sysconfdir/gconf/schemas/gstreamer-0.10.schemas
%dir %_gst_libdir
%_gst_libdir/*.so
%_gst_datadir

%files devel-doc
%_gtk_docdir/*

%changelog
* Tue Feb 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.10.31-alt1
- 0.10.31

* Fri Jun 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.30-alt1
- 0.10.30

* Sun May 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.29-alt1
- 0.10.29

* Sat Jan 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.27-alt1
- 0.10.27

* Thu Dec 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.26-alt1
- 0.10.26

* Wed Dec 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.25.5-alt1
- 0.10.25.5 pre-release

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.25-alt2
- fixed a conflicting version of gst-plugins-bad (closes #24247)

* Fri Sep 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.25-alt1
- 0.10.25

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.24-alt1
- 0.10.24

* Mon May 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.23-alt1
- 0.10.23

* Thu May 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22.2-alt1
- 0.10.22.2 pre-release

* Wed Apr 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt1
- 0.10.22

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.21-alt1
- 0.10.21

* Sat Mar 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.19-alt1
- 0.10.19

* Thu Feb 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.18-alt1
- 0.10.18

* Tue Nov 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt1
- 0.10.17

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.16-alt1
- 0.10.16

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.15.4-alt1
- 0.10.15.4 pre-release

* Wed Jul 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.15-alt4
- rebuild with libraw1394.so.11

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.15-alt3
- rebuild with libpng12 1.2.37-alt2

* Thu Jun 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.15-alt2
- fixed SA35205 security advisory (closes: #20326)

* Thu May 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.15-alt1
- 0.10.15

* Mon Apr 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14-alt3
- added Obsoletes/Provides gst-pulse (closes: #19690)

* Sat Apr 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14-alt2
- enabled pulseaudio plugin

* Fri Feb 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14-alt1
- 0.10.14

* Fri Jan 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13-alt1
- 0.10.13

* Sun Dec 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt5
- enabled experimental

* Sun Dec 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt4
- rebuild without jpeg-mmx

* Mon Nov 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt3
- disabled esd plugin

* Tue Nov 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt2
- disabled OSS plugin

* Sun Oct 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt1
- 0.10.11

* Sat Oct 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt2
- disabled pulse plugin

* Tue Aug 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt1
- 0.10.9

* Thu May 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.8-alt2
- rebuild

* Thu Apr 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.8-alt1
- 0.10.8

* Tue Apr 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.7-alt3
- rebuild (close #15336)

* Thu Feb 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.7-alt2
- join together subpackage

* Thu Feb 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.7-alt1
- 0.10.7

* Mon Feb 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.6-alt2
- use GST_TAG_ARTIST_SORTNAME instead of the deprecated GST_TAG_MUSICBRAINZ_SORTNAME (close #13844)
- build video4linux2 plugin
- spec cleanup
- update build dependencies

* Mon Sep 10 2007 Igor Zubkov <icesik@altlinux.org> 0.10.6-alt1
- 0.10.5 -> 0.10.6

* Mon Apr 23 2007 Igor Zubkov <icesik@altlinux.org> 0.10.5-alt5
- enable ladspa support

* Mon Apr 23 2007 Igor Zubkov <icesik@altlinux.org> 0.10.5-alt4
- enable libcaca support

* Tue Mar 13 2007 Igor Zubkov <icesik@altlinux.org> 0.10.5-alt3
- rebuild with libFLAC.so.8

* Mon Feb 26 2007 Igor Zubkov <icesik@altlinux.org> 0.10.5-alt2
- add patch to build with/without new flac 1.1.3 (closes #10940)

* Wed Feb 21 2007 Igor Zubkov <icesik@altlinux.org> 0.10.5-alt1
- 0.10.4 -> 0.10.5

* Mon Dec 25 2006 Igor Zubkov <icesik@altlinux.org> 0.10.4-alt4
- rebuild with new dbus

* Mon Dec 18 2006 Igor Zubkov <icesik@altlinux.org> 0.10.4-alt3
- disable libcaca support

* Wed Aug 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.4-alt2
- Removed obsolete schema install scripts for gst-plugins-gconf

* Thu Aug 24 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.4-alt1
- Release 0.10.4
- Require libiec61883-devel and libraw1394 >= 1.1.0 for dv1394

* Sat Jun 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.3-alt2
- Fixed a dependency in gst-plugins-good-all

* Thu Jun 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.3-alt1
- Release 0.10.3
- Added icydemux to the container format plugins
- Added annodex, gdk_pixbuf, hal, taglib, ximagesrc plugins
- Disabled check by default due to a failing icydemux test

* Wed Apr 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.2-alt2
- Do configure ladspa, the configure flag had a typo
- The ladspa plugin is never built anyway, disabled it

* Mon Feb 20 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.2-alt1
- 0.10.2
- Renamed debug to test
- Renamed effects to filters, effects-extra to effects
- Added cdio
- Added tags package to contain apetag and id3demux,
  the latter moved from audio-formats

* Wed Jan 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt1
- 0.10.1
- Added id3demux to audio-formats

* Wed Dec 28 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.0-alt2
- Corrected dependencies to install against updated versions of
  gstreamer and gst-plugins-base

* Fri Dec 16 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.0-alt1
- Initial release for Sisyphus of plugins as split in 0.9
