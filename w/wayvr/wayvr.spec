%define _unpackaged_files_terminate_build 1

Name:    wayvr
Version: 26.7.1
Release: alt1

Summary: Your way to enjoy VR on Linux
License: GPL-3.0-only
Group:   Games/Other
URL:     https://github.com/wayvr-org/wayvr
VCS:     https://github.com/wayvr-org/wayvr.git

Source:  %name-%version.tar
Source1: %name-development-%version.tar
Patch0:  wayvr-26.7.0-openvr-system.patch
Patch1:  wayvr-26.7.0-openvr-compat.patch

BuildRequires: rpm-build-rust
BuildRequires: cmake gcc-c++
BuildRequires: libssl-devel libalsa-devel pipewire-libs-devel clang-devel git-core
BuildRequires: python3-dev libshaderc-devel libdbus-devel libxkbcommon-devel
BuildRequires: libxcb-devel libX11-devel libXext-devel libXrandr-devel fontconfig-devel
BuildRequires: libxkbcommon-x11-devel openxr-devel libglvnd-devel libdav1d-devel
BuildRequires: libvulkan-devel glslc libopenvr-devel

Requires: libopenxr
Requires: libopenvr2
Requires: xwayland-satellite

ExclusiveArch: x86_64

%description
WayVR (previously WlxOverlay-S)

A lightweight OpenXR/OpenVR overlay for Wayland and X11 desktops.

WayVR lets you access your desktop screens while in VR, and even launch apps
directly in VR.

In comparison to similar overlays, WayVR aims to run alongside VR games and
experiences while having as little performance impact as possible. The UI appearance
and rendering techniques are kept as simple and efficient as possible, while still
allowing a high degree of customizability.

%prep
%setup -a1
%patch0 -p1
%patch1 -p1

mkdir -p .cargo
cat > .cargo/config.toml << 'CARGO_EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://codeberg.org/CosmicHarper/vdf-rs.git?rev=fc6dcbea9eb13cacb98dea40063f6f56cde6e145"]
git = "https://codeberg.org/CosmicHarper/vdf-rs.git"
rev = "fc6dcbea9eb13cacb98dea40063f6f56cde6e145"
replace-with = "vendored-sources"

[source."git+https://github.com/galister/ovr_overlay_oyasumi?rev=e477bd2a9e04293ea68c1e7529ef2cb131f32acc"]
git = "https://github.com/galister/ovr_overlay_oyasumi"
rev = "e477bd2a9e04293ea68c1e7529ef2cb131f32acc"
replace-with = "vendored-sources"

[source."git+https://github.com/galister/vulkano.git?rev=cf7f92867928a56ce16b376037c1120f2b167678"]
git = "https://github.com/galister/vulkano.git"
rev = "cf7f92867928a56ce16b376037c1120f2b167678"
replace-with = "vendored-sources"

[source."git+https://github.com/wayvr-org/libmonado-rs.git?rev=6f66b26930c24a8a2fc57ddcd85704784894c750"]
git = "https://github.com/wayvr-org/libmonado-rs.git"
rev = "6f66b26930c24a8a2fc57ddcd85704784894c750"
replace-with = "vendored-sources"

[source."git+https://github.com/rust-av/dav1d-rs.git?rev=03477a36c3de4f2aacbab81a8951150ffdb9c4c3"]
git = "https://github.com/rust-av/dav1d-rs.git"
rev = "03477a36c3de4f2aacbab81a8951150ffdb9c4c3"
replace-with = "vendored-sources"

[source."git+https://gitlab.freedesktop.org/galister/pipewire-rs.git?rev=ba32202c3c391004c3bb533b58fa75a50e47ff57"]
git = "https://gitlab.freedesktop.org/galister/pipewire-rs.git"
rev = "ba32202c3c391004c3bb533b58fa75a50e47ff57"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
CARGO_EOF

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
	./vendor/*/.cargo-checksum.json

%build
export OPENVR_NO_VENDOR=1
export SHADERC_LIB_DIR=%_libdir
export CARGO_PROFILE_RELEASE_DEBUG=2

cargo build --release --offline

%install
install -Dm755 target/release/%name -t %buildroot%_bindir/
install -Dm755 target/release/wayvrctl -t %buildroot%_bindir/

install -Dm644 %name/%name.desktop -t %buildroot%_desktopdir/
install -Dm644 %name/%name.png -t %buildroot%_iconsdir/hicolor/128x128/apps/
install -Dm644 %name/%name.svg -t %buildroot%_iconsdir/hicolor/scalable/apps/

%files
%doc LICENSE README.md
%_bindir/%name
%_bindir/wayvrctl
%_desktopdir/%name.desktop
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Wed Jul 15 2026 Sergey Palcheh <minergenon@altlinux.org> 26.7.1-alt1
- new version 26.7.1

* Tue Jul 07 2026 Sergey Palcheh <minergenon@altlinux.org> 26.7.0-alt1
- new version 26.7.0
- added patch wayvr-26.7.0-openvr-system.patch
- added patch wayvr-26.7.0-openvr-compat.patch

* Sat Jun 13 2026 Sergey Palcheh <minergenon@altlinux.org> 26.2.1-alt1
- initial build for ALT Sisyphus

