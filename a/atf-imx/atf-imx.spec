Name: atf-imx
Version: 2.8
Release: alt1

Summary: ARM Trusted Firmware
License: BSD
Group: System/Kernel and hardware

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

%description
ARM Trusted Firmware provides a reference implementation of secure world
software for ARMv8-A, including Exception Level 3 (EL3) software.
This release provides support for the iMX8M SoC families.

%prep
%setup

%build
for plat in imx8mm imx8mn imx8mp imx8mq; do
	make PLAT=$plat bl31
	install -pm0644 -D build/$plat/release/bl31.bin out/$plat/bl31.bin
	make distclean
done

%install
mkdir -p %buildroot%_datadir/atf
cp -a out/* %buildroot%_datadir/atf/

%files
%_datadir/atf/*

%changelog
* Mon Nov 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8-alt1
- 2.8 released

* Thu Jun 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7-alt1
- 2.7 released

* Wed Jan 19 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6-alt1
- 2.6 released

* Thu Jun 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5-alt1
- initial

