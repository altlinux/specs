Name: u-boot-imx
Version: 2023.04
Release: alt1

Summary: Das U-Boot
License: GPLv2+
Group: System/Kernel and hardware

ExclusiveArch: armh aarch64

Source: %name-%version-%release.tar

%ifarch aarch64
%define ATF atf-imx imx-firmware = 8.9
%else
%define ATF %nil
%endif

BuildRequires: %ATF bc ccache dtc >= 1.4 flex libssl-devel lzop zip
BuildRequires: python3(setuptools)
BuildRequires: python3(libfdt)

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports some of iMX6|iMX8 family boards.

%prep
%setup

%build
export DTC=%_bindir/dtc
%ifarch aarch64
boards='pico-imx8mq imx8mq_evk imx8mq_phanbell'
%else
boards='mx6cuboxi'
%endif
for board in $boards; do
	O=build/${board}
%ifarch aarch64
	install -pD %_datadir/atf/imx8mq/bl31.bin ${O}/bl31.bin
	install -p  %_datadir/firmware-imx-*/firmware/hdmi/cadence/signed_hdmi_imx8m.bin  ${O}/
	install -p  %_datadir/firmware-imx-*/firmware/ddr/synopsys/lpddr4_pmu_train_* ${O}/
%endif
	make HOSTCC='ccache gcc' CC='ccache gcc' O=${O} ${board}_defconfig
	%make_build HOSTCC='ccache gcc' CC='ccache gcc' O=${O} \
%ifarch aarch64
	flash.bin
	install -pm0644 -D ${O}/flash.bin out/${board}/flash.bin
%else
	all
	install -pm0644 -D ${O}/SPL out/${board}/SPL
	install -pm0644 ${O}/u-boot.img out/${board}/
%endif
done

%install
mkdir -p %buildroot%_datadir/u-boot
cd out
find . -type f | cpio -pmd %buildroot%_datadir/u-boot

%files
%doc README* doc/board/nxp
%_datadir/u-boot/*

%changelog
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

* Thu Jun 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.04-alt1
- 2021.04 released

* Tue Apr 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.04-alt1
- 2020.04 released

* Thu Jan 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.01-alt1
- 2020.01 released

* Tue Oct 08 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.10-alt1
- 2019.10 released

* Fri Jul 19 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.07-alt1
- 2019.07 released

* Tue Apr 16 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.04-alt1
- 2019.04 released

* Tue Jan 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.01-alt1
- 2019.01 released

* Mon Dec 03 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.11-alt1
- 2018.11 released

* Tue Sep 04 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.07-alt1
- 2018.07 released

* Thu Jun 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt1
- 2018.05 released

* Mon Jan 15 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.01-alt1
- 2018.01 released

* Tue Feb 07 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.01-alt1
- initial
