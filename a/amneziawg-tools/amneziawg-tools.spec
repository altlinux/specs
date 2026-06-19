Name: amneziawg-tools
Version: 1.0.20260618
Release: alt1
Summary: Fast, modern, secure VPN tunnel
License: GPLv2
Group: System/Servers
URL: https://github.com/amnezia-vpn/amneziawg-tools
VCS: https://github.com/amnezia-vpn/amneziawg-tools
Source0: %name-%version.tar
BuildRequires: systemd

%description
%description
AmneziaWG is a user-friendly VPN solution based on the WireGuard protocol, enhanced with
additional features for seamless integration into the AmneziaVPN ecosystem. It leverages
the same state-of-the-art cryptography as WireGuard (the "Noise" protocol), offering
modern security, high performance, and simplicity compared to traditional VPN solutions
like IPSec and OpenVPN. Designed for versatility, it works equally well on embedded systems,
servers, and desktop environments, prioritizing both speed and ease of configuration.
Like WireGuard, it operates over UDP for efficient data transmission.

This package provides customized management tools (awg) and utilities for configuring
and interacting with AmneziaWG

%prep
%setup

%build
%make_build RUNSTATEDIR=/run -C src

%install
%makeinstall \
	     DESTDIR=%buildroot \
             BINDIR=%_bindir \
	     MANDIR=%_mandir \
	     RUNSTATEDIR=/run \
             WITH_BASHCOMPLETION=yes \
	     WITH_WGQUICK=yes \
	     WITH_SYSTEMDUNITS=yes \
	     -C src

%files
%doc README.md contrib
%_bindir/awg
%_bindir/awg-quick
%dir %_sysconfdir/amnezia
%_sysconfdir/amnezia/amneziawg/
%_datadir/bash-completion/completions/awg
%_datadir/bash-completion/completions/awg-quick
%_unitdir/awg-quick@.service
%_unitdir/awg-quick.target
%_mandir/man8/awg.8*
%_mandir/man8/awg-quick.8*

%changelog
* Fri Jun 19 2026 Anton Farygin <rider@altlinux.org> 1.0.20260618-alt1
- 1.0.20260223 -> 1.0.20260618

* Sat Jun 06 2026 Anton Farygin <rider@altlinux.org> 1.0.20260223-alt1
- 1.0.20250903 -> 1.0.20260223

* Mon Sep 08 2025 Anton Farygin <rider@altlinux.com> 1.0.20250903-alt1
- 1.0.20250903 -> 1.0.20250903

* Mon Jul 21 2025 Anton Farygin <rider@altlinux.com> 1.0.20250706-alt1
- 1.0.20241018 -> 1.0.20250706

* Fri Mar 21 2025 Anton Farygin <rider@altlinux.com> 1.0.20241018-alt1
- initial build for ALT, based on the specfile from upstream git
