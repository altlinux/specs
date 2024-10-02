%define _libexecdir %_prefix/libexec

Name: alvr
Version: 20.11.1
Release: alt1

Summary: Stream VR games from your PC to your headset via Wi-Fi
License: MIT
Group: Games/Other
Url: https://github.com/alvr-org/ALVR

Source: %name-%version.tar
Source1: %name-%version-openvr.tar
Source2: %name-%version-vendor.tar

Patch: alvr-20.10.0-alt-use-system-ffmpeg.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: ImageMagick-tools
BuildRequires: gcc-c++
BuildRequires: clang-devel
BuildRequires: libatk-devel
BuildRequires: libclang17
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libpostproc)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libunwind)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(x264)
BuildRequires: pkgconfig(x265)

Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gtk) = 3.0
Requires: libalsa
Requires: libavcodec60
Requires: libavfilter9
Requires: libavutil58
Requires: libunwind
Requires: libvulkan1
Requires: libx264
Requires: libx265-199
Requires: wget

ExclusiveArch: x86_64

# hack for fix verify-elf: WARNING: ./usr/lib64/alvr/bin/linux64/driver_alvr_server.so: not found: libopenvr_api.so
%add_verify_elf_skiplist %_libdir/%name/bin/linux64/*
%add_findreq_skiplist %_libdir/%name/bin/linux64/*
%add_findprov_skiplist %_libdir/%name/bin/linux64/*

%description
ALVR is an open source remote VR display which allows playing SteamVR games on
a standalone headset such as Gear VR or Oculus Go/Quest.

%prep
%setup -a1 -a2
%patch -p1

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/Ralith/openxrs?rev=9270509d23dc774b43a8b7289e8adf69fcac6828"]
git = "https://github.com/Ralith/openxrs"
rev = "9270509d23dc774b43a8b7289e8adf69fcac6828"
replace-with = "vendored-sources"

[source."git+https://github.com/alvr-org/settings-schema-rs?rev=676185f"]
git = "https://github.com/alvr-org/settings-schema-rs"
rev = "676185f"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

sed -i 's:../../../lib64/libalvr_vulkan_layer.so:libalvr_vulkan_layer.so:' alvr/vulkan_layer/layer/alvr_x86_64.json

# script for downloading client apk file
cat >> alvr_get_client <<EOF
#!/usr/bin/env bash
echo -e "We are starting to download the client for the virtual reality helmet.\n"
wget -c https://github.com/alvr-org/ALVR/releases/download/v%version/alvr_client_android.apk \
-O alvr_client_%version.apk
[ "$?" == 0 ] && echo -e "Done.\n" || echo -e "An error occurred while downloading.\n"
EOF

%build
# export CARGO_PROFILE_RELEASE_LTO=true
# export RUSTUP_TOOLCHAIN=stable
export CARGO_TARGET_DIR=target
export CARGO_NET_OFFLINE=true

export ALVR_ROOT_DIR=%_prefix
export ALVR_LIBRARIES_DIR=%_libdir
export ALVR_OPENVR_DRIVER_ROOT_DIR="%_libdir/%name"
export ALVR_VRCOMPOSITOR_WRAPPER_DIR=%_libexecdir/%name
# export FIREWALL_SCRIPT_DIR="$ALVR_ROOT_DIR/share/%name/"

cargo run --release --frozen -p alvr_xtask -- --platform linux --no-nvidia

cargo build \
    --frozen \
    --release \
    -p alvr_server_openvr \
    -p alvr_dashboard \
    -p alvr_vulkan_layer \
    -p alvr_vrcompositor_wrapper

%define _alvrBuildDir "target/release"

%install
install -Dm755 %_alvrBuildDir/alvr_dashboard -t %buildroot%_bindir/
install -Dm755 alvr_get_client -t %buildroot%_bindir/

# vrcompositor wrapper
install -Dm755 %_alvrBuildDir/alvr_vrcompositor_wrapper %buildroot%_libexecdir/%name/vrcompositor-wrapper
install -Dm644 %_alvrBuildDir/alvr_drm_lease_shim.so -t %buildroot%_libexecdir/%name/

# OpenVR Driver
install -Dm644 %name/xtask/resources/driver.vrdrivermanifest -t %buildroot%_libdir/%name/
install -Dm644 %_alvrBuildDir/libalvr_server_openvr.so %buildroot%_libdir/%name/bin/linux64/driver_alvr_server.so
install -Dm644 openvr/bin/linux64/libopenvr_api.so -t %buildroot%_libdir/%name/bin/linux64/

# Vulkan Layer
install -Dm644 %_alvrBuildDir/libalvr_vulkan_layer.so -t %buildroot%_libdir/
install -Dm644 alvr/vulkan_layer/layer/alvr_x86_64.json -t %buildroot%_datadir/vulkan/explicit_layer.d/

# Desktop
install -Dm644 alvr/xtask/resources/%name.desktop -t %buildroot%_desktopdir/

# Icons
for res in 16 32 48 128 256; do
    mkdir -p %buildroot%_iconsdir/hicolor/$res'x'$res/apps/
    convert resources/alvr.png -resize $res'x'$res %buildroot%_iconsdir/hicolor/$res'x'$res/apps/%name.png
done

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/alvr_dashboard
%_bindir/alvr_get_client
%_libdir/%name/
%_libdir/libalvr_vulkan_layer.so
%_libexecdir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/vulkan/explicit_layer.d/alvr_x86_64.json

%changelog
* Wed Oct 02 2024 Mikhail Tergoev <fidel@altlinux.org> 20.11.1-alt1
- 20.11.1

* Thu Feb 08 2024 Mikhail Tergoev <fidel@altlinux.org> 20.6.1-alt1
- initial build for ALT Sisyphus (thx @toxblh)
