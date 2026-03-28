%define _unpackaged_files_terminate_build 1

Name: falcond
Version: 2.0.1
Release: alt1

Summary: Advanced Linux Gaming Performance Daemon

License: MIT
Group: System/Kernel and hardware
Url: https://git.pika-os.com/general-packages/falcond

# Source-url: https://git.pika-os.com/general-packages/falcond/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

ExclusiveArch: %zig_arches

BuildRequires(pre): rpm-macros-zig
BuildRequires: zig

Requires: ppd-service falcond-profiles scx-scheds

%description
falcond is a powerful system daemon designed to automatically optimize your Linux gaming experience. It intelligently manages system resources and performance settings on a per-game basis, eliminating the need to manually configure settings for each game.

%prep
%setup -a1

%build
cd %name
cp -r ../zig-cache ./
%zig_build

%install
cd %name
mkdir -p %buildroot%_unitdir/
install -Dm644 debian/falcond.service %buildroot%_unitdir
%zig_install

%files
%doc LICENSE
%doc README.md
%_bindir/falcond
%_unitdir/falcond.service


%changelog
* Sat Mar 28 2026 Boris Yumankulov <boria138@altlinux.org> 2.0.1-alt1
- new version 2.0.1
- replace power-profiles-daemon to ppd-service

* Thu Jan 08 2026 Boris Yumankulov <boria138@altlinux.org> 1.2.3-alt1
- new version 1.2.3

* Mon Jan 05 2026 Boris Yumankulov <boria138@altlinux.org> 1.2.2-alt1
- new version 1.2.2

* Sun Oct 19 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.9-alt1
- new version 1.1.9

* Mon Sep 29 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.7-alt1
- initial build for ALT Sisyphus

