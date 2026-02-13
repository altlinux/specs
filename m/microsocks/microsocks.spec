Name: microsocks
Version: 1.0.5
Release: alt1

Summary: Tiny SOCKS5 server

License: MIT
Group: System/Servers
Url: https://github.com/rofl0r/microsocks

# Source-url: https://github.com/rofl0r/microsocks/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: %name.service
Source2: %name.sysconfig

%description
MicroSocks is a multithreaded, small, efficient SOCKS5 server.
It is a SOCKS5 service that you can run on your remote boxes to tunnel
connections through them, if for some reason SSH tunneling is not practical.
It uses threads and the main process consumes only about 600KB of RAM.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
install -Dp -m 0755 microsocks %buildroot%_bindir/microsocks
install -Dp -m 0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -Dp -m 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

%files
%doc COPYING README.md
%_bindir/microsocks
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Fri Feb 13 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- initial build for ALT Sisyphus
