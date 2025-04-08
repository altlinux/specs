Name: rk35-firmware
Version: 20241023
Release: alt2

Summary: RK35 BSP firmware
License: Distributable
Group: System/Kernel and hardware

Conflicts: atf-rockchip < 2.12-alt2

AutoReqProv: no
ExclusiveArch: aarch64

Source: %name.tar

%description
%summary

%install
mkdir -p %buildroot%_datadir/{atf/rk35{6,8}8,rkbin/bin/rk35}
tar xf %SOURCE0 -C %buildroot%_datadir/rkbin/bin/rk35
ln -svr %buildroot%_datadir/rkbin/bin/rk35/*3568*bl31* %buildroot%_datadir/atf/rk3568/bl31.elf
%set_verify_elf_method none

%files
%_datadir/rkbin/bin/rk35
%_datadir/atf/rk3568

%check
cd %buildroot%_datadir/rkbin/bin/rk35 && md5sum -c MD5SUM

%changelog
* Fri Feb 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 20241023-alt2
- readded bl31 for rk3568

* Fri Jan 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 20241023-alt1
- updated rk3568/rk3588 ddr blobs to 1.23/1.18
- dropped bl31 blobs

* Fri Nov 17 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20230616-alt1
- updated with rk3568 blobs

* Mon Mar 27 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20230207-alt1
- initial
