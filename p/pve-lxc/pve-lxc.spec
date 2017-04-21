%define rname lxc

Name: pve-%rname
Version: 2.0.7
Release: alt4.2
Summary: Linux containers usersapce tools
Group: System/Configuration/Other
License: LGPL
URL: https://linuxcontainers.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64
Requires: lxcfs
Conflicts: %rname %rname-libs

Source: %rname.tgz

Patch1: 0002-jessie-systemd-remove-Delegate-flag-to-silence-warni.patch
Patch2: 0003-pve-run-lxcnetaddbr-when-instantiating-veths.patch
Patch3: 0004-deny-rw-mounting-of-sys-and-proc.patch
Patch4: 0005-separate-the-limiting-from-the-namespaced-cgroup-roo.patch
Patch5: 0006-start-initutils-make-cgroupns-separation-level-confi.patch
Patch6: 0007-rename-cgroup-namespace-directory-to-ns.patch
Patch7: 0008-possibility-to-run-lxc-monitord-as-a-regular-daemon.patch
Patch8: 0009-CVE-2017-5985-Ensure-target-netns-is-caller-owned.patch

Patch10: lxc-io.patch
Patch20: lxc-alt.patch
Patch21: lxc-altlinux-lxc.patch

BuildRequires: docbook2X libcap-devel libdbus-devel libgnutls-devel libseccomp-devel libselinux-devel

%description
Containers provides resource management through control groups and
resource isolation through namespaces. The linux containers, lxc, aims
to use these new functionalities to provide an userspace container
object which provides full resource isolation and resource control for
an applications or a system.

%add_findreq_skiplist %_datadir/%rname/lxc-patch.py
%add_findreq_skiplist %_datadir/%rname/templates/*

%prep
%setup -q -n %rname
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1

%patch10 -p1
%patch20 -p1
%patch21 -p1

%build
%autoreconf
%configure \
    --disable-rpath \
    --with-distro=altlinux \
    --with-init-script=systemd \
    --disable-apparmor \
    --enable-selinux \
    --enable-bash \
    --disable-cgmanager \
    --disable-python \
    --disable-lua \
    --disable-examples \
    --enable-seccomp \
    --localstatedir=%_var

echo "#define MAJOR_IN_SYSMACROS 1" >> src/config.h

%make_build

%install
%make DESTDIR=%buildroot install

rm -fr %buildroot/usr/lib/%rname/%rname-apparmor-load

%files
%config(noreplace) %_sysconfdir/sysconfig/%rname
%dir %_sysconfdir/%rname
%config(noreplace) %_sysconfdir/%rname/default.conf
#_sysconfdir/bash_completion.d/%rname
%systemd_unitdir/*.service
%_bindir/%rname-*
%_sbindir/init.%rname
/usr/lib/%rname
%_libdir/%rname
%_libdir/*.so.*
%_datadir/%rname
%_man1dir/*.1*
%_man5dir/*.5*
%_man7dir/*.7*

%changelog
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

