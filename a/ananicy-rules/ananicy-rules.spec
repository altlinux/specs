%define _unpackaged_files_terminate_build 1

Name: ananicy-rules
Version: 1.1.43
Release: alt1

Summary: List of rules used to assign specific nice values to specific processes

License: GPL-3.0-only
Group: System/Kernel and hardware
Url: https://github.com/CachyOS/ananicy-rules

# Source-url: https://github.com/CachyOS/ananicy-rules/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

ExcludeArch: i586

%description
%summary.

%prep
%setup

%install
install -d %buildroot%_sysconfdir/ananicy.d
cp -rfv 00-default %buildroot%_sysconfdir/ananicy.d/
cp -rfv 00-cgroups.cgroups %buildroot%_sysconfdir/ananicy.d/
cp -rfv 00-types.types %buildroot%_sysconfdir/ananicy.d/
cp -rfv ananicy.conf %buildroot%_sysconfdir/ananicy.d/

%files
%_sysconfdir/ananicy.d/
%config(noreplace) %_sysconfdir/ananicy.d/ananicy.conf
%doc LICENSE
%doc README.md

%changelog
* Mon Jul 06 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.43-alt1
- new version 1.1.43

* Wed Apr 29 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.35-alt1
- new version 1.1.35

* Sat Apr 11 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.34-alt1
- new version 1.1.34

* Sat Mar 28 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.32-alt1
- new version 1.1.32

* Mon Mar 23 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.31-alt1
- new version 1.1.31

* Fri Mar 20 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.30-alt1
- new version 1.1.30

* Wed Feb 18 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.23-alt1
- new version 1.1.23

* Sun Feb 08 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.21-alt1
- new version 1.1.21

* Tue Jan 27 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.20-alt1
- new version 1.1.20

* Sun Jan 11 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.19-alt1
- new version 1.1.19

* Mon Jan 05 2026 Boris Yumankulov <boria138@altlinux.org> 1.1.18-alt1
- new version 1.1.18

* Mon Dec 22 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.15-alt1
- new version 1.1.15

* Sun Nov 30 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.11-alt1
- new version 1.1.11

* Sat Nov 22 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.10-alt1
- new version 1.1.10

* Fri Nov 07 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.6-alt1
- new version 1.1.6

* Sun Oct 19 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.3-alt1
- new version 1.1.3

* Wed Sep 10 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.0-alt1
- initial build for ALT Sisyphus

