# -*- rpm-spec -*-
# $Id: avr-libc,v 1.33 2005/06/03 10:59:46 grigory Exp $

%define cross_arch avr

Summary: AVR libc
Name: avr-libc
Version: 1.7.1
Release: alt2
Serial: 1
License: GPL, LGPL, BSD, Public Domain
Group: Development/Other
URL: http://savannah.gnu.org/projects/avr-libc

Source0: http://savannah.gnu.org/download/avr-libc/avr-libc-%version.tar.bz2
Patch0: 1.7.0.fix.patch

# Automatically added by buildreq on Sun Nov 29 2009
BuildRequires: azenis-fonts-ttf cm-super-fonts-pfb doxygen
Buildrequires: netpbm tetex-core transfig ghostscript-classic

BuildRequires: avr-binutils >= 2.20
BuildRequires: avr-gcc >= 4.5.1-alt3
BuildRequires: avr-gcc-c++ >= 4.5.1-alt3

Requires: avr-binutils >= 2.20
Requires: avr-gcc >= 4.5.1-alt3
Requires: avr-gcc-c++ >= 4.5.1-alt3

%define libavrdir %_libdir/%cross_arch
%define includeavrdir %_includedir/%cross_arch

%description
Avr-libc is a C library for developing applications for Atmel AVR microcontrollers.

%package doc
Summary: Documentation for avr-libc
Group: Development/Other
%description doc
Documentation for avr-libc in html, postscript and pdf formats.


%prep
%setup -q -n %name-%version
%patch0 -p1

%build
./configure \
	--host=avr \
	--build=$(./config.guess) \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--includedir=%includeavrdir \
	--mandir=%_mandir \
	--infodir=%_infodir \
	--enable-doc --disable-versioned-doc --disable-pdf-doc
#	--exec-prefix=%libavrdir \

%__make

%install
%__make \
	prefix=%buildroot%_prefix \
	exec_prefix=%buildroot%_libdir \
	mandir=%buildroot%_mandir \
	infodir=%buildroot%_infodir \
	libdir=%buildroot%_libdir \
	includedir=%buildroot%includeavrdir \
	install

# Move lib and include files from /usr/avr -> /usr/lib/avr
%__mkdir_p %buildroot%_libdir
%__mv %buildroot%_prefix/avr %buildroot%_libdir/

%files
%doc AUTHORS ChangeLog INSTALL LICENSE NEWS README
%doc doc/CHANGES.old doc/ChangeLog doc/INSTALL doc/TODO
%libavrdir/include/*
%libavrdir/lib/*

%files doc
%_bindir/*
%_datadir/doc/avr-libc/*

%changelog
* Thu Mar 17 2011 Grigory Milev <week@altlinux.ru> 1:1.7.1-alt2
- rebuilded with avr-gcc-4.5.1-alt3

* Thu Mar 10 2011 Grigory Milev <week@altlinux.ru> 1:1.7.1-alt1
- new version released

* Thu Jan 13 2011 Grigory Milev <week@altlinux.ru> 1:1.7.0-alt2
- rebuild by new binutils and gcc

* Wed Nov 03 2010 Grigory Milev <week@altlinux.ru> 1:1.7.0-alt1
- new version released

* Sun Nov 29 2009 Grigory Milev <week@altlinux.ru> 1:1.6.7-alt1
- new version released
- remove .pdf from manual package

* Tue Jun 23 2009 Grigory Milev <week@altlinux.ru> 1:1.6.6-alt1
- new version released (see ChangeLog inside package)

* Mon Dec 29 2008 Grigory Milev <week@altlinux.ru> 1:1.6.4-alt1
- new version released

* Mon May 19 2008 Grigory Milev <week@altlinux.ru> 1:1.6.2-alt1
- new version released
- fixed build requires (LaTex utf8.def)

* Wed Jan 09 2008 Grigory Milev <week@altlinux.ru> 1:1.6.1-alt1
- new version released

* Wed Oct  4 2006 Grigory Milev <week@altlinux.ru> 1:1.4.4-alt1
- new version released
- fixating spec
- move avr-man to doc package
- clean up spec

* Mon Sep 19 2005 Grigory Milev <week@altlinux.ru> 1:1.2.5-alt1
- new version released

* Fri Jun 03 2005 Grigory Milev <week@altlinux.ru> 1:1.2.3-alt1
- new version released
- do not compile documents, get it from precompiled (due some bugs)

* Fri Jan 21 2005 Grigory Milev <week@altlinux.ru> 1:1.2.0-alt1
- new version released

* Fri May 28 2004 Grigory Milev <week@altlinux.ru> 1:1.0.4-alt1
- new version released

* Tue Apr 13 2004 Grigory Milev <week@altlinux.ru> 1:1.0.3-alt1
- new version released

* Wed Oct  8 2003 Grigory Milev <week@altlinux.ru> 1:1.0-alt1
- first release
- build user-manual

* Fri Sep  5 2003 Grigory Milev <week@altlinux.ru> 20030805-alt1
- new cvs snapshot released

* Thu Jun 19 2003 Grigory Milev <week@altlinux.ru> 20030512-alt1
- new cvs snapshot released

* Tue Apr 22 2003 Grigory Milev <week@altlinux.ru> 20030414-alt1
- new snapshot version

* Mon Feb 10 2003 Grigory Milev <week@altlinux.ru> 20030203-alt2
- new cvs version (snapshot)

* Tue Nov  5 2002 Grigory Milev <week@altlinux.ru> 20021028-alt1.cvs
- new version (snapshot)

* Fri Oct 25 2002 Grigory Milev <week@altlinux.ru> 20020203-alt1
- Initial build for ALT Linux

* Fri May 03 2002 Theodore Roth <troth@verinet.com>
- Added patch to fix timer.h for mega128.

* Mon Apr 29 2002 Theodore Roth <troth@verinet.com>
- Added patch to fix headers.
- Fix strncasecmp_P macro in pgmspace.h.

* Wed Mar 27 2002 Theodore Roth <troth@verinet.com>
- Updated avr-gcc dependency to 3.0.4-2.
- Fixed up %files section to work with rh-7.1.

* Mon Mar 17 2002 Theodore Roth <troth@verinet.com>
- Initial spec file.


