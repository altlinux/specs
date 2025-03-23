%define nameB com.github.marinm.songrec

Name: songrec
Version: 0.4.3
Release: alt1

Summary: An open-source Shazam client for Linux.
License: GPL-3.0-only
Group: Sound
Url: https://github.com/marin-m/SongRec
VCS: https://github.com/marin-m/SongRec

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: libalsa-devel libssl-devel pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gio-2.0) libcairo-devel
BuildRequires: pkgconfig(gdk-pixbuf-2.0) pkgconfig(pango)
BuildRequires: pkgconfig(cairo-gobject) pkgconfig(atk) 
BuildRequires: pkgconfig(gdk-3.0) libpulseaudio-devel

Requires: ffmpeg

%description
SongRec is an open-source Shazam client for Linux, written in Rust.
Features:
- Recognize audio from an arbitrary audio file.
- Recognize audio from the microphone.
- Usage from both GUI and command line (for the file recognition part).
- Provide an history of the recognized songs on the GUI, exportable to CSV.
- Continuous song detection from the microphone, with the ability to choose 
your input device.
- Ability to recognize songs from your speakers rather than your microphone 
(on compatible PulseAudio setups).

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

install -Dm 0644 packaging/rootfs/usr/share/icons/hicolor/scalable/apps/%nameB.svg %buildroot%_iconsdir/hicolor/128x128/apps/%nameB.svg
install -Dm 0644 packaging/rootfs/usr/share/applications/%nameB.desktop %buildroot%_datadir/applications/%nameB.desktop
install -Dm 0644 packaging/rootfs/usr/share/metainfo/%nameB.metainfo.xml %buildroot%_datadir/metainfo/%nameB.metainfo.xml

for locale in fr_FR nl it pl es ja ca de_DE ko_KR sk_SK pt_BR; do
 install -Dm 0644 translations/${locale}/LC_MESSAGES/%name.mo %buildroot%_datadir/locale/${locale}/LC_MESSAGES/%name.mo
done

%check
%rust_test

%files
%doc *.md LICENSE
%_bindir/%name
%_iconsdir/hicolor/*/apps/%nameB.svg
%_datadir/applications/%nameB.desktop
%_datadir/metainfo/%nameB.metainfo.xml
%_datadir/locale/*/LC_MESSAGES/%name.mo

%changelog
* Sun Mar 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt1
- Initial build for ALT Linux.
