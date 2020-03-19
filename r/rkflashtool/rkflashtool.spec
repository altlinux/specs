Name: rkflashtool
Version: 0.1
Release: alt1

Summary: Tools for flashing Rockchip devices

Group: File tools
License: BSD like
Url: https://github.com/linux-rockchip/rkflashtool

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/linux-rockchip/rkflashtool/archive/master.zip
Source: %name-%version.tar

BuildRequires: libusb-devel

%description
Tools for flashing Rockchip devices.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc README doc/protocol.txt examples/
%_bindir/rkcrc
%_bindir/rkflashtool
%_bindir/rkmisc
%_bindir/rkpad
%_bindir/rkparameters
%_bindir/rkparametersblock
%_bindir/rkunpack
%_bindir/rkunsign

%changelog
* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
