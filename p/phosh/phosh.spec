%def_disable snapshot
%define _libexecdir %prefix/libexec
%define ver_major 0.56
%define beta %nil
%define libver 0.45
%define gi_api_ver 0
%define namespace Phosh
%define api_ver %ver_major
%define doc_api_ver 0
%define rdn_name mobi.phosh.Shell
%define dev_uid 1000

# since 0.41 gvc & libcallui subprojects use wrap-files
%define gvc_ver d2442f45
%define callui_ver 0.1.5

# shared libs disabled by default
%def_enable shared_libs
# introspection is disabled by default
%def_enable introspection
%def_enable gtk_doc
%def_enable vala
%def_enable man
# since 0.49, disabled by default
%def_disable searchd
# not installed
%def_disable tools
%def_disable check

Name: phosh
Version: %ver_major.0
Release: alt1%beta

Summary: A pure Wayland shell for mobile devices
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/Phosh/phosh

Vcs: https://gitlab.gnome.org/World/Phosh/phosh.git

%if_disabled snapshot
#Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
Source: https://gitlab.gnome.org/World/Phosh/phosh/-/archive/v%version/%name-v%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-0.48.pam
Source2: sm.puri.OSK0.desktop
# https://gitlab.gnome.org/GNOME/libgnome-volume-control.git
Source10: gvc-%gvc_ver.tar
# https://gitlab.gnome.org/World/Phosh/libcall-ui/
Source11: libcall-ui-%callui_ver.tar

Patch1: %name-0.48.0-alt-tcb-check.patch
# https://bugzilla.altlinux.org/46930
Patch2: %name-0.43.0-alt-service.patch
# https://bugzilla.altlinux.org/46978
Patch3: %name-0.29.0-alt-service-dm.patch
# https://bugzilla.altlinux.org/54947
Patch4: %name-0.48-alt-tcb_egid_fix.patch
# https://bugzilla.altlinux.org/55117
# faled with 0.52.0
Patch5: %name-0.48.0-alt-app-grig-keyboard-fix.patch

%define gmobile_ver 0.1.0
%define feedback_ver 0.7.0
%define appstream_ver 1.0.0

Requires: %name-data = %EVR
# to avoid circular dependency
%filter_from_requires /\/usr\/bin\/%name-session/d
%filter_from_requires /\/usr\/libexec\/%name/d
Requires: phoc >= %ver_major
Requires: feedbackd >= %feedback_ver
Requires: gnome-shell-data
Requires: mutter-gnome
# see phosh.session
Requires: gnome-settings-daemon
Requires: gnome-session
Requires: iio-sensor-proxy
Requires: fonts-ttf-google-lato
# since 0.36
Requires: /sbin/capsh
# since 0.39, specific X-GNOME directories
#Requires: gnome-menus-x-gnome
# since 0.40.0
Requires: sound-theme-phosh
# since 0.45 to uninstall apps from app-grid
Requires: gnome-software
# since 0.46 (ALT #53890)
Requires: xdg-desktop-portal-phosh >= 0.53
# syncthing quick setting in 0.55.0
Requires: syncbus

# squeekboard provides osk-wayland
#Requires: /usr/bin/osk-wayland
# since 0.50.1 (ALT #56838)
# stevia provides mobi.phosh.OSK.service
Requires: %_userunitdir/mobi.phosh.OSK.service

