Name: alterator-openvpn-sh-functions    
Version: 1.1
Release: alt1

Summary: Openvpn helper functions
License: GPL-3.0-or-later
Group: System/Base
BuildArch: noarch

Requires: openvpn

Source0: %name

%description
Helper functions for working with Openvpn

%install
install -Dpm 644 %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Wed Sep 02 2026 Mikhail Efremov <sem@altlinux.org> 1.1-alt1
- Sort openvpn lists output (closes: #50237).
- list_*(): Add optional argument for default label name.
- cleanup: remove redundant whitespaces.

* Mon Mar 02 2020 Slava Aseev <ptrnine@altlinux.org> 1.0-alt1
- Initial build for ALT

