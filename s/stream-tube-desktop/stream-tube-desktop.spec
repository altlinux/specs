Name: stream-tube-desktop
Version: 0.7.3~alpha
Release: alt1

Summary: Native YouTube desktop client

License: MIT
Group: Video
URL: https://github.com/Avaneesh-Inamdar/Stream-Tube-Desktop
# Source-url: https://github.com/Avaneesh-Inamdar/Stream-Tube-Desktop/archive/refs/tags/v0.7.3-alpha.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust rpm-build-cmake clang /proc
BuildRequires: pkgconfig(fontconfig) pkgconfig(freetype2)
BuildRequires: pkgconfig(wayland-client) pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11) pkgconfig(x11) pkgconfig(xcb)
BuildRequires: pkgconfig(vulkan) pkgconfig(openssl) pkgconfig(libzstd)

Requires: libmpv2

# gpui-pre-linux fails on i586: E0308, u64 passed where c_ulong is u32.
ExcludeArch: %ix86

%description
Stream Tube is a native YouTube client with SponsorBlock, DeArrow and
Return YouTube Dislike built in. It uses GPUI for its interface and libmpv
for video playback.

%prep
%setup -a1
printf '{"files":{},"package":null}\n' > vendor/gpui-pre-windows/.cargo-checksum.json
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install streamtube
install -Dpm0644 packaging/linux/streamtube.desktop %buildroot%_desktopdir/streamtube.desktop
install -Dpm0644 assets/logo.png %buildroot%_iconsdir/hicolor/256x256/apps/streamtube.png
install -Dpm0644 assets/logo.svg %buildroot%_iconsdir/hicolor/scalable/apps/streamtube.svg
install -Dpm0644 packaging/linux/io.github.avaneesh_inamdar.StreamTube.metainfo.xml %buildroot%_datadir/metainfo/io.github.avaneesh_inamdar.StreamTube.metainfo.xml

%files
%_bindir/streamtube
%_desktopdir/streamtube.desktop
%_iconsdir/hicolor/256x256/apps/streamtube.png
%_iconsdir/hicolor/scalable/apps/streamtube.svg
%_datadir/metainfo/io.github.avaneesh_inamdar.StreamTube.metainfo.xml
%doc README.md
%doc LICENSE

%changelog
* Wed Nov 25 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7.3~alpha-alt1
- exclude i586: vendored gpui-pre-linux fails with E0308 (u64/c_ulong).
- require libmpv for video playback.
- new version (0.7.3~alpha)
- add Cargo checksum metadata for the local Windows text patch.
- fix the package file list for ALT.

