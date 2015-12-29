Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/docbook2man /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/xmlto libgio-devel pkgconfig(cairo) pkgconfig(dbus-1) pkgconfig(dbus-glib-1) pkgconfig(gdk-2.0) pkgconfig(gdk-3.0) pkgconfig(gdk-x11-2.0) pkgconfig(gdk-x11-3.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gnome-keyring-1) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libcanberra-gtk) pkgconfig(libcanberra-gtk3) pkgconfig(libmatepanelapplet-4.0) pkgconfig(libnotify) pkgconfig(mate-desktop-2.0) pkgconfig(unique-1.0) pkgconfig(unique-3.0) pkgconfig(upower-glib) pkgconfig(x11) pkgconfig(xext) pkgconfig(xproto) pkgconfig(xrandr) pkgconfig(xrender)
# END SourceDeps(oneline)
%filter_from_requires /^hal$/d
BuildRequires: mate-common
%define _libexecdir %_prefix/libexec
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mate-power-manager
%define version 1.10.2
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.10

# Settings used for build from snapshots.
%{!?rel_build:%global commit 3a68372f379644cc50d4cd9bb6f012653eddb683}
%{!?rel_build:%global commit_date 20150319}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:          mate-power-manager
Version:       %{branch}.2
Release:       alt2
#Release:       0.1%{?git_rel}%{?dist}
Summary:       MATE power management service
License:       GPLv2+
URL:           http://pub.mate-desktop.org
Requires:	upower

# for downloading the tarball use 'spectool -g -R mate-power-manager.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}
Source44: import.info



%description
MATE Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive MATE session.


%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}

# needed for git snapshots
#NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static --enable-applets \
     --enable-docbook-docs \
     --enable-unique \
     --with-gtk=2.0 \
     --disable-schemas-compile

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

desktop-file-install                               \
     --delete-original                             \
     --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/*.desktop

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/mate-power-manager.convert

%find_lang %{name} --with-gnome --all-name


%files  -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/mate-power-*.*
%{_bindir}/mate-power-manager
%{_bindir}/mate-power-preferences
%{_bindir}/mate-power-statistics
%{_sbindir}/mate-power-backlight-helper
%{_datadir}/applications/mate-*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mate-power-manager/
%{_datadir}/icons/hicolor/*/apps/mate-*.*
%{_datadir}/polkit-1/actions/org.mate.power.policy
%{_datadir}/mate-panel/applets/org.mate.BrightnessApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.InhibitApplet.mate-panel-applet
%{_datadir}/glib-2.0/schemas/org.mate.power-manager.gschema.xml
%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet


%changelog
* Tue Dec 29 2015 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.10.2-alt2
- requires: upower added (closes: #31672)

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt3_1
- rebuilt against libupower-glib.so.3

* Mon Mar 31 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_1
- rebuild with new upower

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_3
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_2
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1
- new fc release

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt3_2
- new fc release

* Thu Apr 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt3_1
- new fc release

* Tue Apr 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt3
- crash fixed

* Mon Apr 08 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt2
- added suspend/hybernate via logind
- enabled systemdinhibit

* Thu Apr 04 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.0-alt1
- new version
- drop upstreamed patches
- disable systemdinhibit

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_6
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_4
- new fc release

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- get rid of hal dependency

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

