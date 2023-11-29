%def_enable snapshot
%define optflags_lto %nil

%define ver_major 0.5
%define rdn_name org.pipewire.Helvum

%def_disable bootstrap

Name: helvum
Version: %ver_major.1
Release: alt1

Summary: GTK-based patchbay for PipeWire
License: GPL-3.0-only
Group: Sound
Url: https://gitlab.freedesktop.org/pipewire/helvum

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.freedesktop.org/pipewire/helvum.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

ExcludeArch: %ix86 armh

%define glib_ver 2.66
%define gtk_ver 4.4.0
%define adw_ver 1.4

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo clang clang-devel
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(libpipewire-0.3)

%description
Helvum is a GTK-based patchbay for pipewire, inspired by the JACK tool catia.

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
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Thu Nov 30 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- first build for Sisyphus (0.5.1-7-ge78d6f5)


