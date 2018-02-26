%define firmware_name ql2200
%define firmware_fname ql2200_fw.bin

Name: firmware-%firmware_name
Version: 2.2.8
Release: alt2
License: distributable
Group: System/Kernel and hardware
Summary: Firmware for the QLogic HBAs, based on ISP22xx chips (qla2xxx driver)
Source0: %firmware_fname.%version
Source1: %firmware_name-LICENSE
Url: ftp://ftp.qlogic.com/outgoing/linux/firmware
BuildArch: noarch
Requires: hotplug

%description
This package contains the firmware for the QLogic HBAs, based on
ISP22xx chips (qla2xxx driver). Usage of the firmware is subject
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
* Tue Oct 14 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.8-alt2
- fix firmware installation path on x86_64

* Mon Jan 08 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.8-alt1
- initial release

