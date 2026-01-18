# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-gnome/ReadySet to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define app_id org.altlinux.ReadySet
%define _libexecdir %_prefix/libexec
%define libname lib%name
%define girname ReadySet
%define api_version 0

Name: ready-set
Version: 0.3.0
Release: alt1

Summary: The utility for configuring the system at the first start
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.space/alt-gnome/ReadySet
Vcs: https://altlinux.space/alt-gnome/ReadySet.git

Source: %name-%version.tar

Requires: %name-translation = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rpm-build-vala
BuildRequires: rpm-build-gir
BuildRequires: meson
BuildRequires: vala
BuildRequires: gobject-introspection-devel
BuildRequires: blueprint-compiler
BuildRequires: gir(Gtk) = 4.0
BuildRequires: gir(Peas) = 2
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

%description
%summary.

%package translation
Summary: Translation file for %name frontends
Group: System/Internationalization

BuildArch: noarch

%description translation
%summary: cli and gui.

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

%build
%meson -Dpassword_check_backend=both
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files
%_libexecdir/%name
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%_iconsdir/hicolor/*/apps/%{app_id}*
%doc README.en.md

%files translation -f %name.lang

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
%_libdir/%name/plugins/keyboard.plugin
%_libdir/%name/plugins/libkeyboard.so

%files plugin-language
%_datadir/polkit-1/rules.d/%app_id.Plugin.Language.rules
%_libdir/%name/plugins/language.plugin
%_libdir/%name/plugins/liblanguage.so

%files plugin-user-common
%_datadir/polkit-1/rules.d/%app_id.Plugin.User.rules
%_libexecdir/%name-set-root-password

%files plugin-user-passwdqc
%_libdir/%name/plugins/user-passwdqc.plugin
%_libdir/%name/plugins/libuser-passwdqc.so

%files plugin-user-pwquality
%_libdir/%name/plugins/user-pwquality.plugin
%_libdir/%name/plugins/libuser-pwquality.so

%files plugin-welcome
%_libdir/%name/plugins/welcome.plugin
%_libdir/%name/plugins/libwelcome.so

%changelog
* Fri Jan 16 2026 Vladimir Romanov <rirusha@altlinux.org> 0.3.0-alt1
- New version: 0.3.0.

* Thu Dec 11 2025 Anton Midyukov <antohami@altlinux.org> 0.2.8-alt1
- Initial build.
