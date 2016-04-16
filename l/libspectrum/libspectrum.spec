Name: libspectrum
Version: 1.1.1
Release: alt1.qa1

Summary: ZX Spectrum emulation shared library

Packager: ZX Spectrum Development Team <spectrum@packages.altlinux.org>

License: GPL
Group: Emulators
Url: http://fuse-emulator.sourceforge.net/libspectrum.php

Source: http://prdownloads.sf.net/fuse-emulator/%name-%version.tar

# manually removed: gcc-g77 hostinfo 
# Automatically added by buildreq on Sun Feb 06 2005
BuildRequires: bzlib-devel gcc-c++ glib2-devel libgcrypt-devel libgpg-error-devel libstdc++-devel pkgconfig zlib-devel

%package devel
Summary: ZX Spectrum emulation library, header files
Group: Emulators
Requires: %name = %version-%release

%description
libspectrum is a library which is designed to make the input and
output of ZX Spectrum emulator files slightly easier than it would be
otherwise. It should hopefully compile and run on Unix-based systems,
Win32 and Mac OS X.

%description devel
libspectrum is a library which is designed to make the input and
output of ZX Spectrum emulator files slightly easier than it would be
otherwise. It should hopefully compile and run on Unix-based systems,
Win32 and Mac OS X.

This package contains header files for %name.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%_man3dir/*

%files devel
%_libdir/%name.so
%_includedir/%name.h

%changelog
* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.qa1
- NMU: rebuilt with libgcrypt.so.11 -> libgcrypt.so.20.

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Sat Dec 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2
- NMU: new version 1.0.0
- release alt2 to resolve accidental conflict with autoimports

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.3.0.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Fri Jan 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3.0.1-alt2
- cleanup spec

* Sun May 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3.0.1-alt1
- new version 0.3.0.1 (with rpmrb script)

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- NMU: new version (GTK2)

* Tue Sep 30 2003 Alexey Tourbin <at@altlinux.ru> 0.2.0-alt1
- initial revision
