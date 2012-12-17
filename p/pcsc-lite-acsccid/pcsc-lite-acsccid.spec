Name:           pcsc-lite-acsccid
BuildRequires:  libusb-compat-devel libpcsclite-devel flex
Version:        1.0.4
Release:        alt1
Group:          System/Servers
License:        LGPLv2.1+
Url:            http://acsccid.sourceforge.net/
Summary:        PCSC Driver for ACS CCID Based Smart Card Readers
Source:         %name-%version.tar
Patch0:         %name-%version-alt-fix.patch

Provides: pcsc-acsccid = %version-%release
Obsoletes: pcsc-acsccid < %version-%release

%description
This package contains a ACS USB CCID (Chip/Smart Card Interface
Devices) driver.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

%prep
%setup
%patch0 -p2

%build
%configure --enable-composite-as-multislot
%make

%install
make install DESTDIR=%buildroot
mkdir -p %buildroot/lib/udev
mkdir %buildroot/lib/udev/rules.d
sed 's:GROUP="pcscd":GROUP="scard":' <src/92_pcscd_acsccid.rules >%buildroot/lib/udev/rules.d/92_pcscd_acsccid.rules


%files
%doc AUTHORS COPYING README
/lib/udev/rules.d/*.rules
%_libdir/pcsc/drivers/*

%changelog
* Mon Dec 17 2012 Ivan Ovcherenko <asdus@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4

* Tue Sep 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.3-alt2
- added 072f:90cc USB ID 

* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Nov 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt0.20110919
- 1.0.3-20110919

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1
- initial
