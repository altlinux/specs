Name: ipv6calc
Version: 0.93.1
Release: alt1

Summary: IPv6 address format change and calculation utility
License: GPLv2
Group: Networking/Other
URL: http://www.deepspace6.net/projects/%name.html
# ftp://ftp.bieringer.de/pub/linux/IPv6/%name/%name-version.tar.gz
Source: %name-%version.tar
Conflicts: iputils < 20020124-alt5
%{?!_without_check:%{?!_disable_check:BuildRequires: perl-Digest-SHA1 perl-URI}}

%description
ipv6calc is a small utility which formats and calculates IPv6 addresses
in different ways.

%prep
%setup
iconv -fiso88591 -tutf8 -o CREDITS{,}

%build
%configure
%make_build

%install
%makeinstall_std

# Move ipv6calc
mkdir -p %buildroot/bin
mv %buildroot%_bindir/ipv6calc %buildroot/bin/

## Install examples and helper files
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir

# docs
cp -p ChangeLog README CREDITS TODO LICENSE USAGE doc/ipv6calc.html \
	%buildroot%docdir/

# ipv6logconv
mkdir -p %buildroot%docdir/ipv6logconv
cp -pr examples/analog/* %buildroot%docdir/ipv6logconv/

# ipv6loganon
mkdir -p %buildroot%docdir/ipv6loganon
cp -p ipv6loganon/README %buildroot%docdir/ipv6loganon/

# ipv6logstats
mkdir -p %buildroot%docdir/ipv6logstats
cd ipv6logstats
cp -pr examples-* example_* collect_ipv6logstats.pl README \
	%buildroot%docdir/ipv6logstats/
cd -

# ipv6calcweb
mkdir -p %buildroot%docdir/ipv6calcweb
cd ipv6calcweb
cp -p USAGE ipv6calcweb.cgi %buildroot%docdir/ipv6calcweb/
cd -

%check
%make_build -k test

%files
/bin/*
%_bindir/*
%_man8dir/*
%docdir/

%changelog
* Fri Apr 27 2012 Dmitry V. Levin <ldv@altlinux.org> 0.93.1-alt1
- Updated to 0.93.1.

* Tue Jan 17 2012 Dmitry V. Levin <ldv@altlinux.org> 0.92.0-alt1
- Updated to 0.92.0.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 0.80.0-alt1
- Updated to 0.80.0.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.45-alt1.1.1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.45-alt1.1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.45-alt1.1
- Rebuilt with openssl-0.9.7d.

* Thu Nov 21 2002 Kachalov Anton <mouse@altlinux.ru> 0.45-alt1
- 0.45

* Thu Apr 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.39-alt1
- Build as outstanding package.

* Tue Apr 02 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt4
- Disabled build of ipv6calc-static.
- Fixed build without kernel-source installed.

* Wed Mar 27 2002 Alexander Bokovoy <ab@altlinux.ru> 20020124-alt3
- Fixed:
    + tftpd removed from installation binaries 

* Mon Mar 25 2002 Alexander Bokovoy <ab@altlinux.ru> 20020124-alt2
- IPUtils ss020124
- IP6Calc 0.39
- Documentation now is built using SGML tools
- Various patches updated

* Thu Jan 03 2002 Stanislav Ievlev <inger@altlinux.ru> 20010805-alt2
- fixed rights on manual pages (bug  #0000292)
- fixed bonding with new interface ( 2.4.x )

* Tue Aug 14 2001 Alexander Bokovoy <ab@altlinux.ru>   20010805-alt1
- IPUtils ss010805
- Fixed: 
    + ping-deadline patch. Ping has been re-designed to eliminate this problem
    + Compiler options
    + Owl patch for ping

* Tue May 08 2001 Stanislav Ievlev <inger@altlinux.ru> 20001110-ipl2mdk
- Merge with patches from OpenWall, RH and MDK

* Fri Jan 12 2001 Dmitry V. Levin <ldv@fandra.org> 20001110-ipl1mdk
- ss001110.

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 20001011-ipl1mdk
- ss001011.
- RE adaptions.

* Tue Oct 10 2000 Jeff Johnson <jbj@redhat.com>
- update to ss001010.
- don't segfault as root with large buffers (#16677).

* Sun Oct  8 2000 Jeff Johnson <jbj@redhat.com>
- update to ss001007.

* Tue Aug  8 2000 Tim Waugh <twaugh@redhat.com>
- fix spelling mistake (#15714).

* Tue Aug  8 2000 Tim Waugh <twaugh@redhat.com>
- turn on -U on machines without TSC (#15223).

* Tue Aug  1 2000 Jeff Johnson <jbj@redhat.com>
- better doco patch (#15050).

* Tue Jul 25 2000 Jakub Jelinek <jakub@redhat.com>
- fix include-glibc/ to work with new glibc 2.2 resolver headers

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- update to ss000418.
- perform reverse DNS lookup only once for same input.

* Sun Mar  5 2000 Jeff Johnson <jbj@redhat.com>
- include README.ifenslave doco.
- "ping -i N" was broke for N >= 3 (#9929).
- update to ss000121:
-- clockdiff: preserve raw socket errno.
-- ping: change error exit code to 1 (used to be 92,93, ...)
-- ping,ping6: if -w specified, transmit until -c limit is reached.
-- ping,ping6: exit code non-zero if some packets not received within deadline.

* Tue Feb 22 2000 Jeff Johnson <jbj@redhat.com>
- man page corrections (#9690).

* Wed Feb  9 2000 Jeff Johnson <jbj@jbj.org>
- add ifenslave.

* Thu Feb  3 2000 Elliot Lee <sopwith@redhat.com>
- List /usr/sbin/rdisc in %files list.

* Thu Jan 27 2000 Jeff Johnson <jbj@redhat.com>
- add remaining binaries.
- casts to remove compilation warnings.
- terminate if -w deadline is reached exactly (#8724).

* Fri Dec 24 1999 Jeff Johnson <jbj@redhat.com>
- create (only ping for now, traceroute et al soon).
