%define _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Summary: Shoreline Firewall is an iptables-based firewall for Linux systems
Name: shorewall-core
Version: 5.2.8
Release: alt2
License: GPLv2
Group: Security/Networking
Source: %name-%version.tar.bz2
Url: http://www.shorewall.net
BuildArch: noarch

Requires: iptables iproute perl-base
Provides: shoreline_firewall = %version-%release
Conflicts: shorewall < 5.1

%description
The Shoreline Firewall, more commonly known as "Shorewall", is a Netfilter
(iptables) based firewall that can be used on a dedicated firewall system,
a multi-function gateway/ router/server or on a standalone GNU/Linux system.

%prep
%setup -n %name-%version
sed -i "s|SERVICEDIR=/lib/systemd/system|SERVICEDIR=%_unitdir|g" shorewallrc.alt

%build
%install
./configure.pl --host=%_vendor \
               --prefix=%prefix \
               --perllibdir=%perl_vendorlib \
               --libexecdir=%_libexecdir \
               --sbindir=%_sbindir

DESTDIR=%buildroot ./install.sh

%files
%doc COPYING INSTALL changelog.txt releasenotes.txt
%dir %_datadir/shorewall
%_datadir/shorewall/*
%dir %_libexecdir/shorewall
%_libexecdir/shorewall/wait4ifup
%_sbindir/shorewall
%_man8dir/*

%changelog
* Tue Jul 02 2024 Alexey Shabalin <shaba@altlinux.org> 5.2.8-alt2
- Fix systemd unit path.

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 5.2.8-alt1
- 5.2.8

* Mon Mar 25 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.3.2-alt1
- 5.2.3.2

* Thu Feb 07 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.2-alt1
- 5.2.2

* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.1.4-alt1
- 5.2.1.4

* Fri Nov 16 2018 Alexey Shabalin <shaba@altlinux.org> 5.2.1.1-alt1
- 5.2.1.1

* Sat Jul 14 2018 Alexey Shabalin <shaba@altlinux.ru> 5.2.1-alt0.Beta2
- Initial build for 5.2.1-Beta2