BuildRequires(pre): rpm-macros-meson rpm-build-systemd %{?_enable_introspection:rpm-build-gir}
BuildRequires: meson
BuildRequires: desktop-file-utils
BuildRequires: pam-devel
BuildRequires: libcallaudio-devel
BuildRequires: libfeedback-devel >= %feedback_ver
BuildRequires: pkgconfig(gmobile) >= %gmobile_ver
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gcr-3) >= 3.7.5
BuildRequires: pkgconfig(gio-2.0) >= 2.80.0
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.58
BuildRequires: pkgconfig(gnome-desktop-3.0) >= 43
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= 47
BuildRequires: pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.24
BuildRequires: pkgconfig(gtk+-wayland-3.0) >= 3.24
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libfeedback-0.0)
BuildRequires: pkgconfig(libhandy-1) >= 1.1.90
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libnm) >= 1.14
BuildRequires: pkgconfig(mm-glib) >= 1.24
BuildRequires: pkgconfig(libpulse) >= 2.0
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(polkit-agent-1) >= 0.105
BuildRequires: pkgconfig(upower-glib) >= 1.90
BuildRequires: pkgconfig(wayland-client) >= 1.14
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libecal-2.0)
BuildRequires: pkgconfig(evince-document-3.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(gnome-bluetooth-3.0)
BuildRequires: pkgconfig(appstream) >= %appstream_ver
# since 0.52
BuildRequires: pkgconfig(qrcodegen)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel
BuildRequires: gir(Gcr) = 3 gir(Handy) = 1 gir(NM) = 1.0
BuildRequires: gir(GnomeDesktop) = 3.0} gir(GnomeBluetooth) = 3.0
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_man:BuildRequires: /usr/bin/rst2man}
%{?_enable_check:BuildRequires: xvfb-run dbus at-spi2-core
BuildRequires: python3(black) python3(ruff) python3(flake8) python3(dbusmock)}

%description
Phosh is a simple shell for Wayland compositors speaking the layer-surface
protocol. It currently supports

* a lockscreen
* brightness control and nighlight
* the gcr system-prompter interface
* acting as a polkit auth agent
* enough of org.gnome.Mutter.DisplayConfig to make gnome-settings-daemon happy
* a homebutton that toggles a simple favorites menu
* status icons for battery, wwan and wifi

%package data
Summary: Arch independent files for Phosh
Group: Graphical desktop/GNOME
BuildArch: noarch

%description data
This package provides noarch data needed for Phosh to work.

%package devel
Summary: Development files for Phosh
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides files needed to develop Phosh plugins.

%package -n lib%name
Summary: Phosh shared library
Group: System/Libraries

%description -n lib%name
This package contains shared Phosh library to generate bindings.

%package -n lib%name-devel
Summary: Development files for Phosh shared library
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains development files for Phosh shared library.

%prep
%setup -n %name-%{?_disable_snapshot:v}%version%beta -a10 -a11
mv gvc-%gvc_ver subprojects/gvc
mv libcall-ui-%callui_ver subprojects/libcall-ui

%patch1 -p1 -b .tcb
%patch2 -p1 -b .alt
%patch3 -p1 -b .alt-dm
%patch4 -p1 -b .tcb_egid_fix
#%%patch5 -p1 -b .osk
sed -i 's|\(User=\)1000|\1%dev_uid|' data/%name.service
# full path to capsh
sed -i 's|\(capsh\)|/sbin/\1|' data/%name.service

%build
# src/media-player.c:203:14
%ifarch %ix86 armh
%add_optflags -Wno-error=format
%endif
%meson \
    %{subst_enable_meson_bool shared_libs bindings-lib} \
    %{subst_enable_meson_bool introspection introspection} \
    %{subst_enable_meson_bool vala vapi} \
    %{subst_enable_meson_bool gtk_doc gtk_doc} \
    %{subst_enable_meson_bool man man} \
    %{subst_enable_meson_bool searchd searchd} \
    %{subst_enable_meson_bool tools tools} \
    -Dphoc_tests=disabled
%nil
%meson_build

%install
%meson_install
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -Dpm 0644 data/phosh.service %buildroot%_unitdir/phosh.service
mkdir -p %buildroot%_sysconfdir/systemd/system/%name.service.d

install -d %buildroot%_datadir/applications
desktop-file-install --dir %buildroot%_datadir/applications %SOURCE2

%{?_enable_shared_libs:rm -f %buildroot%_libdir/lib%name-%libver.a}

