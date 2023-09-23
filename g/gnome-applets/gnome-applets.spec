%def_disable snapshot

%define ver_major 3.50
%define xdg_name org.gnome.gnome-applets

%def_enable frequency_selector
%def_enable battstat
%def_enable command
%def_enable mini_commander
%def_enable timer
%def_enable tracker

Name: gnome-applets
Version: %ver_major.0
Release: alt1

Summary: Small applications for the GNOME panel
License: GPL-2.0 and GFDL-1.1
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/GnomeApplets

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Source1: 01-cpufreq.pkla
Patch1: %name-3.22.0-alt-cpufreq_libs.patch

# From configure.ac
%define gtk_ver 3.20.0
%define glib_ver 2.44.0
%define gnome_panel_ver %ver_major
%define libgtop_ver 2.12.0
%define libgail_ver 3.0
%define libxklavier_ver 4.0
%define libwnck_ver 43.0
%define libnotify_ver 0.7.1
%define icon_theme_ver 3.14
%define libgweather4_ver 3.99
%define tracker_api_ver 3.0

Requires: gnome-panel >= %gnome_panel_ver
Requires: gvfs
%{?_enable_tracker:Requires: tracker3}

Obsoletes: %name-common < 3.37
Provides: %name-common = %EVR
Obsoletes: %name-charpick < 3.37
Provides: %name-charpick = %EVR
Obsoletes: %name-drivemount < 3.37
Provides: %name-drivemount = %EVR
Obsoletes: %name-stickynotes < 3.37
Provides: %name-stickynotes = %EVR
Obsoletes: %name-geyes < 3.37
Provides: %name-geyes = %EVR
Obsoletes: %name-gweather < 3.37
Provides: %name-gweather = %EVR
Obsoletes: %name-multiload < 3.37
Provides: %name-multiload = %EVR
Obsoletes: %name-accessx-status < 3.37
Provides: %name-accessx-status = %EVR
Obsoletes: %name-netspeed < 3.37
Provides: %name-netspeed = %EVR
Obsoletes: %name-brightness < 3.37
Provides: %name-brightness = %EVR
Obsoletes: %name-inhibit < 3.37
Provides: %name-inhibit = %EVR
Obsoletes: %name-window-buttons < 3.37
Provides: %name-window-buttons = %EVR
Obsoletes: %name-window-title < 3.37
Provides: %name-window-title = %EVR
Obsoletes: %name-cpufreq-usermode < 3.37
Provides: %name-cpufreq-usermode = %EVR
Obsoletes: %name-tracker-search-bar < 3.37
Provides: %name-tracker-search-bar = %EVR
%{?_enable_frequency_selector:
Obsoletes: %name-cpufreq < 3.37
Provides: %name-cpufreq = %EVR}
%{?_enable_mini_commander:
Obsoletes: %name-mini-commander < 3.37
Provides: %name-mini-commander = %EVR}
%{?_enable_battstat:
Obsoletes: %name-battstat < 3.37
Provides: %name-battstat = %EVR}
%{?_enable_command:
Obsoletes: %name-command < 3.37
Provides: %name-command = %EVR}
%{?_enable_timer:
Obsoletes: %name-timer < 3.37
Provides: %name-timer = %EVR}

BuildRequires(pre): rpm-build-gnome
# From configure.ac
BuildRequires: autoconf-archive
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgnome-panel-devel >= %gnome_panel_ver
BuildRequires: libgtop-devel >= %libgtop_ver
BuildRequires: libgail3-devel >= %libgail_ver
BuildRequires: libxklavier-devel >= %libxklavier_ver
BuildRequires: libwnck3-devel >= %libwnck_ver
BuildRequires: libnotify-devel >= %libnotify_ver
BuildRequires: icon-theme-adwaita >= %icon_theme_ver
BuildRequires: libX11-devel libXt-devel
BuildRequires: libgucharmap-devel >= 2.33.2
BuildRequires: libgweather4.0-devel >= %libgweather4_ver
BuildRequires: icon-theme-adwaita
BuildRequires: gnome-settings-daemon-devel
BuildRequires: libxml2-devel libdbus-devel
BuildRequires: libpolkit-devel xorg-cf-files yelp-tools
%{?_enable_battstat:BuildRequires: libupower-devel}
%{?_enable_tracker:BuildRequires: pkgconfig(tracker-sparql-%tracker_api_ver)}
%{?_enable_frequency_selector:BuildRequires: libcpufreq-devel}

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

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
    %{?_disable_battstat:--disable-battstat} \
    %{?_disable_frequency_selector:--disable-frequency-selector}
