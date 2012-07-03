Name: trafshow
Version: 5.2.3
Release: alt2

Summary: A tool for real-time network traffic visualization
License: BSD
Group: Monitoring
Url: http://soft.risp.ru/trafshow/index.shtml

# real source: Source: ftp://ftp.nsk.su/pub/RinetSoftware/%name-%version.tgz
# is dead in time of 5.2.3-alt2
Source: ftp://ftp.nsk.su/pub/RinetSoftware/%name-%version.tar.gz
Patch1: %name-5-makefile.patch
Patch2: %name-3.1-alt-without-termcap.patch
Patch3:	%name-gcc44.patch
#Patch3: %name-4-linux.patch
Packager: Fr. Br. George <george@altlinux.ru>

#BuildPreReq: autoconf_2.13

# Automatically added by buildreq on Tue Feb 17 2004
BuildRequires: libncurses-devel libpcap-devel libtinfo-devel

%description
TrafShow continuously display the information regarding packet traffic
on the configured network interface that match the boolean expression.
It periodically sorts and updates this information.

This funny program may be useful for locating suspicious network
traffic on the net or to evaluate current utilization of the network
interface.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
# this is from PLD. What for?
#sed -i 's/static//' screen.c

%build
%set_autoconf_version 2.13
autoconf
%configure
%make_build CCOPT="%optflags"

%install
%makeinstall DESTDIR=%buildroot

%files
%doc INSTALL README
%config %_sysconfdir/%name
%_bindir/*
%_mandir/man?/*

%changelog
* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 5.2.3-alt2
- GCC44 fixup build

* Thu Nov 16 2006 Fr. Br. George <george@altlinux.ru> 5.2.3-alt1
- Version up

* Fri Jun 04 2004 Fr. Br. George <george@altlinux.ru> 4.0-alt2
- Packager field changed

* Tue Feb 17 2004 Fr. Br. George <george@altlinux.ru> 4.0-alt1
- Version upgrade, patches fixed

* Tue Nov 04 2003 Konstantin Timoshenko <kt@altlinux.ru> 3.1-alt3
- added DLT_LINUX_SLL patch from Andy Pershin <apa@puug.org.ru>

* Sat Jan 25 2003 Michael Shigorin <mike@altlinux.ru> 3.1-alt2.1
- small spec cleanup (autoconf version fixed)
- rebuild in actual environment

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.1-alt2
- Fixed compile and link options.
- Rebuilt with libpcap-0.7.1.

* Tue Oct 30 2001 Konstantin Timoshenko <kt@altlinux.ru> 3.1-alt1
- initial specfile
- bzip sources