%find_lang %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%dir %_sysconfdir/systemd/system/%name.service.d
%config(noreplace) %_sysconfdir/pam.d/%name
%_bindir/%name-session
%attr(2711, root, chkpwd) %_libexecdir/%name
%_libexecdir/%name-calendar-server
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%dir %_libdir/%name/plugins/prefs
%_libdir/%name/plugins/lib%name-plugin-calendar.so
%_libdir/%name/plugins/calendar.plugin
%_libdir/%name/plugins/lib%name-plugin-ticket-box.so
%_libdir/%name/plugins/ticket-box.plugin
%_libdir/%name/plugins/launcher-box.plugin
%_libdir/%name/plugins/libphosh-plugin-launcher-box.so
%_libdir/%name/plugins/lib%name-plugin-upcoming-events.so
%_libdir/%name/plugins/upcoming-events.plugin
%_libdir/%name/plugins/emergency-info.plugin
%_libdir/%name/plugins/lib%name-plugin-emergency-info.so
%_libdir/%name/plugins/prefs/lib%name-plugin-prefs-ticket-box.so
%_libdir/%name/plugins/prefs/lib%name-plugin-prefs-emergency-info.so
%_libdir/%name/plugins/prefs/lib%name-plugin-prefs-upcoming-events.so
%_libdir/%name/plugins/prefs/lib%name-plugin-prefs-pomodoro-quick-setting.so
%_libdir/%name/plugins/prefs/lib%name-plugin-prefs-caffeine-quick-setting.so
%_libdir/%name/plugins/caffeine-quick-setting.plugin
%_libdir/%name/plugins/lib%name-plugin-caffeine-quick-setting.so
%_libdir/%name/plugins/lib%name-plugin-location-quick-setting.so
%_libdir/%name/plugins/location-quick-setting.plugin
%_libdir/%name/plugins/lib%name-plugin-simple-custom-quick-setting.so
%_libdir/%name/plugins/simple-custom-quick-setting.plugin
%_libdir/%name/plugins/lib%name-plugin-night-light-quick-setting.so
%_libdir/%name/plugins/night-light-quick-setting.plugin
%_libdir/%name/plugins/dark-mode-quick-setting.plugin
%_libdir/%name/plugins/lib%name-plugin-dark-mode-quick-setting.so
%_libdir/%name/plugins/lib%name-plugin-mobile-data-quick-setting.so
%_libdir/%name/plugins/mobile-data-quick-setting.plugin
%_libdir/%name/plugins/lib%name-plugin-pomodoro-quick-setting.so
%_libdir/%name/plugins/pomodoro-quick-setting.plugin
%_libdir/%name/plugins/lib%name-plugin-wifi-hotspot-quick-setting.so
%_libdir/%name/plugins/wifi-hotspot-quick-setting.plugin
%_libdir/%name/plugins/lib%name-plugin-scaling-quick-setting.so
%_libdir/%name/plugins/lib%name-plugin-syncthing-quick-setting.so
%_libdir/%name/plugins/syncthing-quick-setting.plugin
%_libdir/%name/plugins/scaling-quick-setting.plugin
%_libdir/%name/plugins/lib%name-plugin-media-players.so
%_libdir/%name/plugins/media-players.plugin
%_libdir/%name/plugins/lib%name-plugin-simple-custom-status-icon.so
%_libdir/%name/plugins/simple-custom-status-icon.plugin
%_libdir/%name/plugins/lib%name-plugin-load-meter-status-icon.so
%_libdir/%name/plugins/load-meter-status-icon.plugin

%{?_enable_searchd:
%_libexecdir/%name-searchd
%_datadir/dbus-1/services/%rdn_name.Search.service}

%doc NEWS README.md

