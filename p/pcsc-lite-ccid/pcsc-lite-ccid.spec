# vim: set ft=spec: -*- rpm-spec -*-

Name: pcsc-lite-ccid
Version: 1.4.5
Release: alt3

Summary: USB CCID IFD Handler
Group: System/Libraries
License: LGPL
Url: https://alioth.debian.org/projects/pcsclite/

Requires: pcsc-lite

Source: %name-%version.tar

Patch1: pcsc-lite-ccid-alt-jacarta-support.patch

# Automatically added by buildreq on Thu Sep 10 2009
BuildRequires: flex libpcsclite-devel libusb-devel

Provides: ccid = %version-%release
Obsoletes: ccid < %version-%release

%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
This package provides generic USB CCID (Chip/Smart Card Interface
Devices) driver for PC/SC Lite.

%prep
%setup
%patch1 -p2

%build
%autoreconf
%configure --enable-twinserial
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/lib/udev/rules.d/
cp -a src/92_pcscd_ccid.rules %buildroot/lib/udev/rules.d/

%files
%doc contrib/Kobil_mIDentity_switch/README_Kobil_mIDentity_switch.txt
%doc AUTHORS README NEWS SCARDGETATTRIB.txt
%config(noreplace) %_sysconfdir/reader.conf.d/libccidtwin
%ifddir/ifd-ccid.bundle
%_libdir/pcsc/drivers/serial/libccidtwin.so
/lib/udev/rules.d/92_pcscd_ccid.rules

%changelog
* Tue May 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt3
- Add JaCarta Flash support (ALT #27377)

* Wed Mar 21 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt2
- Add JaCarta support (Alladin)

* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt1
- [1.4.5]

* Sun Jun 27 2010 Alexey I. Froloff <raorn@altlinux.org> 1.3.13-alt1
- [1.3.13]

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.11-alt1
- Initial build

