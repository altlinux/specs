%define _unpackaged_files_terminate_build 1
%define commit a3e0e63303c0a310a504c5f3e2a9d71496d7aaab
%define shortcommit %(c=%commit; echo ${c:0:7})

Name: falcond-profiles
Version: 1.0
Release: alt3.git%shortcommit

Summary: List of rules used in falcond

License: MIT
Group: System/Kernel and hardware
Url: https://github.com/PikaOS-Linux/falcond-profiles

# Source-url: https://github.com/PikaOS-Linux/falcond-profiles/archive/%commit.tar.gz?/falcond-profiles-%commit.tar.gz
Source: %name-%version.tar

ExclusiveArch: %zig_arches

BuildRequires(pre): rpm-macros-zig

%description
%summary.

%prep
%setup

%build
%install
mkdir -p %buildroot%_datadir/falcond/
mkdir -p %buildroot%_datadir/falcond/profiles/
mkdir -p %buildroot%_datadir/falcond/profiles/handheld/
mkdir -p %buildroot%_datadir/falcond/profiles/htpc/
cp -a usr/share/falcond/system.conf %buildroot%_datadir/falcond/
cp -a usr/share/falcond/profiles/* %buildroot%_datadir/falcond/profiles/
cp -a usr/share/falcond/profiles/handheld/* %buildroot%_datadir/falcond/profiles/handheld/
cp -a usr/share/falcond/profiles/htpc/* %buildroot%_datadir/falcond/profiles/htpc/

%files
%doc LICENSE
%doc README.md
%_datadir/falcond/system.conf
%_datadir/falcond/profiles/*.conf
%_datadir/falcond/profiles/handheld/*.conf
%_datadir/falcond/profiles/htpc/*.conf

%changelog
* Sat Mar 28 2026 Boris Yumankulov <boria138@altlinux.org> 1.0-alt3.gita3e0e63
- updated to upstream git a3e0e63

* Mon Jan 05 2026 Boris Yumankulov <boria138@altlinux.org> 1.0-alt2.git0f87c74
- updated to upstream git 0f87c74
- pin commit to 0f87c748cf34a9bcbc4351ad051bcef8cce79158

* Mon Sep 29 2025 Boris Yumankulov <boria138@altlinux.org> 1.0-alt1.git56f49e5
- initial build for ALT Sisyphus

