Name: cmdproxyd
Version: 0.1
Release: alt2

Summary: A command proxy daemon
License: GPL
Group: System/Servers
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: %name-%version.tar

PreReq: shadow-utils, service

%description
This is a command proxy daemon.

%prep
%setup -q

%build
%make_build CFLAGS="%optflags -Werror -W"

%install
%make_install install DESTDIR=%buildroot
install -pD -m755 %name.init %buildroot%_initdir/%name
install -pD -m644 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name

%post
/usr/sbin/groupadd -r -f %name
/usr/sbin/useradd -r -g %name -d /dev/null -s /dev/null -n %name >/dev/null 2>&1 ||:
%post_service %name

%preun
%preun_service %name

%files
%config %_initdir/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sbindir/*

%changelog
* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt2
- Reduced macro abuse in specfile.

* Wed May 26 2004 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
