%define ver_major 3.4
%def_disable static
%def_disable gstmix

Name: gnome-media
Version: %ver_major.0
Release: alt1

%define pkgdocdir %_docdir/%name-%version

Summary: GNOME media programs
License: LGPLv+2
Group: Graphical desktop/GNOME
URL: ftp://ftp.gnome.org/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Patch: %name-2.26.0-alt-gst-mixer.patch

Provides: gnome2-media = %version
Obsoletes: gnome2-media

# From configure.ac
%define GConf_ver 2.10.0
%define scrollkeeper_ver 0.3.14
%define intltool_ver 0.35
%define glib_ver 2.18.2
%define gtk_ver 2.91.0
%define gstreamer_ver 0.10.23
%define gstreamer_plugins_ver 0.10.0
%define libxml_ver 2.5.0
%define gnome_common_ver 2.8.0

%{?_enable_gstmix:Requires: %name-gmix = %version-%release}
Requires: %name-grecord = %version-%release

BuildRequires: GConf >= %GConf_ver libGConf-devel >= %GConf_ver
BuildRequires: scrollkeeper >= %scrollkeeper_ver
BuildRequires: intltool >= %intltool_ver gnome-doc-utils
BuildRequires: gnome-common >= %gnome_common_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: gstreamer-devel >= %gstreamer_ver
BuildRequires: gstreamer-utils >= %gstreamer_ver
BuildRequires: gst-plugins-devel >= %gstreamer_plugins_ver
BuildRequires: libxml2-devel >= %libxml_ver
BuildRequires: libcanberra-gtk3-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libgnome-media-profiles-devel

%description
GNOME media programs for the GNOME 3 desktop contains the following:

grecord                 - GNOME Sound Recorder.
gstreamer-properties    - GStreamer Properties Capplet.
gst-mixer               - GNOME GStreamer-based audio mixer. (deprecated)

%package common
Summary: Common files for GNOME media programs
Group: Graphical desktop/GNOME
PreReq: GConf >= %GConf_ver
PreReq: scrollkeeper >= %scrollkeeper_ver

Requires: gstreamer(audio-hardware-sink) >= %gstreamer_plugins_ver
Requires: gst-plugins-audio-filters >= %gstreamer_plugins_ver
Requires: gst-plugins-gconf >= %gstreamer_plugins_ver
Requires: gst-plugins-test >= %gstreamer_plugins_ver
Requires: gst-plugins-video-filters >= %gstreamer_plugins_ver

Provides: gnome2-media-common = %version
Obsoletes: gnome2-media-common

%description common
This package contains common files needed to run GNOME media programs.

%package gmix
Summary: GNOME GStreamer-based audio mixer.
Group: Sound
PreReq: %name-common = %version-%release
Requires: pulseaudio-daemon >= 0.9.16
# ALT #2431
Requires: alsa-plugins-pulse

%description gmix
gnome-volume-control is a GNOME enabled audio mixer.

%package grecord
Summary: GNOME Sound recorder.
Group: Sound
PreReq: %name-common = %version-%release
Requires: gstreamer(audio-hardware-source) >= %gstreamer_plugins_ver
Requires: gst-plugins-base >= %gstreamer_plugins_ver

%description  grecord
The application enables you to record and play waveform .wav sound files.

%define _libexecdir %_bindir

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
    --disable-schemas-install \
    %{subst_enable static} \
    %{subst_enable vumeter} \
    %{subst_enable cddbslave} \
    %{subst_enable gnomecd} \
    %{subst_enable gstmix}

%make_build

%install
%make_install DESTDIR=%buildroot install

%define programs grecord gnome-sound-recorder gstreamer-properties
%find_lang --with-gnome %name %name-2.0 %programs

for omf in %programs; do
grep -F "$omf" %name.lang >> $omf.lang ||:
done

grep -v '\.omf$' %name.lang >> %name-2.0.lang
cat gstreamer-properties.lang >> %name-2.0.lang
cat gnome-sound-recorder.lang >> grecord.lang

install -d -m755 %buildroot%pkgdocdir
install -p -m644 AUTHORS MAINTAINERS NEWS README \
    %buildroot%pkgdocdir/

%post grecord
%gconf2_install gnome-sound-recorder

%preun grecord
if [ $1 = 0 ]; then
%gconf2_uninstall gnome-sound-recorder
fi

%files

%files common -f %name-2.0.lang
%_bindir/gstreamer-properties
%_desktopdir/gstreamer-properties.desktop
%_datadir/gstreamer-properties
%_datadir/%name
%_datadir/sounds/gnome/default/alerts/*.ogg
%_iconsdir/hicolor/*x*/apps/gstreamer-properties.png
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/MAINTAINERS
%pkgdocdir/NEWS
%pkgdocdir/README

