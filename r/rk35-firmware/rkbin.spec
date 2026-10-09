Name: rk35-firmware
Version: 20260626
Release: alt1

Summary: RK35 BSP firmware
License: Distributable
Group: System/Kernel and hardware

Conflicts: atf-rockchip < 2.15-alt1

AutoReqProv: no

%ifndef crossbuild
ExclusiveArch: aarch64
%endif

Source0: %name-%version.tar
Source1: README.md
Source2: LICENSE

%description
%summary

%define _customdocdir %_docdir/rk35-firmware

%install
mkdir -p %buildroot%_datadir/{atf/rk35{6,8}8,rkbin,doc/rk35-firmware}
tar xf %SOURCE0 -C %buildroot%_datadir/rkbin
ln -svr %buildroot%_datadir/rkbin/bin/rk35/*3568*bl31_v* %buildroot%_datadir/atf/rk3568/bl31.elf
cp -p %SOURCE1 %SOURCE2 %buildroot%_customdocdir

%set_verify_elf_method none

%files
%_customdocdir
%_datadir/rkbin/bin/rk35
%_datadir/atf/rk3568

%changelog
* Fri Oct 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 20260626-alt1
- updated from 20260626 snapshot

* Tue Mar 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 20241023-alt4
- readded bl31 for rk3568, again

* Thu Nov 27 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 20241023-alt3
- dropped rk3568 bl31 in favour of ATF one

* Fri Feb 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 20241023-alt2
- readded bl31 for rk3568

* Fri Jan 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 20241023-alt1
- updated rk3568/rk3588 ddr blobs to 1.23/1.18
- dropped bl31 blobs

* Fri Nov 17 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20230616-alt1
- updated with rk3568 blobs

* Mon Mar 27 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20230207-alt1
- initial
