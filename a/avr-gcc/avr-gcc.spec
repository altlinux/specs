# -*- rpm-spec -*-
# $Id: avr-gcc,v 1.14 2003/09/05 12:16:22 grigory Exp $

#define snapshot_version 20030512
%define cross_arch avr

Summary: GNU Compiler for AVR (C language only).
Name: %cross_arch-gcc
Version: 4.5.1
Release: alt3

Copyright: GPL
Group: Development/Other
URL: http://gcc.gnu.org

Source0: gcc-core-%version.tar.bz2
Source1: gcc-g++-%version.tar.bz2
Patch0: avr-gcc-4.5.0-new_devices.patch
Patch1: avr-gcc-4.5.1-register-fix.patch
Patch2: gcc-atmega2560-usart23.patch

# Automatically added by buildreq on Thu Oct 24 2002
BuildRequires: avr-binutils flex

BuildRequires: avr-binutils >= 2.20-alt1
BuildRequires: zlib-devel libmpc-devel libmpfr-devel libgmp-devel
Requires: avr-binutils >= 2.20-alt1

%define libavrdir /usr/lib/gcc/%cross_arch
%define libavrexecdir /usr/libexec/gcc/%cross_arch
%define includeavrdir %_includedir/%cross_arch


%description
The avr-gcc package contains the GNU Compiler Collection version 3.0 for the
Atmel AVR target.

%package c++
Summary: C++ support for gcc for AVR
Group: Development/Other
Requires: avr-gcc = %version-%release

%description c++
This package adds C++ support to the GNU C compiler version 3.0 for the Atmel
AVR target.

WARNING - This is still fairly experimental and only supports c++ programming
on the mega128 devices.


%prep
%setup -q -n gcc-%version
%setup -q -T -D -b 1 -n gcc-%version
%patch0 -p0
%patch1 -p1
%patch2 -p1
contrib/gcc_update --touch

#cd %_builddir/gcc-%version/gcc


%build
echo "" > gcc/cp/g++.1
%__mkdir obj-avr-%_target_platform
cd obj-avr-%_target_platform

#remove_optflags optflags_nocpp optflags_notraceback
#CC=%__cc \
#        CFLAGS="$RPM_OPT_FLAGS" \
#        CXXFLAGS="$RPM_OPT_FLAGS" \
#        GCJFLAGS="$RPM_OPT_FLAGS" \
#        XCFLAGS="$RPM_OPT_FLAGS" \
#        TCFLAGS="$RPM_OPT_FLAGS" \
#

# %optflags_default
CC="%__cc $RPM_OPT_FLAGS" \
	../configure \
		--target=%cross_arch \
		--enable-languages="c,c++" \
		--disable-nls \
		--disable-libssp \
		--prefix=%_prefix \
		--mandir=%_mandir \
		--infodir=%_infodir \
		--with-system-zlib \
		--enable-version-specific-runtime-libs \
		--with-pkgversion="ALT Linux %version-%release" \
		--with-bugurl="http://bugzilla.altlinux.org" \
		--with-objcopy=%_bindir/avr-objcopy \
		--enable-target-optspace \
		--with-as=%_bindir/avr-as \
		--with-ld=%_bindir/avr-ld \
		--with-ar=%_bindir/avr-ar \
		--with-nm=%_bindir/avr-nm \

#		--includedir=%includeavrdir \
#		--exec-prefix=%_libdir \
#		--libdir=%_libdir \
#		--libexecdir=/usr/lib/avr/bin


#		--libexecdir=/usr/libexec \
#		--with-as=%libavrdir/bin/as \
#		--with-ld=%libavrdir/bin/ld
%make_build


%install
%__mkdir_p %buildroot%_bindir
cd obj-avr-%_target_platform
# TARGET_PLATFORM=%_target_platform
echo timestamp > gcc/cstamp-h

%make_build DESTDIR=%buildroot install
#	prefix=%buildroot%_prefix \
#	exec_prefix=%buildroot%_libdir \
#	libdir=%buildroot%_libdir \
#	libexecdir=%buildroot/usr/libexec \
#	includedir=%buildroot%includeavrdir \
#	mandir=%buildroot%_mandir \
#	infodir=%buildroot%_infodir install

