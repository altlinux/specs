%define _unpackaged_files_terminate_build 1

Name: blue-recorder
Version: 0.3.0
Release: alt1

Summary: Simple desktop recorder for Linux systems
License: GPL-3.0
Group: Video

Url: https://github.com/xlmnxp/blue-recorder
Vcs: https://github.com/xlmnxp/blue-recorder

Source: %name-%version.tar
Source1: vendor.tar

Requires: pipewire
Requires: ffmpeg
Requires: xwininfo
Requires: xdg-desktop-portal

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: gettext-tools
BuildRequires: libglib2-devel
BuildRequires: libgio-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libcairo-devel
BuildRequires: libcairo-gobject-devel
BuildRequires: libpango-devel
BuildRequires: libgtk4-devel
BuildRequires: libatk-devel
BuildRequires: libgtk+3-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: pkgconfig(libadwaita-1)

%description 
Simple Screen Recorder with support for Wayland display server on GNOME session
written in Rust (based on Green Recorder).

%description -l ru_RU.UTF-8
Простой рекордер экрана с поддержкой сервера отображения Wayland в сеансе GNOME
написанный на Rust (на основе Green Recorder).

%prep
%setup -a1
subst 's|locales|%_datadir/%name/locales|' gui/src/fluent.rs
subst 's|data/blue-recorder.svg|%_iconsdir/hicolor/96x96/apps/%name.png|' gui/src/ui.rs
%rust_prep

%build
%rust_build

%install
install -d %buildroot{%_bindir,%_datadir/%name,%_datadir/%name/locales,%_iconsdir/hicolor/{scalable,96x96}/apps}
install -D -p -m 755 target/release/%name %buildroot%_bindir/%name
install -D -p -m 644 data/%name.desktop %buildroot%_desktopdir/%name.desktop
install -D -p -m 644 data/screenshot*.svg %buildroot%_iconsdir/hicolor/scalable/apps
install -D -p -m 644 data/%name@x96.png %buildroot%_iconsdir/hicolor/96x96/apps/%name.png
cp -a locales/*.ftl %buildroot%_datadir/%name/locales/

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%doc LICENSE.md README.md

%changelog
* Fri Aug 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.3.0-alt1
- 0.2.0 -> 0.3.0
- added VCS
- dropped old patch

* Fri May 17 2024 Anastasia Osmolovskaya <lola@altlinux.org> 0.2.0-alt1.gitb989880
- Initial build for ALT.
