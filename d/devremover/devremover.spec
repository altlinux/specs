# vim: set ft=spec : -*- rpm-spec -*-

Name: devremover
Version: 1.0.0
Release: alt1

Summary: System administration - Remove some devices at system boot

Group: System/Servers
License: GPL
Url: http://etersoft.ru

Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: rpm-build-intro

%description
Remove some devices after system boot.

%prep
%setup

%install
mkdir -p %buildroot%_initddir/
mkdir -p %buildroot%_sysconfdir/
install -D -m750 etc/rc.d/init.d/%name %buildroot%_initdir/%name
install -D -m640 etc/sysconfig/%name %buildroot/%_sysconfigdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc doc
%_initddir/%name
%config(noreplace) %_sysconfigdir/%name

%changelog
* Mon Jul 16 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

* Mon Apr 17 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt7
- Added restore action

* Mon Apr 17 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt6
- Fixed bug in script

* Mon Apr 17 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt5
- Added condstop into script

* Mon Apr 17 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt4
- Added condrestart into script

* Mon Apr 17 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt3
- Added BuildPreReq

* Mon Apr 17 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt2
- Bug fixing

* Mon Apr 17 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt1
- Initial build
