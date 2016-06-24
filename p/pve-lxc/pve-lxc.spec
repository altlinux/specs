%define rname lxc

Name: pve-%rname
Version: 1.1.5
Release: alt1
Summary: Linux containers usersapce tools
Group: System/Configuration/Other
License: LGPL
URL: https://linuxcontainers.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64
Requires: cgmanager lxcfs
Conflicts: %rname > %version %rname-libs > %version

Source: %rname.tgz
Patch0: fix-systemd-service-depends.patch
Patch1: remove-systemd-delegate-flag.patch
Patch2: include-linux-sched.patch
Patch3: use-var-lib-vz-as-default-dir.patch
Patch4: run-lxcnetaddbr.patch
Patch5: 0001-added-stop-hook-entries.patch
Patch6: 0002-run-stop-hook-between-STOPPING-and-STOPPED-states.patch
Patch7: 0003-pass-namespace-handles-to-the-stop-hook.patch
Patch8: 0004-document-the-stop-hook.patch
Patch9: 0005-added-the-unmount-namespace-hook.patch
Patch10: 0006-hooks-put-binary-hooks-in-usr-lib-lxc-hooks.patch
Patch11: delete_network_show_error.diff
Patch13: 0002-Added-lxc.monitor.unshare.patch

Patch20: lxc-alt.patch

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
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch13 -p1

%patch20 -p1

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
%_sysconfdir/bash_completion.d/%rname
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
* Fri Jun 24 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5-alt1
- initial release

