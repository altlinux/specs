Name:    usbeehive
Version: 0.11.0
Release: alt1

Summary: USB device and USB-C cable diagnostics tool
License: MIT
Group:   System/Kernel and hardware
URL:     https://github.com/abrauchli/usbeehive

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libudev-devel
BuildRequires: rpm-macros-systemd

%description
usbeehive is a command-line tool and a Rust library that report in plain
English what each USB device and USB-C cable connected to your Linux
machine can actually do: vendor, product, serial, negotiated link speed,
USB version, power draw, device class, kernel driver and hub topology.

For USB-C ports it additionally decodes cable e-marker information,
charger PDO lists and USB Power Delivery VDOs, and identifies charging
bottlenecks such as a cable limiting link speed or an undersized charger.

The package also installs usbeehived, a D-Bus daemon exposing the
org.usbeehive.Devices5 interface on the session bus for desktop
integrations like the usbee GNOME Shell extension.

%prep
%setup -a1
%rust_prep

%build
export RUSTFLAGS="${RUSTFLAGS} -g"
cargo build --release %{?_smp_mflags} --offline --features dbus

%install
%rust_install usbeehive usbeehived
install -Dm 644 systemd/usbeehived.service %buildroot%_userunitdir/usbeehived.service

%files
%doc LICENSE README.md
%_bindir/%name
%_bindir/usbeehived
%_userunitdir/usbeehived.service

%changelog
* Fri Aug 14 2026 Sergey Palcheh <minergenon@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus
