%define _unpackaged_files_terminate_build 1
%define commit 56f49e5f51074d9b851e9e7f5d72e3c79d50d1a3
%define shortcommit %(c=%commit; echo ${c:0:7})

Name: falcond-profiles
Version: 1.0
Release: alt1.git%shortcommit

Summary: List of rules used in falcond

License: MIT
Group: System/Kernel and hardware
Url: https://github.com/PikaOS-Linux/falcond-profiles

# Source-url: https://github.com/PikaOS-Linux/falcond-profiles.git
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
* Mon Sep 29 2025 Boris Yumankulov <boria138@altlinux.org> 1.0-alt1.git56f49e5
- initial build for ALT Sisyphus

