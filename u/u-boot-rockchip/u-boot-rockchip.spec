Name: u-boot-rockchip
Version: 2023.01
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

BuildRequires: atf-rockchip >= 2.6
BuildRequires: bc ccache dtc >= 1.4 flex libssl-devel libuuid-devel libgnutls-devel
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
egrep -lr 'CONFIG_ROCKCHIP_(PX30|RK3328|RK3399)' configs |xargs sed -i \
	-e '/^CONFIG_BAUDRATE/ s,1500000,115200,'

%build
export PYTHON=python3
export DTC=%_bindir/dtc

buildit()
{
  O=build/${board}
  BL31=%_datadir/atf/$1/bl31.elf \
  %make_build HOSTCC='ccache gcc' CC='ccache gcc' O=${O} ${board}_defconfig all
  install -pm0644 -D ${O}/u-boot-rockchip.bin out/${board}/u-boot-rockchip.bin
}

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
