Name: stm32flash
Version: 0.5
Release: alt1
Summary: Flash Program for the STM32 Bootloader
License: GPLv2+
Group: System/Kernel and hardware
Url: https://sourceforge.net/projects/stm32flash
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# Source-url: https://sourceforge.net/projects/stm32flash/files/stm32flash-%version.tar.gz/download
# PATCH-FIX-UPSTREAM
Patch1: 0001-Fix-for-device-0x442-System-memory-start-address.patch
# PATCH-FIX-UPSTREAM
Patch2: 0003-dev_table-Mark-0x417-0x429-0x427-for-no-mass-erase.patch
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
%patch1 -p1
%patch2 -p1

%build
%make_build

%install
%makeinstall_std PREFIX=/usr

%files
%doc AUTHORS gpl-2.0.txt HOWTO I2C.txt protocol.txt TODO
%_bindir/*
%_mandir/man?/*.*

%changelog
* Sat Apr 29 2017 Anton Midyukov <antohami@altlinux.org> 0.5-alt1
- Initial build for ALT Linux Sisyphus.
