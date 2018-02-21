Group: Graphical desktop/MATE
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize imake libX11-devel libXt-devel libapm-devel libgio-devel pkgconfig(dbus-1) pkgconfig(dbus-glib-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-3.0) xorg-cf-files xorg-kbproto-devel
# END SourceDeps(oneline)
BuildRequires: libcpupower-devel
BuildRequires: xvfb-run
%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-applets
%define version 1.20.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.20

# Settings used for build from snapshots.
%{!?rel_build:%global commit c3b48ea39ab358b45048e300deafaa3f569748ad}
%{!?rel_build:%global commit_date 20140211}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-applets
Version:        %{branch}.0
%if 0%{?rel_build}
Release:        alt1_1
%else
Release:        alt1_1
%endif
Summary:        MATE Desktop panel applets
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R mate-applets.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: libgucharmap-devel libgucharmap-gir-devel
BuildRequires: libgtop-devel libgtop-gir-devel
BuildRequires: libnotify-devel libnotify-gir-devel
BuildRequires: libmateweather-devel
BuildRequires: libwnck libwnck3-devel libwnck3-gir-devel
BuildRequires: libxml2-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: mate-common
BuildRequires: mate-settings-daemon-devel
BuildRequires: mate-notification-daemon
BuildRequires: mate-panel-devel
BuildRequires: libpolkit-devel libpolkit-gir-devel
BuildRequires: libstartup-notification-devel
Buildrequires: libupower-devel libupower-gir-devel
Buildrequires: libgtksourceview3-devel libgtksourceview3-gir-devel
BuildRequires: libwireless-devel
%ifnarch s390 s390x sparc64
BuildRequires: libcpupower-devel
%endif

Provides:   mate-netspeed = %{version}-%{release}
Provides:   mate-netspeed = %{version}-%{release}
Obsoletes:  mate-netspeed < %{version}-%{release}
Source44: import.info
Patch33: mate-applets-1.12.1-alt-geyes_schema.patch
Patch34: gnome-applets-2.6.0-alt-install_makefile.patch
Source45: 01-cpufreq.pkla


%description
MATE Desktop panel applets

%prep
%if 0%{?rel_build}
%setup -q

%else
%setup -q -n %{name}-%{commit}

%endif

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}
%patch33 -p1
%patch34 -p1

%build
%configure   \
    --disable-schemas-compile                \
    --disable-static                         \
    --with-x                                 \
    --enable-polkit                          \
    --enable-ipv6                            \
    --enable-stickynotes                     \
    --libexecdir=%{_libexecdir}/mate-applets \
    --with-cpufreq-lib=cpupower

%make_build V=1

%install
%{makeinstall_std}

%find_lang %{name} --with-gnome --all-name
# alt 01-cpufreq.pkla
install -pD -m 644 %{SOURCE45} %buildroot%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mate-cpufreq-selector
%{_libexecdir}/mate-applets
%config(noreplace) %{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.mate.CPUFreqSelector.conf
%{_datadir}/mate-applets
%{_datadir}/mate-panel/applets
%{_datadir}/dbus-1/services/org.mate.panel.applet.CommandAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.TimerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.TrashAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.NetspeedAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.battstat.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.charpick.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.drivemount.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.geyes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.multiload.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.stickynotes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.cpufreq.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.command.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.timer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.netspeed.gschema.xml
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/devices/*.png
%{_datadir}/icons/hicolor/*/status/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/*
%{_datadir}/mate/ui/accessx-status-applet-menu.xml
%{_datadir}/mate/ui/battstat-applet-menu.xml
%{_datadir}/mate/ui/charpick-applet-menu.xml
%{_datadir}/mate/ui/drivemount-applet-menu.xml
%{_datadir}/mate/ui/geyes-applet-menu.xml
%{_datadir}/mate/ui/stickynotes-applet-menu.xml
%{_datadir}/mate/ui/trashapplet-menu.xml
%{_datadir}/mate/ui/mateweather-applet-menu.xml
%{_datadir}/mate/ui/multiload-applet-menu.xml
%{_datadir}/mate/ui/cpufreq-applet-menu.xml
%{_datadir}/mate/ui/netspeed-menu.xml
%{_datadir}/pixmaps/mate-accessx-status-applet
%{_datadir}/pixmaps/mate-cpufreq-applet
%_sysconfdir/polkit-1/localauthority/50-local.d/01-cpufreq.pkla


%changelog
* Wed Feb 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.2-alt1_1
- new fc release

* Fri Sep 15 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.1-alt1_2
- new fc release

* Wed Sep 13 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.1-alt1_1
- new fc release

* Thu Sep 07 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_3
- new fc release

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_1
- update to 1.16

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new version

* Thu Oct 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.3-alt1_1
- new version

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt4_1
- rebuilt against libupower-glib.so.3

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt3_1
- rebuild with libgtop

* Mon Mar 31 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_1
- rebuild with new upower

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_5
- new fc release

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Thu Apr 04 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.2-alt2_2
- package plain 01-cpufreq.pkla instead of tar.xz file (closes: 28794)

* Thu Apr 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.2-alt1_2.1
- hal dependence removed

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_2
- new fc release

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1
- new fc release

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

