Name: amneziawg-go
Version: 0.2.12
Release: alt1

Summary: Go Implementation of AmneziaWG
License: MIT
Group: System/Servers

Url: https://amnezia.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/amnezia-vpn/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# go mod vendor
Source1: vendor.tar

BuildRequires: golang
BuildRequires: python3

%description
AmneziaWG is a contemporary version of the WireGuard protocol. It's a fork of WireGuard-Go and offers protection
against detection by Deep Packet Inspection (DPI) systems. At the same time, it retains the simplified architecture and
high performance of the original.

The precursor, WireGuard, is known for its efficiency but had issues with detection due to its distinctive packet
signatures. AmneziaWG addresses this problem by employing advanced obfuscation methods, allowing its traffic to
blend seamlessly with regular internet traffic. As a result, AmneziaWG maintains high performance while adding an
extra layer of stealth, making it a superb choice for those seeking a fast and discreet VPN connection.

%prep
%setup -a 1

%build
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/%name

%changelog
* Sun Aug 18 2024 Nazarov Denis <nenderus@altlinux.org> 0.2.12-alt1
- Initial build for ALT Linux

