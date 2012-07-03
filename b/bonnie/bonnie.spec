Name: bonnie
Version: 1.4
Release: alt3

Summary: Unix filesystem performance benchmark
License: Artistic
Group: System/Kernel and hardware

URL: http://www.garloff.de/kurt/linux/bonnie
Source: %url/bonnie-%version.tar.bz2

%description
bonnie is a classic file system and storage device benchmark. It tests
for linear character-based and block-based reads and writes, and the
rewrite pattern. It also does a seek test. While other benchmarks do
more sophisticated tests, bonnie is a very reliable and portable program
that is suitable for basic testing. Optionally, you can test the
operations with direct I/O (O_DIRECT on Linux).

%prep
%setup -n bonnie

%build
%__subst 's|asm/page.h|sys/user.h|' Bonnie.c
%make CFLAGS="%optflags"

%install
install -pD -m755 Bonnie %buildroot%_bindir/bonnie
install -pD -m644 bonnie.1 %buildroot%_man1dir/bonnie.1

%files
%_bindir/*
%_man1dir/*
%doc bonnie.doc README

%changelog
* Mon Feb 18 2008 Victor Forsyuk <force@altlinux.org> 1.4-alt3
- Include sys/user.h for PAGE_MASK definition due to unexported
  asm/page.h in glibc-kernheaders-2.6.18-alt4.

* Fri Apr 13 2007 Victor Forsyuk <force@altlinux.org> 1.4-alt2
- Fix "License:" value: license is Artistic, not just distributable.

* Wed May 11 2005 Victor Forsyuk <force@altlinux.ru> 1.4-alt1
- New version from new maintainer.
- Better description (taken from freshmeat project page).

* Fri Oct 04 2002 Rider <rider@altlinux.ru> 1.0-ipl9mdk
- Rebuild

* Tue Mar 26 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-ipl8mdk
- Rebuilt

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl7mdk
- RE and Fandra adaptions.

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0-6mdk
- group fix

* Sun Nov 28 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Fix group

* Thu Nov 11 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- initial release.
