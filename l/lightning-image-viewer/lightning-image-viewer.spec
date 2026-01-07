%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: lightning-image-viewer
Version: 0.5.1
Release: alt1

Summary: Fast and lightweight desktop image (pre)viewer
License: GPL-3.0
Group: Graphics
Url: https://github.com/shatsky/lightning-image-viewer

Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libheif)
BuildRequires: pkgconfig(sdl3)

BuildRequires: rust-cargo
BuildRequires: rust /proc
BuildRequires: rpm-build-rust

Requires: zenity

%description
Fast and lightweight desktop image viewer featuring minimalistic 
"transparent fullscreen overlay" UI/UX with controls similar to map
apps, implemented in C and Rust with SDL3 and image-rs; 
pan/zoom/fullscreen controls basically replicate controls of leaflet.js
which powers most web maps (but zoom and keyboard pan are 2x more 
granular) and Firefox and Chrome browsers.

%prep
%setup -a1

mkdir -p .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'

[source.vendored-sources]
directory = 'vendor'
EOF

sed -i 's|^Categories=.*|Categories=Graphics;Viewer;|' share/applications/lightning-image-viewer.desktop

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/scalable/apps/%{name}.*

%changelog
* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.1-alt1
- New Rust-based version 0.5.1.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Sat Jun 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
