%define ver_major 3.4
%define panel_api_ver 4.0
%def_enable frequency_selector
%def_disable mixer
%def_without hal
%def_disable battstat
%def_disable mini_commander

# Uses libapm that doesn't exist on x86_64. GNOME Power Manager does the
# same work better.
%def_disable battstat
# Requires system-tools-backends that are not likely to appear in Sisyphus,
# but who knows?
%def_disable modemlights
%def_with hal

Name: gnome-applets
Version: %ver_major.1
Release: alt1

Summary: Small applications for the GNOME panel
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Source1: 01-cpufreq.pkla
Patch: %name-2.6.0-alt-install_makefile.patch
Patch1: %name-2.9.90-alt-modemlights.patch
Patch2: %name-2.3.5-alt-geyes_schema.patch
Patch3: %name-2.16.1-relax-buildreqs.patch

# From configure.in
%define gtk_ver 2.99.3
%define glib_ver 2.27.5
%define GConf_ver 2.8.0
%define scrollkeeper_ver 0.1.4
%define gnome_panel_ver 2.91.4
%define libgtop_ver 2.11.92
%define libglade_ver 2.4.0
%define libgail_ver 1.1.0
%define libxklavier_ver 4.0
%define libwnck_ver 2.9.3
%define system_tools_backends_ver 1.1.3
%define libnotify_ver 0.7.1
%define icon_theme_ver 2.91.6
%define libgweather_ver 2.91.6
%define nm_ver 0.7

Requires: %name-charpick = %version-%release
Requires: %name-drivemount = %version-%release
Requires: %name-stickynotes = %version-%release
Requires: %name-geyes = %version-%release
Requires: %name-gweather = %version-%release
%{?_enable_mini_commander:Requires: %name-mini-commander = %version-%release}
Requires: %name-multiload = %version-%release
Requires: %name-accessx-status = %version-%release

# From configure.in
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libGConf2-devel >= %GConf_ver
BuildPreReq: scrollkeeper >= %scrollkeeper_ver
BuildPreReq: libgnome-panel-devel >= %gnome_panel_ver
BuildPreReq: libgtop-devel >= %libgtop_ver
BuildPreReq: libglade-devel >= %libglade_ver
BuildPreReq: libgail3-devel >= %libgail_ver
BuildPreReq: libxklavier-devel >= %libxklavier_ver
BuildPreReq: libwnck3-devel >= %libwnck_ver
BuildPreReq: libnotify-devel >= %libnotify_ver
BuildPreReq: gnome-icon-theme >= %icon_theme_ver
BuildPreReq: intltool >= 0.35
BuildPreReq: libX11-devel libXt-devel
BuildPreReq: libgucharmap-devel >= 2.33.2
BuildPreReq: libgweather-devel >= %libgweather_ver
BuildPreReq: NetworkManager-devel >= 0.7
BuildPreReq: GConf >= %GConf_ver
BuildRequires: rpm-build-gnome
BuildRequires: python-devel python-modules-compiler gnome-settings-daemon-devel libxml2-devel
BuildRequires: libdbus-devel libdbus-glib-devel gst-plugins-devel libSM-devel libgdbm-devel
BuildRequires: libpolkit-gnome-devel libpolkit1-devel gnome-common xorg-cf-files gnome-doc-utils docbook-utils xsltproc

%if_enabled battstat
BuildPreReq: libapm-devel
%endif

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. The gnome-applets package provides
following small utilities for the GNOME panel:

battstat-applet is a utility that displays the status of the power
managment subsystem on laptops. It queries the APM BIOS and displays
remaining battery charge percentage in a graphical window.

charpick_applet allows you to easily write many characters which are not
available on standard keyboards such as accented  characters,  certain
mathematical  symbols and punctuation, and some other special symbols.

drivemount_applet allows to quickly and easily mount and unmount various
types of drives and file systems on computer.

geyes_applet is a pair of eyes which follow mouse pointer around the screen.

gweather displays the current temperature and weather conditions in
numeric and iconified form inside the applet.

mini_commander_applet adds a command line to your Panel. It features
command completion, command history, changeable macros and an optional
built-in clock. Because of the changeable macros you can use it for many
different tasks. You can simply start a program (or a short macro) or
view a web page or search for a man/info page etc.

multiload_applet contains 5 applets: CPU Load Applet, Load Average
Applet, Memory Load Applet, Net Load Applet and Swap Load Applet.

