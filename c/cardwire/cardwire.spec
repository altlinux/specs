%define xdg_name org.opengamingcollective.cardwire
%define _unpackaged_files_terminate_build 1

Name: cardwire
Version: 0.12.3
Release: alt1

Summary: A GPU Manager for linux that uses eBPF LSM hooks to block GPUs
License: GPL-3.0-or-later
Group: System/Configuration/Hardware

Url: https://opengamingcollective.github.io/cardwire/
# Source-url: https://github.com/OpenGamingCollective/cardwire/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-bpfel-unknown-none-target
BuildRequires: libsqlite3-devel
BuildRequires: libudev-devel
BuildRequires: libbpf-devel
BuildRequires: clang-devel
BuildRequires: libxcb-devel
BuildRequires: bpf-linker

ExcludeArch: i586

Requires: hwdata
Requires: upower

Conflicts: switcheroo-control
Provides: switcheroo-control

%description
%summary.

%package gui
Summary: GUI for cardwire
Group: System/Configuration/Hardware
Requires: %name = %EVR

%description gui
%summary.

%prep
%setup -a1

mkdir -p .cargo
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
# aya-ebpf needs unstable BPF asm; remove when supported on stable.
export RUSTC_BOOTSTRAP=aya_ebpf
%rust_build

%install

# bin
install -Dm755 target/release/cardwire %buildroot%_bindir/cardwire
install -Dm755 target/release/cardwired %buildroot%_bindir/cardwired
install -Dm755 target/release/cardwire-gui %buildroot%_bindir/cardwire-gui

# service
install -Dm644 assets/cardwired.service %buildroot%_unitdir/cardwired.service
install -Dm644 assets/99-cardwired.preset %buildroot%_presetdir/99-cardwired.preset
install -Dm644 assets/%xdg_name.conf %buildroot%_datadir/dbus-1/system.d/%xdg_name.conf
install -Dm644 assets/%xdg_name.metainfo.xml %buildroot%_datadir/metainfo/%xdg_name.metainfo.xml

# desktop and icons
install -Dm644 assets/cardwire-gui.desktop %buildroot%_desktopdir/cardwire-gui.desktop
for icon in assets/icons/*.svg; do
    install -Dm644 "$icon" "%buildroot%_iconsdir/hicolor/scalable/apps/$(basename "$icon")"
done

%files
%_bindir/cardwire
%_bindir/cardwired
%_unitdir/cardwired.service
%_presetdir/99-cardwired.preset
%_datadir/dbus-1/system.d/%xdg_name.conf
%_datadir/metainfo/%xdg_name.metainfo.xml

%files gui
%_bindir/cardwire-gui
%_desktopdir/cardwire-gui.desktop
%_iconsdir/hicolor/scalable/apps/%{xdg_name}*.svg

%changelog
* Wed Oct 21 2026 Boris Yumankulov <boria138@altlinux.org> 0.12.3-alt1
- new version 0.12.3 (ALT bug: 60739)

* Sun Aug 09 2026 Boris Yumankulov <boria138@altlinux.org> 0.11.1-alt1
- initial build for ALT Sisyphus
