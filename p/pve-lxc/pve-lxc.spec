%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define rname lxc

Name: pve-%rname
Version: 5.0.2
Release: alt1
Summary: Linux containers userspace tools
Group: System/Configuration/Other
License: LGPL-2.1+
URL: https://linuxcontainers.org/

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source2: config.tar
Source99: debian.tar
Patch: %name-%version.patch

Requires: lxcfs
Requires: criu >= 3.15
Requires: rsync wget
Requires: iproute2 iptables iptables-ipv6
Conflicts: %rname %rname-libs liblxc1 %rname-core %rname-net %rname-runtime
Provides: %rname-pve = %EVR

BuildRequires(pre): meson >= 0.61
BuildRequires: docbook2X
BuildRequires: libcap-devel libseccomp-devel libselinux-devel libssl-devel
BuildRequires: bash-completion
BuildRequires: pkgconfig(systemd)

%description
Containers provides resource management through control groups and
resource isolation through namespaces. The linux containers, lxc, aims
to use these new functionalities to provide an userspace container
object which provides full resource isolation and resource control for
an applications or a system.

%add_findreq_skiplist %_datadir/%rname/lxc-patch.py
%add_findreq_skiplist %_datadir/%rname/templates/*

%prep
%setup
mkdir debian
tar -xf %SOURCE99 -C debian --strip-components 1
tar -xf %SOURCE2 -C config --strip-components 1

%patch -p1

for p in `cat debian/patches/series`; do
    patch -p1 < debian/patches/$p
done

%build
%meson \
    -Ddistrosysconfdir='/etc/sysconfig' \
    -Dinit-script=systemd \
    -Dapparmor=false \
    -Dselinux=true \
    -Dseccomp=true \
    -Dexamples=false \
    -Dcgroup-pattern='lxc/%%n'

%meson_build

%install
%meson_install

mkdir -p %buildroot%_datadir/lxc/config
for i in config/*.conf.in; do
	sed -e "s|@LXCTEMPLATECONFIG@|%_datadir/lxc/config|g" $i > %buildroot%_datadir/lxc/${i%%.in};
done

# cleanup
rm -fr %buildroot%_libexecdir/%rname/%rname-apparmor-load
rm -f %buildroot%_datadir/lxc/lxc-patch.py
rm -fr %buildroot%_includedir
rm -f %buildroot%_libdir/liblxc.so
rm -f %buildroot%_libdir/liblxc.a
rm -fr %buildroot%_pkgconfigdir
rm -fr %buildroot%_mandir/{ja,ko}

%post
usermod --add-subgids 100000-165535 --add-subuids 100000-165535 root ||:

%files
%config(noreplace) %_sysconfdir/sysconfig/%rname
%dir %_sysconfdir/%rname
%config(noreplace) %_sysconfdir/%rname/default.conf
%_datadir/bash-completion/completions/*
%_unitdir/*.service
%_bindir/%rname-*
%_sbindir/init.%rname
%_libexecdir/%rname
%_libdir/%rname
%_libdir/*.so.*
%_datadir/%rname
%_man1dir/*.1*
%_man5dir/*.5*
%_man7dir/*.7*

%changelog
* Wed Mar 22 2023 Alexey Shabalin <shaba@altlinux.org> 5.0.2-alt1
- 5.0.2-2

* Mon Apr 11 2022 Alexey Shabalin <shaba@altlinux.org> 4.0.12-alt1
- 4.0.12

* Tue Feb 15 2022 Alexey Shabalin <shaba@altlinux.org> 4.0.11-alt2
- build from gear
- update requires and conflicts
- package bash-completion
- disable apparmor support
- add usermod in %%post

* Mon Dec 20 2021 Valery Inozemtsev <shrek@altlinux.ru> 4.0.11-alt1
- 4.0.11-1

* Wed Sep 29 2021 Valery Inozemtsev <shrek@altlinux.ru> 4.0.9-alt1
- 4.0.9-4

* Thu Sep 03 2020 Valery Inozemtsev <shrek@altlinux.ru> 4.0.3-alt1
- 4.0.3-1

* Mon Aug 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.0-alt5
- NMU: fixed build with new selinux.

* Wed Jan 15 2020 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt4
- remove dependency on policycoreutils

* Wed Aug 28 2019 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt3
- 3.1.0-64

* Tue Feb 12 2019 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt2
- merge fix for CVE-2019-5736

* Wed Feb 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt1
- 3.1.0-2
- not provide liblxc.so.1 (closes: #36009)

* Thu Oct 11 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.2-alt3
- 3.0.2+pve1-3

* Fri Sep 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.2-alt2
- fixed ns path

* Thu Sep 06 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.2-alt1.S1
- 3.0.2+pve1-2

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.1.0-alt0.M80C.1
- backport to c8 branch

* Tue Sep 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.1.0-alt0.M80P.1
- backport to p8 branch

* Tue Sep 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.1.0-alt1
- 2.1.0-2

* Mon Jul 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.8-alt0.M80P.1
- backport to p8 branch

* Mon Jul 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.8-alt1
- 2.0.8-3

* Mon May 15 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt5.M80P.1
- backport to p8 branch

* Mon May 15 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt6
- run lxcnetdelbr when deleting veths

* Fri Apr 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt2.M80P.4
- backport to p8 branch

* Fri Apr 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt4.2
- disable cgmanager

* Thu Apr 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt1.M80P.4
- backport to p8 branch

* Thu Apr 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt4.1
- fixed starting unprivileged container

* Mon Apr 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt0.M80P.4
- backport to p8 branch

* Mon Apr 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt4
- 2.0.7-4

* Thu Feb 02 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt0.M80P.1
- backport to p8 branch

* Thu Feb 02 2017 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Thu Nov 24 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0.6-alt0.M80P.1
- backport to p8 branch

* Thu Nov 24 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Wed Nov 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0.5-alt1
- 2.0.5-2

* Wed Sep 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0.4-alt2
- added altlinux configs

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Fri Jun 24 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5-alt1
- initial release

