Name: u-boot-meson
Version: 2024.10
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware
Url: https://docs.u-boot.org/en/latest/

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

BuildRequires: bc ccache dtc >= 1.7 flex libgnutls-devel libssl-devel libuuid-devel

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports various AMLogic Meson family boards.

%prep
%setup

%build
export DTC=%_bindir/dtc
boards=$(grep -lr ARCH_MESON configs |sed 's,^configs/\(.\+\)_defconfig,\1,')
for board in $boards; do
	O=build/${board}
	%make_build HOSTCC='ccache gcc' CC='ccache gcc' O=${O} ${board}_defconfig all
	install -pm0644 -D ${O}/u-boot.bin out/${board}/u-boot.bin
done

%install
mkdir -p %buildroot%_datadir/u-boot
cd out
find . -type f | cpio -pmd %buildroot%_datadir/u-boot

%files
%doc README doc/board/amlogic
%_datadir/u-boot/*

%changelog
* Tue Oct 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.10-alt1
- 2024.10 released

* Wed Jul 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.07-alt1
- 2024.07 released

* Thu Apr 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.04-alt1
- 2024.04 released

* Fri Jan 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2024.01-alt1
- 2024.01 released

* Mon Oct 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.10-alt1
- 2023.10 released

* Tue Jul 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.07-alt1
- 2023.07 released

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

* Tue Apr 27 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt3
- fix usb keyboard handling

* Mon Apr 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt2
- eth phy timings aligned with kernel ones

* Wed Apr 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt1
- 2021.04 released

* Wed Jan 27 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.01-alt1
- 2021.01 released

* Tue Oct 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.10-alt1
- 2020.10 released

* Sun Jul 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.07-alt1
- 2020.07 released

* Tue Apr 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.04-alt1
- 2020.04 released

* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.01-alt1
- 2020.01 released

* Tue Oct 08 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.10-alt1
- 2019.10 released

* Fri Jul 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Mon Apr 15 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Thu Jan 17 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Wed Dec 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- 2018.11 released

* Wed Sep 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.07-alt1
- 2018.07 released

* Thu Jun 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt1
- 2018.05 released

* Mon Jan 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.01-alt1
- 2018.01 released

* Tue Feb 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.01-alt1
- initial
