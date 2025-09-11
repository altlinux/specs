%define _unpackaged_files_terminate_build 1

Name: inputplumber
Version: 0.62.2
Release: alt1

Summary: Open source input router and remapper daemon for Linux

License: GPL-3.0
Group: System/Configuration/Other
Url: https://github.com/ShadowBlip/InputPlumber

# Source-url: https://github.com/ShadowBlip/InputPlumber/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires: rust-cargo
BuildRequires: cmake gcc-c++
BuildRequires: libudev-devel clang-devel libiio-devel
Requires: dbus udev

%description
InputPlumber is an open source input routing and control daemon for Linux. It can be used to combine any number of input devices (like gamepads, mice, and keyboards) and translate their input to a variety of virtual device formats.

%prep
%setup -a1

mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[source.virtual-usb-rs]
git = "https://github.com/ShadowBlip/virtual-usb-rs.git"
rev = "5c4c551a23b56f627a36d6775a5876c174be9eb3"
replace-with = "vendored-sources"

[source.evdev]
git = "https://github.com/emberian/evdev.git"
rev = "42b58ee08508b7799322a13bf89121a1d29cf0a2"
replace-with = "vendored-sources"
EOF

%build
%make_build build

%install
%make_install install PREFIX=%buildroot/%prefix NO_RELOAD=true

# Re-assign devices with gyro as ds-edge devices instead of xb elite
%__subst 's/- xbox-elite/- ds5-edge/g' %buildroot%_datadir/inputplumber/devices/50-rog_ally.yaml
%__subst 's/- xbox-elite/- ds5-edge/g' %buildroot%_datadir/inputplumber/devices/50-rog_ally_x.yaml
%__subst 's/- xbox-elite/- ds5-edge/g' %buildroot%_datadir/inputplumber/devices/50-legion_go.yaml
%__subst 's/- xbox-elite/- ds5-edge/g' %buildroot%_datadir/inputplumber/devices/50-legion_go_s.yaml
%__subst 's/- xbox-elite/- ds5-edge/g' %buildroot%_datadir/inputplumber/devices/50-msi_claw7_a2vm.yaml
%__subst 's/- xbox-elite/- ds5-edge/g' %buildroot%_datadir/inputplumber/devices/50-msi_claw8_a2vm.yaml
%__subst 's/- xbox-elite/- ds5-edge/g' %buildroot%_datadir/inputplumber/devices/50-msi_claw_a1m.yaml

# Fixup for elite v2 not being detected
%__subst 's/02e3,0b00/02e3,0b00,0b22,0b05/g' %buildroot%_datadir/inputplumber/devices/60-xbox_one_elite_gamepad.yaml

%files
%_bindir/inputplumber
%_datadir/dbus-1/system.d/org.shadowblip.InputPlumber.conf
%_datadir/inputplumber/
%_unitdir/inputplumber-suspend.service
%_unitdir/inputplumber.service
%_udevhwdbdir/59-inputplumber.hwdb
%_udevhwdbdir/60-inputplumber-autostart.hwdb
%_udevrulesdir/90-inputplumber-autostart.rules

%changelog
* Wed Sep 10 2025 Boris Yumankulov <boria138@altlinux.org> 0.62.2-alt1
- new version 0.62.2

* Thu Jul 10 2025 Boris Yumankulov <boria138@altlinux.org> 0.59.3-alt1
- new version 0.59.3

* Sun Jul 06 2025 Boris Yumankulov <boria138@altlinux.org> 0.59.2-alt1
- new version 0.59.2
- drop loongarch64 patch (no need on nix 0.29.0)

* Fri Jul 04 2025 Ilya Sorochan <k0tran@altlinux.org> 0.58.6-alt2
- add patch for old nix crate version (0.26.4) to enable build on loongarch64

* Thu Jun 19 2025 Boris Yumankulov <boria138@altlinux.org> 0.58.6-alt1
- new version 0.58.6

* Mon Jun 02 2025 Boris Yumankulov <boria138@altlinux.org> 0.58.2-alt1
- initial build for ALT Sisyphus

