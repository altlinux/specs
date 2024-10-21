%def_disable snapshot
%define optflags_lto %nil

%define _libexecdir %_prefix/libexec
%define _name control-center
%define ver_major 47
%define beta %nil
%define api_ver 2.0
%define xdg_name org.gnome.Settings

%def_disable debug
%def_enable bluetooth
%def_enable snap
%def_enable malcontent
%def_enable doc
%def_enable check

Name: gnome-control-center
Version: %ver_major.1
Release: alt1%beta

Summary: GNOME Control Center
License: GPL-2.0-or-later
Group: Graphical desktop/GNOME
Url: https://www.gnome.org

%if_enabled snapshot
Source: %name-%version%beta.tar
%else
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz
%endif
Source1: https://raw.githubusercontent.com/eggert/tz/main/zone.tab

%define glib_ver 2.75.0
%define gtk4_ver 4.15.2
%define adwaita_ver 1.6
%define desktop_ver 43
%define fontconfig_ver 1.0.0
%define gsds_ver 47
# nm_client_get_permissions_state()
%define nm_ver 1.46
%define goa_ver 3.49.1
%define acc_ver 0.6.39
%define sett_daemon_ver 42
%define bt_api_ver 3.0
%define bt_ver 42
%define systemd_ver 40
%define wacom_ver 0.7
%define ibus_ver 1.5.2
%define colord_ver 1.0
%define pwq_ver 1.2.2
%define upower_ver 0.99.8
%define grilo_ver 0.3.0
%define polkit_ver 0.114
%define snapd_ver 1.62
%define malcontent_ver 0.11.0
%define gudev_ver 232
%define pulse_ver 2.0
%define cups_ver 1.4

Requires: %name-data = %EVR

# For /usr/share/gnome
Requires: gnome-filesystem
Requires: gnome-settings-daemon >= %sett_daemon_ver
# for graphical passwd changing apps
Requires: accountsservice >= %acc_ver
Requires: cups-pk-helper
Requires: geoclue2
Requires: shadow-utils
Requires: setxkbmap
Requires: fwupd
Requires: gnome-online-accounts >= %goa_ver
Requires: gnome-bluetooth%bt_api_ver
# for VPN
Requires: NetworkManager-openvpn-gtk4
Requires: NetworkManager-pptp-gtk4
Requires: NetworkManager-vpnc-gtk4
Requires: NetworkManager-l2tp-gtk4
# for sharing
Requires: gnome-user-share
# for media sharing
Requires: rygel
# for desktop sharing
Requires: gnome-remote-desktop

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-systemd
BuildRequires: meson desktop-file-utils gtk-doc xsltproc libappstream-glib-devel
BuildRequires: fontconfig-devel >= %fontconfig_ver
BuildRequires: libgtk4-devel >= %gtk4_ver
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: pkgconfig(gnome-desktop-4) pkgconfig(gnome-bg-4) pkgconfig(gnome-rr-4)
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: gnome-settings-daemon-devel >= %sett_daemon_ver
BuildRequires: libcolord-devel >= %colord_ver pkgconfig(colord-gtk4)
BuildRequires: libibus-devel >= %ibus_ver libxkbfile-devel setxkbmap
BuildRequires: libupower-devel >= %upower_ver libpolkit1-devel >= %polkit_ver
BuildRequires: libgio-devel librsvg-devel libxml2-devel
BuildRequires: libX11-devel libXi-devel
BuildRequires: libgtop-devel libcups-devel >= %cups_ver
BuildRequires: libpulseaudio-devel >= %pulse_ver iso-codes-devel
BuildRequires: libpwquality-devel >= %pwq_ver libkrb5-devel libsmbclient-devel
BuildRequires: gobject-introspection-devel libgtk4-gir-devel
# for test-endianess
BuildRequires: glibc-i18ndata
BuildRequires: libnm-devel >= %nm_ver libmm-glib-devel pkgconfig(libnma-gtk4) pkgconfig(gcr-4)
BuildRequires: libgnome-online-accounts-devel >= %goa_ver
BuildRequires: libaccountsservice-devel >= %acc_ver
BuildRequires: libwacom-devel >= %wacom_ver
BuildRequires: pkgconfig(systemd) >= %systemd_ver
BuildRequires: libgrilo-devel >= %grilo_ver
BuildRequires: libsecret-devel libgnutls-devel
BuildRequires: libudisks2-devel
BuildRequires: tecla-devel
%{?_enable_bluetooth:BuildRequires: pkgconfig(gnome-bluetooth-ui-%bt_api_ver) >= %bt_ver}
%{?_enable_snap:BuildRequires: pkgconfig(snapd-glib-2) >= %snapd_ver}
%{?_enable_malcontent:BuildRequires: pkgconfig(malcontent-0) >= %malcontent_ver}
BuildRequires: libgudev-devel >= %gudev_ver libgsound-devel
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: libepoxy-devel
%{?_enable_check:BuildRequires: python3(dbusmock)}

