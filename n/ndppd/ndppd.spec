# Spec file for ndppd - NDP Proxy Daemon

Name: ndppd
Version: 0.2.5
Release: alt1

Summary: IPv6 NDP Proxy Daemon

License: %gpl3plus
Group: System/Configuration/Networking
URL: https://github.com/DanielAdolfsson/ndppd

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: %name.service
Source2: %name.init

Patch1:  %name-0.2.5-debian-pid_perms.patch
Patch2:  %name-0.2.5-alt-version.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Mon Jun 28 2021
# optimized out: libstdc++-devel python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4
BuildRequires: gcc-c++

%description
ndppd, or NDP Proxy Daemon, is a daemon that proxies IPv6 NDP
(neighbour discovery) messages. It listens for Neighbor
Solicitation Messages on a specified interface and responds
with Neighbor Advertisement messages in order to allow IPv6
routing as described in RFC 4861 (section 7.2) without relying
on Linux "proxy_ndp",


%prep
%setup -q
%patch0 -p1

%patch1 -p1
%patch2

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-3.0+ %_docdir/%name/LICENSE) LICENSE

%build
%make_build PREFIX=%prefix

%install
%make_install DESTDIR=%buildroot PREFIX=%prefix install

# Configuration file
install -pD -m0644 ndppd.conf-dist %buildroot%_sysconfdir/%name/%name.conf

# Unit file
install -pD -m0644 %SOURCE1 %buildroot%_unitdir/%name.service

# Init file
install -pD -m0755 %SOURCE2 %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README ChangeLog
%doc --no-dereference LICENSE

%attr(750,root,wheel) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf

%_sbindir/%name
%_man1dir/%name.*
%_man5dir/%name.conf.*

%config    %_initdir/%name
%_unitdir/%{name}*.service

%changelog
* Tue Jun 29 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.2.5-alt1
- Initial build for ALT Linux Sisyphus
