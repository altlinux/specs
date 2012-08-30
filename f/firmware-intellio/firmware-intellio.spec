Name: firmware-intellio
Version: 5.6
Release: alt1

Summary: Firmware for MOXA Intellio Family Device Driver
License: Redistributable, no modification permitted
Group: System/Kernel and hardware

Url: http://www.moxa.com/product/c218turbo.htm
Source: mxdrv-%version.tar

BuildArch: noarch

# FIXME: should be defined in rpm-build-$whatever
%define firmwaredir /lib/firmware

%description
Firmware for MOXA PCI/ISA Intellio Multiserial cards

%prep
%setup -n mxdrv-%version

%install
install -pD -m644 driver/cp204unx.cod %buildroot%firmwaredir/cp204unx.cod
install -pD -m644 driver/c218tunx.cod %buildroot%firmwaredir/c218tunx.cod
install -pD -m644 driver/c320tunx.cod %buildroot%firmwaredir/c320tunx.cod

%files
%firmwaredir/cp204unx.cod
%firmwaredir/c218tunx.cod
%firmwaredir/c320tunx.cod

%changelog
* Thu Aug 30 2012 Ivan Ovcherenko <asdus@altlinux.org> 5.6-alt1
- Initial build (MOXA's build#12033014)
