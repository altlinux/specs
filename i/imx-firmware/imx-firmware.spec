Name: imx-firmware
Version: 8.9
Release: alt1

Summary: iMX8M BSP firmware
License: NXP Software License
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: https://www.nxp.com/lgfiles/NMG/MAD/YOCTO/firmware-imx-%version.bin

%description
%summary

%install
mkdir -p %buildroot%_datadir
cd %buildroot%_datadir && sh %SOURCE0 --auto-accept

%files
%_datadir/firmware-imx-%version

%changelog
* Thu Jun 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.9-alt1
- initial