%description
GNOME (the GNU Network Object Model Environment) is an attractive and
easy-to-use GUI desktop environment. The control-center package
provides the GNOME Control Center utilities that allow you to setup
and configure your system's GNOME environment (things like the desktop
background and theme, the screensaver, the window manager, system
sounds, and mouse behavior).

If you install GNOME, you need to install control-center.

%package data
Summary: Arch independent files for GNOME Control Center
Group: Networking/Instant messaging
BuildArch: noarch

%description data
This package provides noarch data needed for GNOME Control Center to work.

%package devel
Summary: GNOME Control Center development files
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: %name = %EVR

%description devel
If you're interested in developing panels for the GNOME control center,
you'll want to install this package.

%name-devel helps you create the panels for the control center.

%prep
%setup -n %name-%version%beta
# define TZ_DATA_FILE "/usr/share/zoneinfo/zone.tab"
#sed -i 's|zone\.tab|zone1970.tab|' panels/system/datetime/tz.h
sed -i 's|\(\/usr\/share\/\)zoneinfo\/\(zone.tab\)|\1%name/\2|' panels/system/datetime/tz.h

%build
%meson \
    %{subst_enable_meson_bool snap snap} \
    %{subst_enable_meson_bool malcontent malcontent} \
    %{subst_enable_meson_bool doc documentation}
%nil
%meson_build

%install
%meson_install
sed -e '/Simferopol/d' %SOURCE1 > %buildroot%_datadir/%name/zone.tab
%find_lang --with-gnome --output=%name.lang %name-%api_ver %name-%api_ver-timezones %_name

%check
%__meson_test

%files
%_bindir/%name
%_libexecdir/%name-search-provider
%_libexecdir/%name-print-renderer

