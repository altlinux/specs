Name: proxychains-ng
Version: 4.16
Release: alt1

Summary: Redirects the connections through SOCKS4a/5 or HTTP proxies

License: GPL-2.0-or-later
Group: Networking/Other
Url: https://github.com/rofl0r/proxychains-ng

VCS: git://github.com/rofl0r/proxychains-ng.git
Source: %name-%version.tar
Source1: %name.watch

Provides: proxychains = %version
Obsoletes: proxychains < %version

%description
ProxyChains is a UNIX program, that hooks network-related libc functions in
DYNAMICALLY LINKED programs via a preloaded DLL (dlsym(), LD_PRELOAD) and
redirects the connections through SOCKS4a/5 or HTTP proxies.

It supports TCP only (no UDP/ICMP etc).

The user configuration is stored in $HOME/.proxychains/proxychains.conf, to run
a command with proxychains:

	proxychains4 command

%prep
%setup

%build
%configure --libdir=%_libdir/%name
%make_build

%install
%makeinstall_std install-config
ln -s proxychains4 %buildroot%_bindir/proxychains

%files
%doc AUTHORS COPYING README

%config(noreplace) %_sysconfdir/proxychains.conf

%_bindir/proxychains
%_bindir/proxychains4
%_bindir/proxychains4-daemon

%dir %_libdir/%name
%_libdir/%name/libproxychains4.so

%changelog
* Mon Jan 24 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.16-alt1
- Updated to 4.16.

* Tue Sep 21 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.15-alt1
- Initial built for ALT Sisyphus.
