Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/docbook2man /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/xmlto libgio-devel pkgconfig(dbus-1) pkgconfig(gdk-2.0) pkgconfig(gdk-x11-2.0) pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libsystemd-daemon) pkgconfig(libsystemd-login) pkgconfig(mate-keyring-1) pkgconfig(unique-3.0) pkgconfig(x11) pkgconfig(xext) pkgconfig(xproto) pkgconfig(xrandr) pkgconfig(xrender)
# END SourceDeps(oneline)
%filter_from_requires /^hal$/d
%define _libexecdir %_prefix/libexec
Name:          mate-power-manager
Version:       1.6.0
Release:       alt3
Summary:       MATE power management service
License:       GPLv2+
URL:           http://pub.mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
Patch0:	mpm-alt-logind-support.patch

BuildRequires: libcairo-devel
BuildRequires: libdbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: libcanberra-devel
BuildRequires: libmatenotify-devel
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: mate-common
BuildRequires: mate-control-center-devel
BuildRequires: mate-doc-utils
BuildRequires: mate-keyring-devel
BuildRequires: mate-panel-devel
BuildRequires: popt-devel
BuildRequires: rarian-compat
BuildRequires: systemd-devel
BuildRequires: libunique-devel
BuildRequires: libupower-devel
BuildRequires: libnotify-devel
Source44: import.info


%description
MATE Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive MATE session.


%prep
%setup -q
%patch -p2
NOCONFIGURE=1 ./autogen.sh


%build
%configure  --disable-static --disable-scrollkeeper --enable-applets --without-systemdinhibit
make V=1 %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
%find_lang %{name} --all-name
desktop-file-install                               \
     --delete-original                             \
     --remove-category=MATE                        \
     --add-category=X-Mate                         \
     --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/*.desktop


%files  -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/**
%{_bindir}/mate-power-bugreport.sh
%{_bindir}/mate-power-manager
%{_bindir}/mate-power-preferences
%{_bindir}/mate-power-statistics
%{_sbindir}/mate-power-backlight-helper
%{_datadir}/omf/mate-power-manager/
%{_datadir}/applications/mate-*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mate-power-manager/
%{_datadir}/icons/hicolor/*/apps/mate-*.*
%{_datadir}/polkit-1/actions/org.mate.power.policy
%{_datadir}/mate/help/mate-power-manager/
%{_datadir}/mate-2.0/ui/brightness-applet-menu.xml
%{_datadir}/mate-2.0/ui/inhibit-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.BrightnessApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.InhibitApplet.mate-panel-applet
%{_datadir}/glib-2.0/schemas/org.mate.power-manager.gschema.xml
%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet

%changelog
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

