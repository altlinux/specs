Name:    pcsc-lite-asedriveiiie-usb
Version: 3.7
Release: alt2
Group:   System/Servers
License: Redistributable
Url:     http://www.athena-scs.com
Summary: PCSC Driver for Asedrive USB Smart Card Readers

Source:  %name-%version.tar

BuildRequires: libusb-compat-devel libpcsclite-devel flex

Provides: pcsc-asedriveiiie-usb = %version-%release
Obsoletes: pcsc-asedriveiiie-usb < %version-%release
Provides: pcsc-lite-asekey = %version-%release
Obsoletes: pcsc-lite-asekey < %version-%release

Requires(pre): pcsc-lite

%description
This package contains a Asedrive USB driver.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup

%build
%configure
sed -i "s,/etc/udev/rules.d/,\${DESTDIR}%_udevrulesdir/," Makefile
%make

%install
mkdir -p %buildroot%_udevrulesdir
make install DESTDIR=%buildroot

%files
%doc LICENSE README
%_udevrulesdir/*.rules
%_libdir/pcsc/drivers/*

%changelog
* Sun Apr 05 2026 Andrey Cherepanov <cas@altlinux.org> 3.7-alt2
- Required pcsc-lite for group pcscd for udev rules.

* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7-alt1
- initial
