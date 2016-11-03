%define _pseudouser_user     _radvd
%define _pseudouser_group    _radvd
%define _pseudouser_home     %_localstatedir/radvd

%define _unpackaged_files_terminate_build 1

Name: radvd
Version: 2.15
Release: alt1

Summary: A Router Advertisement daemon
# The code includes the advertising clause, so it's GPL-incompatible
License: BSD with advertising
Group: System/Servers

Url: http://www.litech.org/radvd/
# git://github.com/reubenhwk/radvd.git
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Source3: %name-tmpfs.conf
Patch: %name-%version-%release.patch

BuildRequires: libcheck-devel
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
%patch -p1

%build
%autoreconf
%add_optflags -fno-strict-aliasing -fno-strict-overflow
%configure \
	--with-pidfile=/var/run/radvd/radvd.pid \
	--with-systemdsystemunitdir=%systemd_unitdir
%make_build

#check
#make check

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_initdir
mkdir -p %buildroot/var/run/radvd

install -m 644 redhat/radvd.conf.empty %buildroot%_sysconfdir/radvd.conf
install -m 755 %SOURCE1 %buildroot%_initdir/radvd
install -m 644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/radvd
install -Dm0644 %SOURCE3 %buildroot%_sysconfdir/tmpfiles.d/%name.conf

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
%config %_sysconfdir/tmpfiles.d/%name.conf
%config %systemd_unitdir/%name.service
%_initdir/%name
%dir %attr(0771,root,%_pseudouser_group) /var/run/radvd/
%doc radvd.conf.example
%_mandir/*/*
%_sbindir/radvd
%_sbindir/radvdump

%changelog
* Thu Nov 03 2016 Mikhail Efremov <sem@altlinux.org> 2.15-alt1
- Use service file from upstream.
- radvd.service: Use sysconfig file.
- Updated to 2.15.

* Mon Jul 18 2016 Mikhail Efremov <sem@altlinux.org> 2.14-alt1
- Updated to 2.14.

* Thu Apr 28 2016 Mikhail Efremov <sem@altlinux.org> 2.13-alt1
- Updated to 2.13.

* Fri Feb 12 2016 Mikhail Efremov <sem@altlinux.org> 2.12-alt1
- Updated to 2.12.

* Fri Jan 23 2015 Mikhail Efremov <sem@altlinux.org> 2.10-alt1
- Updated to 2.10.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 2.9-alt1
- Updated to 2.9.

* Mon Oct 06 2014 Mikhail Efremov <sem@altlinux.org> 2.8-alt1
- Add -fno-strict-overflow to %%optflags.
- Add -fno-strict-aliasing to %%optflags.
- Updated to 2.8.

* Mon Sep 15 2014 Mikhail Efremov <sem@altlinux.org> 2.7-alt1
- Updated to 2.7.

* Wed Sep 10 2014 Mikhail Efremov <sem@altlinux.org> 2.6-alt1
- Updated to 2.6.

* Tue Aug 05 2014 Mikhail Efremov <sem@altlinux.org> 2.5-alt1
- Updated to 2.5.

* Fri Aug 01 2014 Mikhail Efremov <sem@altlinux.org> 2.4-alt2
- Disable tests.

* Fri Aug 01 2014 Mikhail Efremov <sem@altlinux.org> 2.4-alt1
- Enable tests.
- Updated to 2.4.

* Wed Jul 23 2014 Mikhail Efremov <sem@altlinux.org> 2.1-alt1
- Updated to 2.1.

* Fri Mar 21 2014 Mikhail Efremov <sem@altlinux.org> 1.10.0-alt1
- Updated to 1.10.0.

* Tue Mar 04 2014 Mikhail Efremov <sem@altlinux.org> 1.9.9-alt1
- Updated to 1.9.9.

* Tue Jan 14 2014 Mikhail Efremov <sem@altlinux.org> 1.9.8-alt1
- Updated to 1.9.8.

* Fri Nov 22 2013 Mikhail Efremov <sem@altlinux.org> 1.9.7-alt1
- Updated to 1.9.7.

* Tue Nov 19 2013 Mikhail Efremov <sem@altlinux.org> 1.9.6-alt1
- Updated to 1.9.6.

* Thu Oct 03 2013 Mikhail Efremov <sem@altlinux.org> 1.9.5-alt1
- Updated to 1.9.5.

* Tue Oct 01 2013 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt1
- Updated to 1.9.4.

* Tue Apr 02 2013 Mikhail Efremov <sem@altlinux.org> 1.9.3-alt1
- Add systemd support.
- Updated to 1.9.3.

* Thu Dec 20 2012 Mikhail Efremov <sem@altlinux.org> 1.9.2-alt1
- Updated to 1.9.2.

* Tue Oct 23 2012 Mikhail Efremov <sem@altlinux.org> 1.9.1-alt1
- Updated to 1.9.1 (closes: #27883).

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
