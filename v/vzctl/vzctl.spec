Name: vzctl
Version: 3.3
Release: alt1

Summary: OpenVZ Virtual Environments control utility
License: GPL
Group: System/Configuration/Other
Url: http://openvz.org/
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>

# http://download.openvz.org/utils/vzctl/%version/src/vzctl-%version.tar.bz2
Source: %name-%version.tar
Patch: %name-%version-alt.patch

# these reqs are for vz helper scripts
Requires: vzquota >= 2.7.0-4 ploop >= 1.1
Requires: network-config-subsystem
# vzmigrate
Requires: rsync

BuildRequires: setproctitle-devel ploop libploop-devel libxml2-devel

%define _pkgconfdir /etc/vz
%add_findreq_skiplist %_pkgconfdir/dists/scripts/*

%description
OpenVZ is an Operating System-level server virtualization solution, built
on Linux.  OpenVZ creates isolated, secure virtual private servers on a
single physical server enabling better server utilization and ensuring
that applications do not conflict.  Each VE performs and executes exactly
like a stand-alone server; VEs can be rebooted independently and have
root access, users, IP addresses, memory, processes, files, applications,
system libraries and configuration files.

This package contain the control tool to manipulate
OpenVZ Virtual Environments.

%prep
%setup
%patch -p1

%build
%autoreconf
%add_optflags -fno-strict-aliasing
%configure --enable-bashcomp --enable-logrotate --disable-silent-rules
%make_build

%install
%makeinstall_std install-altlinux
if [ %_initdir != /etc/init.d ]; then
	mkdir -p `dirname %buildroot%_initdir`
	mv %buildroot/etc/init.d %buildroot%_initdir
fi
chmod 700 %buildroot%_pkgconfdir
chmod 710 %buildroot/var/lib/vz
chmod 700 %buildroot/var/lib/vz/*
chmod 710 %buildroot/var/lib/vz/template
chmod 3770 %buildroot/var/lib/vz/template/cache

touch %buildroot/etc/sysconfig/vzeventd

%pre
/usr/sbin/groupadd -r -f _vzctl
if [ -L %_pkgconfdir/conf -a -d %_pkgconfdir/conf -a ! -e %_pkgconfdir/conf.rpmsave ]; then
	mv %_pkgconfdir/conf %_pkgconfdir/conf.rpmsave
	if [ "$(readlink %_pkgconfdir/conf.rpmsave)" = ../sysconfig/vz-scripts ]; then
		mkdir -p %_pkgconfdir/conf &&
		mv %_pkgconfdir/conf.rpmsave/* \
			%_pkgconfdir/conf/
	fi
fi

%post
rm -f /dev/vzctl
mknod -m 600 /dev/vzctl c 126 0
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add vz ||:
fi

%post_service vzeventd

# (Upgrading from <= vzctl-3.0.24)
# If vz is running and vzeventd is not, start it
if %_initddir/vz status >/dev/null 2>&1; then
	if ! %_initddir/vzeventd status >/dev/null 2>&1; then
		%_initddir/vzeventd start
	fi
fi
exit 0

%preun
%preun_service vz
%preun_service vzeventd

%files
%doc ChangeLog
%defattr(-,root,root,-)
%config %_initdir/*
%config(noreplace) /etc/logrotate.d/*
%_datadir/vzctl
%_sbindir/*
%_libdir/lib*
%_mandir/man?/*
%dir %_pkgconfdir
%dir %_pkgconfdir/names
%config(noreplace) %_pkgconfdir/vz.conf
%config(noreplace) %_pkgconfdir/download.conf
%config(noreplace) %_pkgconfdir/osrelease.conf
%ghost %config(noreplace) /etc/sysconfig/vzeventd
%config %_pkgconfdir/conf
%config %_pkgconfdir/dists
%config /etc/sysconfig/network-scripts/*
%config /etc/net/*/*
%config /etc/udev/rules.d/*
%config /etc/bash_completion.d/*

%defattr(-,root,_vzctl,-)
/var/lib/vz

%changelog
* Fri Jun 15 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.3-alt1
- Updated to vzctl-3.3

* Mon May 21 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.2.1-alt1
- Updated to vzctl-3.2.1

* Sun May 06 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.2-alt1
- Updated to vzctl-3.2

* Sat Mar 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.1-alt1
- Updated to vzctl-3.1 (commit 1975a5c0efff90d7d75d96e92b0021acd04635a2)
- Update BuildRequires (ploop support)
- Stop changing configuration (CONFIGFILE=basic -> CONFIGFILE=vswap-256m) by initscript

* Wed Jan 25 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.30.2-alt2
- Fix in initscript changing configuration (CONFIGFILE=basic -> CONFIGFILE=vswap-256m)

* Sat Jan 21 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.30.2-alt1
- Updated to vzctl-3.0.30.2

* Thu Oct 06 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.29.3-alt1
- Updated to vzctl-3.0.29.3
- Add mount/umount cgroups in init script vz

* Sun Sep 18 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.29.1-alt1
- Updated to vzctl-3.0.29.1 d01a4819 (closes: #26279)

* Fri Jul 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.28.3-alt3
- Patch vzifup-post 

* Fri Jul 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.28.3-alt2
- Fix post for add vzeventd

* Fri Jun 24 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.28.3-alt1
- Updated to vzctl-3.0.28.3 d2c69648 (closes: #9878 #13147 #25620)

* Sat May 28 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.27-alt1
- Updated to vzctl-3.0.27

* Mon May 09 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.26.3-alt1
- Updated to vzctl-3.0.26.3

* Mon Mar 28 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.26.2-alt2
- Fix error in %post
- Add patch for vz-altlinux.in: check for disabled ipv6 (thanks mike@)

* Sat Mar 26 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.26.2-alt1
- Updated to vzctl-3.0.26.2
- Update spec and init scripts for support vzeventd

* Fri Dec 24 2010 Dmitry V. Levin <ldv@altlinux.org> 3.0.24.2-alt1
- Updated to vzctl-3.0.24-42-gf3bf518+3.0.24.2 (closes: #24812).

* Wed Aug 11 2010 Dmitry V. Levin <ldv@altlinux.org> 3.0.24.1-alt1
- Updated to vzctl-3.0.24-32-gda3a366 (closes: #23873).

* Thu Jul 08 2010 Dmitry V. Levin <ldv@altlinux.org> 3.0.24-alt1
- Updated to vzctl-3.0.24-19-gb9eca2c.
- Fixed chkconfig stop priority number (closes: #23677).

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 3.0.23-alt3
- Updated to vzctl-3.0.23-21-g2b97841.
- vznetaddbr: Fixed iface init code (Dmitry Lebkov; closes: #19546).
- vzmigrate (RSYNC_OPTIONS): Added -A -X options, made it redefinable
  (Vladimir Kamarzin; closes: #17870, #17871).

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.23-alt2
- Updated to vzctl-3.0.23-8-g71ad397.
- Removed obsolete package dependencies and %%post_ldconfig/%%postun_ldconfig calls.

* Fri Oct 31 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.23-alt1
- Updated to 3.0.23.

* Sat Jun 07 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.22-alt3
- postcreate.sh:
  + Copy /etc/localtime from HN to VE (closes: #14363).
- vzmigrate:
  + Fixed typo in 'if' statement (closes: #15085).
  + Added -x to rsync options.
- functions (change_hostname):
  + Add comment to /etc/hosts (closes: #15072).
  + Handle multiple 127.0.0.1 names (closes: #15073).

* Sat Feb 23 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.22-alt2
- Updated to vzctl-3.0.22-6-gcb3bf5f.

* Wed Dec 19 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.22-alt1
- Updated to vzctl-3.0.22.

* Thu Nov 15 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.19-alt2
- Updated to vzctl-3.0.19-1-g65925ca.

* Tue Nov 13 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.19-alt1
- Updated to vzctl-3.0.19.

* Sun Oct 07 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.18-alt3
- vzctl: Backported "update meminfo on privvmpages change".
- vps-create: Fixed typo in uncompressed tarball support.

* Fri Oct 05 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.18-alt2
- Updated to vzctl-3.0.18-9-g277c60c.
- Fixed cron script creation in startup script.

* Wed Sep 05 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.18-alt1
- Updated to vzctl-3.0.18-3-g1af86a4.

* Fri May 18 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.16-alt5
- Updated to vzctl-3.0.16-32-g3c4d0f1.
- vps-net_add.in: Add given IP address to neighbour table
  prior to adding routing for this address (#11192).

* Mon Apr 23 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.16-alt4
- Updated to vzctl-3.0.16-24-g93eca3a.
- Implemented non-gzipped template cache support.
- Startup script: Added /var/lock/subsys/vz check to "status".

* Fri Apr 20 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.16-alt3
- Updated to vzctl-3.0.16-22-g2409c72.
- Startup script: Added check for running kernel.
- Enhanced HN etcnet support.

* Sun Mar 25 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.16-alt2
- vzsplit: Changed /vz to /var/lib/vz (#11112).
- etc/dists/scripts/*: Added /etc/hooks support:
  + etcnet-add_ip.sh: Hooked up /etc/hooks/add_ip.d/
  + etcnet-del_ip.sh: Hooked up /etc/hooks/del_ip.d/
  + postcreate.sh: Hooked up /etc/hooks/post_create.d/
  + redhat-set_hostname.sh: Hooked up /etc/hooks/set_hostname.d/
  + set_dns.sh: Hooked up /etc/hooks/set_dns.d/
  + set_userpass.sh: Hooked up /etc/hooks/set_userpass.d/

* Tue Mar 13 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.16-alt1
- Updated to vzctl-3.0.16.
- Added fstab /tmp entry workarounds to postcreate.sh.

* Sun Mar 11 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.15-alt1
- Updated to vzctl-3.0.15-3-gc7374ad.

* Mon Mar 05 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.14-alt3
- etcnet-add_ip.sh:
  + Fixed adding first ip address.
  + Fixed removing all ip addresses.

* Sun Mar 04 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.14-alt2
- Updated to vzctl-3.0.14-18-gf92323d.
- vzctl: Reintroduced initial network setup on VE start.
- etcnet-add_ip.sh: Enhanced to ensure that venet0 is not configured
  in VE if no venet parameters specified (#9886).
- vz.conf: Changed DEF_OSTEMPLATE from "fedora-core-4" to "altlinux"
  (#10945).

* Sun Feb 18 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.14-alt1
- Updated to vzctl-3.0.14-2-ga01572a.
- Relocated vz-scripts and conf directories
  from /etc/sysconfig to %_pkgconfdir
- Created group _vzctl and made /var/lib/vz/template/cache
  writable to this group.

* Thu Nov 30 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.13-alt2
- vps-functions: More arp handing fixes.

* Sun Nov 26 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.13-alt1
- Updated to vzctl-3.0.13-1-ge2968e9.
- vps-functions:
  (vzarp, vzarpipdetect, vzarpipset): Fixed arp handling.
  (vzaddrouting4): Enhanced source ip selection (#10324).

* Mon Oct 09 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.12-alt1
- Updated to 3.0.12.

* Sat Sep 23 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.11-alt2
- Updated to 3.0.11-2-g27c2c01.
- etc/dists/scripts/*-add_ip.sh:
  Changed FAKEGATEWAY/FAKEGATEWAYNET from
  191.255.255.1/191.255.255.0 to 192.0.2.1/192.0.2.0
  (see RFC 3330 for rationale).
- etc/dists/scripts/etcnet-add_ip.sh: create_venet_config():
  Add "dev venet0" to venet0/ipv4route, to workaround bug
  in old /etc/net/scripts/config-ipv4 ipv4route parser.

* Thu Aug 17 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.11-alt1
- Updated to 3.0.11.
- arpsend: Fixed long options handling (#9876).
- Changed HOME environment variable from "/" to "/root".
- Changed PATH to "/sbin:/usr/sbin:/bin:/usr/bin".
- Use setproctitle(3) instead of local hacks.
- vzctl enter:
  + Fixed descriptors handling on error path.
  + Fixed off-by-one error which resulted to broken PATH.

* Sat Aug 05 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.10-alt5
- Updated init.d/vz to ALT policy.
- Fixed bash-isms in shell scripts.
- Dropped obsolete vps-postcreate.
- Cleaned up vzmigrate, vzpid and postcreate.sh a bit.
- Added inittab and syslog.conf workarounds to postcreate.sh.

* Fri Jul 14 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.10-alt4
- Fixed compilation warnings.
- Added VPS name support (igor@openvz).

* Mon Jun 19 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.10-alt3
- Requires: network-config-subsystem
- Added create-venet etcnet script.
- Added venet0/options etcnet config.

* Fri Jun 16 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.10-alt2
- Added %_pkgconfdir/dists/{altlinux{,-2.4,-3.0},owl}.conf configs.
- Added %_pkgconfdir/dists/scripts/etcnet-{add,del}_ip.sh scripts.
- %_initdir/vz: Added cond* targets.

* Thu Jun 15 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.10-alt1
- Adopted scripts and specfile for Sisyphus.
- Relocated /usr/lib/vzctl/scripts/vps-* scripts to
  /usr/share/vzctl/scripts/.
- Relocated /vz to /var/lib/vz.
- Relocated /var/lib/vzctl/veip to /var/lib/vz/veip.
- Merged libvzctl-simfs into libvzctl.
- Moved g_log symbol definition from vzcfgvalidate to libvzctl.
