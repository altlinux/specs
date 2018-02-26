%define firmware_name ql2100
%define firmware_fname ql2100_fw.bin

Name: firmware-%firmware_name
Version: 1.19.38
Release: alt2
License: distributable
Group: System/Kernel and hardware
Summary: Firmware for the QLogic HBAs, based on ISP21xx chips (qla2xxx driver)
Source0: %firmware_fname.1.17.38
Source1: %firmware_fname.1.19.38
Source10: %firmware_name-LICENSE
Source11: %firmware_name-README
Url: ftp://ftp.qlogic.com/outgoing/linux/firmware
BuildArch: noarch
Requires: hotplug

%description
This package contains the firmware for the QLogic HBAs, based on
ISP21xx chips (qla2xxx driver). Usage of the firmware is subject
to the terms contained in %_docdir/%name-%version/%firmware_name-LICENSE.
Please read the license carefully.

%install
%__install -d %buildroot/lib/firmware
%__install -d %buildroot/%_docdir/%name-%version

%__install -m644 %SOURCE0 %buildroot/lib/firmware/
%__install -m644 %SOURCE1 %buildroot/lib/firmware/
%__install -m644 %SOURCE10 %buildroot/%_docdir/%name-%version/
%__install -m644 %SOURCE11 %buildroot/%_docdir/%name-%version/

pushd %buildroot/lib/firmware
	ln -s %firmware_fname.1.17.38 %firmware_fname
popd

%files
/lib/firmware/%firmware_fname.1.17.38
/lib/firmware/%firmware_fname.1.19.38
/lib/firmware/%firmware_fname
%dir %_docdir/%name-%version
%_docdir/%name-%version/%firmware_name-LICENSE
%_docdir/%name-%version/%firmware_name-README

%changelog
* Wed Oct 15 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.19.38-alt2
- spec-file typo fixed

* Tue Oct 14 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.19.38-alt1
- fix firmware installation path on x86_64
- add README and new version of firmware

* Mon Jan 08 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1.17.38-alt1
- initial release

