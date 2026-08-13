%define xdg_name com.github.opengamingcollective.cardwire
%define _unpackaged_files_terminate_build 1

Name: cardwire
Version: 0.11.1
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
BuildRequires: libudev-devel
BuildRequires: libbpf-devel
BuildRequires: clang-devel

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
%rust_build

%install

# bin
install -Dm755 target/release/cardwire %buildroot%_bindir/cardwire
install -Dm755 target/release/cardwired %buildroot%_bindir/cardwired
install -Dm755 target/release/cardwire-gui %buildroot%_bindir/cardwire-gui

# service
install -Dm644 assets/cardwired.service %buildroot%_unitdir/cardwired.service
install -Dm644 assets/%xdg_name.conf %buildroot%_datadir/dbus-1/system.d/%xdg_name.conf

# desktop and icons
install -Dm644 assets/cardwire-gui.desktop %buildroot%_desktopdir/cardwire-gui.desktop
install -Dm644 assets/icons/%xdg_name.tray.svg %buildroot%_iconsdir/hicolor/scalable/apps/%xdg_name.tray.svg
install -Dm644 assets/icons/%xdg_name.tray-hybrid.svg %buildroot%_iconsdir/hicolor/scalable/apps/%xdg_name.tray-hybrid.svg
install -Dm644 assets/icons/%xdg_name.tray-integrated.svg %buildroot%_iconsdir/hicolor/scalable/apps/%xdg_name.tray-integrated.svg
install -Dm644 assets/icons/%xdg_name.tray-manual.svg %buildroot%_iconsdir/hicolor/scalable/apps/%xdg_name.tray-manual.svg
install -Dm644 assets/icons/%xdg_name.tray-smart.svg %buildroot%_iconsdir/hicolor/scalable/apps/%xdg_name.tray-smart.svg

%files
%_bindir/cardwire
%_bindir/cardwired
%_unitdir/cardwired.service
%_datadir/dbus-1/system.d/%xdg_name.conf

%files gui
%_bindir/cardwire-gui
%_desktopdir/cardwire-gui.desktop
%_iconsdir/hicolor/scalable/apps/%xdg_name.tray.svg
%_iconsdir/hicolor/scalable/apps/%xdg_name.tray-hybrid.svg
%_iconsdir/hicolor/scalable/apps/%xdg_name.tray-integrated.svg
%_iconsdir/hicolor/scalable/apps/%xdg_name.tray-manual.svg
%_iconsdir/hicolor/scalable/apps/%xdg_name.tray-smart.svg

%changelog
* Sun Aug 09 2026 Boris Yumankulov <boria138@altlinux.org> 0.11.1-alt1
- initial build for ALT Sisyphus
