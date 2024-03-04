Name: ytdlp-gui
Version: 1.0.2
Release: alt2
Summary: A GUI for ytdlp written in Rust
License: GPL-3.0
Group: Networking/File transfer
Url: https://github.com/BKSalman/ytdlp-gui
Source: %name-%version.tar
Source1: vendor.tar
Patch3500: cty-nix-loongarch64.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: cmake
BuildRequires: fontconfig-devel
BuildRequires: gcc-c++
BuildRequires: rust-cargo
BuildRequires: cargo-vendor-checksum diffstat

Requires: ffmpeg
Requires: yt-dlp

%description
%summary.

%prep
%setup -a 1
%patch3500 -p1
diffstat -l -p1 %PATCH3500 | sed -re 's@vendor/@@' | xargs -r cargo-vendor-checksum -f

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_desktopdir \
         %buildroot%_iconsdir/hicolor
install -m 755 target/release/%name %buildroot%_bindir/%name
install -m 644 data/applications/%name.desktop %buildroot%_desktopdir/%name.desktop
cp -pr data/icons/* %buildroot%_iconsdir/hicolor

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Mon Mar 04 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.2-alt2
- NMU: fixed FTBFS on LoongArch (trivial patches for cty and nix crates).

* Wed Feb 28 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
