Name: dwall
Version: 0.5.3
Release: alt3
License: GPL
Summary: All-purpose iptables firewall generator
Group: Security/Networking
URL: http://dag.wieers.com/home-made/dwall/
Packager: Denis Medvedev <nbr@altlinux.ru> 
Source0: dwall-%{version}.tar.bz2
Source1: changelog.old
Source2: dwall.init

BuildRequires: iptables
Requires: iptables, iproute, bash

%description
Dwall is a versatile firewall frontend to configure and manage iptables
firewalls. It generates an iptables firewall based on simple config
files. It allows you to give a simple overview of your whole network.

%prep
%setup

%build

%install
%makeinstall

mkdir -p %buildroot%_initdir/
cp %SOURCE2 %buildroot/%_initdir/dwall
mkdir -p %buildroot%_datadir/%name-%version/
cp %SOURCE1 %buildroot%_datadir/%name-%version/changelog.old

%post
/sbin/chkconfig --add dwall
if ! grep -q "/var/log/dwall" /etc/syslog.conf; then
	echo -e "#kern.debug\t\t\t\t\t\t\t/var/log/dwall" >>%_sysconfdir/syslog.conf
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del dwall
fi

%files
%doc AUTHORS ChangeLog EXAMPLE README TODO chains-example/
%_datadir/%name-%version/changelog.old
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/%name/scripts/
%config %_sysconfdir/dwall/services/
%config %_sysconfdir/logrotate.d/*
%config %_initrddir/*
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/backup/
%dir %_sysconfdir/%name/tmp/
%_bindir/*
/usr/lib/%name/


%changelog
* Sun May 04 2008 Denis Medvedev <nbr@altlinux.ru> 0.5.3-alt3
- Bug fixes: init script, interface detection. Icmp, bittorrent rules update . 

* Fri Apr 5 2007 Denis Medvedev <nbr@altlinux.ru> 0.5.3-alt2
- x86_64 spec fixes
* Wed Sep 13 2006 Mikhail Pokidko <pma@altlinux.ru> 0.5.3-alt1
- Initial build
