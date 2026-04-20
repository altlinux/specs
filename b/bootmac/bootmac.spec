%define _unpackaged_files_terminate_build 1

Name: bootmac
Version: 0.7.1
Release: alt1
Summary: Configures the MAC addresses of WLAN and Bluetooth interfaces at boot
License: GPLv3
Group: System/Kernel and hardware
Url: https://gitlab.postmarketos.org/postmarketOS/bootmac
VCS: https://gitlab.postmarketos.org/postmarketOS/bootmac.git
ExclusiveArch: aarch64

Source: %name-%version.tar

Requires: bluez
Requires: bluez-btmgmt
Requires: rfkill

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires: meson
BuildRequires: pkgconfig(udev)

%description
Bootmac configures the MAC addresses of WLAN and Bluetooth interfaces at boot.
Bootmac can be invoked in various ways at boot, but currently only udev rules
are tested. Bootmac generates MAC addresses from the serialno provided by
Android bootloaders through /proc/cmdline or /etc/machine-id with prefix 02:00.

%prep
%setup

%build
%meson -Dsystemd_units=true
%meson_build -v

%install
%meson_install

%files
%doc README.md
%_bindir/%name
%_unitdir/%name@.service
%_udevrulesdir/*

%changelog
* Mon Apr 20 2026 Vasiliy Doylov <neko@altlinux.org> 0.7.1-alt1
- Initial package
