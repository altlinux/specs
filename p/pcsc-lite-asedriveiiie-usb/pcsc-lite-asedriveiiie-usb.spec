Name:           pcsc-lite-asedriveiiie-usb
BuildRequires:  libusb-compat-devel libpcsclite-devel flex
Version:        3.7
Release:        alt1
Group:          System/Servers
License:        Redistributable
Url:            http://http://www.athena-scs.com
Summary:        PCSC Driver for Asedrive USB Smart Card Readers
Source:         %name-%version.tar

Provides: pcsc-asedriveiiie-usb = %version-%release
Obsoletes: pcsc-asedriveiiie-usb < %version-%release

%description
This package contains a Asedrive USB  driver.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup

%build
%configure
sed -i "s,/etc/udev/rules.d/,\${DESTDIR}/lib/udev/rules.d/," Makefile
%make

%install
mkdir -p %buildroot/lib/udev/rules.d/
make install DESTDIR=%buildroot

%files
%doc LICENSE README
/lib/udev/rules.d/*.rules
%_libdir/pcsc/drivers/*

%changelog
* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7-alt1
- initial