%nil
%make_build

%install
%makeinstall_std localstatedir=%buildroot%_localstatedir
install -pD -m 644 %SOURCE1 %buildroot%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla
%define applets accessx-status battstat char-palette cpufreq-applet command-line drivemount gweather geyes stickynotes_applet multiload trashapplet netspeed_applet windowpicker brightness inhibit %{?_enable_tracker:tracker-search-bar} window-buttons window-title
%find_lang --with-gnome --output=%name.lang %name %applets

%files -f %name.lang

%_libdir/gnome-panel/modules/org.gnome.gnome-applets.so
%_datadir/%name
%_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%_iconsdir/hicolor/*x*/*/*.png
%_iconsdir/hicolor/scalable/*/*.svg
%_datadir/glib-2.0/schemas/%xdg_name.charpick.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.cpufreq.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.gweather.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.multiload.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.netspeed.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.stickynotes.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.window-buttons.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.window-picker-applet.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.gnome-applets.window-title.gschema.xml
%_datadir/polkit-1/actions/org.gnome.cpufreqselector.policy
%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla
%_datadir/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%_datadir/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%config %_datadir/glib-2.0/schemas/%xdg_name.geyes.gschema.xml
%{?_enable_battstat:%_datadir/glib-2.0/schemas/%xdg_name.battstat.gschema.xml}
%{?_enable_command:%_datadir/glib-2.0/schemas/%xdg_name.command.gschema.xml}
%{?_enable_mini_commander:%_datadir/glib-2.0/schemas/%xdg_name.mini-commander.gschema.xml}
%{?_enable_timer:%_datadir/glib-2.0/schemas/%xdg_name.timer.gschema.xml}

%if_enabled frequency_selector
%attr(4711,root,root) %_bindir/cpufreq-selector
%endif

%doc AUTHORS NEWS README*

%exclude %_libdir/gnome-panel/modules/*.la

%changelog
* Sat Sep 23 2023 Yuri N. Sedunov <aris@altlinux.org> 3.50.0-alt1
- 3.50.0

* Sun Oct 02 2022 Yuri N. Sedunov <aris@altlinux.org> 3.46.0-alt1
- 3.46.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.0-alt1
- 3.44.0

* Sat Oct 23 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.0-alt1
- 3.42.0

* Thu Mar 25 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Sat Oct 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.37.2-alt1
- updated to 3.37.2-12-g28254e22d
- removed all subpackages
- disabled traker-2.0 based tracker-search-bar

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Sun Mar 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Thu Mar 26 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sat Mar 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0-4-g42040d292

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun May 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0 (removed modem-lights applet)

* Tue Feb 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt2
- rebuilt battstat against current libapm

* Sun Sep 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt2
- rebuilt against libgtop-2.0.so.11/tracker-2.0

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt2
- rebuilt against libpanel-applet.so.3

* Sat Oct 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sat Apr 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0, new -timer and -command applets/subpackages

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Sun Sep 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0
- new -brightness, -inhibit, -tracker subpackages

* Tue Aug 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.2-alt1
- 3.17.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0
- new -netspeed subpackage

* Sun Feb 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1
- 3.15.2

* Wed Oct 29 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed Oct 29 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Sep 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Thu Mar 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt0.2
- rebuilt for GNOME-3.7.x

* Tue Oct 23 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt0.1
- 3.6.1 snapshot

* Sat Sep 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.92-alt1
- 3.5.92

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