%package common
Summary: Common files for GNOME panel applets
Group: Graphical desktop/GNOME
PreReq: GConf2 >= %GConf_ver
PreReq: scrollkeeper
# since 2.9
Obsoletes: %name-cdplayer
Obsoletes: %name-wireless
Obsoletes: %name-mailcheck
Obsoletes: %name-gkb
Obsoletes: %name-modemlights
# Just to make sure applets don't get installed without the panel itself
# (an implicit dependency on libgnome-panel is not enough).
Requires: gnome-panel >= %gnome_panel_ver

%description common
This package contains common files needed to run GNOME panel applets.

%package accessx-status
Summary: Accessibility Keyboard Status Applet for the GNOME panel
Group: Graphical desktop/GNOME
PreReq: %name-common = %version-%release

%description accessx-status
This applet shows the status of the keyboard accessibility features,
including the current state of the keyboard, if those features are in
use.

%if_enabled battstat
%package battstat
Summary: Laptop Power Subsystem Applet for the GNOME panel
Group: Monitoring
PreReq: %name-common = %version-%release

%description battstat
battstat-applet is a utility that displays the status of the power
managment subsystem on laptops. It queries the APM BIOS and displays
remaining battery charge percentage in a graphical window.
%endif

%package cpufreq
Summary: GNOME CPUFreq Applet
Group: Monitoring
PreReq: %name-common = %version-%release
Requires: polkit-gnome

%description cpufreq
GNOME CPUFreq Applet is a CPU Frequency Scaling Monitor for GNOME Panel.

%package cpufreq-usermode
Summary: Local authority configuration for GNOME CPUFreq Applet
Group: Monitoring
BuildArch: noarch
Requires: %name-cpufreq = %version-%release

%description cpufreq-usermode
GNOME CPUFreq Applet is a CPU Frequency Scaling Monitor for GNOME Panel.

Install this package to allow users from group "wheel" to change CPUs
frequency via applet.

%package charpick
Summary: Character Picker Applet for the GNOME panel
Group: Graphical desktop/GNOME
PreReq: %name-common = %version-%release

%description charpick
charpick_applet allows you to easily write many characters which are not
available on standard keyboards such as accented  characters,  certain
mathematical  symbols and punctuation, and some other special symbols.

%package drivemount
Summary: Drive Mount Applet for the GNOME panel.
Group: Graphical desktop/GNOME
PreReq: %name-common = %version-%release

%description drivemount
drivemount_applet allows to quickly and easily mount and unmount various
types of drives and file systems on computer.

%package geyes
Summary: gEyes Applet for the GNOME panel
Group: Toys
PreReq: %name-common = %version-%release

%description geyes
geyes_applet is a pair of eyes which follow mouse pointer around the screen.

%package gweather
Summary: Weather Applet for the GNOME panel
Group: Toys
PreReq: %name-common = %version-%release

%description gweather
gweather displays the current temperature and weather conditions in
numeric and iconified form inside the applet.

%package mini-commander
Summary: Mini-Commander Applet for the GNOME panel
Group: Graphical desktop/GNOME
PreReq: %name-common = %version-%release

%description mini-commander
mini_commander_applet adds a command line to your Panel. It features
command completion, command history, changeable macros and an optional
built-in clock. Because of the changeable macros you can use it for many
different tasks. You can simply start a program (or a short macro) or
view a web page or search for a man/info page etc.

%package mixer
Summary: Mixer Applet for the GNOME panel
Group: Sound
PreReq: %name-common = %version-%release
Requires: gnome-media-gmix

%description mixer
mixer_applet provides a simple and convenient interface for controlling
the sound volume and launching the Audio Mixer.

%if_enabled modemlights
%package modemlights
Summary: Modem Lights applet for the GNOME panel
Group: Monitoring
PreReq: %name-common = %version-%release

%description modemlights
modemlights_applet can be used to tell if your modem is working, and to
track its behavior and performance. It can also be configured to call a
separate script or program to have your modem connect and disconnect
when you click on the button with the single green light.
%endif

%package multiload
Summary: Multiload (cpu, load average, memory, net, swap) applet for the GNOME panel
Group: Monitoring
PreReq: %name-common = %version-%release
Requires: gnome-system-monitor

%description multiload
multiload_applet contains 5 applets: CPU Load Applet, Load Average
Applet, Memory Load Applet, Net Load Applet and Swap Load Applet.

%package stickynotes
Summary: Stickynotes applet for the GNOME panel
Group: Office
PreReq: %name-common = %version-%release
Requires: libwnck >= %libwnck_ver

%description stickynotes
stickynotes_applet enables to create, view, and manage sticky-notes on
Gnome Desktop.

