%def_disable snapshot

%define _name Iconic
%define binary_name folder_icon
%define ver_major 2026.4
%define rdn_name nl.emphisia.icon

%def_enable check
%def_disable bootstrap

Name: iconic
Version: %ver_major.1
Release: alt1

Summary: Easilly add icons on top of folders
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/youpie/Iconic

Vcs: https://github.com/youpie/Iconic.git

%if_disabled snapshot
Source: https://github.com/youpie/Iconic/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: %_name-%version-cargo.tar

# xmp_toolkit failed for 32-bit
ExcludeArch: %ix86
# and with LTO
%define optflags_lto %nil

Requires: dconf
Requires: icon-theme-adwaita

%define adw_ver 1.8

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(libxml-2.0)
# for vendor/xmp_toolkit
BuildRequires: gcc-c++ libexpat-devel zlib-devel
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli
BuildRequires: /usr/bin/glib-compile-schemas}

%description
An application made for GNOME written in Rust to easilly add images on
top of folders.

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
%meson \
    -Dprofile=default
%nil
%meson_build

%install
%meson_install
cat << _EOF_ > \
%buildroot%_datadir/glib-2.0/schemas/00_%rdn_name.gschema.override
[%rdn_name]
folder-svg-path='%_iconsdir/Adwaita/scalable/places/folder.svg'
_EOF_


%find_lang --output=%name.lang %_name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%_name
%_datadir/%_name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/glib-2.0/schemas/00_%rdn_name.gschema.override
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sun Apr 12 2026 Yuri N. Sedunov <aris@altlinux.org> 2026.4.1-alt1
- 2026.4.1

* Wed Oct 01 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.9.1-alt1
- 2025.9.1

* Thu Apr 03 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.3.2-alt1
- 2025.3.2

* Tue Mar 25 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.3.1-alt1
- 2025.3.1

* Fri Dec 20 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.12.2-alt1
- updated to v2024.12.2-7-g8fc73bd

* Sun Dec 08 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.12.1-alt1
- 2024.12.1

* Wed Oct 30 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.10.2-alt1
- updated to v2024.10.2-3-g7385daa

* Wed Oct 16 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.10.1-alt1
- updated to v2024.10.1-2-g93c41e3

* Sun Aug 25 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.8.1-alt1
- first build for Sisyphus (v2024.8.1-4-gb103890)


