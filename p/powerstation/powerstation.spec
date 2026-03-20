%define _unpackaged_files_terminate_build 1

Name: powerstation
Version: 0.8.1
Release: alt1

Summary: Daemon for controlling TDP and performance over DBus

License: GPL-3.0
Group: System/Configuration/Other
Url: https://github.com/ShadowBlip/PowerStation

# Source-url: https://github.com/ShadowBlip/PowerStation/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires: gcc-c++ rust-cargo
BuildRequires: cmake clang-devel
BuildRequires: libudev-devel
BuildRequires: libpci-devel
BuildRequires: pkgconfig(systemd)
Requires: dbus

%description
Powerstation is a daemon for controlling TDP and performance over DBus.
It is designed for use on AMD platforms with access to libryzenadj.

%prep
%setup -a1

mkdir -p .cargo
cat <<EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://gitlab.com/shadowapex/libryzenadj-rs"]
git = "https://gitlab.com/shadowapex/libryzenadj-rs"
replace-with = "vendored-sources"

[source."git+https://gitlab.com/asus-linux/asusctl"]
git = "https://gitlab.com/asus-linux/asusctl"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%make_build build

%install
%make_install install PREFIX=%buildroot/%prefix NO_RELOAD=true

%files
%doc LICENSE
%doc README.md
%_bindir/powerstation
%_datadir/dbus-1/system.d/org.shadowblip.PowerStation.conf
%_datadir/powerstation/
%_unitdir/powerstation.service

%changelog
* Fri Mar 20 2026 Boris Yumankulov <boria138@altlinux.org> 0.8.1-alt1
- new version 0.8.1

* Wed Sep 10 2025 Boris Yumankulov <boria138@altlinux.org> 0.7.0-alt1
- new version 0.7.0

* Thu Jun 19 2025 Boris Yumankulov <boria138@altlinux.org> 0.6.1-alt1
- new version 0.6.1

* Mon Jun 02 2025 Boris Yumankulov <boria138@altlinux.org> 0.5.0-alt1
- initial build for ALT Sisyphus


