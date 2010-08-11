Name: cmdproxyd
Version: 0.2
Release: alt1

Summary: A command proxy daemon
License: GPLv2+
Group: System/Servers

Source: %name-%version.tar

PreReq: shadow-utils, service

%description
This is a command proxy daemon.

%prep
%setup

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
* Wed Aug 11 2010 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Minor fixes and enhancements.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt2
- Reduced macro abuse in specfile.

* Wed May 26 2004 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
