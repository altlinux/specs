%define diethome %_prefix/lib/%name

Name: dietlibc
%define cvsdate 20121030
Version: 0.33
Release: alt0.1
Summary: C library optimized for size
License: GPLv2+
Group: Development/C
Url: http://www.fefe.de/%name/
%if %cvsdate
Source: %name-cvs-%cvsdate.tar
%else
Source: ftp://ftp.kernel.org/pub/linux/libs/%name/%name-%version.tar
%endif
Source1: %name-Makefile.rules
Patch: %name-%version-%release.patch

%description
Small libc for building embedded applications.


%prep
%if %cvsdate
%setup -n %name-cvs-%cvsdate
%else
%setup
%endif
%patch -p1


%build
%add_optflags -fno-stack-protector -U_FORTIFY_SOURCE

DisableFeatures()
{
local F
for F in $@; do
	sed -i -r -e '/^#[[:blank:]]*define[[:blank:]]+WANT_'"$F"'[[:blank:]]*$/s|^.*$|/* & */|' dietfeatures.h
done
}

EnableFeatures()
{
local F
for F in $@; do
	sed -i -r -e '/^\/\*[[:blank:]]*#[[:blank:]]*define[[:blank:]]+WANT_'"$F"'[[:blank:]]*\*\/$/s|^.*(#.*)[[:blank:]]*\*\/|\1|' \
	          -e 's/[[:blank:]]*$//' dietfeatures.h
done
}

DisableFeatures \
	FASTER_STRING_ROUTINES \
	LLMNR \
	VALGRIND_SUPPORT \
	FREAD_OPTIMIZATION \
	LD_SO_GDB_SUPPORT \
	IPV6_DNS \
	HIGH_PRECISION_MATH \
	SSP \
	STACKGAP
EnableFeatures \
	MALLOC_ZERO

%make_build CC="%__cc %optflags" prefix=%diethome
gzip -9c CHANGES > CHANGES.gz


%install
%make_install prefix=%diethome BINDIR=%_bindir MAN1DIR=%_man1dir DESTDIR=%buildroot install
install -p -m 0644 %SOURCE1 %buildroot%diethome/Makefile.rules