%files data -f %name.lang
%dir %_datadir/%name
%_datadir/%name/keybindings
%_datadir/%name/pixmaps
%_datadir/%name/zone.tab
%_desktopdir/*.desktop
%_datadir/pixmaps/faces/
%_iconsdir/hicolor/*/*/*
%_iconsdir/gnome-logo-text*.svg
%_datadir/sounds/gnome/default/alerts/*.ogg
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/polkit-1/actions/org.gnome.controlcenter.system.policy
%_datadir/polkit-1/actions/org.gnome.controlcenter.user-accounts.policy
%_datadir/polkit-1/rules.d/gnome-control-center.rules
%_datadir/polkit-1/actions/org.gnome.controlcenter.remote-login-helper.policy
%_datadir/polkit-1/actions/org.gnome.controlcenter.remote-session-helper.policy
%_datadir/dbus-1/services/%xdg_name.SearchProvider.service
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%{?_enable_doc:%_man1dir/%name.1.*}
%_datadir/bash-completion/completions/gnome-control-center
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS README*

%files devel
%_datadir/pkgconfig/gnome-keybindings.pc
%_datadir/gettext/its/gnome-keybindings.its
%_datadir/gettext/its/gnome-keybindings.loc
%_datadir/gettext/its/sounds.its
%_datadir/gettext/its/sounds.loc


%changelog
* Mon Oct 21 2024 Yuri N. Sedunov <aris@altlinux.org> 47.1-alt1
- 47.1

* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0.1-alt1
- 47.0.1

* Mon Aug 05 2024 Yuri N. Sedunov <aris@altlinux.org> 46.4-alt1
- 46.4

* Fri Jun 28 2024 Yuri N. Sedunov <aris@altlinux.org> 46.3-alt1
- 46.3

* Mon May 27 2024 Yuri N. Sedunov <aris@altlinux.org> 46.2-alt1
- 46.2

* Mon Apr 22 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt1
- 46.1

* Wed Mar 27 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0.1-alt1
- 46.0.1

* Mon Mar 18 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Tue Feb 27 2024 Yuri N. Sedunov <aris@altlinux.org> 45.3-alt1.1
- used local copy of zone.tab for datetime panel

* Mon Feb 12 2024 Yuri N. Sedunov <aris@altlinux.org> 45.3-alt1
- 45.3

* Thu Dec 07 2023 Yuri N. Sedunov <aris@altlinux.org> 45.2-alt1
- 45.2

* Mon Oct 23 2023 Yuri N. Sedunov <aris@altlinux.org> 45.1-alt1
- 45.1
- updated runtime dependencies

* Fri Sep 15 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Fri Sep 15 2023 Yuri N. Sedunov <aris@altlinux.org> 44.4-alt1
- 44.4

* Fri Jun 30 2023 Yuri N. Sedunov <aris@altlinux.org> 44.3-alt1
- 44.3

* Tue Jun 27 2023 Yuri N. Sedunov <aris@altlinux.org> 44.2-alt2
- 44.2-13-g8e7079697 (updated translations)
- panels/datetime/tz.h: switched TZ_DATA_FILE to zone1970.tab
- enabled %%check

* Fri May 26 2023 Yuri N. Sedunov <aris@altlinux.org> 44.2-alt1
- 44.2

* Fri Apr 21 2023 Yuri N. Sedunov <aris@altlinux.org> 44.1-alt1
- 44.1

* Sun Mar 19 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Mon Feb 13 2023 Yuri N. Sedunov <aris@altlinux.org> 43.4.1-alt1
- 43.4.1

* Fri Dec 23 2022 Yuri N. Sedunov <aris@altlinux.org> 43.2-alt1
- 43.2

* Tue Oct 18 2022 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 43-alt0.9.rc
- 43.rc

* Fri Jul 01 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Fri May 27 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Tue Apr 26 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sun Mar 06 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc (ported to GTK4)

* Mon Feb 28 2022 Yuri N. Sedunov <aris@altlinux.org> 41.4-alt1
- 41.4

* Fri Dec 03 2021 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Fri Oct 29 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Fri Oct 29 2021 Yuri N. Sedunov <aris@altlinux.org> 40.6-alt1
- 40.6

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.8.rc
- 40.rc

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.5-alt1
- 3.38.5

* Mon Feb 15 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.4-alt1
- 3.38.4

* Fri Jan 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sun Oct 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Jul 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Wed Jun 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Fri May 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Fri Mar 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Fri Feb 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Sat Oct 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0.1-alt1
- 3.34.0.1

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Fri Mar 29 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0.1-alt1
- 3.32.0.1

* Fri Feb 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Thu Nov 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Wed Sep 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Jun 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt2
- fixed buildreqs

* Tue May 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Nov 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Tue Oct 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Wed Apr 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Mar 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Nov 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt2
- rebuilt against libgrilo-0.2.so.10

* Wed Jul 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Thu Mar 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt2
- rebuilt against libupower-glib.so.3

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Jun 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt3
- rebuilt against libgtop-2.0.so.10

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt2
- rebuilt against libcolord.so.2

* Wed Apr 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Mar 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Sep 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.5-alt1
- 3.8.5

* Wed Jul 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Mon Jul 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt2
- updated to 2a9463c (fixed BGO ##701514, 703607, 703946, 703359, 703189,
  702093, 702344...)

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue May 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1.5-alt1
- 3.8.1.5

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sat Feb 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt3
- rebuilt against libcolord.so.2

* Mon Dec 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt2
- updated to 44a5f16d9

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Mon Oct 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt2
- updated to c35850649
- built with ibus

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt2
- updated from upstream git (89498b5)

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Sat Dec 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt2
- updated from upstream git (fixed some GNOME and RH bugs)
- added gnome-online-accounts to reqs
- enabled cheese webcam support
- split up noarch data in separate -data subpackage

* Wed Nov 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Sep 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90
- no more -devel-doc subpackage

* Wed Aug 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- updated from upstream git

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sat Apr 30 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1.1-alt1
- 3.0.1.1

* Sat Apr 30 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- using URL handlers for browsers and mailers to be compatible with
  glib-2.28
- updated russian translation from git

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt2
- fixed translation error (patch0)

* Tue Apr 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt2
- new desktop-effects-integration.patch (tnx to Valery V. Inozemtsev)

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Sat Feb 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt3
- fixed find_lang usage

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Thu Dec 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4
- temporarily disabled compiz configuration dialog patch
- updated buildreqs

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt2
- readded compiz configuration dialog

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Mon Aug 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Wed Jun 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt3
- added russian translation for compiz configuration dialog (shrek@)

* Fri May 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- removed dependence on xscreensaver
- implemented compiz configuration dialog based on ubuntu
  95_desktop-effects-integration.patch (tnks to Valery V. Inozemtsev)
- applied ubuntu patches add touchpad configuration
- updated buildreqs

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Mar 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Tue Jan 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.3-alt1
- 2.25.3
- removed obsolete %%post{,un} scripts
- updated buildreqs

* Sun Oct 26 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0.1-alt3
- rebuild

* Tue Sep 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0.1-alt2
- fix schemas list

* Sun Sep 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0.1-alt1
- 2.24.0.1

* Sun Sep 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.2.1-alt2
- fix gnome bug #529773 (requires patched libxklavier-3.7)
- small fix in russian translation.

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2.1-alt1
- 2.22.2.1
- make about me capplet use userpasswd for passwords (patch7)(#15742)
- fix problems with the home address not being saved,
  and addresses being swapped or the like (patch8) (GNOME #317835,#15742)

* Mon Apr 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1
- changed path background(updated patch5)
- updated randr patch

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.0-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gnome-control-center

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Mon Mar 10 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- new version (2.21.92)
- remove package gnome-setting-daemon
- update section %%files

* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.3-alt1
- new version (2.20.3)
- removed patches:
  + for RH bug #330501 (more key defaults) (fixed upstream)
  + for GNOME bug #489973 (orca command) (fixed upstream)

* Tue Dec 11 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add Packager
- add patches from fedora8
- disabled patch1 (control-center-2.18-custom-keybinding.diff)
- add a "valid" OnlyShowIn entry, otherwise desktop-file-install complains 
- fix section files
- update buildreq

* Sun Jul 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.1-alt1
- new version (2.18.1)
- updated dependencies
- applied a patch from OpenSolaris that enables editing custom keybindings.
- invoke gnome-doc-prepare and autoreconf to get around GNOME Bug 427939
- use new macros from rpm-build-gnome
- gnome-settings-daemon now resides in its own subpackage; maintainers of GNOME
  programs that interact with it are encouraged to add a corresponding Requires
- updated the files list and the schemas list; schemas list is split into two,
  one for g-s-d, the other one installed with control-center.

* Wed Apr 25 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt4
- fixed bug #11610

* Tue Apr 10 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt3
- switched debug off by default

* Wed Apr 04 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt2
- introduced 'debug' switch.

* Thu Feb 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version 2.16.3 (with rpmrb script)

* Wed Dec 27 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt2
- rebuild with new dbus

* Thu Dec 21 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt1
- new version 2.16.2 (with rpmrb script)

* Tue Oct 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version 2.16.1 (with rpmrb script)

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt3
- enabled aboutme capplet
- let pkgconfig handle dependencies of the -devel subpackage.
- added gnome-filesystem as a container of /usr/share/gnome path.
- added /usr/share/gnome/help/control-center to the files list.
- gnome-settings-daemon now lives in plain %%_libexecdir

* Wed Sep 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt2
- removed spurious dependency on gnome-session.

* Tue Sep 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version 2.16.0.
- removed unneeeded dependency on kernel-headers.

* Fri Sep 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt3
- added dependency on gnome-session >= 2.15.92 due to transition from Bonobo to DBus.

* Wed Aug 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt2
- rebuilt with new gstreamer.

* Sun Aug 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt1
- new version 2.15.92 (with rpmrb script)

* Sat Aug 19 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)
- updated dependencies
- added 'aboutme' switch
- disabled about-me capplet, waiting for evolution-data-server >= 1.7.90
- replaced Bonobo with DBus for gnome-settings-daemon

* Sun Jul 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt2
- Bumped up the release to bump up the robot to build g-c-c with
  gstreamer-0.10.

* Wed May 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version (2.14.1)
- removed Debian menu support.

* Wed Feb 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.92-alt1
- new version
- buildreqs revised

* Thu Feb 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version

* Wed Feb 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5.1-alt2
- added switches for alsa and gstreamer.
- enabled aboutme capplet, themes:/// and fonts:/// uri schemes.

* Sun Jan 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5.1-alt1
- new version
- updated dependencies
- cleaned up the files list

* Mon Jan 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5-alt1
- new version

* Tue Jan 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.4-alt1
- new version

* Sat Nov 19 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version
- %%exclude .la files instead of removing them before packaging.
- rewritten schemas installing, now changes of the schemas list won't go unnoticed by a maintainer.

* Mon Oct 24 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Sun Sep 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92

* Wed Jul 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Tue Apr 05 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Thu Feb 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91

* Mon Feb 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.4-alt1
- 2.9.4

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Wed Sep 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Fri Apr 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Thu Apr 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.3-alt1
- 2.6.0.3

* Sat Mar 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Feb 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Thu Feb 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt3
- fix GNOME_SettingsDaemon.server

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt2
- rebuild with libxklavier-0.97

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Sat Jan 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- do not package .la files.
- do not build %%name-devel-static subpackage by default.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Tue Jul 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt2
- remove %%preun with %%gconf2_uninstall.

* Mon Jul 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Wed Jun 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Thu May 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Fri Mar 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Feb 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Thu Jan 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Fri Jan 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Thu Dec 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Sun Dec 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt2
- ugly theme_switcher updated from cvs.

* Sun Nov 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Fri Oct 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1.1-alt2
- Renamed to gnome-control-center.

* Sat Oct 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1.1-alt1.2
- Rebuild with new pango, gtk, gnome-desktop (soname changed).

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.1.1-alt1.1
- fixed %post script (Yuri don't use comma in %gconf2_install macros)

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1.1-alt1
- 2.0.1.1

* Fri Jul 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt1
- First build control-center for GNOME2.
