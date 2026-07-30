Name: lamco-rdp-server
Version: 1.4.4
Release: alt1
Summary: Wayland RDP server for Linux desktop sharing with GUI

License: 0BSD AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-1-Clause AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND BUSL-1.1 AND CC0-1.0 AND GPL-2.0-only AND ISC AND LGPL-2.1-or-later AND MIT AND MIT-0 AND MPL-2.0 AND NCSA AND OpenSSL AND Unicode-3.0 AND Unlicense AND Zlib
Group: System/Servers
URL: https://www.lamco.ai/products/lamco-rdp-server/
Source0: https://github.com/lamco-admin/lamco-rdp-server/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0: cros-libva-vp9-compat.patch

ExcludeArch: %ix86

BuildRequires: rust >= 1.88
BuildRequires: rust-cargo >= 1.88

# System libraries
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: nasm

# PipeWire
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libspa-0.2)

# Wayland/Portal
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)

# D-Bus
BuildRequires: pkgconfig(dbus-1)

# VA-API (hardware encoding)
BuildRequires: pkgconfig(libva) >= 1.20.0

# PAM (authentication)
BuildRequires: pam-devel

# OpenSSL (TLS)
BuildRequires: pkgconfig(openssl)

# FUSE (clipboard file transfer)
BuildRequires: pkgconfig(fuse3)

# Clang for bindgen
BuildRequires: clang
BuildRequires: clang-devel

# Desktop/metainfo validation
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# Runtime dependencies
Requires: pipewire
Requires: xdg-desktop-portal
Requires: pam

%description
lamco-rdp-server is a high-performance RDP server for Wayland-based Linux
desktops. It provides automatic capability detection to select the appropriate
screen capture and input methods for the running environment.

Features:
- H.264 video encoding via EGFX channel (AVC420/AVC444)
- Hardware-accelerated encoding (VA-API, NVENC)
- Multi-monitor support
- Clipboard synchronization
- Keyboard and mouse input
- Automatic platform and DE detection
- Full-featured configuration GUI (10-tab interface)

%prep
%setup -q
%patch -P 0 -p1
# Clear vendored cros-libva checksum so cargo doesn't reject the patched file
sed -i 's/"files":{[^}]*}/"files":{}/' vendor/cros-libva/.cargo-checksum.json

%build
%define _lto_cflags %nil
# Use vendored dependencies (tarball includes vendor/ and .cargo/config.toml)
export CARGO_HOME="$PWD/.cargo"
export CARGO_TARGET_DIR="$PWD/target"

# Override release profile for distro build constraints:
# - Thin LTO instead of fat: reduces peak memory from ~10GB to ~4GB
# - codegen-units=4: allows parallel codegen, reduces build time
# Upstream Cargo.toml uses lto=true/codegen-units=1 for maximum optimization;
# these overrides adapt for mock/koji resource limits while preserving >96%
# of runtime performance. No features are affected.
export CARGO_PROFILE_RELEASE_LTO=thin
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=4

# Build release binaries (server + GUI).
# vsock + websocket activate the AF_VSOCK (Hyper-V Enhanced
# Session Mode) and WebSocket+RDCleanPath transport listeners introduced
# in v1.4.4 — pure Rust additions, no extra system-library BuildRequires.
cargo build --release --offline --features "default,vaapi,gui,vsock,websocket"

%install
install -Dm755 target/release/%name %buildroot%_bindir/%name
install -Dm755 target/release/%name-gui %buildroot%_bindir/%name-gui

# Config directory (server creates default config on first run)
install -dm755 %buildroot%_sysconfdir/%name

# Systemd user service
install -Dm644 packaging/systemd/%name.service %buildroot%_userunitdir/%name.service

# Desktop file (validated by desktop-file-install)
desktop-file-install \
    --dir=%buildroot%_desktopdir \
    data/io.lamco.rdp-server.desktop

# AppStream metainfo
install -Dm644 data/io.lamco.rdp-server.metainfo.xml %buildroot%_datadir/metainfo/io.lamco.rdp-server.metainfo.xml
install -Dm644 data/icons/io.lamco.rdp-server.svg %buildroot%_datadir/icons/hicolor/scalable/apps/io.lamco.rdp-server.svg
for size in 48 64 128 256; do
    install -Dm644 data/icons/io.lamco.rdp-server-$size.png \
        %buildroot%_datadir/icons/hicolor/$sizex$size/apps/io.lamco.rdp-server.png
done

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun_with_restart %name.service

%files
%doc README.md LICENSE licenses/OpenH264-BINARY_LICENSE.txt
%_bindir/%name
%_bindir/%name-gui
%dir %_sysconfdir/%name
%_userunitdir/%name.service
%_desktopdir/io.lamco.rdp-server.desktop
%_datadir/metainfo/io.lamco.rdp-server.metainfo.xml
%_iconsdir/hicolor/scalable/apps/io.lamco.rdp-server.svg
%_iconsdir/hicolor/*/apps/io.lamco.rdp-server.png

%changelog
* Mon Jul 27 2026 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1
- Initial build for Sisyphus.
