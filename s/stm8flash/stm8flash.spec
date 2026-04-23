%define _unpackaged_files_terminate_build 1

Name: stm8flash
Version: 2026.02.11
Release: alt1

Summary: SWIM flash programmer for STM8 microcontrollers
License: GPL-2.0-or-later
Group: Development/Tools
Url: https://github.com/vdudouyt/stm8flash
Vcs: https://github.com/vdudouyt/stm8flash.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildRequires: libusb-devel

%description
stm8flash is a command-line utility for programming STM8 family
microcontrollers via the SWIM interface. It supports ST-Link V1,
V2, V2-1, V3 and ESP-STLink programmers, and can read, write and
verify flash, EEPROM and option bytes using Intel HEX, Motorola
S-Record or raw binary files.

%prep
%setup

%build
%make_build RELEASE=1 CFLAGS="%optflags"

%install
install -Dpm 755 stm8flash %buildroot%_bindir/stm8flash

%files
%doc README.md COPYING LICENSE-CHANGE
%_bindir/stm8flash

%changelog
* Thu Apr 16 2026 Ajrat Makhmutov <rauty@altlinux.org> 2026.02.11-alt1
- Initial build for ALT Linux (upstream snapshot b2b5818).
