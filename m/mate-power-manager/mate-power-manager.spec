Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/docbook2man /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/xmlto libgio-devel pkgconfig(dbus-1) pkgconfig(gdk-2.0) pkgconfig(gdk-x11-2.0) pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libsystemd-daemon) pkgconfig(libsystemd-login) pkgconfig(mate-keyring-1) pkgconfig(unique-3.0) pkgconfig(x11) pkgconfig(xext) pkgconfig(xproto) pkgconfig(xrandr) pkgconfig(xrender)
# END SourceDeps(oneline)
%filter_from_requires /^hal$/d
%define _libexecdir %_prefix/libexec
Name:           mate-power-manager
Version:        1.5.1
Release:        alt1_4
Summary:        MATE power management service

License:        GPLv2+
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

# PATCH-FIX-UPSTREAM - systemd inhibit requires systemd >= 195, adding checks
# fixes crasher, https://github.com/mate-desktop/mate-power-manager/pull/43
Patch0:         %{name}-1.5.1-add_systemd_checks.patch

BuildRequires: mate-panel-devel
BuildRequires: popt-devel
BuildRequires: mate-doc-utils
BuildRequires: desktop-file-utils
BuildRequires: libcairo-devel
BuildRequires: libcanberra-devel
BuildRequires: libmatenotify-devel
BuildRequires: libupower-devel
BuildRequires: libunique-devel
BuildRequires: glib2-devel
BuildRequires: rarian-compat
BuildRequires: gtk2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: mate-control-center-devel
BuildRequires: mate-common
BuildRequires: mate-keyring-devel
BuildRequires: systemd-devel

Requires: dbus-tools-gui
Requires: mate-panel-libs
Source44: import.info
Patch33: mate-power-manager-dont-eat-the-logs.patch

%description
MATE Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive MATE session.

%prep
%setup -q
%patch0 -p1
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1


%build
%configure \
        --disable-static \
        --disable-scrollkeeper \
        --enable-applets

make V=1 %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original             \
  --remove-category=MATE                           \
  --add-category=X-Mate                            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-*.desktop

%find_lang %{name} --with-gnome

%files  -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/*
%{_sbindir}/*
%{_sysconfdir}/xdg/autostart/mate-*.desktop
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
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet
%{_mandir}/man1/*.1.*


%changelog
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

