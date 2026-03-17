# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-gnome/ReadySet to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define app_id org.altlinux.ReadySet
%define _libexecdir %_prefix/libexec
%define libname lib%name
%define girname ReadySet
%define api_version 0
%define gis_name gnome-initial-setup

Name: ready-set
Version: 0.6.0
Release: alt1

Summary: The utility for configuring the system at the first start
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://altlinux.space/alt-gnome/ReadySet
VCS: https://altlinux.space/alt-gnome/ReadySet.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: %name-common = %EVR
Conflicts: %gis_name

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
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(libadwaita-1) >= 1.7
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(passwdqc)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(gdm)
BuildRequires: pkgconfig(xkbcommon)

%description
%summary.

%package gdm
Summary: Files needed for work as initial-setup in gdm
Group: Graphical desktop/Other

Requires: %name = %EVR
Requires: gdm

%description gdm
%summary.

%package common
Summary: Common files for %name frontends
Group: Other

Obsoletes: %name-translation <= 0.3.0-alt1
Provides: %name-translation = %EVR

%description common
%summary.

# %package cli
# Summary: CLI %name frontend
# Group: Other

# BuildArch: noarch

# Requires: %name-common = %EVR
# Conflicts: %name = %EVR

# %description cli
# %summary.

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

%description plugin-keyboard
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
%meson -Dpassword_check_backend=both -Duser_with_set_root=true
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files
%_libexecdir/%name
%_iconsdir/hicolor/*/apps/%{app_id}*
%_datadir/applications/%{app_id}*
%_datadir/polkit-1/rules.d/%app_id.rules

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

# %files cli

%files common -f %name.lang
%_libexecdir/%app_id
%_sysconfdir/%name
%_datadir/%name
%_sharedstatedir/%name
%_sysconfdir/dbus-1/system.d/%app_id.conf
%_datadir/polkit-1/actions/%app_id.policy
%_datadir/dbus-1/system-services/%app_id.service
%_unitdir/%name.service
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%doc README.en.md

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
