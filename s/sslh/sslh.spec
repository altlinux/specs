Name: sslh
Version: 1.18
Release: alt2

Summary: A ssl/ssh multiplexer

License: GPL
Group: System/Servers
Url: http://www.rutschle.net/tech/sslh.shtml

# Source-url: http://www.rutschle.net/tech/sslh/sslh-v%version.tar
Source: %name-%version.tar
Source1: sslh.init
Source2: sslh.config

#BuildRequires: tcpd-devel perl gcc make gzip

# Automatically added by buildreq on Sat Aug 04 2012
# optimized out: perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators
BuildRequires: libconfig-devel perl-Pod-Parser

%description
sslh lets one accept both HTTPS and SSH connections on the
same port. It makes it possible to connect to an SSH server
on port 443 (e.g. from inside a corporate firewall) while
still serving HTTPS on that port.

Author: Yves Rutschle

%prep
%setup

%build
%make_build

%install
%makeinstall PREFIX=%buildroot%prefix
install -D -m 644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -D -m 755 %SOURCE1 %buildroot%_initdir/%name
install -D -m 644 scripts/systemd.sslh.service %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md
%_man8dir/sslh.8.*
%_sbindir/sslh
%_unitdir/%name.service
%config(noreplace) %_initdir/sslh
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Wed Dec 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.18-alt2
- pack .service file

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.18-alt1
- new version (1.18) with rpmgs script

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.17-alt1
- new version 1.17 (with rpmrb script)

* Wed Sep 24 2014 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt1
- new version 1.16 (with rpmrb script)

* Sat Aug 04 2012 Vitaly Lipatov <lav@altlinux.ru> 1.13b-alt1
- new version (1.13b) with rpmgs script

* Sat Aug 04 2012 Vitaly Lipatov <lav@altlinux.ru> 1.6g-alt1
- initial build for ALT Linux Sisyphus

* Sun Jan 18 2009 Holger Manthey <holger.manthey@web.de>
- Initial spec file
