%define firmware_name ql2400

Name: firmware-%firmware_name
Version: 8.03.00
Release: alt1
License: distributable
Group: System/Kernel and hardware
Summary: Firmware for the QLogic HBAs, based on ISP24xx chips (qla2xxx driver)
Url: https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git
BuildArch: noarch

Source0: %{firmware_name}_fw.bin
Source1: LICENCE.qla2xxx

%description
This package contains the firmware for the QLogic HBAs, based on
ISP24xx chips (qla2xxx driver). Usage of the firmware is subject
to the terms contained in %_docdir/%name-%version/LICENSE.qla2xxx
Please read the license carefully.

%install
install -pD -m0644 %SOURCE0 %buildroot/lib/firmware/%{firmware_name}_fw.bin
install -pD -m0644 %SOURCE1 %buildroot/%_docdir/%name-%version/LICENCE.qla2xxx

%files
/lib/firmware/*.bin
%_docdir/%name-%version

%changelog
* Tue Oct 25 2016 Valery Inozemtsev <shrek@altlinux.ru> 8.03.00-alt1
- 8.03.00

* Tue Oct 14 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.4.5-alt1
- 4.4.5
- fix firmware installation path on x86_64
- add README and new version of firmware

* Sun Mar 18 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.27-alt1
- 4.0.27

* Mon Jan 08 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.26-alt1
- initial release

