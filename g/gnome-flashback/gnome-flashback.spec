%def_disable snapshot

%define ver_major 3.22
%define _libexecdir %_prefix/libexec
%def_with compiz

Name: gnome-flashback
Version: %ver_major.1
Release: alt1

Summary: GNOME Flashback session
License: GPLv3
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/GnomeFlashback

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.44.0
%define gtk_ver 3.20.0
%define desktop_ver 3.12.0
%define dbus_glib_ver 0.76
%define gsds_ver 3.12.0

PreReq: xinitrc
Requires: gnome-session gnome-settings-daemon gnome-panel gnome-applets metacity3.0
Requires: libcanberra-gnome libcanberra-gtk3
Requires: altlinux-freedesktop-menu-gnome3
Requires: dbus-tools-gui
Requires: gnome-filesystem
Requires: xdg-user-dirs
Requires: gnome-icon-theme gnome-icon-theme-symbolic
Requires: fonts-otf-abattis-cantarell gnome-backgrounds
Requires: gnome-screensaver
Requires: gnome-keyring
Requires: gnome-control-center
Requires: nautilus
# since 3.18
Requires: polkit accountsservice
Requires: pinentry-gnome3
Requires: upower
Requires: bluez
Requires: NetworkManager-applet-gtk
Requires: ibus xkeyboard-config
# since 3.20
Conflicts: notification-daemon < 3.20

BuildRequires: rpm-build-gnome gnome-common
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libdbus-glib-devel >= %dbus_glib_ver
BuildRequires: libgnome-desktop3-devel >= %desktop_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: libcanberra-gtk3-devel libpulseaudio-devel
BuildRequires: libXext-devel libXrandr-devel
BuildRequires: libupower-devel
# since 3.18
BuildRequires: libpolkit-devel libgnome-bluetooth-devel libxcb-devel
BuildRequires: libibus-devel libxkbcommon-x11-devel libXi-devel
BuildRequires: libxkbfile-devel xkeyboard-config-devel

%description
GNOME Flashback provides unofficial session and helper application.

This session consists of gnome-applets, gnome-flashback, gnome-panel and
metacity. And all other modules that are used in official GNOME session.

Helper application main job is to provide all features that is need for
our session, but has been removed from GNOME and/or moved to mutter or
gnome-shell.

NOTE: This session is not supported by GNOME in any way!

%package session-compiz
Summary: A Compiz session for the GNOME Flashback
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: %name = %version-%release
Requires: compiz

%description session-compiz
This package permits to log into GNOME Flashback with Compiz.


%prep
%setup

%build
%autoreconf
%configure \
    --disable-schemas-compile
%make_build

%install
%makeinstall_std

# link to our gnome3 menus
ln -sf gnome-applications.menu %buildroot/%_xdgmenusdir/%name-applications.menu

%find_lang --with-gnome --output=%name.lang %name

%check
%make check

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-compiz
%_libexecdir/%name-metacity
%_desktopdir/%name.desktop
%_desktopdir/%name-init.desktop
%_datadir/desktop-directories/X-GNOME-Flashback-Settings-System.directory
%_datadir/desktop-directories/X-GNOME-Flashback-Settings.directory
%_datadir/gnome-session/sessions/%name-compiz.session
%_datadir/gnome-session/sessions/%name-metacity.session
%config %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_xdgmenusdir/%name-applications.menu
%_datadir/xsessions/%name-metacity.desktop
%_xdgconfigdir/autostart/%name-nm-applet.desktop
%_xdgconfigdir/autostart/%name-screensaver.desktop
%doc AUTHORS NEWS README

%if_with compiz
%files session-compiz
%_datadir/xsessions/%name-compiz.desktop
%endif


%changelog
* Tue Mar 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Thu Oct 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Jul 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Thu Jul 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt2
- updated to 3.20.1-7-ge76b61f
- packaged compiz session

* Wed May 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sun Apr 03 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Thu Oct 29 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt2
- updated dependencies
- prepared new session-compiz subpackage

* Thu Oct 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt2
- removed /usr/bin/startgnome-flashback

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Aug 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.2-alt1
- 3.17.2

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Apr 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Mar 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt2
- after 3.15.2 snapshot

* Sun Feb 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1
- 3.15.2

* Wed Oct 29 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2.1
- fixed gnome-authentication-agent.desktop

* Wed Oct 29 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2
- run polkit-gnome-authentication-agent-1 if session is gnome-flashback

* Mon Oct 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- first build for Sisyphus

