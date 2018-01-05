Summary: Small, fast daemon to serve DNSBLs
Name: rbldnsd
Version: 0.998
Release: alt1
License: GPLv2+
Group: System/Servers
Url: http://www.corpit.ru/mjt/rbldnsd.html
# http://git.corpit.ru/?p=rbldnsd.git
Source0: http://www.corpit.ru/mjt/rbldnsd/rbldnsd_%version.tar.gz
Source1: rbldnsd.init

BuildRequires: gawk, zlib-devel

Packager: L.A. Kostis <lakostis@altlinux.ru>

%description
Rbldnsd is a small, authoritative-only DNS nameserver designed to serve
DNS-based blocklists (DNSBLs). It may handle IP-based and name-based
blocklists.

%prep
%setup -n %name-%version
sed -i	-e 's@/var/lib/rbldns\([/ ]\)@%_localstatedir/rbldnsd\1@g' \
		-e 's@\(-r/[a-z/]*\) -b@\1 -q -b@g' debian/rbldnsd.default

%build
# this is not an autotools-generated configure script, and does not support --libdir
CFLAGS="%optflags" ./configure
%make_build

%install
mkdir -p %buildroot{%_sbindir,%_mandir/man8,%_initdir,%_sysconfdir/sysconfig}
mkdir -p %buildroot%_localstatedir/rbldnsd
install -m 755 rbldnsd			%buildroot%_sbindir
install -m 644 rbldnsd.8			%buildroot%_mandir/man8
install -m 644 debian/rbldnsd.default	%buildroot%_sysconfdir/sysconfig/rbldnsd
install -m 755 %SOURCE1			%buildroot%_initdir/rbldnsd

%pre
/usr/sbin/groupadd -r rbldns ||:
/usr/sbin/useradd -r -g rbldns -d %_localstatedir/lib/rbldnsd \
		  -s /dev/null -c "rbldns daemon" rbldns ||:

%post
%post_service rbldnsd

%preun
%preun_service rbldnsd

%files
%doc README.user NEWS TODO debian/changelog CHANGES-0.81
%_sbindir/rbldnsd
%_mandir/man8/rbldnsd.8*
%dir %_localstatedir/rbldnsd/
%config(noreplace) %_sysconfdir/sysconfig/rbldnsd
%_initdir/rbldnsd

%changelog
* Fri Jan 05 2018 L.A. Kostis <lakostis@altlinux.ru> 0.998-alt1
- updated to 0.998.
- added LSB header to ease systemd transition.

* Fri Jan 20 2012 L.A. Kostis <lakostis@altlinux.ru> 0.996b-alt1
- fix init.d/rbldnsd (add condstop/condstart).

* Wed Dec 07 2011 L.A. Kostis <lakostis@altlinux.ru> 0.996b-alt0.2
- Add Packager.

* Wed Nov 30 2011 L.A. Kostis <lakostis@altlinux.ru> 0.996b-alt0.1
- Rebuild for ALTLinux.

* Mon Mar 31 2008 Paul Howarth <paul@city-fan.org> 0.996b-1
- update to 0.996b
- _GNU_SOURCE no longer needed

* Wed Feb 20 2008 Paul Howarth <paul@city-fan.org> 0.996a-6
- fix exit codes for reload, stop, and try-restart actions of initscript

* Wed Feb 13 2008 Paul Howarth <paul@city-fan.org> 0.996a-5
- define _GNU_SOURCE for NI_MAXHOST symbol visibility
- LSB-ize initscript (#247043)

* Thu Aug 23 2007 Paul Howarth <paul@city-fan.org> 0.996a-4
- add buildreq gawk

* Thu Aug 23 2007 Paul Howarth <paul@city-fan.org> 0.996a-3
- upstream released a new version without changing the version number (the
  only changes are in debian/control and debian/changelog, neither of which
  are used in the RPM package)
- unexpand tabs in spec
- use the standard scriptlet for user/group creation in %%pre
- drop scriptlet dependencies on /sbin/service by calling initscript directly
- clarify license as GPL version 2 or later

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> 0.996a-2
- FE6 mass rebuild

* Fri Jul 28 2006 Paul Howarth <paul@city-fan.org> 0.996a-1
- update to 0.996a

* Tue Feb 21 2006 Paul Howarth <paul@city-fan.org> 0.996-1
- update to 0.996
- use /usr/sbin/useradd instead of %%{_sbindir}/useradd
- add buildreq zlib-devel to support gzipped zone files

* Wed Feb 15 2006 Paul Howarth <paul@city-fan.org> 0.995-5
- license text not included in upstream tarball, so don't include it

* Tue Jun 28 2005 Paul Howarth <paul@city-fan.org> 0.995-4
- include gpl.txt as %%doc

* Mon Jun 27 2005 Paul Howarth <paul@city-fan.org> 0.995-3
- fix /etc/sysconfig/rbldnsd references to /var/lib/rbldns to point to
  %%{_localstatedir}/lib/rbldnsd instead
- don't enable daemons in any runlevel by default
- add -q option to sample entries in /etc/sysconfig/rbldnsd

* Fri Jun 17 2005 Paul Howarth <paul@city-fan.org> 0.995-2
- first Fedora Extras build, largely based on upstream spec file
