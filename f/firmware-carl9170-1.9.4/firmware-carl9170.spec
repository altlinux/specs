%define	fwname		carl9170
%define	fwversion	1.9.4

Name: firmware-%fwname-%fwversion
Version: %fwversion
Release: alt1

Summary: Firmware for Atheros USB AR9170 devices
License: Redistributable, no modification permitted
Group: System/Kernel and hardware

Url: http://wireless.kernel.org/en/users/Drivers/carl9170
Source: carl9170.tgz

Provides: firmware-%fwname-%fwversion
BuildArch: noarch

# FIXME: should be defined in rpm-build-$whatever
%define firmwaredir /lib/firmware

%description
Firmware for Atheros USB AR9170 devices

%prep
%setup -n carl9170

%install
install -pD -m644 carl9170-1.fw %buildroot%firmwaredir/carl9170-1.fw

%files
%firmwaredir/carl9170-1.fw

%changelog
* Fri Aug 05 2011 Timur Aitov <timonbl4@altlinux.org> 1.9.4-alt1
- initial build

