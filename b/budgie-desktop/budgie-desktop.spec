%global glib2_version 2.64
%global gnome_desktop_version 42.8
%global gnome_settings_daemon_version 42.2
%global gsettings_desktop_schemas_version 42.0
%global gtk3_version 3.24
%global polkit_version 0.105
%global vala_version 0.52.5

Name: budgie-desktop
Version: 10.10.2
Release: alt1

Summary: A feature-rich, modern desktop designed to keep out the way of the user

License: GPLv2 and LGPLv2
Group: Graphical desktop/Other
Url: https://github.com/BuddiesOfBudgie/budgie-desktop

ExcludeArch: %ix86

# Source0-url: %url/releases/download/v%version/%name-v%version.tar.xz
Source0: %name-%version.tar

# vapi for libxfce4windowing (needed until libxfce4windowing uses meson build)
Patch1: add-libxfce4windowing-vapi.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: pkgconfig(accountsservice) >= 0.6.55
BuildRequires: pkgconfig(alsa) >= 1.2.6
BuildRequires: pkgconfig(gee-0.8) >= 0.20.0
BuildRequires: pkgconfig(gnome-desktop-3.0) >= %gnome_desktop_version
BuildRequires: pkgconfig(gnome-settings-daemon) >= %gnome_settings_daemon_version
BuildRequires: pkgconfig(gstreamer-1.0) >= 1.20.0
BuildRequires: pkgconfig(ibus-1.0) >= 1.5.10
BuildRequires: pkgconfig(libcanberra) >= 0.30
BuildRequires: libcanberra-vala
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(libnotify) >= 0.7
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: libpeas2-gir-devel
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libwnck-3.0) >= 3.36.0
BuildRequires: pkgconfig(libxfce4windowing-0)
BuildRequires: libxfce4windowing-gir-devel
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: pkgconfig(polkit-agent-1) >= %polkit_version
BuildRequires: pkgconfig(upower-glib) >= 0.99.13
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(vapigen) >= %vala_version
BuildRequires: budgie-desktop-view
BuildRequires: budgie-screensaver
BuildRequires: desktop-file-utils
#BuildRequires: git
#BuildRequires: gnupg2
BuildRequires: gsettings-desktop-schemas >= %gsettings_desktop_schemas_version
BuildRequires: gtk-doc >= 1.33.0
BuildRequires: intltool
BuildRequires: meson
BuildRequires: rpm-build-cmake
BuildRequires: sassc
BuildRequires: zenity >= 3.91.0
BuildRequires: grim
BuildRequires: slurp
BuildRequires: wlopm
BuildRequires: swayidle
BuildRequires: swaybg
BuildRequires: swaylock
BuildRequires: gammastep
BuildRequires: /usr/bin/eglinfo
BuildRequires: gir(Gtk) = 3.0

Requires: budgie-control-center
Requires: budgie-desktop-view
Requires: budgie-screensaver
Requires: budgie-session
Requires: budgie-desktop-services
Requires: gnome-settings-daemon
Requires: gsettings-desktop-schemas
Requires: PAM(pam_gnome_keyring.so)
Requires: hicolor-icon-theme
Requires: %_bindir/nm-applet
Requires: labwc
Requires: materia-gtk-theme
Requires: papirus-icon-theme
Requires: switcheroo-control
Requires: zenity
#Suggests:       slick-greeter

%description
A feature-rich, modern desktop designed to keep out the way of the user.

%package devel
Group: Development/C
Summary: Development package for budgie-desktop
Requires: %name = %EVR
Requires: vapi-common

%description devel
Header files, libraries, and other files for developing Budgie Desktop.

%package docs
Summary: Documentation for budgie-desktop
Group: Documentation
# due ExcludeArch: %ix86
#BuildArch: noarch
Requires: gtk-doc
Requires: %name = %EVR

%description docs
Documentation for budgie-desktop

%prep
%setup
%patch1 -p1
# Fix missing wnck dependency for appsys vapi consumers
sed -i '/link_with: libappsys,/a \    dependencies: [dep_wnck],' src/appsys/meson.build

