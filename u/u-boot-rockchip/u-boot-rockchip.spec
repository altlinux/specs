Name: u-boot-rockchip
Version: 2024.10
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware
Url: https://docs.u-boot.org/en/latest/

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

BuildRequires: atf-rockchip >= 2.6 rk35-firmware >= 20230616
BuildRequires: bc ccache dtc >= 1.4 flex libgnutls-devel libssl-devel libuuid-devel
BuildRequires: python3(libfdt)
BuildRequires: python3(setuptools)
BuildRequires: python3(elftools.elf.elffile)

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports various Rockchip based boards.

%prep
%setup

%build
export PYTHON=python3
export DTC=%_bindir/dtc
export RKBIN=%_datadir/rkbin/bin/rk35

buildit()
{
  O=build/${board}
  BL31=%_datadir/atf/$1/bl31.elf \
  %make_build HOSTCC='ccache gcc' CC='ccache gcc' O=${O} ${board}_defconfig all
  install -pm0644 -D ${O}/u-boot-rockchip.bin out/${board}/u-boot-rockchip.bin
  rm -rf ${O}
}

export ROCKCHIP_TPL=$RKBIN/rk3588_ddr_lp4_2112MHz_lp5_2736MHz_v1.11.bin
soc=RK3588
boards=$(fgrep -lr CONFIG_ROCKCHIP_${soc} configs |sed 's,^configs/\(.\+\)_defconfig,\1,')
for board in $boards; do buildit ${soc,,[A-Z]}; done

export ROCKCHIP_TPL=$RKBIN/rk3568_ddr_1560MHz_v1.16.bin
soc=RK3568
boards=$(fgrep -lr CONFIG_ROCKCHIP_${soc} configs |sed 's,^configs/\(.\+\)_defconfig,\1,')
for board in $boards; do buildit ${soc,,[A-Z]}; done

unset ROCKCHIP_TPL

sed -i 's,serial2:1500000n8,serial2:115200n8,' dts/upstream/src/arm64/rockchip/*
egrep -lr 'CONFIG_ROCKCHIP' configs |xargs sed -i '/^CONFIG_BAUDRATE/d'

for soc in PX30 RK3328 RK3399; do
boards=$(fgrep -lr CONFIG_ROCKCHIP_${soc} configs |sed 's,^configs/\(.\+\)_defconfig,\1,')
for board in $boards; do buildit ${soc,,[A-Z]}; done
done

%install
mkdir -p %buildroot%_datadir/u-boot
cd out 
find . -type f | cpio -pmd %buildroot%_datadir/u-boot

%files
%doc README doc/README.rockchip doc/board/rockchip
%_datadir/u-boot/*

%changelog
* Tue Oct 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.10-alt1
- 2024.10 released

* Tue Jul 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.07-alt1
- 2024.07 released

* Tue Jun 04 2024 Anton Midyukov <antohami@altlinux.org> 2024.04-alt1.1
- add anbernic-rg552-rk3399_defconfig

* Thu Apr 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.04-alt1
- 2024.04 released

* Thu Jan 11 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2024.01-alt1
- 2024.01 released

* Mon Oct 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.10-alt1
- 2023.10 released

* Fri Jul 21 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.07-alt2
- fixed orangepi4* boards

* Tue Jul 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.07-alt1
- 2023.07 released

* Tue Apr 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.04-alt1
- 2023.04 released

* Thu Feb 16 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.01-alt2
- add orange pi 4 board variants (closes: 45235)

* Tue Jan 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.01-alt1
- 2023.01 released

* Tue Oct 04 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.10-alt1
- 2022.10 released

* Tue Jul 12 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.07-alt1
- 2022.07 released

* Thu Apr 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.04-alt1
- 2022.04 released

* Thu Jan 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2022.01-alt1
- 2022.01 released

* Tue Oct 05 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.10-alt1
- 2021.10 released

* Wed Jul 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.07-alt1
- 2021.07 released

* Tue Apr 27 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt2
- fix usb keyboard handling

* Wed Apr 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt1
- 2021.04 released

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

* Mon Apr 15 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Wed Mar 06 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Tue Sep 04 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.07-alt1
- 2018.07 released

* Thu Apr 19 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.03-alt1
- 2018.03 released

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
