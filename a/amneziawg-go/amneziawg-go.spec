Name: amneziawg-go
Version: 0.2.18
Release: alt1
Epoch: 1

Summary: Go Implementation of AmneziaWG
License: MIT
Group: System/Servers

Url: https://amnezia.org/
Vcs: https://github.com/amnezia-vpn/%name
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
go env
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/%name

%changelog
* Thu Jun 11 2026 Nazarov Denis <nenderus@altlinux.org> 1:0.2.18-alt1
- New version 0.2.18.

* Sat Jan 31 2026 Nazarov Denis <nenderus@altlinux.org> 1:0.2.16-alt2
- Update to 0.2.16

* Mon Dec 29 2025 Nazarov Denis <nenderus@altlinux.org> 1:0.2.13-alt2
- Rollback to 0.2.13 for correct work Amnezia VPN with AmneziaWG protocol (ALT #57204)

* Thu Dec 11 2025 Nazarov Denis <nenderus@altlinux.org> 0.2.16-alt1
- New version 0.2.16.

* Mon Dec 08 2025 Artem Semenov <savoptik@altlinux.org> 0.2.15-alt1
- New version 0.2.15.

* Tue Jul 08 2025 Nazarov Denis <nenderus@altlinux.org> 0.2.13-alt1
- New version 0.2.13.

* Sun Aug 18 2024 Nazarov Denis <nenderus@altlinux.org> 0.2.12-alt1
- Initial build for ALT Linux

