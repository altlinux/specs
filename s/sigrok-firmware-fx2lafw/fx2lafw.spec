Name: sigrok-firmware-fx2lafw
Version: 0.1.5
Release: alt1

Summary: Firmware for Cypress EZ-USB FX2(LP) based scopes
License: GPL
Group: System/Kernel and hardware
Url: https://sigrok.org/

Source: %name-%version.tar

Buildarch: noarch

%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

sigrok-firmware-fx2lafw is a Free/Libre/Open-source firmware for logic
analyzers based on the Cypress EZ-USB FX2(LP) chip, as well as the
Hantek 6022BE and Sainsmart DDS120 USB oscilloscopes.

%install
mkdir -p %buildroot%_datadir/sigrok-firmware
tar xf %SOURCE0 --strip-components=1 -C %buildroot%_datadir/sigrok-firmware --wildcards '*/*.fw'

%files
%_datadir/sigrok-firmware

%changelog
* Thu Jun 22 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.5-alt1
- initial
