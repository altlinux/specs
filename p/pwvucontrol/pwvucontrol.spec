%def_enable snapshot
%define _name pwvucontrol
%define ver_major 0.4
%define xdg_name com.saivert.%_name

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.3
Release: alt1

Summary: Pipewire Volume Control
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/saivert/pwvucontrol

Vcs: https://github.com/saivert/pwvucontrol.git

%if_disabled snapshot
Source: https://github.com/saivert/pwvucontrol/releases/download/v%version/%name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif
Source1: %name-%version-cargo.tar

ExcludeArch: %ix86 armh

%define gtk_ver 4.10.0
%define adw_ver 1.2
%define pw_ver 0.3.83
%define wp_ver 0.4.15

Requires: wireplumber >= %wp_ver
Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(wireplumber-0.4)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils /usr/bin/glib-compile-schemas}

# for bindgen
BuildRequires: clang-devel

%description
This is an attempt at making a volume control applet for Pipewire.

Current implemented features as of 2024-05-04:

Volume control
Mute
Media name display
Peak level meter
Output device (Sink) drop down for playback streams
Default output device
Card profile selection
Port selection for sinks and sources

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
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
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*

%changelog
* Sat Jun 29 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- first build for Sisyphus (0.4.3-8-gdb53d3) (ALT #50761)



