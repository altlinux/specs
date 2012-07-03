Name: had
Version: 1.0.8
Release: alt2

Summary: High Aviability Daemon
License: BSD
Group: System/Servers
Packager: Eugene Prokopiev <enp@altlinux.ru>

PreReq: chkconfig

Source0: %name-%version.tar.bz2

BuildRequires: service
Requires: service

%description
High Aviability Daemon

%prep
%setup

%build
cd src
%make_build

%install
%__mkdir_p %buildroot/%_sbindir
%__mkdir_p %buildroot/%_initdir
%__mkdir_p %buildroot/%_sysconfdir/%name/hasrv

%__install -m 0755 src/%name %buildroot/%_sbindir/%name
%__install -m 0755 %name.init %buildroot/%_initdir/%name
%__install -m 0755 conf/hasrv/* %buildroot/%_sysconfdir/%name/hasrv/
%__install -m 0644 conf/*.conf %buildroot/%_sysconfdir/%name/

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/*
%_initdir/*
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/hasrv/
%config(noreplace) %_sysconfdir/%name/hasrv/*
%config(noreplace) %_sysconfdir/%name/*.conf
%doc docs

%changelog
* Thu Sep 27 2007 Eugene Prokopiev <enp@altlinux.ru> 1.0.8-alt2
- minor spec changes - thanks to php-coder@

* Fri Aug 17 2007 Eugene Prokopiev <enp@altlinux.ru> 1.0.8-alt1
- new version

* Fri Mar 30 2007 Eugene Prokopiev <enp@altlinux.ru> 1.0.6-alt1
- Initial build for Sisyphus - thanx to dfo@


