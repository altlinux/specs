Name:    coppwr
Version: 1.5.1
Release: alt1

Summary: Low level control GUI for the PipeWire multimedia server
License: GPL-3.0
Group:   Other
Url:     https://github.com/dimtpap/coppwr

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar
Patch1: %name-1.5.0-nix-loongarch64.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires:  pkgconfig(libpipewire-0.3) clang-devel
BuildRequires: cargo-vendor-checksum diffstat


ExcludeArch: %ix86 armh

%description
coppwr is a tool that provides low level control over the PipeWire multimedia
server.  It aims to expose and provide as many ways to inspect and control the
many aspects of the PipeWire multimedia server as possible. It can be used as a
diagnostic tool for PipeWire and to help develop software that interacts with
it.

%prep
%setup
%patch1 -p1 
diffstat -p1 -l %PATCH1 | sed -re 's@vendor/@@' | xargs cargo-vendor-checksum -f

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/dimtpap/egui_node_graph.git?rev=b6f7f02d31fdb74b120691a6c221f10d60864d5c"]
git = "https://github.com/dimtpap/egui_node_graph.git"
rev = "b6f7f02d31fdb74b120691a6c221f10d60864d5c"
replace-with = "vendored-sources"

[source."git+https://gitlab.freedesktop.org/dimtpap/pipewire-rs.git?rev=7bd8b2d3c5d91f56b20c345e97244fff9e58ea0f"]
git = "https://gitlab.freedesktop.org/dimtpap/pipewire-rs.git"
rev = "7bd8b2d3c5d91f56b20c345e97244fff9e58ea0f"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install
install -Dm644 assets/io.github.dimtpap.coppwr.desktop %buildroot/%_datadir/applications/io.github.dimtpap.coppwr.desktop
install -Dm644 assets/io.github.dimtpap.coppwr.metainfo.xml %buildroot/%_datadir/metainfo/io.github.dimtpap.coppwr.metainfo.xml
install -Dm644 assets/icon/scalable.svg %buildroot/%_datadir/icons/hicolor/scalable/apps/io.github.dimtpap.coppwr.svg
install -Dm644 assets/icon/512.png %buildroot/%_datadir/icons/hicolor/512x512/apps/io.github.dimtpap.coppwr.png
install -Dm644 assets/icon/256.png %buildroot/%_datadir/icons/hicolor/256x256/apps/io.github.dimtpap.coppwr.png
install -Dm644 assets/icon/128.png %buildroot/%_datadir/icons/hicolor/128x128/apps/io.github.dimtpap.coppwr.png
install -Dm644 assets/icon/64.png %buildroot/%_datadir/icons/hicolor/64x64/apps/io.github.dimtpap.coppwr.png
install -Dm644 assets/icon/48.png %buildroot/%_datadir/icons/hicolor/48x48/apps/io.github.dimtpap.coppwr.png
install -Dm644 assets/icon/32.png %buildroot/%_datadir/icons/hicolor/32x32/apps/io.github.dimtpap.coppwr.png

%check
%rust_test

%files
%doc *.md
%_bindir/*
%_datadir/applications/io.github.dimtpap.coppwr.desktop
%_datadir/metainfo/io.github.dimtpap.coppwr.metainfo.xml
%_datadir/icons/hicolor/*/apps/io.github.dimtpap.coppwr.*

%changelog
* Thu Jan 25 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.1-alt1
- new version 1.5.1

* Thu Jan 04 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.5.0-alt2
- NMU: fixed FTBFS on LoongArch (trivial patch for nix crate).

* Thu Dec 28 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus
