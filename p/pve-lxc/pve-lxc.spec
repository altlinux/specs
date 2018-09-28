%define rname lxc

Name: pve-%rname
Version: 3.0.2
Release: alt2
Summary: Linux containers usersapce tools
Group: System/Configuration/Other
License: LGPL
URL: https://linuxcontainers.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64
Requires: lxcfs
Conflicts: %rname %rname-libs

Source: %rname-%version.tar.gz
Source1: %rname-config.tar

Patch1: 0001-PVE-Config-lxc.service-start-after-a-potential-syslo.patch
Patch2: 0002-PVE-Down-run-lxcnetaddbr-when-instantiating-veths.patch
Patch3: 0003-PVE-Config-deny-rw-mounting-of-sys-and-proc.patch
Patch4: 0004-PVE-Up-separate-the-limiting-from-the-namespaced-cgr.patch
Patch5: 0005-PVE-Up-start-initutils-make-cgroupns-separation-leve.patch
Patch6: 0006-PVE-Config-rename-cgroup-namespace-directory-to-ns.patch
Patch7: 0007-PVE-Up-possibility-to-run-lxc-monitord-as-a-regular-.patch
Patch8: 0008-PVE-Deprecated-Make-lxc-.service-forking.patch
Patch9: 0001-confile-add-lxc.monitor.signal.pdeath.patch
Patch10: 0002-tests-add-lxc.monitor.signal.pdeath.patch
Patch11: 0003-doc-Translate-lxc.monitor.signal.pdeath-into-Japanes.patch
Patch12: 0004-apparmor-profile-generation.patch
Patch13: 0005-tests-add-test-for-generated-apparmor-profiles.patch
Patch14: 0006-conf-fix-path-lxcpath-mixups-in-tty-setup.patch

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
%setup -q -n %rname-%version -a1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

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
    --disable-examples \
    --enable-seccomp \
    --localstatedir=%_var

%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/lxc/config
for i in config/*.conf.in; do
	sed -e "s|@LXCTEMPLATECONFIG@|%_datadir/lxc/config|g" $i > %buildroot%_datadir/lxc/${i%.in};
done

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

