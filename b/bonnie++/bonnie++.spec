Name: bonnie++
Version: 1.03e
Release: alt1

Summary: A program for benchmarking hard drives and filesystems
License: GPL v2
Group: Monitoring

Url: http://www.coker.com.au/bonnie++/
Source: %name-%version.tgz
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Fri Apr 23 2004
BuildRequires: gcc-c++ libstdc++-devel

Summary(ru_RU.KOI8-R): Тест скорости работы жестких дисков и файловых систем

%description
Bonnie++ is a benchmark suite that is aimed at performing a number
of simple tests of hard drive and file system performance.

%description -l ru_RU.KOI8-R
Bonnie++ - тест скорости работы вашей дисковой подсистемы

%prep
%setup

%build
%configure
%make_build

%install
[ -e debian/changelog ] && (rm -f changelog.txt; mv debian/changelog changelog.txt)
subst "s@usr/share/man@%buildroot%_mandir@g" Makefile
%makeinstall eprefix=%buildroot/%prefix DESTDIR=%buildroot
ln -s ../sbin/%name %buildroot/%_bindir/

%files
%_bindir/*
%_sbindir/*
%_mandir/man?/*
%doc copyright.txt credits.txt readme.html

%changelog
* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.03e-alt1
- 1.03e: added direct io support

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 1.03d-alt1
- 1.03d

* Sat Nov 10 2007 Michael Shigorin <mike@altlinux.org> 1.03a-alt3
- added symlink to %name from %_bindir/ (#12348)
  (zcav left in %_sbindir/ only since it's going to work
  with disk block devices hence run as root)

* Wed Apr 18 2007 Michael Shigorin <mike@altlinux.org> 1.03a-alt2
- adopted the package
- clarified License: (#11480)

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.03a-alt1.1
- Rebuilt with libstdc++.so.6.

* Fri Apr 23 2004 Anton Farygin <rider@altlinux.ru> 1.03a-alt1
- 1.03a

* Mon Jan 20 2003 Rider <rider@altlinux.ru> 1.02c-alt2
- build requires fix

* Mon Sep 16 2002 Rider <rider@altlinux.ru> 1.02c-alt1
- 1.02c

* Thu Jan 03 2002 Rider <rider@altlinux.ru> 1.02a-alt1
- 1.02a

* Sun Sep 16 2001 Rider <rider@altlinux.ru> 1.01d-alt1
- 1.01d

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.00f-ipl1mdk
- FHSification.
- RE adaptions.

* Tue Dec 12 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.00f-1mdk
- new in contribs

* Wed Sep 06 2000 Rob Latham <rlatham@plogic.com>
- first packaging
