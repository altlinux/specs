Name: mf2b
Version: 1.1
Release: alt3

Summary: Fail2Ban Replacement with Embedded Systems in Mind
License: GPLv3
Group: Security/Networking
Url: https://sourceforge.net/projects/mf2b

Source0: %name-%version.tar
Source1: %name.sysconfig
Source2: %name.init
Source3: README.ALT
Source4: %name.service

Patch0:%name-%version-alt.patch

%description
Micro Fail2Ban acts as a replacement to the well-known Fail2Ban
daemon, but with embedded systems in mind. Therefore it has been
written in pure C and doesn't depend on external libraries to be
present on the target. Despite the similar concept, it's not a drop-in
replacement as configuration syntax aligns more with that of
logrotate.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
%make_install install DESTDIR=%buildroot
install -Dp -m 644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name
install -Dp -m 755 %SOURCE2 %buildroot%_initdir/%name
install -p -m 644 %SOURCE3 .
install -Dp -m 644 %SOURCE4 %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%_unitdir/%name.service
%_initdir/%name
%_sbindir/%name
%config(noreplace) %_sysconfdir/%{name}.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_man5dir/%name.*
%_man8dir/%name.*
%doc README TODO README.ALT

%changelog
* Sat Aug 16 2014 Terechkov Evgenii <evg@altlinux.org> 1.1-alt3
- Tune unit file a bit

* Sat Aug 16 2014 Terechkov Evgenii <evg@altlinux.org> 1.1-alt2
- Systemd unit file added

* Sat Jan 18 2014 Terechkov Evgenii <evg@altlinux.org> 1.1-alt1
- 1.1

* Sun Jan 12 2014 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- 1.0
