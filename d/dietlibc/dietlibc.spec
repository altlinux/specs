Name: dietlibc
Version: 0.30
Release: alt3
%define diethome %_prefix/lib/%name

Summary: C library optimized for size
License: GPL
Group: Development/C
Url: http://www.fefe.de/%name/

Source: ftp://ftp.kernel.org/pub/linux/libs/%name/%name-%version.tar
Source1: %name-Makefile.rules

Patch1: %name-0.23-alt-getline.patch
Patch2: %name-0.27-alt-ioverflow.patch
Patch3: %name-0.30-alt-config.patch
Patch4: %name-0.27-alt-define.patch
Patch5: %name-0.30-alt-fstatfs64-typo.patch
Patch6: %name-0.30-alt-getmntent_r.patch
Patch7: %name-0.30-alt-no-stack-protector.patch

# MDK
Patch31: %name-0.29-biarch.patch
Patch32: %name-0.27-kernel2.6-types.patch
Patch33: %name-0.27-x86_64-lseek64.patch
Patch34: %name-0.27-x86_64-stat64.patch

# Annvix
Patch60: %name-0.29-avx-fix_no_ipv6.patch

# Fedora
Patch80: %name-0.28-setpriority.patch
Patch81: %name-0.29-scall.patch

Packager: Anton D. Kachalov <mouse@altlinux.org>

%description
Small libc for building embedded applications.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1

%patch60 -p1

%patch80 -p1
%patch81 -p1

%build
%__subst 's,\-W\ ,-Wextra ,g' Makefile
%make_build CC="gcc -fno-stack-protector" prefix=%diethome

%install
%make_install install \
	prefix=%diethome \
	BINDIR=%_bindir \
	MAN1DIR=%_man1dir \
	DESTDIR=%buildroot

%__install -m644 %SOURCE1 %buildroot%diethome/Makefile.rules

%files
%_bindir/*
%_man1dir/*
%diethome
%doc AUTHOR BUGS CAVEAT CHANGES FAQ README README.* THANKS SECURITY

%changelog
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
