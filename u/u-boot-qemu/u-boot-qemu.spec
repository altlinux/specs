Name: u-boot-qemu
Version: 2019.04
Release: alt1

Summary: Das U-Boot
License: GPL
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64

Source: %name-%version-%release.tar

BuildRequires: dtc >= 1.4 flex

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package contains U-Boot image for QEMU virt machine.

%ifarch armh
%define qemu qemu_arm
%endif
%ifarch aarch64
%define qemu qemu_arm64
%endif

%prep
%setup

%build
%make_build %{qemu}_defconfig all

%install
install -pm0644 -D u-boot.bin %buildroot%_datadir/u-boot/%qemu/u-boot.bin

%files
%doc README
%_datadir/u-boot/*

%changelog
* Tue Apr 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- initial
