Name: pam_usb
Version: 0.5.0
Release: alt1.1

Summary: PAM module through external storage

Url: http://www.pamusb.org/
License: GPL
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/pamusb/%name-%version.tar.bz2
Source1: %name-doc.tar.bz2

Requires: pam

# Automatically added by buildreq on Sat Nov 29 2008
BuildRequires: libhal-devel libpam-devel libxml2-devel rpm-build-java rpm-build-mono rpm-build-seamonkey xorg-sdk

%description
pam_usb is a PAM module that enables authentication using a USB storage
device through DSA private/public keys. It can also work with floppy
disks, CD-ROMs, or any kind of mountable device. It supports multiple
users for the same device, multiple hostnames for the same user, a
serial number access list, and private key encryption. It includes the
usbhotplug tool which by default will run xlock when you remove the USB
device and kill it as soon as the same device is plugged back in.

%prep
%setup -q -a1
sed -i 's|lib/security|%_lib/security|g' Makefile
sed -i 's|libs dbus-1`|\0 -lpam|' Makefile

%build
%make_build

%install
#mkdir -p %buildroot{/%_lib/security,%_bindir,%_man1dir}
mkdir -p %buildroot%_sysconfdir/pam.d/usbhotplug

%makeinstall_std

%files
%doc %_docdir/pamusb/
%_bindir/*
/%_lib/security/*
%_man1dir/*
%config(noreplace) %_sysconfdir/pamusb.conf
#%doc AUTHORS Changelog README html
#config(noreplace) %_sysconfdir/hotplug.d/default/pamusb.hotplug
#config(noreplace) %_sysconfdir/pam.d/usbhotplug/usbhotplug.pam
#config(noreplace) %_sysconfdir/pam_usb/handlers/xlock.sh
#config(noreplace) %_sysconfdir/pam_usb/hotplug.conf

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1
- Rebuild with Python-2.7

* Thu Apr 21 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt1
- new version (ported to udisks)

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.1
- Rebuilt with python 2.6

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- new version 0.4.2 (with rpmrb script)

* Thu Jun 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt0.2
- fix build

* Fri Nov 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt0.1
- new version

* Mon Sep 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt0.1
- first build for ALT Linux Sisyphus

* Tue Aug 03 2004 Erwan Velu <erwan@mandrakesoft.com> 0.3.1-2mdk
- Adding documentation
* Tue Aug 03 2004 Erwan Velu <erwan@mandrakesoft.com> 0.3.1-1mdk
- 0.3.1
* Tue May 11 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.2.2-2mdk
- fixed doc permissions

* Tue May 11 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.2.2-1mdk
- removed patch0 (kernel 2.6 is supported upstream now)
- fixed URL
- rpmbuildupdate compatible

* Fri Jan 23 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.2-0.rc2.1mdk
- initial packaging

# end of file
