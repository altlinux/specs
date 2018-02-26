%define _pseudouser_user     _radvd
%define _pseudouser_group    _radvd
%define _pseudouser_home     %_localstatedir/radvd

Name: radvd
Version: 1.8.2
Release: alt1

Summary: A Router Advertisement daemon
# The code includes the advertising clause, so it's GPL-incompatible
License: BSD with advertising
Group: System/Servers

Url: http://www.litech.org/radvd/
#Source: http://www.litech.org/radvd/dist/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig

BuildRequires: flex, byacc

%description
radvd is the router advertisement daemon for IPv6.  It listens to router
solicitations and sends router advertisements as described in "Neighbor
Discovery for IP Version 6 (IPv6)" (RFC 2461).  With these advertisements
hosts can automatically configure their addresses and some other
parameters.  They also can choose a default router based on these
advertisements.

Install radvd if you are setting up IPv6 network and/or Mobile IPv6
services.

%prep
%setup

%build
%configure --with-pidfile=/var/run/radvd/radvd.pid
%make
# make %{?_smp_mflags}
# Parallel builds still fail because seds that transform y.tab.x into
# scanner/gram.x are not executed before compile of scanner/gram.x
#

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_initdir
mkdir -p %buildroot/var/run/radvd

install -m 644 redhat/radvd.conf.empty %buildroot%_sysconfdir/radvd.conf
install -m 755 %SOURCE1 %buildroot%_initdir/radvd
install -m 644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/radvd

%post
%post_service %name

%preun
%preun_service %name

%pre
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'radvd user' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%files
%doc COPYRIGHT README CHANGES INTRO.html TODO
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%dir %attr(0771,root,%_pseudouser_group) /var/run/radvd/
%doc radvd.conf.example
%_mandir/*/*
%_sbindir/radvd
%_sbindir/radvdump

%changelog
* Fri Oct 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.8.2-alt1
- 1.8.2. Security fixes:
  + CVE-2011-3601
  + CVE-2011-3602
  + CVE-2011-3603
  + CVE-2011-3604
  + CVE-2011-3605

* Fri Jan 21 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7-alt1
- 1.7.

* Wed Mar 17 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.6-alt1
- 1.6.

* Mon Feb 08 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.5-alt1
- Initial build for Sisyphus (based on spec by Pekka Savola <pekkas@netcore.fi>)
