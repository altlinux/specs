%def_disable snapshot

%define ver_major 3.4
%define rev %nil
%define gst_api_ver 1.0

%def_without hal
%def_with gudev
%def_enable daap
# required obsolete clutter-gst2.0
%def_disable visualizer
%def_enable grilo
%def_disable gtk_doc
%def_enable zeitgeist
%def_enable soundcloud

Name: rhythmbox
Version: %ver_major.1
Release: alt2%rev

Summary: Music Management Application
License: GPL
Group: Sound
Url: https://wiki.gnome.org/Apps/Rhythmbox

%define pkgdocdir %_docdir/%name-%version

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define dbus_ver 0.35
%define glib_ver 2.36.0
%define gst_ver 1.0
%define gtk_ver 3.6.0
%define mtp_ver 0.3
%define brasero_ver 2.31.5
%define soup_ver 2.42.0
%define totem_ver 3.2.0
%define udev_ver 143
%define gpod_ver 0.8
%define mx_ver 1.0.1
%define secret_ver 0.18
%define dmapsharing_ver 2.9.19
%define grilo_ver 0.3

Requires: lib%name = %version-%release

Requires: gstreamer%gst_api_ver >= %gst_ver
Requires: libgst-plugins%gst_api_ver >= %gst_ver
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gnome-icon-theme
Requires: gnome-icon-theme-symbolic

Provides: %name-plugins-audiocd
Provides: %name-plugins-generic-player

%define _libexecdir %_libdir/%name
# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_compile_include %_libexecdir
# python bindings are linked into rhythmbox statically
Provides: python%__python3_version(rb)
Provides: python%__python3_version(rhythmdb)
Provides: python3(rb)
Provides: python3(rhythmdb)

BuildRequires: rpm-build-python3 python3-module-pygobject3-devel

BuildRequires(Pre): browser-plugins-npapi-devel

BuildRequires: glib2-devel >= %glib_ver
BuildRequires: intltool >= 0.40
BuildRequires: gtk-doc yelp-tools gnome-common desktop-file-utils

BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libdbus-glib-devel >= %dbus_ver
BuildRequires: libsoup-devel >= %soup_ver
BuildRequires: libsoup-gnome-devel >= %soup_ver
BuildRequires: libbrasero-devel >= %brasero_ver
BuildRequires: libtotem-pl-parser-devel >= %totem_ver
BuildRequires: gstreamer%gst_api_ver-devel >= %gst_ver
BuildRequires: gstreamer%gst_api_ver-utils >= %gst_ver
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_ver
BuildRequires: libgpod-devel >= %gpod_ver
BuildRequires: libmtp-devel >= %mtp_ver
BuildRequires: libICE-devel libSM-devel libsecret-devel >= %secret_ver
BuildRequires: iso-codes-devel libcheck-devel
BuildRequires: liblirc-devel libnotify-devel >= 0.7.3
BuildRequires: libxml2-devel libjson-glib-devel libpng-devel
BuildRequires: libpeas-devel libtdb-devel zlib-devel
%{?_enable_grilo:BuildRequires: libgrilo-devel >= %grilo_ver}
BuildRequires: libavahi-glib-devel
BuildRequires: libdmapsharing-devel >= %dmapsharing_ver
%{?_enable_visualizer:BuildRequires: libclutter-gtk3-devel libclutter-gst2.0-devel libmx-devel >= %mx_ver}
%{?_with_hal:BuildRequires: libhal-devel}
%{?_with_gudev:BuildRequires: libgudev-devel}
BuildRequires: libgtk+3-gir-devel libgstreamer%gst_api_ver-gir-devel gst-plugins%gst_api_ver-gir-devel

%description
Rhythmbox is an integrated music management application, supporting
a music library, multiple playlists, internet radio, and more.

%package -n lib%name
Summary: Shared Rhythmbox Library
Group: System/Libraries

%description -n lib%name
This package provides shared library needed for Rhythmbox to work

%package -n lib%name-devel
Summary: Development files for Rhythmbox library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Files needed to develop applications that manipulate Rhythmbox,
an integrated music management application.

%package devel-doc
Summary: API documentation for Rhythmbox
Group: Development/C
BuildArch: noarch
Conflicts: lib%name < %version

%description devel-doc
API documentation for Rhythmbox, an integrated music management application.

%package plugins-audioscrobbler
Summary: Audioscrobbler plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-audioscrobbler
Plugin to the Rhythmbox music manager that adds
Audioscrobbler (Last.fm) service support.

%package plugins-cd-recorder
Summary: CD recorder plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release
Requires: brasero >= %brasero_ver

