Name: u-boot-qemu
Version: 2024.10
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64 %ix86 x86_64 mips mipsel mips64 mips64el riscv32 riscv64 ppc64

Source: %name-%version-%release.tar

BuildRequires: dtc >= 1.4 flex libgnutls-devel libssl-devel libuuid-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(libfdt)

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
%ifarch %ix86
%define qemu qemu-x86
%endif
%ifarch x86_64
%define qemu qemu-x86_64
%endif
%ifarch mips
%define qemu qemu_mips
%endif
%ifarch mipsel
%define qemu qemu_mipsel
%endif
%ifarch mips64
%define qemu qemu_mips64
%endif
%ifarch mips64el
%define qemu qemu_mips64el
%endif
%ifarch mips
%define qemu qemu_mips
%endif
%ifarch ppc64
%define qemu qemu-ppce500
%endif
%ifarch riscv32
%define qemu qemu-riscv32
%endif
%ifarch riscv64
%define qemu qemu-riscv64
%endif

%prep
%setup

%build
export DTC=%_bindir/dtc
%make_build %{qemu}_defconfig all

%install
%ifarch %ix86 x86_64
install -pm0644 -D u-boot.rom %buildroot%_datadir/u-boot/%qemu/u-boot.rom
%else
install -pm0644 -D u-boot.bin %buildroot%_datadir/u-boot/%qemu/u-boot.bin
%endif

%files
%doc README
%_datadir/u-boot/*

%changelog
* Tue Oct 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.10-alt1
- 2024.10 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.07-alt2
- package ROM images on x86 (closes: 50813)

* Tue Jul 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.07-alt1
- 2024.07 released

* Thu Apr 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.04-alt1
- 2024.04 released

* Fri Jan 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2024.01-alt1
- 2024.01 released

* Mon Oct 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.10-alt1
- 2023.10 released

* Tue Jul 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.07-alt1
- 2023.07 released

* Tue Jun 27 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.04-alt2
- fix relative path boot (closes: 46669)

* Tue Apr 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.04-alt1
- 2023.04 released

* Tue Jan 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.01-alt1
- 2023.01 released

* Tue Oct 04 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.10-alt1
- 2022.10 released

* Tue Jul 12 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.07-alt1
- 2022.07 released

* Thu Apr 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.04-alt1
- 2022.04 released

* Wed Jan 19 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.01-alt1
- 2022.01 released

* Tue Oct 05 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.10-alt1
- 2021.10 released

* Wed Jul 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.07-alt1
- 2021.07 released

* Wed Apr 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt1
- 2021.04 released

* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.01-alt1
- 2021.01 released

* Tue Oct 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.10-alt1
- 2020.10 released

* Fri Jul 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.07-alt1
- 2020.07 released

* Tue Apr 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.04-alt1
- 2020.04 released

* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.01-alt1
- 2020.01 released

* Tue Oct 08 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.10-alt1
- 2019.10 released

* Fri Jul 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Tue May 07 2019 Anton Midyukov <antohami@altlinux.org> 2019.04-alt2
- Build for allowed Arch

* Tue Apr 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- initial
