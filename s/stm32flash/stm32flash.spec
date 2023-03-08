Name: stm32flash
Version: 0.7
Release: alt1
Summary: Flash Program for the STM32 Bootloader
License: GPLv2+
Group: System/Kernel and hardware
Url: https://sourceforge.net/projects/stm32flash
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# Source-url: https://sourceforge.net/projects/stm32flash/files/stm32flash-%version.tar.gz/download
BuildRequires: i2c-tools

%description
Open source flash program for the STM32 ARM processors using the ST
serial bootloader over UART or I2C.

Features:
- UART and I2C transports supported
- device identification
- write to flash/ram
- read from flash/ram
- auto-detect Intel HEX or raw binary input format with option to force
  binary
- flash from binary file
- save flash to binary file
- verify & retry up to N times on failed writes
- start execution at specified address
- software reset the device when finished if -R is specified
- resume already initialized connection (for when reset fails, UART only)
- GPIO signalling to enter bootloader mode (hardware dependent)

%prep
%setup
%autopatch -p1

%build
%make_build

%install
%makeinstall_std PREFIX=/usr

%files
%doc AUTHORS gpl-2.0.txt HOWTO I2C.txt protocol.txt TODO
%_bindir/*
%_mandir/man?/*.*

%changelog
* Wed Mar 08 2023 Anton Midyukov <antohami@altlinux.org> 0.7-alt1
- new version (0.7) with rpmgs script

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 0.6-alt1
- new version (0.6) with rpmgs script

* Thu Jun 28 2018 Anton Midyukov <antohami@altlinux.org> 0.5-alt1.1
- Rebuilt for aarch64

* Sat Apr 29 2017 Anton Midyukov <antohami@altlinux.org> 0.5-alt1
- Initial build for ALT Linux Sisyphus.
