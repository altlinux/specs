# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-gnome/ReadySet to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define app_id org.altlinux.ReadySet
%define _libexecdir %_prefix/libexec
%define libname lib%name
%define girname ReadySet
%define api_version 0
%define major_version 9
%define minor_version 2
%define gis_name gnome-initial-setup

Name: ready-set
Version: %api_version.%major_version.%minor_version
Release: alt1

Summary: Modular (System Installer | Initial Setup Wizard)
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://altlinux.space/alt-gnome/ReadySet
VCS: https://altlinux.space/alt-gnome/ReadySet.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Obsoletes: %name-translation <= 0.3.0-alt1
Provides: %name-translation = %EVR
Obsoletes: %name-common <= 0.7.3-alt1
Provides: %name-common = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rpm-build-vala
BuildRequires: rpm-build-gir
BuildRequires: meson
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: gobject-introspection-devel
BuildRequires: blueprint-compiler
BuildRequires: gir(Adw) = 1
BuildRequires: gir(Gtk) = 4.0
BuildRequires: gir(Peas) = 2
BuildRequires: gir(Gdm) = 1.0
BuildRequires: gir(Serialize) = 7
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gdm)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(libadwaita-1) >= 1.7
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(libserialize-7) >= 7.5
BuildRequires: pkgconfig(passwdqc)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(xkbcommon)

%description
%summary.

%package gdm
Summary: Files needed for work as initial-setup in gdm
Group: Graphical desktop/Other

Requires: %name = %EVR
Requires: gdm
Conflicts: %gis_name

%description gdm
%summary.

%package -n %libname%api_version
Summary: %name library
Group: System/Libraries

%description -n %libname%api_version
%summary.

%package -n %libname-devel
Summary: %name development files
Group: Development/C

Requires: %libname%api_version = %EVR

%description -n %libname-devel
%summary.

%package -n %libname%api_version-gir
Summary: %name GIR introspection files
Group: System/Libraries

Requires: %libname%api_version = %EVR

%description -n %libname%api_version-gir
%summary.

%package -n %libname-gir-devel
Summary: %name GIR introspection development files
Group: Development/GNOME and GTK+

BuildArch: noarch
Requires: %libname%api_version-gir = %EVR

%description -n %libname-gir-devel
%summary.

%package plugin-keyboard
Summary: %name keyboard plugin
Group: Other

Requires: %name = %EVR
Requires: %name-plugin-language = %EVR

%description plugin-keyboard
%summary.

%package plugin-license-agreement
Summary: %name license agreement plugin
Group: Other

Requires: %name = %EVR
Requires: %name-plugin-language = %EVR

%description plugin-license-agreement
%summary.

%package plugin-language
Summary: %name language plugin
Group: Other

Requires: %name = %EVR

%description plugin-language
%summary.

%package plugin-user-common
Summary: %name user plugin common files
Group: Other

Requires: gnome-control-center-data
Requires: accountsservice
Requires: shadow-utils
Requires: %name = %EVR

%description plugin-user-common
%summary.

%package plugin-user-passwdqc
Summary: %name user plugin with passwdqc support
Group: Other

Requires: %name-plugin-user-common = %EVR
Conflicts: %name-plugin-user-pwquality

%description plugin-user-passwdqc
%summary.

%package plugin-user-pwquality
Summary: %name user plugin with pwquality support
Group: Other

Requires: %name-plugin-user-common = %EVR

%description plugin-user-pwquality
%summary.

%package plugin-welcome
Summary: %name welcome plugin
Group: Other

Requires: %name = %EVR

%description plugin-welcome
%summary.

%prep
%setup
%autopatch -p1