%files data
%_desktopdir/%rdn_name.desktop
%_desktopdir/sm.puri.OSK0.desktop
%_datadir/glib-2.0/schemas/mobi.phosh.shell.gschema.xml
%_datadir/glib-2.0/schemas/mobi.phosh.shell.enums.xml
%_datadir/glib-2.0/schemas/mobi.phosh.plugins.caffeine-quick-setting.gschema.xml
%_datadir/glib-2.0/schemas/mobi.phosh.plugins.pomodoro.gschema.xml
%_datadir/glib-2.0/schemas/sm.puri.phosh.plugins.launcher-box.gschema.xml
%_datadir/glib-2.0/schemas/sm.puri.phosh.plugins.ticket-box.gschema.xml
%_datadir/glib-2.0/schemas/sm.puri.phosh.plugins.upcoming-events.gschema.xml
%_datadir/glib-2.0/schemas/00_mobi.Phosh.gschema.override
%_datadir/dbus-1/services/%rdn_name.CalendarServer.service
%_datadir/gnome-session/sessions/%name.session
%_datadir/wayland-sessions/%name.desktop
%_datadir/%name/
%_unitdir/phosh.service
%_userunitdir/mobi.phosh.OSK.target
%_userunitdir/gnome-session@%name.target.d/session.conf
%_userunitdir/%rdn_name.service
%_userunitdir/%rdn_name.target
%_datadir/xdg-desktop-portal/portals/%name-shell.portal
%_datadir/xdg-desktop-portal/%name-portals.conf
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%{?_enable_man:%_man1dir/%name.1*
%_man1dir/%name-session.1*
%_man5dir/%name.gsettings.5*}

%files devel
%_includedir/%name/
%_pkgconfigdir/%name-plugins.pc
%_pkgconfigdir/%name-settings.pc
%{?_enable_gtk_doc:%doc %_datadir/doc/%name-%doc_api_ver}

%{?_enable_shared_libs:
%files -n lib%name
%_libdir/lib%name-%libver.so.*
%{?_enable_introspection:%_typelibdir/%namespace-%gi_api_ver.typelib}

%files -n lib%name-devel
%_includedir/lib%name-%libver
%_libdir/lib%name-%libver.so
%_pkgconfigdir/lib%name-%libver.pc
%{?_enable_introspection:%_girdir/%namespace-%gi_api_ver.gir}
%{?_enable_vala:%_vapidir/lib%name-%libver.*}
}

%changelog
* Sun Jul 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.56.0-alt1
- 0.56.0

* Sun May 17 2026 Yuri N. Sedunov <aris@altlinux.org> 0.55.0-alt1
- 0.55.0

* Sun Apr 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.54.0-alt1
- 0.54.0

* Tue Feb 24 2026 Yuri N. Sedunov <aris@altlinux.org> 0.53.1-alt1
- 0.53.1

* Sun Feb 15 2026 Yuri N. Sedunov <aris@altlinux.org> 0.53.0-alt1
- 0.53.0

* Thu Jan 08 2026 Yuri N. Sedunov <aris@altlinux.org> 0.52.1-alt1
- 0.52.1

* Sun Jan 04 2026 Yuri N. Sedunov <aris@altlinux.org> 0.52.0-alt1
- 0.52.0
- disabled broken alt-app-grig-keyboard-fix.patch

* Sun Nov 16 2025 Yuri N. Sedunov <aris@altlinux.org> 0.51.0-alt1
- 0.51.0

* Thu Oct 23 2025 Yuri N. Sedunov <aris@altlinux.org> 0.50.1-alt1
- 0.50.1

* Sun Oct 05 2025 Yuri N. Sedunov <aris@altlinux.org> 0.50.0-alt1
- 0.50.0

* Fri Aug 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.49.0-alt1
- 0.49.0

