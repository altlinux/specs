Name: u-boot-meson
Version: 2018.05
Release: alt1

Summary: Das U-Boot
License: GPL
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

BuildRequires: bc dtc >= 1.4

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports Raspberry 3 board.

%prep
%setup

%build
%make_build odroid-c2_defconfig all

%install
install -pm0644 -D u-boot.bin %buildroot%_datadir/u-boot/odroid-c2/u-boot.bin
cp -p board/amlogic/odroid-c2/README README.odroid-c2

%files
%doc README README.odroid-c2 
%_datadir/u-boot/*

%changelog
* Thu Jun 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt1
- 2018.05 released

* Mon Jan 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.01-alt1
- 2018.01 released

* Tue Feb 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.01-alt1
- initial