%files
%doc AUTHOR BUGS CAVEAT CHANGES.* FAQ PORTING README* THANKS SECURITY TODO
%_bindir/*
%_man1dir/*
%diethome


%changelog
* Thu Nov 08 2012 Led <led@altlinux.ru> 0.33-alt0.1
- CVS 20121030
- fixed Url

* Tue Apr 26 2011 Led <led@altlinux.ru> 0.33-cx0.1
- CVS 20110303
- err(), errx(), verr(), verrx(), warn(), warnx(), vwarn(), vwarnx() moved
  from libcompat into main lib
- features.h: add include sys/cdefs.h

* Wed May 05 2010 Led <led@altlinux.ru> 0.33-tmc0.6
- getdelim(), mempcpy(), getdelim(), getline() moved into main lib

* Thu Apr 01 2010 Led <led@altlinux.ru> 0.33-tmc0.5
- CVS 20100320

* Tue Mar 09 2010 Led <led@altlinux.ru> 0.33-tmc0.4
- in.h: define IPV6_V6ONLY

* Tue Feb 23 2010 Led <led@altlinux.ru> 0.33-tmc0.3
- CVS 20100209
- diet.c: change default gcc options for i386 and x86_64

* Fri Jan 29 2010 Led <led@altlinux.ru> 0.33-tmc0.2
- enabled:
  + MALLOC_ZERO
- disabled:
  + FASTER_STRING_ROUTINES
  + STACKGAP

* Sun Jan 24 2010 Led <led@altlinux.ru> 0.33-tmc0.1
- CVS 20100119

* Fri Jan 22 2010 Led <led@altlinux.ru> 0.32-tmc2
- stdint.h: add limits macros

* Thu Jan 21 2010 Led <led@altlinux.ru> 0.32-tmc1
- 0.32
- cleaned up spec

* Wed Sep 03 2008 Led <led@altlinux.ru> 0.31-alt0.2
- added %name-0.31-x86_64-lseek64.patch

* Wed Nov 21 2007 Led <led@altlinux.ru> 0.31-alt0.1
- 0.31
- updated dietlibc-0.31-avx-fix_no_ipv6.patch
- removed dietlibc-0.30-alt-fstatfs64-typo.patch
- disabled dietlibc-0.27-x86_64-lseek64.patch
- cleaned up spec

* Sat Feb 03 2007 Sergey Vlasov <vsu@altlinux.ru> 0.30-alt3
- diet wrapper: Add -fno-stack-protector to compiler options for gcc >= 4.
  Version is determined either from the compiler name (gcc-<version>) or
  from the GCC_VERSION environment variable.  Fixes #10357 and similar
  problems in other packages using dietlibc without adding workarounds to
  all these packages.

* Sun Jan 07 2007 Sergey Vlasov <vsu@altlinux.ru> 0.30-alt2
- Build with -fno-stack-protector (dietlibc-0.30 does not initialize TLS, which
  is required for stack-protector code with current gcc).
- Added alt-getmntent_r patch: implement getmntent_r() function which is
  required for new busybox.

* Wed Aug 30 2006 L.A. Kostis <lakostis@altlinux.ru> 0.30-alt1.1
- update x86_64-lseek64.patch (fixes #9939).

* Mon Aug 28 2006 L.A. Kostis <lakostis@altlinux.ru> 0.30-alt1
- 0.30
- Update alt-config patch (compile with WANT_STACKGAP)
- Fix fstatfs64 w/o LARGEFILE_BACKCOMPAT
- Add some patches from Fedora:
  + made nice(2) SUSv3 compliantly on x86_64 and other platforms
  + catch the case when syscall(2) is used on archs where it is 
    not implemented yet
- Remove obsoleted MDK patches.

* Wed Jun 14 2006 LAKostis <lakostis at altlinux.org> 0.29-alt1
- NMU:
- 0.29
- Update biarch and alt-config patch.
- Add ipv6 patch from Annvix.
- Remove obsoleted patches.
- Add missing docs.

* Thu Apr 14 2005 Anton D. Kachalov <mouse@altlinux.org> 0.28-alt1
- 0.28
- added syscall code for x86_64

* Thu Feb 17 2005 Anton D. Kachalov <mouse@altlinux.org> 0.27-alt2
- multilib support

* Thu Jan 20 2005 Kachalov Anton <mouse@altlinux.ru> 0.27-alt1
- 0.27
- new improved signal implementation for i386 to work with execshield (RH)
- support __nonnull attribute (RH)

* Mon Jul 26 2004 Kachalov Anton <mouse@altlinux.ru> 0.23-alt1
- Updated to 0.23

* Thu May 01 2003 Dmitry V. Levin <ldv@altlinux.org> 0.22-alt1
- Updated to 0.22
- Disabled few useless (at this moment) features.
- Applied xdr fix from cvs (CAN-2003-0028).
- Applied 3 minor fixes from mdk.

* Tue Oct 29 2002 Dmitry V. Levin <ldv@altlinux.org> 0.21-alt1
- Updated to 0.21
- Our ix86-warnings fixes merged upstream.

* Mon Aug 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.20-alt1
- 0.20.

* Fri Aug 09 2002 Dmitry V. Levin <ldv@altlinux.org> 0.19-alt1
- 0.19.
- Fixed FPE errors introduced in integer overflow fixes.

* Tue Jul 16 2002 Dmitry V. Levin <ldv@altlinux.org> 0.18-alt1
- 0.18.
- Fixed getline declaration.

* Mon May 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.17-alt1
- 0.17.

* Fri Feb 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.15-alt1
- 0.15.

* Tue Jan 29 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.14-alt1
- 0.14.

* Sat Jan 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.13-alt2
- Fixed compilation warnings in dirent.h, stddef.h and string.h

* Thu Jan 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.13-alt1
- Initial revision.
