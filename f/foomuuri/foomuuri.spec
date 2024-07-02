%global _unpackaged_files_terminate_build 1

Name: foomuuri
Version: 0.24
Release: alt1
Summary: Multizone bidirectional nftables firewall
Group: Security/Networking
License: GPL-2.0-or-later
Url: https://github.com/FoobarOy/foomuuri
Vcs: https://github.com/FoobarOy/foomuuri.git
Source: %name-%version.tar
Patch: %name-%version.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-systemd
BuildRequires: python3-module-pylint
BuildRequires: python3-module-dbus
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-pycodestyle
BuildRequires: python3-module-requests
BuildRequires: python3-module-systemd
Requires: nftables
Requires: fping

%description
Foomuuri is a firewall generator for nftables based on the concept of zones.
It is suitable for all systems from personal machines to corporate firewalls,
and supports advanced features such as a rich rule language, IPv4/IPv6 rule
splitting, dynamic DNS lookups, a D-Bus API and FirewallD emulation for
NetworkManager's zone support.

%package firewalld
Summary: FirewallD emulation configuration files for Foomuuri
Group: Security/Networking
BuildArch: noarch
Requires: %name = %EVR
#Conflicts: firewalld

%description firewalld
Foomuuri is a firewall generator for nftables based on the concept of zones.
It is suitable for all systems from personal machines to corporate firewalls,
and supports advanced features such as a rich rule language, IPv4/IPv6 rule
splitting, dynamic DNS lookups, a D-Bus API and FirewallD emulation for
NetworkManager's zone support.

This optional package provides FirewallD D-Bus emulation for Foomuuri,
allowing dynamically assign interfaces to Foomuuri zones via NetworkManager.

%prep
%setup
%autopatch -p1
sed -i \
    -e 's/pycodestyle/pycodestyle.py3/g' \
    -e 's/pylint/pylint.py3/g' \
    test/Makefile

%build
%install
SYSTEMD_SYSTEM_LOCATION=%_unitdir %makeinstall_std

%check
%make test

%post
%tmpfiles_create %name.conf
%post_systemd_postponed foomuuri.service foomuuri-boot.service foomuuri-dbus.service foomuuri-iplist.timer foomuuri-iplist.service foomuuri-monitor.service foomuuri-resolve.timer foomuuri-resolve.service

%preun
%preun_systemd foomuuri.service foomuuri-boot.service foomuuri-dbus.service foomuuri-iplist.timer foomuuri-iplist.service foomuuri-monitor.service foomuuri-resolve.timer foomuuri-resolve.service

%files
%doc README.md CHANGELOG.md COPYING
%_man8dir/%name.8*
%attr(0750, root, adm) %dir %_sysconfdir/%name
%_sbindir/%name
%_sysctldir/50-foomuuri.conf
%_datadir/%name
%exclude %_datadir/%name/dbus-firewalld.conf
%_unitdir/%{name}*
%_tmpfilesdir/%name.conf
%attr(0700, root, root) %dir %_sharedstatedir/%name
%_datadir/dbus-1/system.d/fi.foobar.Foomuuri1.conf

%files firewalld
%_datadir/dbus-1/system.d/fi.foobar.Foomuuri-FirewallD.conf
%_datadir/%name/dbus-firewalld.conf

%changelog
* Tue Jul 02 2024 Alexey Shabalin <shaba@altlinux.org> 0.24-alt1
- Initial build.