%package trash
Summary: GNOME Trash Applet
Group: Graphical desktop/GNOME
PreReq: %name-common = %version-%release
Requires: gvfs

%description trash
This package provides a GNOME Trash Applet. You can drag items from
Nautilus onto this applet to move them to your trash folder.

%define _libexecdir %gnome_appletsdir

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1

%build
gnome-doc-common --copy
%autoreconf
# Note: battstat switch is broken; only --disable-battstat works.
export CFLAGS="$CFLAGS `pkg-config --cflags dbus-glib-1`"
%configure \
    --disable-dependency-tracking\
    --disable-schemas-install \
    --disable-scrollkeeper \
    %{?_enable_mini_commander:--enable-mini-commander} \
    %{subst_with hal} \
    %{?_disable_battstat:--disable-battstat} \
    %{?_disable_frequency_selector:--disable-frequency-selector} \
    %{?_enable_mixer:--enable-mixer-applet}

# SMP-incompatible build
%make

%install
%make_install install DESTDIR=%buildroot _sklocalstatedir=%buildroot%_sklocalstatedir

install -pD -m 644 %SOURCE1 %buildroot%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla

%define applets accessx-status battstat char-palette cpufreq-applet command-line drivemount geyes gweather mixer_applet2 stickynotes_applet multiload trashapplet
%find_lang --with-gnome %name %name-3.0 %applets

%if_enabled battstat
%post battstat
%gconf2_install battstat
%endif

%post cpufreq
%gconf2_install cpufreq-applet

%post charpick
%gconf2_install charpick

%post drivemount
%gconf2_install drivemount

%post geyes
%gconf2_install geyes

%post mini-commander
%gconf2_install mini-commander

%post mixer
%gconf2_install mixer

%post multiload
%gconf2_install multiload

%post stickynotes
%gconf2_install stickynotes

%if_enabled battstat
%preun battstat
if [ $1 = 0 ]; then
%gconf2_install battstat
fi
%endif

%preun cpufreq
if [ $1 = 0 ]; then
%gconf2_install cpufreq-applet
fi

%preun charpick
if [ $1 = 0 ]; then
%gconf2_install charpick
fi

%preun drivemount
if [ $1 = 0 ]; then
%gconf2_install drivemount
fi

%preun geyes
if [ $1 = 0 ]; then
%gconf2_uninstall geyes
fi

%preun mini-commander
if [ $1 = 0 ]; then
%gconf2_uninstall mini-commander
fi

%preun mixer
if [ $1 = 0 ]; then
%gconf2_uninstall mixer
fi

%preun multiload
if [ $1 = 0 ]; then
%gconf2_uninstall multiload
fi

%preun stickynotes
if [ $1 = 0 ]; then
%gconf2_uninstall stickynotes
fi

%files

%files common -f %name-3.0.lang
%doc AUTHORS ChangeLog NEWS README
%gnome_appletsdir/null_applet
%dir %_datadir/%name
%dir %_datadir/%name/builder

%files accessx-status -f accessx-status.lang
%gnome_appletsdir/accessx-status*
%_datadir/%name/ui/accessx-status-applet-menu.xml
%_datadir/pixmaps/accessx-status*
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.AccessxStatusApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.AccessxStatusAppletFactory.service
%_iconsdir/hicolor/48x48/apps/ax-applet.png

%if_enabled battstat
%files battstat -f battstat.lang
%gnome_appletsdir/battstat*
%_datadir/gnome-2.0/*/*Battstat*
%_datadir/gnome-applets/glade/battstat_applet.glade
%config %_sysconfdir/gconf/schemas/battstat*
%config %_sysconfdir/sound/*/battstat*
%endif

%files cpufreq -f cpufreq-applet.lang
%if_enabled frequency_selector
%attr(4711,root,root) %_bindir/cpufreq-selector
%endif
%gnome_appletsdir/cpufreq-applet
%_datadir/%name/ui/cpufreq-applet-menu.xml
%_datadir/gnome-applets/builder/cpufreq-preferences.ui
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.CPUFreqApplet.panel-applet
%_datadir/polkit-1/actions/org.gnome.cpufreqselector.policy
%_datadir/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%_datadir/dbus-1/services/org.gnome.panel.applet.CPUFreqAppletFactory.service
%_iconsdir/hicolor/*/apps/gnome-cpu-frequency-applet.png
%_iconsdir/hicolor/scalable/apps/gnome-cpu-frequency-applet.svg
%config %_sysconfdir/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%config %_sysconfdir/gconf/schemas/cpufreq-applet.schemas

%files cpufreq-usermode
%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla

%files charpick -f char-palette.lang
%gnome_appletsdir/charpick*
%_datadir/%name/ui/charpick-applet-menu.xml
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.CharpickerApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.CharpickerAppletFactory.service
%config %_sysconfdir/gconf/schemas/charpick*

%files drivemount -f drivemount.lang
%gnome_appletsdir/drivemount*
%_datadir/%name/ui/drivemount-applet-menu.xml
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.DriveMountApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.DriveMountAppletFactory.service
%config %_sysconfdir/gconf/schemas/drivemount*

%files geyes -f geyes.lang
%gnome_appletsdir/geyes*
%_datadir/%name/ui/geyes-applet-menu.xml
%_datadir/gnome-applets/geyes
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.GeyesApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.GeyesAppletFactory.service
%_iconsdir/hicolor/*/apps/gnome-eyes-applet.png
%_iconsdir/hicolor/scalable/apps/gnome-eyes-applet.svg
%config %_sysconfdir/gconf/schemas/geyes*

