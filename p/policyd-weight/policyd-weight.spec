%define policyd_weight_user _policyd_weight
%define policyd_weight_group _policyd_weight
%define policyd_weight_home /dev/null

Name: policyd-weight
Version: 0.1.14.17
Release: alt2

Summary: A policy daemon for postfix, allows you to score DNSBLs, HELO, MAIL FROM, Client IP Addresses before queuing
License: GPL
Group: System/Servers

Url: http://policyd-weight.org
Source0: %name-%version.tar
Source1: %name.init
Source2: README.ALT
BuildArch: noarch

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

BuildPreReq: perl-base, perl-Net-DNS

%description
A perl script for the postfix MTA to eliminate most forged envelope sender and
HELOs (i.e. Bogus Mails). Allows you to score DNSBLs, HELO, MAIL FROM, Client IP
Addresses before any queuing is done. Allows you to REJECT messages wich have a
score higher than allowed.

%prep
%setup

%build

%install
install -d -m1775 %buildroot%_var/run/%name
install -pD -m0755 %name %buildroot%_sbindir/%name
install -pD -m0644 %name.conf.sample %buildroot%_sysconfdir/%name.conf
install -pD -m0644 %SOURCE2 README.ALT

install -pD -m0755 %SOURCE1 %buildroot%_initdir/%name

install -pD -m0644 man/man5/%name.conf.5 %buildroot%_man5dir/%name.conf.5
install -pD -m0644 man/man8/%name.8 %buildroot%_man8dir/%name.8

%pre
/usr/sbin/groupadd -r -f %policyd_weight_group ||:
/usr/sbin/useradd -g %policyd_weight_group -c 'The Policyd-weight Daemon' \
        -d %policyd_weight_home -s /dev/null -r %policyd_weight_user >/dev/null 2>&1 ||:
	
%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/%name
%_initdir/%name
%config(noreplace) %_sysconfdir/%name.conf
%dir %attr(1775,root,%policyd_weight_group) %_var/run/%name
%doc documentation.txt changes.txt todo.txt README*
%_mandir/man?/*

%changelog
* Thu Jun 11 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.1.14.17-alt2
- Fixed manpage installation path (Closes: #19830)

* Wed Aug 20 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.1.14.17-alt1
- Updated to 0.1.14 beta17
- Add initscript (due to change start model from postfix-spawn to daemon)

* Fri Jun 08 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 0.1.14.5-alt1
- Updated to 0.1.14 beta5

* Thu Dec 29 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.1.12-alt1.beta4
- Updated to 0.1.12 beta4

* Thu Dec 15 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.1.12-alt1.beta3
- Updated to 0.1.12 beta3

* Mon Dec 12 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.1.12-alt1
- New version
- Run as %policyd_weight_user instead of nobody
- Do not use some macroses anymore (%%__install)
- Updated default config
- Updated README.ALT

* Mon Nov 14 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.1.11-alt1
- Initial build for Sisyphus
