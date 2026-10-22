%define _unpackaged_files_terminate_build 1
%define sglibdir %_prefix/lib/%name

Name: usb-signaller
Version: 0.4.2
Release: alt1
Summary: USB gadget mode manager
License: GPLv3
Group: System/Kernel and hardware
Url: https://codeberg.org/DylanVanAssche/usb-signaller/
VCS: https://codeberg.org/DylanVanAssche/usb-signaller.git

Source: %name-%version.tar
Source1: vendor.tar
Source2: default-config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(udev)

%description
Next Generation implementation of usb-moded aimed at mainline Linux Mobile
devices only. usb-signaller has a usb-moded compatible DBus interface, but is
reimplemented in Rust and focuses soley on Linux mainline kernels.

%prep
%setup -a1
%rust_prep
%autopatch -p 1

%build
%rust_build

%install
mkdir -p %buildroot%_datadir/%name
%rust_install

%__install -Dm644 distro/systemd/usb-signaller-developer-mode.service -t %buildroot%_unitdir
%__install -Dm755 distro/scripts/usb-signaller-developer-mode.sh %buildroot%_bindir/usb-signaller-developer-mode
# Waiting for umtpd
# %__install -Dm644 distro/systemd/usb-signaller-mtp-mode.service -t %buildroot%_unitdir
# %__install -Dm755 distro/scripts/usb-signaller-mtp-mode.sh %_bindir/usb-signaller-mtp-mode
%__install -Dm644 distro/systemd/usb-signaller-tethering-mode.service -t %buildroot%_unitdir
%__install -Dm755 distro/scripts/usb-signaller-tethering-mode.sh %buildroot%_bindir/usb-signaller-tethering-mode

%__install -Dm644 %name.service -t %buildroot%_unitdir
%__install -Dm644 com.meego.usb_moded.conf -t %buildroot%_datadir/dbus-1/system.d/

%__install -Dm644 %SOURCE2 %buildroot%sglibdir/%name.toml


%files
%doc README.md
%_bindir/%name
%_bindir/%name-*
%sglibdir/%name.toml
%_unitdir/%name.service
%_unitdir/%name-*.service
%_datadir/dbus-1/system.d/com.meego.usb_moded.conf

%changelog
* Fri Oct 16 2026 Vasiliy Doylov <neko@altlinux.org> 0.4.2-alt1
- Initial build for ALT.
