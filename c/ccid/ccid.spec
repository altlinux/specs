# vim: set ft=spec: -*- rpm-spec -*-

Name: ccid
Version: 1.3.13
Release: alt1

Summary: USB CCID IFD Handler
Group: System/Libraries
License: LGPL
Url: https://alioth.debian.org/projects/pcsclite/

Requires: pcsc-lite

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Sep 10 2009
BuildRequires: flex libpcsclite-devel libusb-compat-devel

%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
This package provides generic USB CCID (Chip/Smart Card Interface
Devices) driver for PC/SC Lite.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc contrib/Kobil_mIDentity_switch/README_Kobil_mIDentity_switch.txt
%doc AUTHORS README NEWS SCARDCONTOL.txt SCARDGETATTRIB.txt
%_bindir/RSA_SecurID_getpasswd
%_sbindir/Kobil_mIDentity_switch
%ifddir/ifd-ccid.bundle
%_man1dir/RSA_SecurID_getpasswd.1*
%_man8dir/Kobil_mIDentity_switch.8*

%changelog
* Sun Jun 27 2010 Alexey I. Froloff <raorn@altlinux.org> 1.3.13-alt1
- [1.3.13]

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.11-alt1
- Initial build

