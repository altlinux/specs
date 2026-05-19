Name: spek-rs
Version: 0.3.2
Release: alt1

Summary: Acoustic spectrum analyser
License: MIT
Group: Sound
Url: https://github.com/patryk-ku/spek-rs
VCS: https://github.com/patryk-ku/spek-rs

Source0: %name-%version.tar
Source1: vendor.tar

Requires: ffmpeg

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc fontconfig-devel

%description
Acoustic spectrum analyser. Spek alternative written in Rust.
The program is used to create spectrograms of audio files.
It uses FFmpeg for audio decoding, like the original.

%prep
%setup -a1

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
%rust_install

install -Dm 0644 packaging/%name.desktop %buildroot%_datadir/applications/%name.desktop
install -Dm 0644 assets/icon.png %buildroot%_iconsdir/hicolor/512x512/apps/%name.png

%files
%doc *.md LICENSE
%_bindir/%name
%_iconsdir/hicolor/512x512/apps/%name.png
%_datadir/applications/%name.desktop

%changelog
* Tue May 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.3.2-alt1
- Initial build for ALT Linux.

