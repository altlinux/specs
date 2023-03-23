#
# lxc: linux Container library
#
# (C) Copyright IBM Corp. 2007, 2008
# (C) ALT Linux Team 2009-2021
#
# Authors:
# Daniel Lezcano <dlezcano at fr.ibm.com>
# Denis Pynkin <dans at altlinux.org>
# Vladimir D. Seleznev <vseleznv at altlinux.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Spec file adapted for ALT Linux.

%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define sover 1
%def_with systemd

# Skip automatic dependency to optional lsb scripts
%add_findreq_skiplist %_initdir/*

# Needed to disable auto requirements from distro templates
%add_findreq_skiplist %_datadir/lxc/*

# Do not need to check
%add_findreq_skiplist %_libexecdir/lxc/lxc-apparmor-load
%add_findreq_skiplist %_libexecdir/lxc/lxc-net

Name: lxc
Version: 5.0.2
Release: alt1

Summary: Linux Containers

License: LGPL-2.1-or-later
Group: System/Configuration/Other
Url: https://linuxcontainers.org/

VCS: https://github.com/lxc/lxc.git
Source0: lxc-%version.tar
Source1: lxc-net.sysconfig
Source2: lxc-user-nic.control
Source3: lxc.watch

# git://git.altlinux.org:/gears/l/lxc.git
Patch: %name-%version-%release.patch

Requires: lxc-core lxc-net lxc-templates

BuildRequires(pre): meson >= 0.61 rpm-macros-pam
BuildRequires: docbook2X
BuildRequires: libcap-devel libcap-devel-static
BuildRequires: libpam-devel
BuildRequires: libseccomp-devel libselinux-devel libssl-devel
BuildRequires: python3-dev
BuildRequires: pkgconfig(systemd)
BuildRequires: libpam-devel

%description
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This is meta package.

%package core
Summary: Core package for LXC
Group: System/Configuration/Other
Requires: rsync
Requires: service
%ifarch x86_64 aarch64 ppc64le
Requires: criu >= 3.15
%endif
Obsoletes: lxc-sysvinit < %EVR

%package net
BuildArch: noarch
Summary: Network interface for LXC with DHCP
Group: System/Configuration/Networking
Requires: iproute2 dnsmasq lxc-core iptables

%package templates
BuildArch: noarch
Summary: Templates for LXC
Group: System/Configuration/Other
Requires: lxc-core wget

%package -n liblxc%sover
Summary: LXC shared runtime library
Group: System/Libraries
Requires: lxc-runtime

%package runtime
Summary: Runtime files for LXC
Group: System/Configuration/Other
Provides: lxc-libs = %EVR
Obsoletes: lxc-libs < %EVR
Requires(pre): /usr/sbin/groupadd

%package -n liblxc-devel
Summary: Development files for LXC
Group: Development/Other
Provides: lxc-devel = %EVR

%set_pam_name pam_cgfs
%package -n %pam_name
Summary: %summary
Group: System/Base

%description core
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package provides the lxc-* tools, which can be used to start a single
daemon in a container, or to boot an entire "containerized" system, and to
manage and debug your containers.

%description net
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package provides the network interface for containers with DHCP.

%description templates
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package contains templates for LXC.

%description -n liblxc%sover
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package contains runtime shared library for LXC.

%description runtime
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package contains runtime executables and data for LXC.

%description -n liblxc-devel
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package contains development files for LXC.

%description -n %pam_name
%summary
This package provides a Pluggable Authentication Module (PAM) to provide
logged-in users with a set of cgroups which they can administer.
This allows for instance unprivileged containers, and session
management using cgroup process tracking.

%prep
%setup
%autopatch -p1
%ifarch %e2k
echo -e "#undef ARRAY_SIZE\n#define ARRAY_SIZE(x) (sizeof(x)/sizeof(*(x)))" >> src/lxc/macro.h
%endif

%build
%meson \
    -Ddistrosysconfdir='/etc/sysconfig' \
    -Dinit-script=%{?_with_systemd:systemd,}sysvinit \
    -Dcapabilities=true \
    -Dapparmor=false \
    -Dselinux=true \
    -Dseccomp=true \
    -Dpam-cgroup=true \
    -Dcgroup-pattern='lxc/%%n'

%meson_build

%install
%meson_install
mkdir -p %buildroot%_initdir
mv %buildroot%_sysconfdir/init.d/* %buildroot%_initdir/
mv %buildroot%_initdir/lxc-containers %buildroot%_initdir/lxc
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/security %buildroot/%_lib/
mkdir -p %buildroot%_localstatedir/lxc
install -pm644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/lxc-net
install -pDm755 %SOURCE2 %buildroot%_controldir/lxc-user-nic

rm %buildroot%_datadir/lxc/lxc-patch.py
find %buildroot -name '*.a' -delete

%post core
usermod --add-subgids 100000-165535 --add-subuids 100000-165535 root ||:
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add lxc ||:
fi

%preun core
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del lxc ||:
fi

%post net
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add lxc-net ||:
fi

%preun net
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del lxc-net ||:
fi

%pre runtime
groupadd -r -f vmusers ||:
%pre_control lxc-user-nic

%post runtime
%post_control -s vmusers lxc-user-nic

%files

%files core
%doc COPYING doc/FAQ.txt

%dir %_sysconfdir/lxc
%dir %_sysconfdir/sysconfig/lxc
%config(noreplace) %_sysconfdir/lxc/*
%config(noreplace) %_sysconfdir/sysconfig/lxc*

%_datadir/bash-completion/completions/*

%_bindir/lxc-*
%_datadir/lxc/config
%_datadir/lxc/selinux

%dir %_defaultdocdir/lxc
%_defaultdocdir/lxc/examples

%_man1dir/lxc*
%_man5dir/lxc*
%_man7dir/lxc*

%dir %_mandir/ja
%dir %_mandir/ko
%_mandir/ja/*
%_mandir/ko/*

%_initdir/lxc

%if_with systemd
%_unitdir/lxc.service
%_unitdir/lxc@.service
%_unitdir/lxc-monitord.service
%endif

%files net
%_libexecdir/lxc/lxc-net

%_initdir/lxc-net

%if_with systemd
%_unitdir/lxc-net.service
%endif

%files templates
%dir %_datadir/lxc
%_datadir/lxc/templates

%files -n liblxc%sover
%_libdir/liblxc.so.%sover
%_libdir/liblxc.so.%sover.*

%files runtime
%attr(4710,root,vmusers) %_libexecdir/lxc/lxc-user-nic
%_libexecdir/lxc/lxc-containers

%_libexecdir/lxc/lxc-apparmor-load
%_libexecdir/lxc/lxc-containers
%_libexecdir/lxc/lxc-monitord
%_libexecdir/lxc/hooks

%_controldir/lxc-user-nic
%_datadir/lxc/hooks
%_datadir/lxc/lxc.functions

%_sbindir/init.lxc
%_sbindir/init.lxc.static
%_localstatedir/lxc

%dir %_datadir/lxc
%dir %_libexecdir/lxc
%dir %_libdir/lxc
%dir %_libdir/lxc/rootfs
%_libdir/lxc/rootfs/README

%files -n liblxc-devel
%_includedir/lxc
%_libdir/liblxc.so
%_pkgconfigdir/lxc.pc

%files -n %pam_name
%_pam_modules_dir/*
%_man8dir/pam_cgfs.8*

%changelog
* Thu Mar 23 2023 Alexey Shabalin <shaba@altlinux.org> 5.0.2-alt1
- Updated to 5.0.2.

* Tue Feb 15 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.12-alt2
- Actually built 4.0.12 (pointed by shaba@).

* Thu Feb 10 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.0.12-alt1.1
- Fixed build for Elbrus

* Mon Feb 07 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.12-alt1
- Updated to lxc-4.0.12.

* Sat Dec 04 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.11-alt1
- Updated to lxc-4.0.11.
- lxc-net: Added missing dependency to iptables.

* Thu Jul 22 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.10-alt1
- Updated to lxc-4.0.10.

* Wed Jul 14 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.9-alt1
- Updated to lxc-4.0.9.
- Do not require criu on armh, require criu on ppc64le.

* Wed Feb 03 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.6-alt1
- Updated to lxc-4.0.6.

* Fri Oct 23 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.5-alt1
- Updated to lxc-4.0.5.
- lxc-core: %%dir'ed %%_datadir/bash-completion.

* Sun Aug 09 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.4-alt1
- Updated to lxc-4.0.4.
- lxc-core: Packed missing directories.
- lxc-runtime: Built and packed init.lxc.static.

* Tue Aug 04 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.3.0.78.git8bf37e96e-alt1
- Updated to lxc-4.0.3-78-g8bf37e96e.
- Split lxc package to lxc-core, lxc-net and lxc-templates.
- Renamed lxc-libs to lxc-runtime.
- Renamed lxc-devel to liblxc-devel (closes: 38778).
- Moved shared library file to liblxc1 (closes: 38779).
- Moved bash completion to %%_datadir/bash-completion/completion.
- Moved %%_datadir/lxc/hooks to lxc-runtime.
- Do not package %%_datadir/lxc/lxc-patch.py.
- Clean up spec, drop needless build and runtime dependencies.

* Tue Jun 30 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.3-alt1
- Updated to 4.0.3.

* Wed Apr 29 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.2-alt1
- Updated to 4.0.2.

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- Updated to 4.0.1.
- drop requires bridge-utils

* Thu Apr 02 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.0-alt2
- lxc-libs:
  + Made preinstall create required vmusers group.
  + Added runtime dependency for control.
  + Fixed %%attr for lxc-user-nic.
  + Packaged directory %%_libdir/lxc/rootfs and README file placed in it.

* Tue Mar 31 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.0-alt1
- Updated to 4.0.0.
- Added control facility for lxc-user-nic (allowed for vmusers group members
  by default).

* Fri Sep 20 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.4-alt3
- Applied patches:
  + Start lxc service after remote-fs.target (Debian);
  + Hande cpuset initialization race in cgroups (Debian);
  + Initialize cpuset properly in cgroups (Debian);
  + Fix regression: return exit status of command in lxc-attach (Debian);
  + lxc-net.service wants network-online.target (Fedora).
- Obsoleted lxc-sysvinit.
- Packaged COPYING and FAQ.txt.
- Clean up specfile.

* Fri Jul 12 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.4-alt2
- Fixed working on kernel 5.1.
- spec: fixed license LGPL to LGPL-2.1-or-later.

* Thu Jul 04 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.4-alt1
- 3.0.4.

* Wed Feb 13 2019 Denis Pynkin <dans@altlinux.org> 3.0.3-alt3
- Apply patch fixing the startup of LXD containers (after CVE-2019-5736)

* Tue Feb 12 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.3-alt2
- built lxc-3.0.3-15-g94bb05e0 snapshot.
- fixes:
  + CVE-2019-5736: (runC) rexec callers as memfd.

* Wed Feb 06 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.3-alt1
- 3.0.3
- lxc: added wget to runtime dependencies.

* Sun Sep 09 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.2-alt1
- 3.0.2
- rebuilt with seccomp and SELinux support
- explicitly enabled capability support which was enabled automatically in
  previous builds

* Wed Aug 01 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.1-alt4
- really disable SysVinit scripts by default

* Tue Jul 10 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.1-alt3
- tuned SysVinit scripts for ALT
- disable SysVinit scripts by default (according to services policy)

* Tue Jun 26 2018 Michael Shigorin <mike@altlinux.org> 3.0.1-alt2
- Worked around FTBFS on e2k
- Minor spec cleanup

* Sun Jun 24 2018 Denis Pynkin <dans@altlinux.org> 3.0.1-alt1
- Version updated

* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 3.0.0-alt1
- New major version
- python bindings are moved to separate source tree
- pam0_cgfs module has been moved from lxcfs to lxc

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Sep 06 2017 Denis Pynkin <dans@altlinux.org> 2.1.0-alt1
- Version updated
- New script 'lxc-update-config' can be used to upgrade existing
  legacy LXC configurations to valid LXC 2.1
- Updated copyright info in spec file due a lot of local changes

* Tue Aug 29 2017 Denis Pynkin <dans@altlinux.org> 2.0.8-alt4
- Based on patch by Michael Shigorin: introduced systemd knob (on by default)
- Removed dependency to lsb scripts for lxc-sysvinit package

* Tue Aug 29 2017 Denis Pynkin <dans@altlinux.org> 2.0.8-alt3
- Build with both init systems sysvinit and systemd
- new package lxc-sysvinit provided for classic SysVinit boot

* Mon Aug 28 2017 Denis Pynkin <dans@altlinux.org> 2.0.8-alt2
- Fixes #33814
- Fixes #33799

* Thu Jun 29 2017 Denis Pynkin <dans@altlinux.org> 2.0.8-alt1
- Version updated

* Wed Apr 26 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt4
- Fixes #33399

* Thu Mar 30 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt3
- Fixes #33302

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt2
- Disable cgmanager support

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt1
- Version updated

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.6-alt1
- Version updated

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 2.0.5-alt1
- Version updated

* Mon Aug 22 2016 Denis Pynkin <dans@altlinux.org> 2.0.4-alt1
- Bugfix release
- Fixes #32391

* Mon Apr 11 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt1
- Release version

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt0.rc9.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt0.rc9.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.rc9
- Version updated
- Fix of altlinux template

* Mon Feb 29 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.rc4
- Version updated
- Added cgmanager support (for lxd)

* Mon Nov 09 2015 Denis Pynkin <dans@altlinux.org> 1.1.4-alt1
- New version.

* Tue Sep 15 2015 Denis Pynkin <dans@altlinux.org> 1.1.3-alt1
- New version.
  Security fixes and ABI changes in upstream.

* Thu Apr 23 2015 Denis Pynkin <dans@altlinux.org> 1.1.2-alt2
- Removed creation/deletion of unneeded lxc-dnsmasq user.

* Sat Apr 11 2015 Denis Pynkin <dans@altlinux.org> 1.1.2-alt1
- Bugfix release

* Wed Mar 11 2015 Denis Pynkin <dans@altlinux.org> 1.1.0-alt1
- Version 1.1.0
  Added criu (crtools) to dependencies for container dump/restore.
  Added network service and configuration.
  Fixed #30232

* Tue Aug 19 2014 Denis Pynkin <dans@altlinux.org> 1.0.5-alt2
- Fixed reopened #30158
  Added check of services in container before start or stop.
  Added check of syslog config existence prior changing.

* Fri Aug 15 2014 Denis Pynkin <dans@altlinux.org> 1.0.5-alt1
- New version

* Fri Aug 15 2014 Denis Pynkin <dans@altlinux.org> 1.0.4-alt2
- Fixed: #30154 #30119
- New subpackage lxc-python3
- Build both lxc-ls -- legacy and python.
  Correct version is selected via alternatives
- Fixed: #30158 #30159
- Updated template for ALTLinux
- Now used default list of packages in case
  if /etc/lxc/profiles/default is absent

* Sat Jun 14 2014 Denis Pynkin <dans@altlinux.org> 1.0.4-alt1
- New version

* Sun Nov 24 2013 Denis Pynkin <dans@altlinux.org> 0.9.0-alt3
- Fixed rebuild problem

* Mon Jul 01 2013 Denis Pynkin <dans@altlinux.org> 0.9.0-alt2
- 0.9.0 release
- fixed #29113, Thanks to legion@.

* Sun Mar 10 2013 Denis Pynkin <dans@altlinux.org> 0.9.0-alt1.alpha3
- New version

* Fri May 11 2012 Denis Pynkin <dans@altlinux.org> 0.7.5-alt3
- Merged bc31b303c48c615c2cd15dd54831e55196b983f0 to fix
  build with new autotools

* Mon Jan 02 2012 Denis Pynkin <dans@altlinux.org> 0.7.5-alt2
- Merged 1c41ddcb4af633ac906f1d7c9ef1dc7d121d7850 for rpath option

* Mon Oct 03 2011 Denis Pynkin <dans@altlinux.org> 0.7.5-alt1
- New version
- Template for ALTLinux by Alexey Shabalin

* Thu Jul 21 2011 Denis Pynkin <dans@altlinux.org> 0.7.4.2-alt1
- New version

* Sat Apr 30 2011 Denis Pynkin <dans@altlinux.ru> 0.7.4.1-alt1
- New version

* Sun Nov 07 2010 Denis Pynkin <dans@altlinux.ru> 0.7.3-alt1
- New version

* Sat Jul 31 2010 Denis Pynkin <dans@altlinux.ru> 0.7.2-alt1
- New version

* Fri May 28 2010 Denis Pynkin <dans@altlinux.ru> 0.6.5-alt2
- added zgrep in requirements
- added patch c08556c6ece8ad8308f7636adb0ad25b60e3a16d for lazy umount

* Fri Feb 19 2010 Denis Pynkin <dans@altlinux.ru> 0.6.5-alt1
- New version

* Sat Dec 12 2009 Denis Pynkin <dans@altlinux.ru> 0.6.4-alt1
- New version

* Wed Nov 11 2009 Denis Pynkin <dans@altlinux.ru> 0.6.3-alt2
- fixed #22235 (added dirs /var/lib/lxc and /var/cache/lxc)

* Sat Jul 25 2009 Denis Pynkin <dans@altlinux.ru> 0.6.3-alt1
- New version
- Patch for --as-needed

* Thu Jul 23 2009 Denis Pynkin <dans@altlinux.ru> 0.6.2-alt1
- Initial spec for ALT Linux

* Tue Mar 24 2009 Daniel Lezcano <daniel.lezcano@free.fr> - Version 0.6.1
- Removed capability setting, let the user to do that through "lxc-setcap"

* Mon Feb 16 2009 Daniel Lezcano <daniel.lezcano@free.fr> - Version 0.6.0
- Added more capabilities to the executables

* Sun Jan 25 2009 Daniel Lezcano <daniel.lezcano@free.fr> - Version 0.6.0
- Reduced spec file

* Sun Aug 3 2008 Daniel Lezcano <dlezcano@fr.ibm.com> - Version 0.1.0
- Initial RPM release.
