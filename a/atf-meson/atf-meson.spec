Name: atf-meson
Version: 2.15
Release: alt1

Summary: ARM Trusted Firmware
License: BSD
Group: System/Kernel and hardware

%ifndef crossbuild
ExclusiveArch: aarch64
%endif

BuildRequires: aarch64-none-elf-gcc

Source: %name-%version-%release.tar

%description
ARM Trusted Firmware provides a reference implementation of secure world
software for ARMv8-A, including Exception Level 3 (EL3) software.
This release provides initial support for the AMLogic AXG, GXBB, GXL and
G12A SoC families.

%prep
%setup

%build
export CROSS_COMPILE=aarch64-none-elf-
for plat in gxbb; do
	make distclean
	make PLAT=$plat bl31
	install -pm0644 -D build/$plat/release/bl31.bin out/$plat/bl31.bin
done
for plat in axg g12a gxl; do
	make distclean
	make PLAT=$plat
	install -pm0644 -D build/$plat/release/bl31.img out/$plat/bl31.img
done

%install
mkdir -p %buildroot%_datadir/atf
cp -a out/* %buildroot%_datadir/atf/

%files
%_datadir/atf/*

%changelog
* Wed Jun 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.15-alt1
- 2.15 released

* Thu Nov 27 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14-alt1
- 2.14 released

* Fri Jun 27 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.13-alt1
- 2.13 released

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
- initial