%build
%meson -Dpassword_check_backend=both --auto-features=enabled
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%_libexecdir/%name
%_iconsdir/hicolor/*/apps/%{app_id}*
%_datadir/applications/%{app_id}*
%_datadir/polkit-1/rules.d/%app_id.rules
%_userunitdir/gnome-session.target.wants/%name-existing-user.service
%_userunitdir/%name-existing-user.service
%_libexecdir/%app_id
%_sysconfdir/%name
%_datadir/%name
%_sharedstatedir/%name
%_sysconfdir/dbus-1/system.d/%app_id.conf
%_datadir/polkit-1/actions/%app_id.policy
%_datadir/dbus-1/system-services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_unitdir/%name.service
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%_datadir/bash-completion/completions/%name

%files gdm
%_libexecdir/%gis_name
%_desktopdir/%gis_name.desktop
%_datadir/dconf/profile/%gis_name
%_datadir/%gis_name
%_sharedstatedir/%gis_name
%_datadir/gnome-session/sessions/%gis_name.session
%_datadir/gnome-shell/modes/initial-setup.json
%_userunitdir/%gis_name.service
%_userunitdir/gnome-session@%gis_name.target.d
%_sysusersdir/%gis_name.conf
%_tmpfilesdir/%gis_name.conf

%files -n %libname%api_version
%_libdir/%libname-%api_version.so.%api_version
%_libdir/%libname-%api_version.so.%api_version.*

%files -n %libname-devel
%_pkgconfigdir/%libname-%api_version.pc
%_libdir/%libname-%api_version.so
%_includedir/%libname-%api_version.h
%_vapidir/%libname-%api_version.deps
%_vapidir/%libname-%api_version.vapi

%files -n %libname%api_version-gir
%_typelibdir/%girname-%api_version.typelib

%files -n %libname-gir-devel
%_girdir/%girname-%api_version.gir

%files plugin-keyboard
%_datadir/polkit-1/rules.d/%app_id.Plugin.Keyboard.rules
%_libdir/%name/plugins/steps/keyboard.plugin
%_libdir/%name/plugins/steps/libkeyboard.so

%files plugin-language
%_datadir/polkit-1/rules.d/%app_id.Plugin.Language.rules
%_libdir/%name/plugins/steps/language.plugin
%_libdir/%name/plugins/steps/liblanguage.so

%files plugin-license-agreement
%_libdir/%name/plugins/steps/license-agreement.plugin
%_libdir/%name/plugins/steps/liblicense-agreement.so

%files plugin-user-common
%_datadir/polkit-1/rules.d/%app_id.Plugin.User.rules
%_datadir/polkit-1/rules.d/%app_id.Plugin.User.SetRootPassword.rules
%_libexecdir/%name-set-root-password

%files plugin-user-passwdqc
%_libdir/%name/plugins/steps/user-passwdqc.plugin
%_libdir/%name/plugins/steps/libuser-passwdqc.so

%files plugin-user-pwquality
%_libdir/%name/plugins/steps/user-pwquality.plugin
%_libdir/%name/plugins/steps/libuser-pwquality.so

%files plugin-welcome
%_libdir/%name/plugins/steps/welcome.plugin
%_libdir/%name/plugins/steps/libwelcome.so

%changelog
* Thu Jun 25 2026 Vladimir Romanov <rirusha@altlinux.org> 0.9.2-alt1
- Fixed dialog assertions.
- Fixed context vars applying from options/config.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.9.2

* Wed Jun 24 2026 Vladimir Romanov <rirusha@altlinux.org> 0.9.1-alt1
- Fixed pages recreation.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.9.1

* Mon Jun 22 2026 Vladimir Romanov <rirusha@altlinux.org> 0.9.0-alt1
- New version: 0.9.0.
- Added support for pageless plugins.
- Added bash completion for the CLI.
- Reworked keyboard page completely with stevia layouts support.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.9.0

* Sun Jun 14 2026 Vladimir Romanov <rirusha@altlinux.org> 0.8.0-alt1
- New version: 0.8.0.
- Added ability to create pages directly by the installer (`InstallerAddin`).
- `OBJECT` context vars now have string interpretation.
- Added ability to disable `existing-user` mode with gsettings.
- Fixed a few bugs.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.8.0

* Tue Jun 09 2026 Vladimir Romanov <rirusha@altlinux.org> 0.7.6-alt1
- New version: 0.7.6.
- Added comments to vapi file.
- Fixed small bug at username page.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.7.6

* Tue Jun 09 2026 Vladimir Romanov <rirusha@altlinux.org> 0.7.4-alt1
- New version: 0.7.4.
- Removed short options from CLI interface.
- Fixed infinity loop on window reloading.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.7.4

* Mon Jun 01 2026 Vladimir Romanov <rirusha@altlinux.org> 0.7.3-alt1
- New version: 0.7.3.
- Added existing-user mode to configure an existing user who skipped
  the initial setup or when new setup steps are added by vendor.
- Added copying some files from initial-setup user to created user.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.7.3

* Sat May 30 2026 Vladimir Romanov <rirusha@altlinux.org> 0.7.2-alt1
- New version: 0.7.2.
- Fixed error or strange behavior on enabling pages.
- `welcome` page now hide `language` page.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.7.2

* Sat May 30 2026 Vladimir Romanov <rirusha@altlinux.org> 0.7.1-alt1
- New version: 0.7.1.
- Added `license-agreement` plugin for displaying localized license files.
- Completely redesigned main page (`StepsMainPage`) with adaptive layouts
  (`big`, `small`, `vertical`, `horizontal`) using `Adw.BreakpointBin` and
  `Adw.MultiLayoutView`.
- Replaced `BaseBarePage`/`BasePageDesc` with new `StatusPage`.
- User: Split password setup into separate pages (`PagePassword` and
  `PageRootPassword`), renamed context variables
  (`passwd-conf-path` -> `user-passwd-conf-path`, etc.); removed
  `hide-autologin` option; added avatar support via `user-avatar-file`.
- Keyboard: Added dependency on `language` plugin; improved DnD logic moved
  to `InputRow`; fixed crash when dropping item on itself.
- Language: Reloading made smoother.
- Context: Changed `INT` type to `INT64`; made `mode` internal.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.7.1

* Wed Mar 25 2026 Vladimir Romanov <rirusha@altlinux.org> 0.6.2-alt1
- New version: 0.6.2.
- Hook execution IOError now logged as warning instead of error.
- Increased ReadySet DBus service timeout for long-running hooks.
- Keyboard: Added Drag & Drop for reordering input sources.
- Keyboard: Added layout preview dialog.
- Keyboard: Added option to select layout switch combination.
- Keyboard: Using system `xkb-model` instead of hardcoded `pc105`.
- Increased default window size.
- Moved `gnome-initial-setup` conflict to `gdm` subpackage (repocop needs it).
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.6.2

* Tue Mar 17 2026 Vladimir Romanov <rirusha@altlinux.org> 0.6.1-alt1
- New version: 0.6.1.
- Fixed quitting app before GDM verification.
- Fixed visibility of OSK button at end page.
- Don't allow to show steps via gesture with `simple`.

* Tue Mar 17 2026 Vladimir Romanov <rirusha@altlinux.org> 0.6.0-alt1
- New version: 0.6.0.
- Renamed `intact` mode to `sandbox` (CLI option `--sandbox`).
- Added operation modes: `INITIAL_SETUP`, `INSTALLER`, `TOUR`.
- Added On-Screen Keyboard (sm.puri.OSK0) support via D-Bus.
- Implemented pre/post hooks (user and system).
- Added Weblate integration (translate.alt-gnome.ru).
- Keyboard: Added Latin layout check, default `keyboard-input-sources` logic.
- User: Added `user_with_set_root` option, RU->EN username translation.
- Language: Changed transition animation.
- Interface: Improved tooltips and error messages, updated ru translation.
- Full release note here:
  https://altlinux.space/alt-gnome/ReadySet/releases/tag/v0.6.0

* Wed Mar 11 2026 Vladimir Romanov <rirusha@altlinux.org> 0.5.1-alt3
- Added cumulative patch.

* Fri Mar 06 2026 Vladimir Romanov <rirusha@altlinux.org> 0.5.1-alt2
- Merged couple of keyboard patches from main branch.

* Thu Feb 26 2026 Vladimir Romanov <rirusha@altlinux.org> 0.5.1-alt1
- New version: 0.5.1. (closes: #58028)

* Tue Feb 24 2026 Vladimir Romanov <rirusha@altlinux.org> 0.5.0-alt1
- New version: 0.5.0.

* Mon Jan 19 2026 Vladimir Romanov <rirusha@altlinux.org> 0.3.1-alt1
- New version: 0.3.1. (closes: #57526)
- %name-translation renamed with %name-common to store all common files
  between frontends.

* Fri Jan 16 2026 Vladimir Romanov <rirusha@altlinux.org> 0.3.0-alt1
- New version: 0.3.0.

* Thu Dec 11 2025 Anton Midyukov <antohami@altlinux.org> 0.2.8-alt1
- Initial build.
