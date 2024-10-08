Name: u-boot-sunxi
Version: 2024.10
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware
Url: https://docs.u-boot.org/en/latest/

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

Provides: u-boot-sunxi64 = %version-%release
Obsoletes: u-boot-sunxi64

BuildRequires: atf-sunxi >= 2.10 bc ccache dtc >= 1.4 flex libgnutls-devel libssl-devel libuuid-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(libfdt)

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports boards based on Allwinner SoCs.

See http://linux-sunxi.org/Bootable_SD_card#Bootloader for details.

%prep
%setup

%build
export SCP=/dev/null
export DTC=%_bindir/dtc

boards=$(grep -lr MACH_SUN50I configs |sed 's,^configs/\(.\+\)_defconfig,\1,')
for board in $boards; do
	O=build/${board}
	export BL31=%_datadir/atf/sun50i_a64/bl31.bin
	grep -qF SUN50I_H6= configs/${board}_defconfig && \
		export BL31=%_datadir/atf/sun50i_h6/bl31.bin
	grep -qF SUN50I_H616= configs/${board}_defconfig && \
		export BL31=%_datadir/atf/sun50i_h616/bl31.bin
	%make_build HOSTCC='ccache gcc' CC='ccache gcc' O=${O} ${board}_defconfig all
	install -pm0644 -D ${O}/u-boot-sunxi-with-spl.bin out/${board}/u-boot-sunxi-with-spl.bin
done

%install
mkdir -p %buildroot%_datadir/u-boot
cd out
find . -type f | cpio -pmd %buildroot%_datadir/u-boot

%files
%doc README doc/board/allwinner
%_datadir/u-boot/*

%changelog
* Tue Oct 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.10-alt1
- 2024.10 released

* Tue Jul 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.07-alt1
- 2024.07 released

* Thu Apr 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.04-alt1
- 2024.04 released

* Wed Jan 10 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2024.01-alt1
- 2024.01 released

* Mon Oct 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.10-alt1
- 2023.10 released

* Tue Jul 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.07-alt1
- 2023.07 released

* Wed Apr 26 2023 Dmitry Terekhin <jqt4@altlinux.org> 2023.04-alt2
- Add RBS Repka Pi 3 board

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

* Fri Apr 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt2
- fix ethernet support on H5 boards

* Wed Apr 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt1
- 2021.04 released

* Sat Feb 20 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.01-alt2
- always set fdtfile env var to bare dtb filename (closes: 39705)

* Wed Jan 27 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.01-alt1
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

* Wed Jul 17 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Tue Apr 16 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Tue Jan 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Mon Dec 03 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- 2018.11 released

* Tue Sep 04 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.07-alt1
- 2018.07 released

* Fri Jul 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt1
- 2018.05 released

* Mon Jan 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.01-alt1
- 2018.01 released

* Sun Sep 24 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.09-alt1
- 2017.09 released

* Fri Feb 17 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.01-alt1
- 2017.01 released

* Sun Sep 04 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2016.07-alt1
- 2016.07 released

* Tue Apr 14 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2015.04-alt1
- 2015.04 released

* Tue Jan 13 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2015.01-alt1
- 2015.01 released

* Tue Jun 10 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2014.04-alt1
- 2014.04-sunxi released

* Mon Feb 17 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2013.10-alt1
- 2013.10-sunxi released

* Fri Sep 27 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2013.07-alt2
- 2013.07-sunxi released

* Wed Aug 07 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2013.07-alt1
- initial
