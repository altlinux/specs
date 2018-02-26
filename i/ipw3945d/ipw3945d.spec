%define module_name     ipw3945
%define module_version  1.7.22

Name: ipw3945d
Version: 1.7.22
Release: alt1
Packager: Alex Karpov <karpov@altlinux.ru>

Summary: Intel PRO/Wireless 3945ABG network connection regulatory daemon
License: Distributable
Group: System/Servers
Url: http://bughost.org/ipw3945/

Source0: http://bughost.org/ipw3945/daemon/%name-%version.tgz
Source1: %name.init
Source2: %name.sysconfig

%description
Daemon for Intel PRO/Wireless 3945ABG network controller handling

%prep
%setup -q

%install
%ifnarch x86_64
install -pD x86/%name %buildroot%_sbindir/%name
%else
install -pD x86_64/%name %buildroot%_sbindir/%name
%endif

install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/%name.log

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE.ipw3945d README.ipw3945d
%_sysconfdir/sysconfig/%name
%attr (755,root,root) %_sbindir/%name
%attr (755,root,root) %_initdir/%name
%ghost %_logdir/%name.log

%changelog
* Tue Apr 10 2007 Alex Karpov <karpov@altlinux.ru> 1.7.22-alt1
- 1.7.22
- bug 10728 fixed

* Tue Jun 20 2006 Grigory Batalov <bga@altlinux.ru> 1.7.19-alt1
- 1.7.19.

* Thu Jun 08 2006 Grigory Batalov <bga@altlinux.ru> 1.7.18-alt2
- Initscript cleanup.
- Logfile was added.

* Tue Apr 25 2006 Grigory Batalov <bga@altlinux.ru> 1.7.18-alt1
- Initial ALTLinux release.
