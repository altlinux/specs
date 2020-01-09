Name: atf-rockchip
Version: 2.2
Release: alt1

Summary: ARM Trusted Firmware
License: BSD
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar
BuildRequires: arm-none-eabi-gcc

%description
ARM Trusted Firmware provides a reference implementation of secure world
software for ARMv8-A, including Exception Level 3 (EL3) software.
This package provides support for the RK3399 SoC family.

%prep
%setup

%build
make PLAT=rk3399 bl31

%install
install -pm0644 -D build/rk3399/release/bl31/bl31.elf \
	%buildroot%_datadir/atf/rk3399/bl31.elf

%set_verify_elf_method none

%files
%_datadir/atf/rk3399/bl31.elf

%changelog
* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Mon Apr 15 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- 2.1 released

* Wed Mar 06 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt1
- 2.0 released

* Fri Apr 20 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5-alt1
- 1.5 released

* Tue Feb 27 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4-alt1
- 1.4 released
