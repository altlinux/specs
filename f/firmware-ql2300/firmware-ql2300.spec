%define firmware_name ql2300
%define firmware_fname ql2300_fw.bin

Name: firmware-%firmware_name
Version: 3.3.27
Release: alt1
License: distributable
Group: System/Kernel and hardware
Summary: Firmware for the QLogic HBAs, based on ISP23xx chips (qla2xxx driver)
Source0: %firmware_fname.%version
Source1: %firmware_name-LICENSE
Url: ftp://ftp.qlogic.com/outgoing/linux/firmware
BuildArch: noarch
Requires: hotplug

%description
This package contains the firmware for the QLogic HBAs, based on
ISP23xx chips (qla2xxx driver). Usage of the firmware is subject
to the terms contained in %_docdir/%name-%version/%firmware_name-LICENSE.
Please read the license carefully.

%install
%__install -d %buildroot/lib/firmware
%__install -d %buildroot/%_docdir/%name-%version

%__install -m644 %SOURCE0 %buildroot/lib/firmware/%firmware_fname
%__install -m644 %SOURCE1 %buildroot/%_docdir/%name-%version

%files
/lib/firmware/%firmware_fname
%dir %_docdir/%name-%version
%_docdir/%name-%version/%firmware_name-LICENSE

%changelog
* Tue Oct 14 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 3.3.27-alt1
- new version -- 3.3.27
- fix firmware installation path on x86_64

* Mon Jan 08 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 3.3.20-alt1
- initial release

