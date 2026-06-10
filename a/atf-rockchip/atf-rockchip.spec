Name: atf-rockchip
Version: 2.15
Release: alt1

Summary: ARM Trusted Firmware
License: BSD
Group: System/Kernel and hardware

Conflicts: rk35-firmware < 20241023-alt4

%ifndef crossbuild
ExclusiveArch: aarch64
%endif

Source: %name-%version-%release.tar
BuildRequires: dtc
BuildRequires: arm-none-eabi-gcc
BuildRequires: aarch64-none-elf-gcc

%description
ARM Trusted Firmware provides a reference implementation of secure world
software for ARMv8-A, including Exception Level 3 (EL3) software.
This package provides support for the RK3328, RK3399 and PX30 SoC families.

%prep
%setup

%build
export CROSS_COMPILE=aarch64-none-elf-
for plat in px30 rk3328 rk3368 rk3399 rk3576 rk3588; do
	make distclean
	make -j8 PLAT=$plat bl31
	install -pm0644 -D build/$plat/release/bl31/bl31.elf out/$plat/bl31.elf
done

%install
mkdir -p %buildroot%_datadir/atf
cp -a out/* %buildroot%_datadir/atf/

%set_verify_elf_method none

%files
%_datadir/atf/*

%changelog
* Wed Jun 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.15-alt1
- 2.15 released

* Tue Mar 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14-alt2
- 3568 bl31 causes regressions, drop it again

* Thu Nov 27 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14-alt1
- 2.14.0 released

* Fri Jun 27 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.13-alt1
- 2.13 released

* Fri Feb 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.12-alt2
- 3568 bl31 lacks SCMI support, drop it from build

* Fri Jan 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.12-alt1
- 2.12 released

* Thu Apr 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.10-alt1
- 2.10 released

* Thu Jun 29 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9-alt1
- 2.9 released

* Mon Nov 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8-alt1
- 2.8 released

* Thu Jun 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7-alt1
- 2.7 released

* Wed Jan 19 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6-alt1
- 2.6 released

* Thu Jun 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5-alt1
- 2.5 released

* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt1
- 2.4 released

* Thu Jul 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3-alt1
- 2.3 released

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
