Name: lib765
Version: 0.4.1
Release: alt2.qa1

Summary: Library to emulate the uPD765a floppy controller (aka Intel 8272)
Group: System/Libraries
License: LGPL
Url: http://www.seasip.demon.co.uk/Unix/LibDsk/#765

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.seasip.demon.co.uk/Unix/LibDsk/%name-%version.tar.bz2

# Automatically added by buildreq on Mon Sep 29 2003
BuildRequires: libdsk-devel

%description
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy
Disc Controller [FDC] as used in Amstrad computers such as the
PCW, CPC and Spectrum +3. At present it is not a "full" 765;
features not used in the PCW BIOS (such as: DMA; multisector
reads/writes; multitrack mode) are either left unimplemented
or incomplete.

%package devel
Summary: Header files for developing apps which will use %name
Group: Development/C
Requires: %name = %version-%release

%description devel
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy
Disc Controller [FDC] as used in Amstrad computers such as the
PCW, CPC and Spectrum +3. At present it is not a "full" 765;
features not used in the PCW BIOS (such as: DMA; multisector
reads/writes; multitrack mode) are either left unimplemented
or incomplete.

The %name-devel package contains the include files needed to develop
programs that use the %name library.

%prep
%setup

%build
%autoreconf
%configure -with-libdsk --disable-static
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog
%_libdir/*.so.*

%files devel
%doc doc/765.txt
%_includedir/*
%_libdir/*.so

%changelog
* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Fri Jan 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt2
- cleanup spec

* Sun Jul 29 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- new version 0.4.1 (with rpmrb script)

* Sun May 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- restored from orphaned, new version 0.4.0 (with rpmrb script)
- add packager, add Source Url, remove COPYING

* Mon Dec 15 2003 Sir Raorn <raorn@altlinux.ru> 0.3.1.1-alt2
- devel-static and *.la fixes

* Mon Sep 29 2003 Sir Raorn <raorn@altlinux.ru> 0.3.1.1-alt1
- Built for Sisyphus

