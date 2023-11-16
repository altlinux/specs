%def_enable snapshot
%define ver_major 0.0
%define rdn_name com.belmoussaoui.Obfuscate

%def_disable bootstrap
%def_enable check

Name: obfuscate
Version: %ver_major.9
Release: alt1

Summary: Censor private information
License: GPL-3.0-or-later
Group: Graphics
Url: https://apps.gnome.org/Obfuscate

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/obfuscate.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.0
%define adwaita_ver 1.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver

%description
Obfuscate lets you redact your private information from any image.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Thu Nov 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.0.9-alt1
- first build for Sisyphus (0.0.9-17-gff78a3b)


