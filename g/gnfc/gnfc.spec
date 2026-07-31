%define _unpackaged_files_terminate_build 1

Name: gnfc
Version: 0.1.0
Release: alt1
Summary: GNOME NFC Tag Reader
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
Url: https://salsa.debian.org/manut/gnfc
VCS: https://salsa.debian.org/manut/gnfc.git

Source: %name-%version.tar
Source1: vendor.tar
Patch1: 0001-meson-add-host_arch-option.patch
Patch2: 0002-cargo-Relax-versions.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-rust
BuildRequires: clang-devel
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)

%description
A GTK4/libadwaita application for reading (and eventually writing) NFC tags
via the **neard** daemon's D-Bus interface. Designed for mobile phones and
tablets running GNOME/Phosh, but works on any Linux desktop.

%prep
%setup -a1
%rust_prep
%autopatch -p 1

%build
%meson
%meson_build -v

%install
%meson_install

%files
%doc README.md
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml
%_bindir/%name

%changelog
* Wed Jul 22 2026 Vasiliy Doylov <neko@altlinux.org> 0.1.0-alt1
- Initial build for ALT.
