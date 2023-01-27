
Name: vzctl
Version: 7.0.254
Release: alt2

Summary: OpenVZ Virtual Environments control utility
License: GPLv2
Group: System/Configuration/Other
Url: http://openvz.org/
Vcs: https://src.openvz.org/scm/ovzl/vzctl.git

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64

# these reqs are for vz helper scripts
Requires: ploop >= 7.0.199
Requires: network-config-subsystem
Requires: libvzctl >= 7.0.714

BuildRequires(pre): rpm-build-python3
BuildRequires: glibc-devel libuuid-devel
BuildRequires: libudev-devel
# BuildRequires: systemd-devel libudev-devel
BuildRequires: libvzctl-devel >= 7.0.639
BuildRequires: libploop-devel >= 7.0.199
BuildRequires: kernel-headers-ovz-el7 >= 3.10.0

%define _libexecdir /usr/libexec
%define vzdir /etc/vz
%define confdir %vzdir/conf
%define namesdir %vzdir/names
%define lockdir /var/lib/vz/lock
%define vzctl_lockdir /var/lock/vzctl
%define spooldir /var/lib/vz
%define netdir /etc/sysconfig/network-scripts
%define bashcompldir /etc/bash_completion.d

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
%make CFLAGS="%optflags -D_GNU_SOURCE -DVERSION=\\\"%version\\\""

%install
make install \
	DESTDIR=%buildroot \
	SBINDIR=%_sbindir \
	MANDIR=%_mandir \
	SYSTEMDDIR=%_unitdir \
	NETSCRIPTDIR=%netdir \
	VZDIR=%vzdir \
	CONFDIR=%confdir \
	VZLOCKDIR=%lockdir \
	VZCTLLOCKDIR=%vzctl_lockdir \
	VZSPOOLDIR=%spooldir \
	BASHCOMPLDIR=%bashcompldir \
	LOGRDIR=%_logrotatedir \
	MODULESLOADDDIR=/lib/modules-load.d

ln -s -r %buildroot%_unitdir/vzevent.service %buildroot%_unitdir/vzeventd.service

%post
%post_service vzeventd

# Load sysctls
sysctl -p /etc/sysctl.d/99-vzctl.conf > /dev/null 2>&1

# First installation, not upgrade.
#if [ $1 -eq 1 ]; then
#	# Insert iptables rules.
#	%_libexecdir/vz-iptables-config.py add > /dev/null 2>&1
#fi
exit 0

%preun
%preun_service vz
%preun_service vzeventd
%preun_service vz-k8s-inside-ct
# Last deinstallation, not upgrade.
#if [ $1 -eq 0 ]; then
#	# Remove iptables rules.
#	%_libexecdir/vz-iptables-config.py remove > /dev/null 2>&1
#fi

%files
%dir %vzdir
%dir %confdir
%dir %namesdir
%dir %vzdir/dev
%vzdir/vzevent.d
%attr(700,root,root) %lockdir
%spooldir
%bashcompldir/*
%_target_libdir_noarch/dracut/modules.d/*
%_sbindir/*
%_unitdir/*.service
#%%_initdir/*
%_libexecdir/vz
%_libexecdir/vz-k8s-inside-ct
%config(noreplace) %_logrotatedir/vzctl
%confdir/*sample
%_man8dir/*
%_man5dir/*

%config(noreplace) %confdir/networks_classes
%config(noreplace) %vzdir/vz.conf
%config(noreplace) %_sysconfdir/modprobe.d/*.conf
%config %_sysconfdir/sysctl.d/*.conf
%config /lib/modules-load.d/*.conf

%changelog
* Fri Jan 27 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.0.254-alt2
- change modules-load.d directory path to /lib

* Tue Jun 28 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.254-alt1
- 7.0.254

* Thu May 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.252-alt1
- 7.0.252

* Tue Apr 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.251-alt1
- 7.0.251

* Sat Nov 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.249-alt1
- 7.0.249

* Thu Jul 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.248-alt1
- 7.0.248

* Wed Jun 09 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.245-alt1
- 7.0.245

* Thu Apr 22 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.242-alt1
- 7.0.241
- vzlist: reduce the width of CTID field

* Sun Jan 31 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.241-alt1
- 7.0.241

* Tue Jan 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.240-alt1
- 7.0.240

* Tue Dec 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.236-alt2
- add binfmt_misc kernel module for criu functioning
- fix -fno-common default in GCC 10.0
- fix warning: 's' may be used uninitialized in this function

* Thu Nov 19 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.236-alt1
- 7.0.236

* Fri Oct 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.234-alt1
- 7.0.234

* Fri Sep 18 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.233-alt1
- 7.0.233

* Wed Sep 09 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.232-alt2
- add vzubc utility from vzctl 4.11.1

* Fri Sep 04 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.232-alt1
- 7.0.232

* Fri Aug 28 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.230-alt1
- 7.0.230

* Tue Jul 21 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.229-alt1
- 7.0.229

* Wed Jul 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.228-alt1
- 7.0.228 with "k8s inside a CT" feature enabled

* Wed May 27 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.227-alt1
- 7.0.227

* Sat Apr 25 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.226-alt1
- 7.0.226
- fix vz.service terminates during system boot with modern systemd

* Mon Apr 20 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.222-alt1
- 7.0.222

* Tue Mar 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.220-alt1
- 7.0.220

* Thu Mar 19 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.219-alt1
- 7.0.219

* Wed Mar 11 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.218-alt1
- 7.0.218

* Wed Mar 04 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.217-alt1
- 7.0.217

* Wed Feb 19 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.216-alt1
- 7.0.216

* Wed Jan 22 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.215-alt1
- 7.0.215

* Thu Dec 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.209-alt5
- vzgetpa: /bin/bash as in all other OVZ scripts

* Mon Dec 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.209-alt4
- compatibility with libvirt

* Thu Dec 05 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.209-alt3
- fix License

* Mon Nov 11 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.209-alt2
- change /var/run to /run

* Mon Oct 07 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.209-alt1
- Update to 7.0.209

* Wed Sep 25 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.208-alt1
- Update to 7.0.208

* Tue Aug 27 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt5
- spec cleanup

* Tue Aug 27 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt4
- network and service changes for ALT

* Mon Aug 26 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt3
- change prlctl to vzlist/vzctl

* Thu Aug 22 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt2
- drop sysv rc scripts

* Mon Aug 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.207-alt1
- Update to 7.0.207

* Sun Nov 04 2018 Alexey Shabalin <shaba@altlinux.org> 7.0.191-alt1
- Update to 7.0.191

* Mon Feb 12 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.182-alt1
- Initial build vzctl-7.0.182 for VZ-7

* Tue Aug 25 2015 Terechkov Evgenii <evg@altlinux.org> 4.9.4-alt1
- Updated to vzctl-4.9.4