%files gweather -f gweather.lang
%gnome_appletsdir/gweather*
%_datadir/%name/ui/gweather-applet-menu.xml
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.GWeatherApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.GWeatherAppletFactory.service

%if_enabled mini_commander
%files mini-commander -f command-line.lang
%gnome_appletsdir/mini_commander*
%gnome_appletsdir/mc-install*
%_datadir/%name/ui/mini-commander-applet-menu.xml
%_datadir/gnome-applets/builder/mini-commander.ui
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.MiniCommanderApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.MiniCommanderAppletFactory.service
%_liconsdir/gnome-mini-commander.png
%config %_sysconfdir/gconf/schemas/mini-commander*
%endif

%if_enabled mixer
%files mixer -f mixer_applet2.lang
%gnome_appletsdir/mixer*
%_datadir/%name/ui/mixer-applet-menu.xml
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.MixerApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.MixerAppletFactory.service
%config %_sysconfdir/gconf/schemas/mixer*
%endif

%if_enabled modemlights
%files modemlights
%gnome_appletsdir/modemlights*
%_datadir/%name/ui/*modemlights*
%config %_sysconfdir/gconf/schemas/modemlights*
%endif

%files multiload -f multiload.lang
%gnome_appletsdir/multiload*
%_datadir/%name/ui/multiload-applet-menu.xml
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.MultiLoadApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.MultiLoadAppletFactory.service
%_datadir/pixmaps/*cpu*
%config %_sysconfdir/gconf/schemas/multiload*

%files stickynotes -f stickynotes_applet.lang
%gnome_appletsdir/stickynotes*
%_datadir/%name/ui/stickynotes-applet-menu.xml
%_datadir/gnome-applets/builder/stickynotes.ui
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.StickyNotesApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.StickyNotesAppletFactory.service
%_datadir/pixmaps/stickynotes
%_iconsdir/hicolor/*/apps/gnome-sticky-notes-applet.png
%_iconsdir/hicolor/scalable/apps/gnome-sticky-notes-applet.svg
%config %_sysconfdir/gconf/schemas/stickynotes*

%files trash -f trashapplet.lang
%gnome_appletsdir/trashapplet
%_datadir/%name/ui/trashapplet-menu.xml
%_datadir/gnome-applets/builder/trashapplet-empty-progress.ui
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.TrashApplet.panel-applet
%_datadir/dbus-1/services/org.gnome.panel.applet.TrashAppletFactory.service

%exclude %_datadir/dbus-1/services/org.gnome.panel.applet.NullAppletFactory.service
%exclude %_datadir/gnome-panel/4.0/applets/org.gnome.applets.NullApplet.panel-applet

%changelog
* Sun Apr 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri Jan 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.4-alt1
- 2.91.4 git snapshot

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1.1-alt2
- updated buildreq

* Wed Nov 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1.1-alt1
- 2.32.1.1

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Sep 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.92

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Thu Feb 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- new gnome-applets-cpufreq-usermode package (thx shaba@ for idea)

* Wed Jan 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5
- obsolete gswitchit applet removed

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sun May 31 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Mar 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92
- returned -mixer package (see NEWS)

* Sun Jan 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.4-alt1
- 2.25.4
- drop -mixer package (see NEWS)
- updated buildreqs

* Thu Jan 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3.1-alt1
- 2.24.3.1

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Sun Oct 26 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- rebuild

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Mon Sep 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version (2.22.3)

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 2.22.1-alt2
- rebuild

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- updated BuildPreReq

* Wed Mar 12 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.0-alt0.1
- new version (2.22.0)