rename cpp.1 %cross_arch-cpp.1 %buildroot%_man1dir/*
rename gcov.1 %cross_arch-gcov.1 %buildroot%_man1dir/*
%__rm -f %buildroot%_man1dir/%cross_arch-g++*

#%__mv %buildroot%_libdir/bin/* %buildroot%_bindir/
%__ln_s -f %cross_arch-gcc.1.bz2 %buildroot%_man1dir/%cross_arch-g++.1.bz2
%__ln_s -f %cross_arch-gcc %buildroot%_bindir/%cross_arch-gcc-%version
%__ln_s -f %cross_arch-c++ %buildroot%_bindir/%cross_arch-g++

rename avr-avr avr %buildroot%_man1dir/*
%__rm -rf %buildroot{%_infodir,%_man7dir} %buildroot%libavrdir/libiberty.a %buildroot%_libdir/libiberty.a %buildroot%libavrdir/%version/plugin

# Copy specs file to /usr/lib/avr/gcc/avr/*/
%__cp %_builddir/gcc-%version/obj-avr-%_target_platform/gcc/specs %buildroot%libavrdir/%version/

%files
%doc gcc/README* gcc/*ChangeLog*
%dir %libavrexecdir
%dir %libavrexecdir/%version
%dir %libavrexecdir/%version/install-tools

%_bindir/*-cpp
%_bindir/*-gcc*
%_bindir/*-gcov
%libavrdir/%version/avr*
%libavrdir/%version/include*
%libavrdir/%version/libgcc.a
%libavrdir/%version/libgcov.a
%libavrdir/%version/specs
%libavrdir/%version/install-tools*
%libavrexecdir/%version/cc1
%libavrexecdir/%version/collect2
%libavrexecdir/%version/lto-wrapper
%libavrexecdir/%version/install-tools/*
%_man1dir/avr-gcc.1*
%_man1dir/avr-cpp.1*
%_man1dir/avr-gcov.1*
#%_infodir/avr*

%files c++
%_bindir/*-*++*
%libavrexecdir/%version/cc1plus
%_man1dir/avr-g++.1*

%changelog
* Thu Mar 17 2011 Grigory Milev <week@altlinux.ru> 4.5.1-alt3
- added patch for fix problem with USART2 and USART3 on atmega2560

* Thu Jan 13 2011 Grigory Milev <week@altlinux.ru> 4.5.1-alt2
- rebuild with new binutils
- fixed configure scripts

* Wed Nov 03 2010 Grigory Milev <week@altlinux.ru> 4.5.1-alt1
- new version released
- gcc moved to /usr/lib/gcc/avr and /usr/lib/libexec/gcc/avr

* Wed Dec 02 2009 Grigory Milev <week@altlinux.ru> 4.2.2-alt2
- fix build requires

* Wed Jan 09 2008 Grigory Milev <week@altlinux.ru> 4.2.2-alt1
- New version released

* Wed Sep 21 2005 Grigory Milev <week@altlinux.ru> 3.4.4-alt1
- New version released

* Fri Sep  5 2003 Grigory Milev <week@altlinux.ru> 3.3.1-alt1
- 3.3.1 released

* Thu Jun 19 2003 Grigory Milev <week@altlinux.ru> 3.3-alt1.20030512
- new cvs snapshot released

* Tue Apr 22 2003 Grigory Milev <week@altlinux.ru> 3.3-alt1.20030414
- new cvs snapshot released

* Mon Feb 10 2003 Grigory Milev <week@altlinux.ru> 3.2.75-alt2
- new version (snapshot 20030203)

* Tue Nov  5 2002 Grigory Milev <week@altlinux.ru> 3.2.75-alt1.20021028
- new version (snapshot)

* Thu Oct 24 2002 Grigory Milev <week@altlinux.ru> 3.0.4-alt1
- Initial build for ALT Linux

* Tue Mar 17 2002 Theodore A. Roth <troth@verinet.com>
- Initial spec file.