%build
subst 's|@libexecdirroot@/xdg-desktop-portal|/usr/libexec/xdg-desktop-portal|' src/session/budgie-desktop.in
%meson -Dwith-hibernate=false
%meson_build

%install
%meson_install
%find_lang %name
rm -rf %buildroot%_datadir/locale/be_Latn
rm -rf %buildroot%_datadir/locale/es_419
rm -rf %buildroot%_datadir/locale/sr@Cyrl

%check
desktop-file-validate %buildroot%_desktopdir/*.desktop

%files -f %name.lang
%doc README.md
%doc LICENSE
%dir %_datadir/backgrounds/budgie
%dir %_datadir/budgie
%dir %_libdir/%name/
%dir %_libdir/%name/plugins/
%dir %_libdir/%name/plugins/*
%_bindir/budgie-*
%_bindir/org.buddiesofbudgie.*
%_bindir/startbudgielabwc
%_desktopdir/org.buddiesofbudgie*.desktop
%_datadir/backgrounds/budgie/default.jpg
%_datadir/budgie/budgie-version.xml
%_datadir/%name/gammastep.config
%dir %_datadir/%name/labwc/
%_datadir/%name/labwc/menu.xml
%_datadir/%name/labwc/rc.xml
%_datadir/%name/labwc/themerc-*
%_datadir/glib-2.0/schemas/20_buddiesofbudgie.%name.notifications.gschema.override
%_datadir/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override
%_datadir/glib-2.0/schemas/com.solus-project.*.gschema.xml
%_datadir/glib-2.0/schemas/org.buddiesofbudgie.%name.raven.widget.*.gschema.xml
%_datadir/glib-2.0/schemas/org.buddiesofbudgie.%name.screenshot.gschema.xml
%_datadir/glib-2.0/schemas/org.buddiesofbudgie.settings-daemon.*.gschema.xml
# removed in 10.10.0:
#_datadir/polkit-1/actions/org.buddiesofbudgie.settings-daemon.*.policy
%_datadir/gnome-session/sessions/org.buddiesofbudgie.BudgieDesktop.session
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/scalable/status/*.svg
%_iconsdir/hicolor/symbolic/emblems/*.svg
%_datadir/xdg-desktop-portal/budgie-portals.conf
%_datadir/wayland-sessions/%name.desktop
%_libdir/girepository-1.0/Budgie-3.0.typelib
%_libdir/girepository-1.0/BudgieRaven-3.0.typelib
%_libdir/%name/libgvc.so
%_prefix/lib/%name/budgie-screenshot-dialog
%_prefix/lib/%name/labwc_bridge.py
%_libdir/%name/plugins/*/*.plugin
%_libdir/%name/plugins/*/*.so*
%dir %_libdir/%name/raven-plugins/
%dir %_libdir/%name/raven-plugins/*/
%_libdir/%name/raven-plugins/*/*.plugin
%_libdir/%name/raven-plugins/*/*.so*
%_libexecdir/%name/budgie-polkit-dialog
%_libexecdir/%name/budgie-power-dialog
%_libdir/libbudgie-appindexer.so.0*
%_libdir/libbudgie-plugin.so.0*
%_libdir/libbudgie-private.so.0*
%_libdir/libbudgie-raven-plugin.so.0*
%_libdir/libbudgietheme.so.0*
%_libdir/libraven.so.0*
%_libdir/libbudgie-windowing.so.0*
%_man1dir/budgie-*
%_man1dir/org.buddiesofbudgie.BudgieScreenshot.*
%_man1dir/org.buddiesofbudgie.sendto.*
%_man1dir/startbudgielabwc.*
%_sysconfdir/xdg/autostart/*.desktop

%files devel
%dir %_includedir/%name/
%_includedir/%name/*.h
%_datadir/gir-1.0/Budgie-3.0.gir
%_datadir/gir-1.0/BudgieRaven-3.0.gir
%_datadir/vala/vapi/budgie-*.deps
%_datadir/vala/vapi/budgie-*.vapi
%_libdir/libbudgie-appindexer.so
%_libdir/libbudgie-plugin.so
%_libdir/libbudgie-private.so
%_libdir/libbudgie-raven-plugin.so
%_libdir/libbudgietheme.so
%_libdir/libraven.so
%_libdir/libbudgie-windowing.so
%_pkgconfigdir/budgie-3.0.pc
%_pkgconfigdir/budgie-raven-plugin-3.0.pc
%_pkgconfigdir/budgie-theme-1.0.pc
%_pkgconfigdir/budgie-windowing-1.0.pc

%files docs
%_datadir/gtk-doc/html/%name/

%changelog
* Mon Apr 06 2026 Vitaly Lipatov <lav@altlinux.ru> 10.10.2-alt1
- new version 10.10.2
- fix xdg-desktop-portal path

* Mon Feb 02 2026 Vitaly Lipatov <lav@altlinux.ru> 10.10.1-alt1
- new version 10.10.1
- add libxfce4windowing-0.vapi patch (needed until libxfce4windowing uses meson)

* Mon Jan 12 2026 Vitaly Lipatov <lav@altlinux.ru> 10.10.0-alt1
- new version 10.10.0
- add Wayland tools: grim, slurp, wlopm, swayidle, swaybg, swaylock, gammastep
- add runtime deps: budgie-desktop-services, labwc
- bump API versions to 3.0
- add ExcludeArch: ix86

* Thu Dec 18 2025 Vitaly Lipatov <lav@altlinux.ru> 10.9.4-alt1
- new version 10.9.4 (with rpmrb script)

* Sat Mar 08 2025 Vitaly Lipatov <lav@altlinux.ru> 10.9.2-alt1
- initial build for ALT Sisyphus

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Joshua Strobl <joshua@buddiesofbudgie.org> - 10.9.2-4
- Add patch to support latest libxfce4windowing

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 22 2024 Joshua Strobl <joshua@buddiesofbudgie.org> - 10.9.2-2
- Update to final release tarball

* Sat Jun 22 2024 Joshua Strobl <joshua@buddiesofbudgie.org> - 10.9.2-1
- Update to Budgie Desktop 10.9.2

* Sun Mar 24 2024 Joshua Strobl <joshua@buddiesofbudgie.org> - 10.9.1-2
- Backport patches, fix FTBFS on gcc 14, support latest libxfce4windowing git

* Sun Feb 11 2024 Joshua Strobl <me@joshuastrobl.com> - 10.9.1-1
- Update to Budgie Desktop 10.9.1

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 18 2023 Joshua Strobl <me@joshuastrobl.com> - 10.8.2-1
- Updated to 10.8.2

* Sun Oct 01 2023 Joshua Strobl <me@joshuastrobl.com> - 10.8.1-1
- Updated to 10.8.1

* Mon Aug 21 2023 Joshua Strobl <me@joshuastrobl.com> - 10.8-1
- Updated to 10.8

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Joshua Strobl <me@joshuastrobl.com> - 10.7.2-1
- Updated to 10.7.2

* Tue Apr 25 2023 Joshua Strobl <me@joshuastrobl.com> - 10.7.1-4
- Backport relevancy search change that does not trigger Vala generated C to segfault

* Sun Apr 23 2023 Joshua Strobl <me@joshuastrobl.com> - 10.7.1-3
- Backport fixes for mutter and zenity

* Thu Mar 16 2023 Florian Weimer <fweimer@redhat.com> - 10.7.1-2
- Apply upstream patch to fix C99 compatibility issue (#2179136)

* Sun Feb 19 2023 Joshua Strobl <me@joshuastrobl.com> - 10.7.1-1
- Update to Budgie 10.7.1 release

* Thu Feb 16 2023 Joshua Strobl <me@joshuastrobl.com> - 10.7-2
- Add preliminary mutter 12 ABI support patch

* Sun Jan 29 2023 Joshua Strobl <me@joshuastrobl.com> - 10.7-1
- Update to 10.7 release

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 24 2022 Neal Gompa <ngompa@fedoraproject.org> - 10.6.4-2
- Put the gobject-introspection files in the right place

* Tue Aug 30 2022 Joshua Strobl <me@joshuastrobl.com> - 10.6.4-1
- Initial inclusion of Budgie Desktop