* Thu Nov 22 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- new version (2.20.0)
- add Packager
- gswitchit.schemas does not exist anymore

* Wed Jul 18 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt3
- rebuild over again.

* Sun Jul 15 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt2
- rebuild with new libgucharmap.

* Sat Jul 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)
- move all applets to One Well-known Place (defined by %%gnome_appletsdir
  macro).
- use more path macros
- the patch for gswitchit headers is no more needed.
- no more gswitchit-devel subpackage.
- updated the files list.

* Sun Feb 11 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt2
- removed no more needed patch that relaxes DBus dependence to version 0.62
- added a patch that installs an additional header file (for gswitchit-plugins).

* Thu Dec 21 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt1
- new version 2.16.2 (with rpmrb script)

* Mon Oct 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version (2.16.1)
- updated dependencies

* Sat Sep 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0.1-alt1
- new version (2.16.0.1)

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- switched off battstat applet building, as gnome-power-manager provides
  its functionality, and battstat depends on libapm that doesn't exist on
  x86_64.

* Sat Sep 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt3
- fixed broken dependency in the virtual package.

* Thu Aug 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt2
- rebuild, no changes

* Wed Aug 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt1
- new version (2.15.90)

* Tue Aug 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.3-alt1
- new version

* Sat Aug 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt5
- rebuilt with new Gtk+.

* Fri Jun 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt4
- enabled battstat applet building (building WILL fail on x86_64, since
  there's no libapm for this arch).
- fixed more packaging errors.

* Thu Jun 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt3
- spec cleanup

* Wed Jun 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt2
- replaced gstreamer-plugins-devel with gst-plugins-devel in buildreqs.

* Mon Jun 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version (2.14.2)
- fixed excess files in gswitchit subpackage.

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Sat Apr 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version (2.14.0)

* Mon Mar 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.4-alt3
- fixed libgweather packaging mess (Bug #9185).

* Mon Feb 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.4-alt2
- added gweather-devel subpackage.

* Sat Feb 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.4-alt1
- new version
- dependencies updated, spec cleanup
- formally resurrected modemlights applet (disabled, needs system-tools-backends).
- temporarily disabled battstat applet, until libnotify 0.3.2 appears.

* Thu Feb 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.2-alt2.1
- fixed buildreqs.

* Mon Nov 28 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.2-alt2
- new version

* Sun Nov 20 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt3
- Fixed Bug #7862.
- Fixed Bug #8532. Also fixed groups of other subpackages.

* Fri Oct 07 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt2
- Fixed Bug #5838.

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed excess buildreqs.
- Removed the patch that was added in 2.11.93-alt1.
- Added /usr/share/gnome-applets to %files of gnome-applets-common.

* Sun Sep 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.93-alt1
- 2.11.93
- Added a temporary patch for building without HAL (already in GNOME CVS but wasn't released yet).

* Mon Apr 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Tue Mar 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.7-alt1
- 2.9.7.

* Thu Feb 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.6-alt1
- 2.9.6
- gtick built with gucharmap support.

* Mon Feb 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.5-alt1
- 2.9.5.
- gkb, cdplayer, mailcheck, wireless, modemlights obsolete.
- new cpufreq, trash applets.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1.1-alt1
- 2.8.1.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.3-alt1
- 2.7.3

* Thu Aug 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2.1-alt1
- 2.6.2.1

* Tue Jun 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Fri May 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1.1
- fix gswitchit (patch5).

* Fri May 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.8-alt1
- 2.5.8

* Mon Feb 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt2
- rebuild with new libgtop2-2.5.1

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Sat Oct 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0
- additional belorussian locations for gweather from Serg Kozhemyakin

* Thu Sep 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Thu Jul 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Mon Jun 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Mon Jun 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt2
- rebuild with libgtop2-2.0.2

* Mon Jun 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Mon Jun 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3
- new accessibility keyboard status applet.

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Mon Apr 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sun Mar 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Sun Jan 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Mon Jan 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt2
- default lock file for modemlights applet fixed.
- geyes themes installation and schema file fixed.

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Thu Nov 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Wed Nov 06 2002 AEN <aen@altlinux.ru> 2.0.3-alt2
- rebuilt with new gdbm

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt2
- rebuild with new pango, gtk+

* Mon Sep 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt1.1
- buildreqs updated.
- files section for gweather fixed.
- gconf2_install macro used for schemas installation.
- scrollkeeper >= 0.3.11 added to requires list.
- gnome-system-monitor added to requires list for multiload applet.
- gnome-applets virtual package installs all applets.

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Thu Jul 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt1
- First build for Sisyphus.
