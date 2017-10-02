Name: atf-sunxi
Version: 1.0
Release: alt1

Summary: ARM Trusted Firmware
License: BSD
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

%description
ARM Trusted Firmware provides a reference implementation of secure world
software for ARMv8-A, including Exception Level 3 (EL3) software.
This release provides initial support for the Allwinner A64/H5 SoC families.

%prep
%setup

%build
make PLAT=sun50iw1p1 bl31

%install
install -pm0644 -D build/sun50iw1p1/release/bl31.bin \
	%buildroot%_datadir/atf/sun50iw1p1/bl31.bin

%files
%_datadir/atf/sun50iw1p1/bl31.bin

%changelog
* Mon Oct 02 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- initial
