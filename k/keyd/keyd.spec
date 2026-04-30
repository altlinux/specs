%define _unpackaged_files_terminate_build 1

Name: keyd
Version: 2.6.0
Release: alt1

Summary: A key remapping daemon for linux.
License: MIT
Group: System/Configuration/Hardware

Url: https://github.com/rvaiya/keyd
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-build-python3

%description
Linux lacks a good key remapping solution. In order to achieve satisfactory
results a medley of tools need to be employed (e.g xcape, xmodmap) with the end
result often being tethered to a specified environment (X11). keyd attempts to
solve this problem by providing a flexible system wide daemon which remaps keys
using kernel level input primitives (evdev, uinput).

%prep
%setup
%patch0 -p1

%build
%make_build PREFIX=%prefix

%install
%makeinstall_std PREFIX=%prefix FORCE_SYSTEMD=1

#install -Dm644 keyd.service -t %buildroot%_unitdir/

# ghost
install -Dm644 /dev/null %buildroot%_sysconfdir/keyd/default.conf

%pre
/usr/sbin/groupadd -r -f keyd ||:

%files
%_bindir/keyd
%_bindir/keyd-application-mapper
%_datadir/keyd
%dir %_sysconfdir/keyd
%ghost %_sysconfdir/keyd/default.conf
%_unitdir/keyd.service
%_sysusersdir/keyd.conf
%_defaultdocdir/keyd
%_man1dir/*

%changelog
* Thu Apr 30 2026 Egor Ignatov <egori@altlinux.org> 2.6.0-alt1
- New version 2.6.0.

* Mon Dec 08 2025 Egor Ignatov <egori@altlinux.org> 2.5.0-alt2
- package /etc/keyd and /etc/keyd/default.conf (closes: #57138)

* Wed Oct 09 2024 Andrey Kovalev <ded@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Wed May 24 2023 Egor Ignatov <egori@altlinux.org> 2.4.3-alt1
- new version 2.4.3

* Tue Jul 26 2022 Egor Ignatov <egori@altlinux.org> 2.4.2-alt1
- new version 2.4.2

* Mon Jun 20 2022 Egor Ignatov <egori@altlinux.org> 2.4.1-alt1
- new version 2.4.1

* Fri May 13 2022 Egor Ignatov <egori@altlinux.org> 2.4.0-alt1.git3421ccaa
- First build for ALT
