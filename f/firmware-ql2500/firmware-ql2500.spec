%define firmware_name ql2500
%define firmware_fname1 ql2500_fw.bin
%define firmware_fname2 ql2500_fw.bin_mid

Name: firmware-%firmware_name
Version: 4.4.5
Release: alt1
License: distributable
Group: System/Kernel and hardware
Summary: Firmware for the QLogic HBAs, based on ISP24xx chips (qla2xxx driver)
Source0: %firmware_fname1.4.4.5
Source1: %firmware_fname2.4.4.5

Source10: %firmware_name-LICENSE
Source11: %firmware_name-README
Url: ftp://ftp.qlogic.com/outgoing/linux/firmware
BuildArch: noarch
Requires: hotplug

%description
This package contains the firmware for the QLogic HBAs, based on
ISP24xx chips (qla2xxx driver). Usage of the firmware is subject
to the terms contained in %_docdir/%name-%version/%firmware_name-LICENSE.
Please read the license carefully.

%install
%__install -d %buildroot/lib/firmware
%__install -d %buildroot/%_docdir/%name-%version

%__install -m644 %SOURCE0 %buildroot/lib/firmware/%firmware_fname1.4.4.5
%__install -m644 %SOURCE1 %buildroot/lib/firmware/%firmware_fname2.4.4.5

%__install -m644 %SOURCE10 %buildroot/%_docdir/%name-%version/
%__install -m644 %SOURCE11 %buildroot/%_docdir/%name-%version/

pushd %buildroot/lib/firmware
	ln -s %firmware_fname1.4.4.5 %firmware_fname1
popd


%files
/lib/firmware/%firmware_fname1
/lib/firmware/%firmware_fname1.4.4.5
/lib/firmware/%firmware_fname2.4.4.5
%dir %_docdir/%name-%version
%_docdir/%name-%version/%firmware_name-LICENSE
%_docdir/%name-%version/%firmware_name-README

%changelog
* Tue Oct 14 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.4.5-alt1
- initial release

