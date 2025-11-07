%define _unpackaged_files_terminate_build 1

Name: ananicy-rules
Version: 1.1.6
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
* Fri Nov 07 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.6-alt1
- new version 1.1.6

* Sun Oct 19 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.3-alt1
- new version 1.1.3

* Wed Sep 10 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.0-alt1
- initial build for ALT Sisyphus