* Fri Jul 11 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48.0-alt1.1
- applied experimental patch proposed in (ALT #55117)

* Mon Jun 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48.0-alt1
- 0.48.0

* Fri Jun 27 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48-alt0.91.rc1
- phosh.pam: added 'account required pam_permit.so',
  uncommented pam_gnome_keyring (ALT #54954)

* Mon Jun 23 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48-alt0.9.rc1
- 0.48_rc1
- updated alt-tcb-check.patch (ALT #46389)
- added alt-tcb_egid_fix.patch (ALT #54947)

* Sun May 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.47.0-alt1
- 0.47.0

* Fri Apr 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt1.1
- added x-d-p-phosh to runtime dependencies (ALT #53890)

* Mon Mar 31 2025 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt1
- 0.46.0

* Sat Feb 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.45.0-alt1
- updated to v0.45.0-2-g8fc14f4c

* Sat Jan 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.44.1-alt1
- 0.44.1

* Mon Dec 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.44.0-alt1
- 0.44.0

* Fri Dec 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.43.1-alt1
- 0.43.1

* Mon Nov 18 2024 Yuri N. Sedunov <aris@altlinux.org> 0.43.0-alt1.1
- updated service.patch after 0.43.0 change

* Fri Nov 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.43.0-alt1
- 0.43.0

* Mon Sep 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt1
- 0.42.0

* Fri Sep 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.1-alt1
- 0.41.1

* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt1
- 0.41.0

* Thu Aug 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt0.9.rc1
- v0.41.0_rc1-4-g8aa9c66c

* Sun Jun 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0

* Wed Jun 26 2024 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt0.9.rc1
- 0.40.0.rc1

* Wed May 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.39.0-alt1
- 0.39.0

* Sun Apr 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0

* Mon Apr 01 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.1-alt1
- 0.37.1

* Wed Mar 20 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1.2
- data/phosh-session.in: dropped @session_manager@ option
  incompatible with gnome-session-46 (ALT #49750)

* Sat Mar 09 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1.1
- rebuilt against libecal-2.0.so.3

* Fri Mar 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1
- 0.37.0

* Sat Feb 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.36.0-alt1
- 0.36.0

* Sun Jan 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.35.0-alt1
- 0.35.0

* Wed Dec 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.34.1-alt1
- 0.34.1

* Wed Dec 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt1
- 0.34.0

* Fri Nov 03 2023 Yuri N. Sedunov <aris@altlinux.org> 0.33.0-alt1
- 0.33.0

* Thu Oct 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Mon Sep 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.31.1-alt1
- 0.31.1

* Thu Aug 17 2023 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1.1
- phosh.pam: commented-out pam_gnome_keyring

* Thu Aug 03 2023 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1
- 0.30.0
- required /usr/bin/osk-wayland

* Tue Jul 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1.3
- split noarch data to separate subpackage
- data/phosh.service: added "Alias=display-manager.service" to prevent
  starting prefdm (ALT #46978)

* Fri Jul 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1.2
- data/phosh.service: removed "Environment=LANG=C.UTF-8",
  switched TTYPath/UtmpIdentifier from tty7 to tty1 (ALT#46930)

* Thu Jul 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1.1
- required gnome-shell-data & mutter-gnome (ALT#46896)

* Thu Jul 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1
- 0.29.0

* Mon Jun 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1.1
- cas@: fixed lock screen authentication (ALT #46389)

* Thu Jun 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 0.28.0

* Tue May 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.27.0-alt1
- 0.27.0
- restored default UID from 500 to 1000
- enabled gtk-doc and man builds

* Mon Apr 03 2023 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Sun Mar 12 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.2-alt1
- 0.25.2

* Thu Mar 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.1-alt1
- 0.25.1

* Wed Mar 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.0-alt1
- 0.25.0

* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Wed Dec 28 2022 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1
- 0.23.0
- new -devel subpackage

* Wed Dec 7 2022 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- v0.22.0-13-g3c3ce51a

* Thu Sep 29 2022 Yuri N. Sedunov <aris@altlinux.org> 0.21.1-alt1
- 0.21.1

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Sat Jul 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt0.5.beta3
- first build for Sisyphus

