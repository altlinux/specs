# -*- rpm-spec -*-
# $Id: avr-binutils,v 1.11 2003/09/05 11:18:56 grigory Exp $

#define snapshot_version 030512
%define cross_arch avr

Summary: A GNU collection of binary utilities.
Name: %cross_arch-binutils
Version: 2.21
Release: alt1
Serial: 1
Copyright: GPL
Group: Development/Other
URL: ftp://ftp.kernel.org/pub/linux/devel/binutils/
Source: binutils-%version.tar.bz2
Patch0: patch-coff-avr-2.20.51.0.9.patch
#Patch0: binutils-%version-info_fix.diff

%define libavrdir %_libdir/%cross_arch
%define includeavrdir %_includedir/%cross_arch

# Automatically added by buildreq on Mon Nov 29 2010
BuildRequires: avr-gcc-c++ expect flex gcc-c++ glibc-devel-static perl-Pod-Parser zlib-devel

%description
Avr-Binutils is a collection of binary utilities, including avr-ar (for
creating, modifying and extracting from archives), avr-as (a family of GNU
assemblers), avr-ld (the GNU linker), avr-nm (for listing symbols from object
files), avr-objcopy (for copying and translating object files), avr-objdump
(for displaying information from object files), avr-ranlib (for generating an
index for the contents of an archive), avr-size (for listing the section sizes
of an object or archive file), avr-strings (for listing printable strings from
files), avr-strip (for discarding symbols), and avr-addr2line (for converting
addresses to file and line).

This package is for cross-development of AVR programs.

%prep
%setup -n binutils-%version -q
#%patch0 -p1
#%patch0 -p1 -b .avrinfo

%build
# Binutils come with its own custom libtool
%define __libtoolize echo
./configure \
	--prefix=%_prefix \
	--mandir=%_mandir \
	--infodir=%_infodir \
	--includedir=%includeavrdir \
	--libdir=%libavrdir \
	--exec-prefix=%libavrdir \
	--disable-nls \
	--target=avr \
	--program-prefix="avr-" \
	--enable-languages="c,c++"
%make_build

%install
%__mkdir_p %buildroot{%libavrdir/bin,%includeavrdir,%_bindir}

%makeinstall \
	prefix=%buildroot%_prefix \
	exec_prefix=%buildroot%libavrdir \
	libdir=%buildroot%libavrdir \
	includedir=%buildroot%includeavrdir \
	mandir=%buildroot%_mandir
%__make install-info \
	prefix=%buildroot%_prefix \
	infodir=%buildroot%_infodir

%__mv %buildroot%_bindir/* %buildroot%libavrdir/bin/
for i in `ls -1 %buildroot%libavrdir/bin/`; do
	%__ln_s ../..%libavrdir/bin/$i %buildroot%_bindir/$i
done
for i in `ls -1 %buildroot%libavrdir/%cross_arch/bin/`; do
	%__ln_s %cross_arch-$i %buildroot%libavrdir/bin/$i
done
%__rm -rf %buildroot%libavrdir/%cross_arch/bin

%__ln_s ../bin %buildroot%libavrdir/avr/bin
%__ln_s ./ %buildroot%libavrdir/lib
%__ln_s ../../..%includeavrdir %buildroot%libavrdir/include

%__rm -f %buildroot%_bindir/*c++filt*
%__rm -fr %buildroot%_infodir

%__ln_s %_libdir/%cross_arch %buildroot%_prefix/%cross_arch

%files
%doc README
%includeavrdir
%libavrdir
%_bindir/*
%libavrdir/*
%_prefix/%cross_arch
%_man1dir/*

%changelog
* Thu Jan 13 2011 Grigory Milev <week@altlinux.ru> 1:2.21-alt1
- new version released
- updated from fc src.rpm
- removed coff patch
- fixed link paths

* Mon Nov 29 2010 Grigory Milev <week@altlinux.ru> 1:2.20.51.0.9-alt2
- fix build requires

* Wed Nov 03 2010 Grigory Milev <week@altlinux.ru> 1:2.20.51.0.9-alt1
- New version released

* Wed Dec 02 2009 Grigory Milev <week@altlinux.ru> 1:2.18.50.0.3-alt3
- fix build requires
- build using gcc 3.4

* Sat Jan 12 2008 Grigory Milev <week@altlinux.ru> 1:2.18.50.0.3-alt2
- added avr coff patch

* Wed Jan 09 2008 Grigory Milev <week@altlinux.ru> 1:2.18.50.0.3-alt1
- New version released

* Wed Sep 21 2005 Grigory Milev <week@altlinux.ru> 1:2.16-alt1
- New version released

* Fri Sep  5 2003 Grigory Milev <week@altlinux.ru> 1:2.14-alt1
- 2.14 released

* Thu Jun 19 2003 Grigory Milev <week@altlinux.ru> 20030512-alt1
- new version released

* Tue Apr 22 2003 Grigory Milev <week@altlinux.ru> 20030414-alt1
- new version (cvs snapshot 20030414)

* Mon Feb 10 2003 Grigory Milev <week@altlinux.ru> 2.13.75-alt2
- new version (snapshot 030118)

* Tue Nov  5 2002 Grigory Milev <week@altlinux.ru> 2.13.75-021028
- new version (snapshot)

* Wed Oct 30 2002 Grigory Milev <week@altlinux.ru> 2.11.2-alt1
- Initial build for ALT Linux 

* Tue Mar 27 2002 Theodore Roth <troth@verinet.com>
- dir directive for %{_prefix}/avr/{bin,lib}

* Mon Mar 17 2002 Theodore Roth <troth@verinet.com>
- Initial spec file.

