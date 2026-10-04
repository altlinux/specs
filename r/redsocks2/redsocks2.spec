Name: redsocks2
Version: 0.72
Release: alt1

Summary: Transparent redirector of any TCP/UDP connection to proxy

License: Apache-2.0 and GPL-3.0-or-later and LGPL-2.1-or-later
Group: System/Servers
Url: https://github.com/semigodking/redsocks

# Source-url: https://github.com/semigodking/redsocks/archive/refs/tags/release-%version.tar.gz
Source: %name-%version.tar
Source1: %name.sysusers
Patch0: redsocks2-alt-systemd-unit.patch

BuildRequires(pre): rpm-macros-systemd
BuildRequires: libevent-devel libssl-devel

%description
redsocks2 is a modified version of redsocks, a tool that allows you
to redirect any TCP connection to SOCKS or HTTPS proxy using your
firewall, so redirection may be system-wide or network-wide.

In addition to the original redsocks features it supports:
- redirecting TCP connections which are blocked via proxy automatically;
- redirecting UDP traffic via SOCKS5 or Shadowsocks proxy;
- Shadowsocks and HTTPS proxies;
- TCP DNS forwarding;
- transparent proxy with TPROXY.

%prep
%setup
%patch0 -p1

%build
%make_build CFLAGS="%optflags" ENABLE_HTTPS_PROXY=true

%install
install -D -m0755 %name %buildroot%_bindir/%name
install -D -m0640 redsocks.conf.example %buildroot%_sysconfdir/%name.conf
install -D -m0644 %name.service %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_sysconfdir/sysconfig
echo 'REDSOCKS_CONF=%_sysconfdir/%name.conf' > %buildroot%_sysconfdir/sysconfig/%name
install -D -m0644 %SOURCE1 %buildroot%_sysusersdir/%name.conf

%pre
%sysusers_create_package %name %SOURCE1

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc README.md redsocks.conf.example
%_bindir/%name
%attr(0640,root,redsocks) %config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf

%changelog
* Sat Oct 03 2026 Vitaly Lipatov <lav@altlinux.ru> 0.72-alt1
- initial build for Sisyphus
