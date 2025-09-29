%define _unpackaged_files_terminate_build 1

Name: falcond
Version: 1.1.7
Release: alt1

Summary: Advanced Linux Gaming Performance Daemon

License: MIT
Group: System/Kernel and hardware
Url: https://git.pika-os.com/general-packages/falcond

# Source-url: https://git.pika-os.com/general-packages/falcond/archive/v%version.tar.gz
Source: %name-%version.tar

ExclusiveArch: %zig_arches

BuildRequires(pre): rpm-macros-zig
BuildRequires: zig

Requires: power-profiles-daemon falcond-profiles scx-scheds

%description
falcond is a powerful system daemon designed to automatically optimize your Linux gaming experience. It intelligently manages system resources and performance settings on a per-game basis, eliminating the need to manually configure settings for each game.

%prep
%setup

%build
cd %name
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
* Mon Sep 29 2025 Boris Yumankulov <boria138@altlinux.org> 1.1.7-alt1
- initial build for ALT Sisyphus