%if_enabled gstmix
%files gmix -f gnome-volume-control.lang
# gstmix
%_bindir/gnome-volume-control-settings
%_desktopdir/gnome-volume-control-settings.desktop
%endif

%files grecord -f grecord.lang
%_bindir/gnome-sound-recorder
%_desktopdir/gnome-sound-recorder.desktop
%_datadir/gnome-sound-recorder
%_iconsdir/hicolor/*/*/gnome-sound-recorder.*
%config %_sysconfdir/gconf/schemas/gnome-sound-recorder.*

%changelog
* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Feb 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.2-alt1
- 2.91.2

* Thu Nov 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- gnome-media-gmix reqs alsa-plugins-pulse (ALT #2431)
- removed debugging code

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun Aug 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.6-alt1
- 2.31.6

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Wed Feb 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.5-alt1
- 2.28.5

* Thu Oct 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.1-alt1
- 2.28.1

* Wed Sep 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Sun Sep 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.91-alt4
- avoid crashing when switching profiles quickly

* Mon Sep 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.91-alt3
- translated desktop files

* Fri Sep 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.91-alt2
- updated Russian translation

* Fri Sep 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.91-alt1
- 2.27.91

* Fri Aug 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Fri Aug 07 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt4
- fixed russian translation (closes #20228)

* Tue May 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt3
- fixed "Categories" in gnome-volume-control.desktop (shrek@)

* Tue May 05 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- a set of ubuntu patches to make gstmix to work (shrek@)
- %%pkgdocdir owned by gnome-media-common

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Mar 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- removed obsolete %%post{,un} scripts
- updated buildreqs
- gmix subpackage provides removed gnome-applets-mixer

* Sun Sep 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0.1-alt1
- 2.24.0.1
- drop alt-MTA.patch
- don't buld deprecated cddbslave and gnome-cd.
- spec cleanup

* Fri Aug 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt4
- don't build useless vumeter.

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt3
- remove requires gnome-control-center(#12799)

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 2.22.0-alt2
- add Packager tag

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.0-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gnome-media-vumeter

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Sun Mar 16 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version: 2.22.0

* Wed Sep 26 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 2.20.1-alt1
- new version: 2.20.1

* Sat Oct 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.16.1-alt2
- Rebuilt with new nautilus-cd-burner

* Fri Sep 08 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.16.1-alt1
- Updated to 2.16.1

* Mon Jul 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.14.2-alt3
- Added gst-plugins-base to build dependencies ('playbin' is wanted)
- gnome-media-grecord needs gst-plugins-base for playbin

* Mon Jun 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.14.2-alt2
- Versioned the provided legacy names

* Fri Jun 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.14.2-alt1
- Updated to 2.14.2
- Patch1 is not needed anymore

* Thu Mar 16 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.14.0-alt1
- Release 2.14.0

* Sun Mar 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.13.93-alt1
- Updated to 2.13.93
- Removed 2 from package names
- Patch1: make gnome-media buildable with ld --as-needed
- Refurbished dependencies
- Made gcdplayer depend on the more modern cdio plugin
- Lowered the required gstreamer versions to 0.10.0
- Spec cleanup

* Fri Feb 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.91-alt1
- new version, requires gstreamer 0.10
- removed Debian-style menu support.
- fixed a typo in the name of libcddb2-devel-static package.

* Thu Jan 26 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.7-alt1
- New version.
- Fixed Bug #8567.
- Require GStreamer-0.10
- Updated dependencies.
- Minor spec improvements.

* Sat Sep 24 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Sat Jul 16 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.10.2-alt1.1
- rebuild with new libnautilus-burn.so.1 .

* Fri Apr 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Mon Apr 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92

* Wed Feb 09 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- 2.9.90

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Fri May 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.1

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Fri Apr 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Mar 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.1-alt1
- 2.4.1.1

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.8-alt1
- 2.3.8

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Thu Jul 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Thu Jul 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Mon Jun 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Thu Apr 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Wed Feb 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1.1-alt1
- 2.2.2.1

* Wed Feb 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Fri Jan 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Wed Jan 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5
- gstreamer-properties.desktop removed

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1
- grecord uses gstreamer!

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2.5-alt3
- rebuild with new pango, gtk+

* Sun Sep 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2.5-alt2.1
- gnome2-media virtual package installs all media programs
- gconf2_install macro used for schemas installation.
- scrollkeeper >= 0.3.11 added to requires list.

* Wed Sep 25 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.0.2.5-alt2
- Disabled system MTA seek at build time.

* Mon Sep 23 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.0.2.5-alt1.1
- Fixed buildreq.

* Sat Sep 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2.5-alt1
- First build for Sisyphus.
