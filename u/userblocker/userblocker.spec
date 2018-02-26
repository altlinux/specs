Name: userblocker
Version: 0.0.1
Release: alt1

Summary: Squid lightsquid based userblocker
License: GPLv3
Group: Networking/WWW

Packager: Timur Batyrshin <erthad@altlinux.org>

Source: %name-%version.tar.bz2

BuildArch: noarch

Requires: ruby ruby-ldap ruby-module-yaml ruby-module-date-time ruby-module-fileutils

BuildRequires: libruby-devel ruby-stdlibs ruby squid-common

%description
UserBlocker is a simple program that blocks and unblocks the LDAP-stored Squid users
according to the traffic statistics collected by LightSquid.

It reads the usernames and blocking policy from LDAP, traffic statistics from LightSquid
reports and generates several text files to use in Squid or redirecotr ACLs.


%prep
%setup -q

%install
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_sysconfdir/cron.d
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_bindir
install -pm 755 %name.rb %buildroot%_bindir/%name
install -pm 640 %name.conf %buildroot%_sysconfdir/%name/%name.conf
install -pm 644 %name.cron %buildroot%_sysconfdir/cron.d/%name

%files
%_bindir/%name
%dir %attr(0775,root,squid) %_localstatedir/%name
%dir %attr(0750,root,squid) %_sysconfdir/%name
%config %attr(0640,root,squid) %_sysconfdir/%name/%name.conf
%config %_sysconfdir/cron.d/%name

%changelog
* Thu Jun 04 2009 Timur Batyrshin <erthad@altlinux.org> 0.0.1-alt1
- initial package build
