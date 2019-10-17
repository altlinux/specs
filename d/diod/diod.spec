Name: diod
Version: 1.0.24.0.53.git0d87511
Release: alt2

Summary: multi-threaded, userspace file server that speaks 9P2000.L protocol

License: GPL-2.0-or-later
Group: Networking/Other
Url: https://github.com/chaos/diod

# https://github.com/chaos/diod
Source: %name-%version.tar
Source1: diod.init
Patch1: diod-alt-configure-ac-version.patch
Patch2: diod-alt-Makefile-am-fix-double-slash-in-path.patch
Patch3: diod-alt-rundir.patch
Patch4: diod-alt-service-reload.patch

# FIXME: build against munge (missing build dependency)
BuildRequires: libattr-devel libcap-devel liblua5.1-devel libncurses-devel libpopt-devel

%description
This package contains diod, a multi-threaded, user space file server
that speaks 9P2000.L protocol.

%prep
%setup
%autopatch -p1

%build
%autoreconf
export CFLAGS="%optflags"
%configure
%make_build

%install
%makeinstall_std systemddir=%_unitdir
install -pm755 %SOURCE1 -D %buildroot%_initdir/diod
ln -s diodmount %buildroot%_sbindir/mount.diod
ln -s diodmount.8 %buildroot%_man8dir/mount.diod.8

%files
%doc AUTHORS COPYING NEWS README.md
%config(noreplace) %_sysconfdir/auto.diod
%config(noreplace) %_sysconfdir/diod.conf
%_sbindir/*
%_man5dir/*
%_man8dir/*
%_initdir/diod
%_unitdir/diod.service

%changelog
* Thu Oct 17 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.0.24.0.53.git0d87511-alt2
- Fixed rundir patch.

* Sun Oct 13 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.0.24.0.53.git0d87511-alt1
- Initial build for ALT Sisyphus.
