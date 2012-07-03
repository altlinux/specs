# -*- coding: latin-1; mode: rpm-spec -*-

Name: lltdscan
Version: 0.0
Release: alt1

Summary: Scan for LLTD-enabled hosts on your network
License: Public Domain
Group: Networking/Other
Url: http://github.com/zed-0xff/lltdscan
Source: %name-%version.tar

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildRequires: libnet2-devel libpcap-devel

%description
LLTD is a Link Layer Topology Discovery Protocol.
protocol specs are available from Microsoft at
http://www.microsoft.com/whdc/connect/Rally/LLTD-spec.mspx

%prep
%setup
%build
make

%install
install -D -m 755 %name %buildroot%_bindir/%name
install -D -m 644 %name.8 %buildroot%_man8dir/%name.8

%files
%_bindir/%name
%_man8dir/%name.*
%doc README

%changelog
* Sat May 14 2011 Terechkov Evgenii <evg@altlinux.org> 0.0-alt1
- Initial build for ALT Linux Sisyphus
