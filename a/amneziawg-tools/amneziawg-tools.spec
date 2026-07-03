Name: amneziawg-tools
Version: 1.0.20260618
Release: alt2
Summary: Fast, modern, secure VPN tunnel
License: GPLv2
Group: System/Servers
URL: https://github.com/amnezia-vpn/amneziawg-tools
VCS: https://github.com/amnezia-vpn/amneziawg-tools
Source0: %name-%version.tar
BuildRequires: systemd

%description
AmneziaWG management tools do not establish VPN connections themselves; they
are designed solely for configuring and controlling the underlying kernel modules.

AmneziaWG is a user-friendly VPN solution based on the WireGuard protocol,
enhanced for seamless integration with the AmneziaVPN ecosystem. It uses modern
cryptography (the Noise protocol), providing strong security, high performance,
and simpler configuration compared to traditional solutions such as IPSec and OpenVPN.

This package includes management tools (awg) and utilities for configuring
and interacting with AmneziaWG.

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
* Fri Jul 03 2026 Anton Farygin <rider@altlinux.org> 1.0.20260618-alt2
- 1.0.20260618 -> 1.0.20260618-2

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
