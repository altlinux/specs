%define rname lxc

Name: pve-%rname
Version: 2.0.4
Release: alt2
Summary: Linux containers usersapce tools
Group: System/Configuration/Other
License: LGPL
URL: https://linuxcontainers.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64
Requires: cgmanager lxcfs
Conflicts: %rname %rname-libs

Source: %rname.tgz
Patch0: fix-systemd-service-depends.patch
Patch1: remove-systemd-delegate-flag.patch
Patch2: include-linux-sched.patch
Patch3: use-var-lib-vz-as-default-dir.patch
Patch4: run-lxcnetaddbr.patch
Patch5: 0001-tools-move-rcfile-to-the-common-options-list.patch
Patch6: 0002-tools-set-configfile-after-load_config.patch
Patch7: 0003-doc-add-rcfile-to-common-opts.patch

Patch20: lxc-alt.patch
Patch21: lxc-altlinux-lxc.patch

BuildRequires: docbook2X libcap-devel libcgmanager-devel libdbus-devel libgnutls-devel libseccomp-devel libselinux-devel

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

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
    --enable-cgmanager \
    --disable-python \
    --disable-lua \
    --disable-examples \
    --enable-seccomp \
    --localstatedir=%_var

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
* Wed Sep 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0.4-alt2
- added altlinux configs

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Fri Jun 24 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5-alt1
- initial release

