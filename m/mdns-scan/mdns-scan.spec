Name:           mdns-scan
Version:        0.5
Release:        alt1
License:        GPLv2
Group:          Networking/DNS
Summary: Sscanning for mDNS/DNS-SD published services on the local network
Source:         %name-%version.tar
%description
Mdns-scan is a tool for scanning for mDNS/DNS-SD published services on
the local network. It issues a mDNS PTR query to the special RR
_services._dns-sd._udp.local for retrieving a list of all currently
registered services on the local link.

Mdns-scan is not a good mDNS citizen since it queries continuously for
services and doesn't implement features like Duplicate Suppression. It
is intended for usage as a debugging tool only.

%prep
%setup

%build
%make

%install
install -D %name %buildroot/%_bindir/%name
install -D %name.1 %buildroot/%_man1dir/%name.1

%files
%doc README.md
%_bindir/*
%_man1dir/*

%changelog
* Fri Nov 06 2026 Fr. Br. George <george@altlinux.org> 0.5-alt1
- Initial build for ALT
