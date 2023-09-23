%def_disable snapshot

%define ver_major 3.50
%define _libexecdir %_prefix/libexec
%def_with compiz

Name: gnome-flashback
Version: %ver_major.0
Release: alt1

Summary: GNOME Flashback session
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Projects/GnomeFlashback

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.44.0
%define gtk_ver 3.22.0
%define desktop_ver 43
%define gsds_ver 3.32.0
%define compiz_ver 0.9.14.0
%define bt_api_ver 3.0
%define panel_ver %ver_major
%define applets_ver %ver_major
%define metacity_ver %ver_major

Requires(pre): xinitrc
Requires: wm-common-freedesktop
Requires: gnome-session >= 3.33.90 gnome-settings-daemon
Requires: gnome-panel >= %panel_ver gnome-applets >= %applets_ver metacity3.0 >= %metacity_ver
Requires: altlinux-freedesktop-menu-gnome3
Requires: dbus-tools-gui
Requires: gnome-filesystem
Requires: xdg-user-dirs
Requires: gnome-icon-theme gnome-icon-theme-symbolic
Requires: fonts-otf-abattis-cantarell gnome-backgrounds
Requires: gnome-keyring
Requires: gnome-control-center
Requires: nautilus
# since 3.18
Requires: polkit accountsservice
Requires: pinentry-gnome3
Requires: upower
Requires: bluez gnome-bluetooth%bt_api_ver
Requires: NetworkManager-applet-gtk
Requires: ibus xkeyboard-config
Requires: alacarte
# since 3.20
Conflicts: notification-daemon < 3.20

BuildRequires(pre): rpm-build-gnome rpm-build-xdg rpm-build-systemd gnome-common
BuildRequires: libgnome-panel-devel >= %panel_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgnome-desktop3-devel >= %desktop_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: libcanberra-gtk3-devel libpulseaudio-devel
BuildRequires: libXext-devel libXrandr-devel
BuildRequires: libupower-devel
# since 3.18
BuildRequires: libpolkit-devel pkgconfig(gnome-bluetooth-%bt_api_ver) libxcb-devel
BuildRequires: libibus-devel libxkbcommon-x11-devel libXi-devel
BuildRequires: libxkbfile-devel xkeyboard-config-devel
# since 3.36 (for screensaver)
BuildRequires: libpam-devel
BuildRequires: gdm-libs-devel libXxf86vm-devel
%{?_with_compiz:BuildRequires: libcompiz-devel >= %compiz_ver}

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
# remove pre-generated
find ./ -name "*enum-types.[c,h]" -print0 | xargs -r0 rm -f --

%build
%autoreconf
%configure \
    --disable-static \
    --disable-schemas-compile \
    %{?_with_compiz:--with-compiz-session}
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
%_libdir/gnome-panel/modules/system_indicators.so
%exclude %_libdir/gnome-panel/modules/system_indicators.la
%_libexecdir/%name-metacity
%_libexecdir/%name-clipboard
%_libexecdir/%name-media-keys
%_libexecdir/%name-idle-monitor
%_libexecdir/%name-polkit
%_desktopdir/%name.desktop
%_datadir/gnome-panel/layouts/%name.layout
%_datadir/desktop-directories/X-GNOME-Flashback-Settings-System.directory
%_datadir/desktop-directories/X-GNOME-Flashback-Settings.directory
%_datadir/gnome-session/sessions/%name-metacity.session
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.%name.desktop.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.%name.desktop.background.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.%name.desktop.enums.xml
%_datadir/glib-2.0/schemas/org.gnome.%name.desktop.icons.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.%name.keybindings.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.%name.system-indicators.input-sources.gschema.xml
%_datadir/glib-2.0/schemas/00_gnome-flashback.gschema.override
%_datadir/gnome-control-center/keybindings/50-gnome-flashback-screenshots.xml
%_xdgmenusdir/%name-applications.menu
%_datadir/xsessions/%name-metacity.desktop
%_xdgconfigdir/autostart/%name-idle-monitor.desktop
%_xdgconfigdir/autostart/%name-nm-applet.desktop
%_xdgconfigdir/autostart/%name-clipboard.desktop
%_xdgconfigdir/autostart/%name-media-keys.desktop
%_xdgconfigdir/autostart/%name-polkit.desktop

%_userunitdir/%name.service
%_userunitdir/%name.target
%_userunitdir/gnome-session@gnome-flashback-metacity.target.d/session.conf
%doc AUTHORS NEWS README*

%if_with compiz
%files session-compiz
%_libexecdir/%name-compiz
%_userunitdir/gnome-session@gnome-flashback-compiz.target.d/session.conf
%_datadir/gnome-session/sessions/%name-compiz.session
%_datadir/xsessions/%name-compiz.desktop
%_sysconfdir/compizconfig/%name.conf
%_sysconfdir/compizconfig/%name.ini
%endif


%changelog
* Sat Sep 23 2023 Yuri N. Sedunov <aris@altlinux.org> 3.50.0-alt1
- 3.50.0

* Tue Oct 04 2022 Yuri N. Sedunov <aris@altlinux.org> 3.46.0-alt1
- 3.46.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 3.44.0-alt1
- 3.44.0

* Tue Nov 23 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.1-alt1
- 3.42.1

* Tue Nov 02 2021 Yuri N. Sedunov <aris@altlinux.org> 3.42.0-alt1
- 3.42.0

* Thu Mar 25 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Sat Oct 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Thu Aug 20 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Thu Apr 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Thu Apr 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Sun Mar 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Tue Feb 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.35.2-alt1
- 3.35.2

* Fri Nov 01 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Thu Oct 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun May 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Sep 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Jul 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt2
- fixed buildreqs

* Sun Mar 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Mar 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt2
- updated to 3.26.0-31-ge5fd9bc

* Thu Oct 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Mar 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

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

