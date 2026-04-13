%define _unpackaged_files_terminate_build 1

Name: jolt
Version: 1.2.0
Release: alt1

Summary: A terminal-based battery and energy monitor
License: MIT
Group: Monitoring
URL: https://github.com/jordond/jolt

Source: %name-%version.tar
Source1: vendor.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust

%description
Jolt helps laptop users understand what's draining their battery.
It provides real-time insights into power consumption,
process energy usage, and battery health - in a clean, themeable TUI.

%prep
%setup -a 1 -q
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/*
%doc README.md

%changelog
* Thu Apr 09 2026 Sergey Savelev <medovi@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
