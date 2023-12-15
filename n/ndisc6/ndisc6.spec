Name: ndisc6
Version: 1.0.7
Release: alt2

Summary: IPv6 diagnostic tools
License: GPLv2+
Group: System/Configuration/Networking

URL: https://www.remlab.net/ndisc6/
Vcs: https://git.remlab.net/git/ndisc6.git
Source: %name-%version.tar
Source1: rdnssd.init
Source2: rdnssd.tmpfiles
Source3: rdnssd.service
Patch: %name-%version-%release.patch

%define _unpackaged_files_terminate_build 1
%set_verify_elf_method strict

%description
This package gathers a few diagnostic tools for IPv6 networks:
 - ndisc6, which performs ICMPv6 Neighbor Discovery in userland,
 - rdisc6, which performs ICMPv6 Router Discovery in userland,
 - rltraceroute6, yet another IPv6 implementation of traceroute,
 - tcptraceroute6, a TCP/IPv6-based traceroute implementation,
 - tracert6, a ICMPv6 Echo Request based traceroute,
 - tcpspray6, a TCP/IP Discard/Echo bandwidth metter.

%package -n rdnssd
Summary: Recursive DNS Servers discovery Daemon
Group: System/Configuration/Networking

%description -n rdnssd
rdnssd autoconfigures the list of DNS servers through slateless IPv6
autoconfiguration (RFC5006).

%prep
%setup
%patch -p1

%build
#Hack for gettext_noop mainly
find /usr/share/gettext -name gettext.h -exec ln -s '{}' include/gettext.h ';' -quit

%autoreconf
%add_optflags %(getconf LFS_CFLAGS)
CFLAGS="%optflags -fno-strict-aliasing" \
%configure \
	--localstatedir=%_var \
	--disable-suid-install

%make_build

%install
%makeinstall_std
%find_lang %name
touch %buildroot/%_runtimedir/rdnssd/resolv.conf
install -Dm0755 %SOURCE1 %buildroot%_initdir/rdnssd
install -Dm0644 %SOURCE2 %buildroot%_tmpfilesdir/rdnssd.conf
install -Dm0644 %SOURCE3 %buildroot%systemd_unitdir/rdnssd.service

%pre -n rdnssd
groupadd -r -f rdnssd
useradd -r -g rdnssd -d %_runtimedir/rdnssd -s /dev/null -N rdnssd >/dev/null 2>&1 ||:

%post -n rdnssd
%post_service rdnssd

%preun -n rdnssd
%preun_service rdnssd

%files -f %name.lang
%doc NEWS README
%_sbindir/*
%_bindir/*
%_man1dir/*
%_man8dir/*
%exclude %_sbindir/rdnssd
%exclude %_man8dir/rdnssd.8.*

%files -n rdnssd
%_initdir/rdnssd
%_tmpfilesdir/rdnssd.conf
%systemd_unitdir/rdnssd.service
%_sysconfdir/rdnssd
%_sbindir/rdnssd
%_man8dir/rdnssd.8.*
%attr(755,rdnssd,rdnssd) %dir %_runtimedir/rdnssd
%ghost %_runtimedir/rdnssd/resolv.conf

%changelog
* Fri Dec 15 2023 Mikhail Efremov <sem@altlinux.org> 1.0.7-alt2
- Patch from upstream:
  + Fix reading uninitialized memory when parsing PREF64.

* Wed Apr 05 2023 Mikhail Efremov <sem@altlinux.org> 1.0.7-alt1
- Enabled LFS on 32-bit systems.
- Added 'set_verify_elf_method strict'.
- Updated to 1.0.7.

* Wed Aug 03 2022 Mikhail Efremov <sem@altlinux.org> 1.0.6-alt1
- Updated to 1.0.6.

* Tue Jan 11 2022 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1
- Added Vcs tag.
- Don't use rpm-build-licenses.
- Updated to 1.0.5.

* Mon Jan 14 2019 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt2
- Updated to 1.0.4 release.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1.git4c794b5512d2.qa1
- NMU: applied repocop patch

* Wed Oct 03 2018 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1.git4c794b5512d2
- Minor spec cleanup.
- Use _unpackaged_files_terminate_build.
- Upstream git snapshot.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt2
- Allow build with gettext-0.18.3.
- Updated to 1.0.3 release.

* Fri Sep 12 2014 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1.git20140907
- Updated from upstream git.

* Tue Apr 09 2013 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt3.git20121003
- Fix build with new gettext.

* Thu Jan 24 2013 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt2.git20121003
- Added rdnssd.service for systemd.
- Fix owner of /var/run/rdnssd directory (closes: #28430).

* Fri Oct 12 2012 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.git20121003
- Updated from upstream git.

* Tue Jul 17 2012 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.git20120603
- rdnssd: Add resolvconf support.
- Initial build.

