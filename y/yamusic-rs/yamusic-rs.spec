Name: yamusic-rs
Version: 1.1.10
Release: alt1

Summary: Unofficial Yandex Music desktop client written in Rust
License: GPL-3.0-only
Group: Sound
URL: https://github.com/SpolzerMod/yamusic-rs
VCS: https://github.com/SpolzerMod/yamusic-rs

Source0: %name-%version.tar
Source1: crates.tar
Source2: skia-src.tar

ExclusiveArch: aarch64 x86_64

BuildRequires: rust-bindgen rust-cargo /proc
BuildRequires: curl libstdc++-devel
BuildRequires: clang clang-devel gcc-c++ gn ninja-build
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(wuffs)
BuildRequires: pkgconfig(zlib)

%description
Yamusic-rs is an unofficial desktop client for Yandex Music, written in
Rust with a Slint UI. It supports playback, playlists and album downloads,
an equalizer, MPRIS integration and lyrics, without Electron.

%prep
%setup -a1 -a2

%conf
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
# find out required skia version
skia_ver=$(sed -n '/^\[package.metadata\]/,/^\[/p' \
	vendor/skia-bindings*/Cargo.toml \
	| sed -n 's/^skia = "\(.*\)"/\1/p' | head -1)
test -n "$skia_ver"
# now, vendor skia
curl -fsSL https://codeload.github.com/rust-skia/skia/tar.gz/$skia_ver |\
	tar zx --strip-components=1 -C skia-src
# switch to system wuffs
sed -ri -e '/public_include_dirs\s*=/ s,"[^"]+","/usr/include/wuffs",' \
        -e '/sources\s*=/ s,"[^"]+","/usr/include/wuffs/wuffs-v0.3.c",' \
    skia-src/third_party/wuffs/BUILD.gn
tar cf %SOURCE2 skia-src
%endif

%build
export FORCE_SKIA_BUILD=1
export SKIA_USE_SYSTEM_LIBRARIES=1
export SKIA_SOURCE_DIR=$(pwd)/skia-src
export SKIA_GN_COMMAND=gn
cargo build %_smp_mflags --offline --release

%install
install -pm0755 -D target/release/%name %buildroot%_bindir/%name
install -pm0644 -D packaging/%name.desktop %buildroot%_desktopdir/%name.desktop
for size in 16 32 48 64 128 256; do
	install -pm0644 -D packaging/icons/$size.png \
		%buildroot%_iconsdir/hicolor/${size}x${size}/apps/%name.png
done

%files
%doc README.md LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Fri Nov 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.10-alt1
- 1.1.10 released

* Thu Nov 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.9-alt1
- 1.1.9 released

* Wed Nov 25 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.8-alt1
- 1.1.8 released

* Wed Nov 25 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.7-alt1
- 1.1.7 released

* Tue Nov 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.6-alt1
- 1.1.6 released

* Tue Nov 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.5-alt1
- initial
