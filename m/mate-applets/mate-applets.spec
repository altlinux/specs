Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/gdk-pixbuf-csource /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/jw /usr/bin/xsltproc libICE-devel libSM-devel libX11-devel libapm-devel libcpufreq-devel libgio-devel pkgconfig(NetworkManager) pkgconfig(dbus-1) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) pkgconfig(gucharmap-2) pkgconfig(hal) pkgconfig(libgtop-2.0) pkgconfig(mate-settings-daemon) python-devel python-module-pygobject-devel xorg-kbproto-devel
# END SourceDeps(oneline)
BuildRequires: xvfb-run
%define _libexecdir %_prefix/libexec
Name:           mate-applets
Version:        1.5.1
Release:        alt1_4
Summary:        MATE Desktop panel applets
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires: libdbus-glib-devel
BuildRequires: libgucharmap-devel
BuildRequires: libgtop2-devel
BuildRequires: libmatekeyring-devel
BuildRequires: libmatenotify-devel
BuildRequires: libmateweather-devel
BuildRequires: libmatewnck-devel
BuildRequires: libnm-gtk-devel
BuildRequires: libxml2-devel
BuildRequires: mate-common
BuildRequires: mate-control-center-devel
BuildRequires: mate-desktop-devel
BuildRequires: mate-doc-utils
BuildRequires: mate-file-manager-devel
BuildRequires: mate-icon-theme-devel
BuildRequires: mate-keyring-devel
BuildRequires: mate-menus-devel
BuildRequires: mate-notification-daemon
BuildRequires: mate-panel-devel
BuildRequires: libpolkit-devel
BuildRequires: python-module-pygtk-devel
BuildRequires: rarian-compat
BuildRequires: librarian-devel
BuildRequires: libstartup-notification-devel
Buildrequires: libupower-devel
Source44: import.info
Patch33: mate-applets-1.5.1-alt-geyes_schema.patch
Patch34: gnome-applets-2.6.0-alt-install_makefile.patch
Patch35: gnome-applets-2.9.90-alt-modemlights.patch

%description
MATE Desktop panel applets

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1
%patch34 -p1
%patch35 -p1


%build
%configure                       \
    --disable-schemas-compile    \
    --disable-scrollkeeper       \
    --with-gnu-ld                \
    --with-x                     \
    --enable-polkit              \
    --enable-networkmanager      \
    --enable-ipv6                \
    --enable-frequency-selector  \
    --enable-suid                \
    --disable-cpufreq            \
    --disable-timer-applet      

xvfb-run -a make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
%find_lang %{name} --all-name

#make python script executable
#http://forums.fedoraforum.org/showthread.php?t=284962
chmod a+x %{buildroot}%{python_sitelibdir_noarch}/mate_invest/chart.py
# alt 01-cpufreq.pkla
install -pD -m 644 %SOURCE0 %buildroot%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mate-invest-chart
%{python_sitelibdir_noarch}/mate_invest
%{_libexecdir}/invest-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.InvestAppletFactory.service
%{_datadir}/icons/hicolor/scalable/apps/mate-invest-applet.svg
%{_datadir}/mate/help/mate-invest-applet
%{_datadir}/omf/mate-invest-applet
%{_datadir}/mate-applets
%{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_libexecdir}/accessx-status-applet
%{_libexecdir}/battstat-applet-2
%{_libexecdir}/charpick_applet2
%{_libexecdir}/drivemount_applet2
%{_libexecdir}/geyes_applet2
%{_libexecdir}/stickynotes_applet
%{_libexecdir}/trashapplet
%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.TrashAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.battstat.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.charpick.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.geyes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.stickynotes.gschema.xml
%{_datadir}/icons/hicolor/*x*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-eyes-applet.svg
%{_datadir}/icons/hicolor/scalable/apps/mate-sticky-notes-applet.svg
%{_datadir}/icons/mate/48x48/apps/ax-applet.png
%{_datadir}/mate-2.0/ui/accessx-status-applet-menu.xml
%{_datadir}/mate-2.0/ui/battstat-applet-menu.xml
%{_datadir}/mate-2.0/ui/charpick-applet-menu.xml
%{_datadir}/mate-2.0/ui/drivemount-applet-menu.xml
%{_datadir}/mate-2.0/ui/geyes-applet-menu.xml
%{_datadir}/mate-2.0/ui/stickynotes-applet-menu.xml
%{_datadir}/mate-2.0/ui/trashapplet-menu.xml
%{_datadir}/mate-panel/applets
%{_datadir}/mate/help/mate-accessx-status
%{_datadir}/mate/help/mate-battstat
%{_datadir}/mate/help/mate-char-palette
%{_datadir}/mate/help/mate-drivemount
%{_datadir}/mate/help/mate-geyes
%{_datadir}/mate/help/mate-stickynotes_applet
%{_datadir}/mate/help/mate-trashapplet
%{_datadir}/mate/help/mateweather
%{_datadir}/omf/mate-accessx-status
%{_datadir}/omf/mate-battstat
%{_datadir}/omf/mate-char-palette
%{_datadir}/omf/mate-drivemount
%{_datadir}/omf/mate-geyes
%{_datadir}/omf/mate-stickynotes_applet
%{_datadir}/omf/mate-trashapplet
%{_datadir}/omf/mateweather
%{_datadir}/omf/mate-multiload
%{_datadir}/pixmaps/mate-accessx-status-applet
%{_datadir}/pixmaps/mate-stickynotes
%{_datadir}/MateConf/gsettings/stickynotes-applet.convert
%{_libexecdir}/mateweather-applet-2
%{_libexecdir}/multiload-applet-2
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.multiload.gschema.xml
%{_datadir}/mate-2.0/ui/mateweather-applet-menu.xml
%{_datadir}/mate-2.0/ui/multiload-applet-menu.xml
%{_datadir}/mate/help/mate-multiload
%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla

%changelog
* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_4
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1
- new version

* Mon Nov 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1.1.1
- fixed build

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Tue Aug 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

