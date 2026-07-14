%define _unpackaged_files_terminate_build 1

Name: espflash
Version: 4.5.0
Release: alt1

Summary: Utils for flashing Espressif devices
License: MIT or Apache-2.0
Group: Development/Tools
Url: https://github.com/esp-rs/espflash
Vcs: https://github.com/esp-rs/espflash

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

Source: %name-%version.tar
Source1: vendor.tar

%description
Serial flasher utilities for Espressif devices, based loosely
on esptool.py. Supports the ESP32, ESP32-C2/C3/C5/C6/C61, ESP32-H2,
ESP32-P4, and ESP32-S2/S3.

%package -n cargo-espflash
Summary: Cargo extension for flashing Espressif devices
Group: Development/Tools

%description -n cargo-espflash
Cross-compiler and Cargo extension for flashing Espressif devices.
Supports the ESP32, ESP32-C2/C3/C5/C6/C61, ESP32-H2, ESP32-P4,
and ESP32-S2/S3

%prep
%setup -a1
%rust_prep

%build
export RUSTFLAGS="-Copt-level=3"
%rust_build

%install
%rust_install espflash cargo-espflash

%check
export RUSTFLAGS="-Copt-level=3"
%rust_test

%files
%doc LICENSE-MIT espflash/README.md
%_bindir/espflash

%files -n cargo-espflash
%doc LICENSE-MIT cargo-espflash/README.md
%_bindir/cargo-espflash

%changelog
* Tue Jul 14 2026 Mikhail Nogin <joycap@altlinux.org> 4.5.0-alt1
- Updated to 4.5.0.

* Mon Apr 27 2026 Mikhail Nogin <joycap@altlinux.org> 4.4.0-alt1
- Initial built for Sisyphus.