%description plugins-cd-recorder
Plugin to the Rhythmbox music manager that provides
support for recording audio CDs from playlists

%package plugins-daap
Summary: DAAP plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-daap
Plugin to the Rhythmbox music manager that provides
support for DAAP Music Sharing

%package plugins-fmradio
Summary: FM radio plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-fmradio
Plugin to the Rhythmbox music manager that provides
Support for FM radio broadcasting services

%package plugins-ipod
Summary: iPod plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release
%description plugins-ipod
Plugin to the Rhythmbox music manager that adds
support for Apple iPod media player.

%package plugins-mtpdevice
Summary: MTP device plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-mtpdevice
Plugin to the Rhythmbox music manager that adds
support for MTP devices.

%package plugins-iradio
Summary: Internet Radio plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release
%description plugins-iradio
Plugin to the Rhythmbox music manager that provides
support for Internel Radio

%package plugins-lirc
Summary: LIRC plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-lirc
Plugin to the Rhythmbox music manager that adds
Linux Infrared Remote Control support.

%package plugins-mmkeys
Summary: Media Player Keys plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-mmkeys
Plugin to the Rhythmbox music manager that provides
control Rhythmbox using key shortcuts

%package plugins-power-manager
Summary: Power Manager plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-power-manager
Plugin to the Rhythmbox music manager that provides
inhibit Power Manager from suspending the machine while playing

%package plugins-visualizer
Summary: Visualizer plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-visualizer
Plugin to the Rhythmbox music manager that provides
displays visualizations

%package plugins-mozilla
Summary: Browser plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release
Requires: browser-plugins-npapi

%description plugins-mozilla
Plugin for Mozilla based browsers to handle itms:// links

%package plugins-im-status
Summary: IM status plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-im-status
This plugin updates IM status according to the current song (works with
Empathy & Gossip)

%package plugins-notification
Summary: Status icon plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-notification
Status icon and notification popups plugin for Rhythmbox

%package plugins-media-server
Summary: MediaServer2 D-Bus interface for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-media-server
This plugin provides an implementation of the MediaServer2 D-Bus
interface specification for Rhythmbox.

%package plugins-mpris
Summary: MPRIS D-Bus interface for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-mpris
This plugin provides an implementation of the MPRIS D-Bus interface
specification for Rhythmbox.

%package plugins-grilo
Summary: Grilo browser for Rhythmbox
Group: Sound
Requires: %name = %version-%release

%description plugins-grilo
A plugin to let you browse media content from various sources using
Grilo.

%package plugins-android
Summary: Android plugin for Rhythmbox
Group: Sound
Requires: %name = %version-%release
Requires: gvfs-backend-mtp

%description plugins-android
A plugin that supports Android 4.0+ devices (via MTP).

%package plugins-python
Summary: Python plugins for Rhythmbox
Group: Sound
Requires: %name = %version-%release
Requires: lib%name-gir = %version-%release
%{?_enable_zeitgeist:Requires: zeitgeist}

%package -n lib%name-gir
Summary: GObject introspection data for the Gedit
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Rhythmbox music manager/

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Rhythmbox
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Rhythmbox music manager.

%description plugins-python
Python scripting language capabilities and several Python plugins
to the Rhythmbox music manager.

%package plugins
Summary: All plugins for Rhythmbox
Group: Sound
BuildArch: noarch

Requires: %name-plugins-audioscrobbler = %version-%release
Requires: %name-plugins-cd-recorder = %version-%release
%{?_enable_daap:Requires: %name-plugins-daap = %version-%release}
Requires: %name-plugins-fmradio = %version-%release
Requires: %name-plugins-ipod = %version-%release
Requires: %name-plugins-iradio = %version-%release
Requires: %name-plugins-lirc = %version-%release
Requires: %name-plugins-mmkeys = %version-%release
Requires: %name-plugins-mtpdevice = %version-%release
Requires: %name-plugins-power-manager = %version-%release
%{?_enable_visualizer:Requires: %name-plugins-visualizer = %version-%release}
Requires: %name-plugins-im-status = %version-%release
Requires: %name-plugins-notification = %version-%release
Requires: %name-plugins-media-server = %version-%release
Requires: %name-plugins-mpris = %version-%release
%{?_enable_grilo:Requires: %name-plugins-grilo = %version-%release}
Requires: %name-plugins-android = %version-%release
Requires: %name-plugins-python = %version-%release

%description plugins
This virtual package installs all Rhythmbox plugins

%prep
%setup -n %name-%version

%build
%autoreconf
export MOZILLA_PLUGINDIR=%browser_plugins_path
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--disable-static \
	--disable-schemas-compile \
	--disable-dependency-tracking \
	--enable-lirc \
	--with-brasero \
	--with-mtp \
	--with-ipod \
	%{subst_with hal} \
	%{subst_with gudev} \
	%{subst_enable grilo}

%make_build

%install
%makeinstall_std

install -d -m755 %buildroot%pkgdocdir
install -p -m644 AUTHORS DOCUMENTERS MAINTAINERS ChangeLog README* NEWS THANKS %buildroot%pkgdocdir/
bzip2 -9 %buildroot%pkgdocdir/ChangeLog
ln -s %_licensedir/GPL-2 %buildroot%pkgdocdir/COPYING

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/rhythmbox-metadata
%_libdir/%name/plugins/generic-player
%_libdir/%name/plugins/audiocd
%_datadir/%name
%_datadir/applications/*
%_datadir/dbus-1/services/*
%_datadir/icons/hicolor/*/*/*
%_man1dir/*
%config %_datadir/glib-2.0/schemas/org.gnome.rhythmbox.gschema.xml
%_datadir/appdata/%name.appdata.xml
%dir %pkgdocdir
%doc %pkgdocdir/AUTHORS
%doc %pkgdocdir/DOCUMENTERS
%doc %pkgdocdir/MAINTAINERS
%doc %pkgdocdir/COPYING
%doc %pkgdocdir/ChangeLog.bz2
%doc %pkgdocdir/NEWS
%doc %pkgdocdir/README
%doc %pkgdocdir/THANKS

%files -n lib%name
%_libdir/lib%name-core.so.*

%files -n lib%name-devel
%_libdir/lib%name-core.so
%_includedir/%name/
%_libdir/pkgconfig/%name.pc

%files plugins-audioscrobbler
%_libdir/%name/plugins/audioscrobbler/

%files plugins-cd-recorder
%_libdir/%name/plugins/cd-recorder/

%if_enabled daap
%files plugins-daap
%_libdir/%name/plugins/daap/
%endif

%files plugins-fmradio
%_libdir/%name/plugins/fmradio/

%files plugins-ipod
%_libdir/%name/plugins/ipod/

%files plugins-mtpdevice
%_libdir/%name/plugins/mtpdevice/

%files plugins-iradio
%_libdir/%name/plugins/iradio/

%files plugins-lirc
%_libdir/%name/plugins/rblirc/

%files plugins-mmkeys
%_libdir/%name/plugins/mmkeys/

%files plugins-power-manager
%_libdir/%name/plugins/power-manager/

%if_enabled visualizer
%files plugins-visualizer
%_libdir/%name/plugins/visualizer/
%endif

%files plugins-mozilla
%browser_plugins_path/librhythmbox-itms-detection-plugin.so
%exclude %browser_plugins_path/librhythmbox-itms-detection-plugin.la

%files plugins-im-status
%_libdir/%name/plugins/im-status/

%files plugins-notification
%_libdir/%name/plugins/notification/

%files plugins-media-server
%_libdir/%name/plugins/dbus-media-server/

%files plugins-mpris
%_libdir/%name/plugins/mpris/

%if_enabled grilo
%files plugins-grilo
%_libdir/%name/plugins/grilo/
%endif

%files plugins-android
%_libdir/%name/plugins/android/

%files -n lib%name-gir
%_libdir/girepository-1.0/MPID-3.0.typelib
%_libdir/girepository-1.0/RB-3.0.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/MPID-3.0.gir
%_datadir/gir-1.0/RB-3.0.gir

%files plugins-python
%_libdir/%name/plugins/rb/
%_libdir/%name/plugins/python-console/
%_libdir/%name/plugins/artsearch/
%_libdir/%name/plugins/lyrics/
#%_libdir/%name/plugins/magnatune/
%_libdir/%name/plugins/context/
%_libdir/%name/plugins/replaygain/
%_libdir/%name/plugins/sendto/
%_libdir/%name/plugins/webremote/
%{?_enable_zeitgeist:%_libdir/%name/plugins/rbzeitgeist/}
%{?_enable_soundcloud:%_libdir/%name/plugins/soundcloud/}

%exclude %_libdir/%name/plugins/*/*.la
%exclude %browser_plugins_path/*.la

%files plugins

#%%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/rhythmbox/
#%%endif

%exclude %_libdir/%name/sample-plugins/

%changelog
* Tue Jan 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt2
- temporarily disabled visualizer (depends on obsolete clutter-gst2.0)

* Sat Sep 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Sun Aug 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.4-alt1
- 3.4

* Sun Apr 03 2016 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

* Thu Mar 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.3-alt2
- disabled grilo plugin, not ready for 0.3

* Sun Jan 24 2016 Yuri N. Sedunov <aris@altlinux.org> 3.3-alt1
- 3.3
- new -plugins-android subpackage

* Sat Sep 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt3
- rebuilt for gnome-3.18

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- rebuilt against libgrilo-0.2.so.10

* Sun Apr 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 3.2-alt1
- 3.2

* Sun Sep 28 2014 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1

* Mon May 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2, built for gnome-3.12
- temporarily disabled magnatune plugin

* Sun Oct 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Sep 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt2
- rebuild against libtotem-plparser.so.18
- disabled obsolete zeitgeist plugin

* Wed Sep 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0
- used python3 for plugins
- enabled daap plugin again
- webkit support enabled to show html

* Sat Apr 13 2013 Yuri N. Sedunov <aris@altlinux.org> 2.99.1-alt1
- 2.99.1

* Sun Apr 07 2013 Yuri N. Sedunov <aris@altlinux.org> 2.99-alt1
- 2.99
- enabled visualizer plugin

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 2.98-alt3
- updated to 6ffa66a
- removed upstreamed patch
- updated buildrqs
- daap plugin temporarily disabled

* Sat Oct 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.98-alt2
- updated to 2a405e3
- webkit support disbaled to avoid mixed gstreamer-0.10/1.0 linkage
- applied patch from https://bugzilla.gnome.org/show_bug.cgi?id=686320

* Sun Sep 30 2012 Yuri N. Sedunov <aris@altlinux.org> 2.98-alt1
- 2.98
- visualizer plugin temporarily disabled

* Mon Jun 04 2012 Yuri N. Sedunov <aris@altlinux.org> 2.97-alt1
- 2.97

* Thu Apr 12 2012 Yuri N. Sedunov <aris@altlinux.org> 2.96-alt3
- fixed install

* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 2.96-alt2
- enabled grilo plugin

* Sun Mar 11 2012 Yuri N. Sedunov <aris@altlinux.org> 2.96-alt1
- 2.96
- grilo plugin temporarily disabled

* Wed Feb 01 2012 Yuri N. Sedunov <aris@altlinux.org> 2.95-alt2
- rebuilt against libmtp.so.9

* Sun Jan 15 2012 Yuri N. Sedunov <aris@altlinux.org> 2.95-alt1
- 2.95

* Sat Oct 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.90.1-alt1.1
- Rebuild with Python-2.7

* Fri May 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.90.1-alt1
- 2.90.1
- new gir{,-devel} packages
- status-icon replaced by notification plugin

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.13.3-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for rhythmbox

* Thu Mar 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt2
- current snapshot built
- updated buildreqs

* Sun Jan 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt1
- 0.13.3

* Sun Oct 31 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2
- new media-server and mpris plugins

* Thu Oct 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt2
- rebuild against libbrasero-media.so.1 (brasero-2.32)

* Wed Oct 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1
- new -devel subpackage
- daap plugin temporalily disabled

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.8-alt1
- 0.12.8

* Thu Mar 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt2
- rebuild against new libgnome-desktop and libtotem-pl-parser

* Sun Feb 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Sun Nov 22 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.6-alt1
- 0.12.6

* Tue Sep 29 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt2
- rebuild with new %%browser_plugins_path

* Fri Sep 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt1
- 0.12.5

* Sun Aug 23 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Sun Jul 05 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3
- new im-status and status-icon plugins
- updated buildreqs

* Mon Jun 01 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- 0.12.2
- updated buildreqs

* Tue Apr 28 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1
- updated buildreqs

* Thu Mar 19 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0
- updated buildreqs

* Tue Dec 09 2008 Yuri N. Sedunov <aris@altlinux.org> 0.11.6-alt4r6096
- updated to rev 6096
- removed upstreamed patches, updated link patch (#3)
- new plugins-mozilla subpackage with plugin to handle itms:// links
- updated buildreqs
- plugins-python requires python-module-gst (altbug #18035)
- built devel-doc subpackage as noarch
- removed obsolete %%post{,un} scripts

* Wed Oct 01 2008 Yuri N. Sedunov <aris@altlinux.org> 0.11.6-alt3
- rebuild for gnome-2.24

* Thu Jul 24 2008 Yuri N. Sedunov <aris@altlinux.org> 0.11.6-alt2
- %%name-plugins virtual package
- Fedora patches (5,6)

* Thu Jul 10 2008 Yuri N. Sedunov <aris@altlinux.org> 0.11.6-alt1
- new version
- don't modify desktop file (patch2 removed).

* Sun May 25 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.5-alt4
- Build with mtp

* Sat May 17 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.5-alt3
- Rebuild with new gstreamer build

* Sun Apr 06 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.5-alt2
- Requires notification-daemon

* Thu Apr 03 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.5-alt1
- 0.11.5
- {update,cliean}_menus fix
- *.desktop fix

* Fri Mar 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.4-alt2
- Rebuild with soup2.4

* Wed Mar 12 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.3-alt5
- rebuild with separate totem-pl-parser

* Fri Feb 29 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.3-alt4
Thanks to Alexey Shabalin <shaba@altlinux.ru>

- enable gnome-keyring support
- add patches:
  + patch0 - fix for upstream bug #506440
  + patch1 - fix for upstream bug #512549
  + patch2 - add support llibsoup-2.4 
  + patch3 - new multimedia keys API, fix for upstream bug #510406 
  + patch4 - force python thread init, fix for upstream bug #499208
  + patch5 - fix for upstream bug #510323
  + patch6 - disable power-plugin by default, RH bug #428034 
  + patch8 - fix for upstream bug #346434
  + patch9 - fix for upstream bug #497430
  + patch10 - fix Gnome bug #507450, RH bug #427612
  + patch11-13 - patches from PLD

* Fri Feb 22 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.3-alt3
- Dependency changed due gstreamer repackaging

* Wed Jan 09 2008 Igor Zubkov <icesik@altlinux.org> 0.11.3-alt2
- rebuild with new totem-gstreamer

* Mon Dec 17 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.3-alt1
- Include audiocd and generic-player plugins into core package
  (thanks to Alexey Shabalin<shaba@altlinux.ru>)

* Mon Nov 19 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.3-alt0.2
- 0.11.3

* Tue Sep 11 2007 Igor Zubkov <icesik@altlinux.org> 0.11.0-alt0.2
- rebuild with libgpod-devel

* Tue May 29 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.11.0-alt0.1
- Release 0.11.0

* Mon May 28 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.10.90-alt0.1
- Release 0.10.90

* Tue Apr 03 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.10.0-alt0.1
- Release 0.10.0

* Tue Feb 06 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.7-alt1.0
- Rebuilt with libgpod.so.1.

* Sat Jan 13 2007 Ilya Mashkin <oddity@altlinux.ru> 0.9.7-alt1
- new version

* Sat Oct 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.6-alt2
- Rebuilt with new nautilus-cd-burner

* Sun Oct 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.6-alt1
- Release 0.9.6
- Added cd-recorder plugin package
- Updated dependencies

* Sun Jun 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.5-alt1
- Release 0.9.5
- Patch1 is obsolete
- Added plugin package for ipod
- No more rhythmbox-devel

* Mon Jun 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.4.1-alt2
- Conditionally enabled python support
- Provide dependency targets needed for the python plugin

* Fri Jun 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.4.1-alt1
- Release 0.9.4.1
- Patch0: has gone upstream
- Patch1: correct a libnotify version condition check to work with 0.4.0
- Do not require gst-plugins-visualization

* Wed Apr 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.4-alt1
- Release 0.9.4
- Added plugin packages
- Buildreq

* Fri Mar 17 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.3.1-alt1
- Updated to 0.9.3.1
- Build with GStreamer 0.10
- Removed Debian-style menu
- Removed most of enable/with options
- Disabled iPod support by default
- Patch0: fix link order to build with ld --as-needed

* Wed Oct 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.8-alt0.5
- 0.8.8

* Mon Sep 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.6-alt0.5
- 0.8.6

* Thu Jul 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.5-alt0.5
- 0.8.5

* Sat May 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.3-alt0.5
- 0.8.3

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.1-alt0.5
- 0.8.1

* Sat Apr 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt0.5
- 0.8.0

* Sat Apr 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.2-alt0.5
- 0.7.2

* Fri Apr 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.1-alt0.5
- 0.7.1

* Mon Dec 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.3-alt0.5
- 0.6.3

* Thu Dec 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.2-alt0.5
- 0.6.2

* Thu Nov 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.1-alt0.5
- 0.6.1

* Mon Oct 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.88-alt0.5
- 0.5.88

* Fri Sep 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.3-alt0.5
- 0.5.3

* Thu Aug 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.2-alt0.5
- 0.5.2

* Wed Aug 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.1-alt0.5
- 0.5.1

* Tue Mar 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.1-alt0.5
- First build for Sisyphus.



