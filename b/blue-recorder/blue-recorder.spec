%define _unpackaged_files_terminate_build 1
%define hash b989880

Name: blue-recorder
Version: 0.2.0
Release: alt1.git%{hash}

Summary: Simple desktop recorder for Linux systems
License: GPL-3.0
Group: Video
Url: https://github.com/xlmnxp/blue-recorder
Source: %name-%version.tar
Source1: vendor.tar
Patch1: alt-fix-path-work-dir.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
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

Requires: pipewire
Requires: ffmpeg
Requires: xwininfo
Requires: xdg-desktop-portal

%description 
Simple Screen Recorder with support for Wayland display server on GNOME session
written in Rust (based on Green Recorder).

%description -l ru_RU.UTF-8
Простой рекордер экрана с поддержкой сервера отображения Wayland в сеансе GNOME
написанный на Rust (на основе Green Recorder).

%prep
%setup -a 1
%patch1 -p1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/gtk-rs/gtk-rs-core"]
git = "https://github.com/gtk-rs/gtk-rs-core"
replace-with = "vendored-sources"

[source."git+https://github.com/gtk-rs/gtk4-rs.git"]
git = "https://github.com/gtk-rs/gtk4-rs.git"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
install -d %buildroot{%_bindir,%_datadir/%name,%_iconsdir/hicolor/{scalable,96x96}/apps}
install -D -p -m 755 target/release/%name %buildroot%_bindir/%name
install -D -p -m 644 data/%name.desktop %buildroot%_desktopdir/%name.desktop
install -D -p -m 644 data/screenshot*.svg %buildroot%_iconsdir/hicolor/scalable/apps
install -D -p -m 644 data/%name@x96.png %buildroot%_iconsdir/hicolor/96x96/apps/%name.png
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%doc LICENSE.md README.md

%changelog
* Fri May 17 2024 Anastasia Osmolovskaya <lola@altlinux.org> 0.2.0-alt1.gitb989880
- Initial build for ALT.
