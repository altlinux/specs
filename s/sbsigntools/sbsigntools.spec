Name: sbsigntools
Version: 0.6
Release: alt1

Summary: Canonical EFI binary signing tools
License: GPLv3
Group: System/Kernel and hardware

Source0: %name-%version.tar.gz
Source1: ccan-0.0.2.tar.gz

# Automatically added by buildreq on Thu Nov 01 2012
# optimized out: perl-Encode perl-Locale-gettext pkg-config python3-base
BuildRequires: binutils-devel git-core gnu-efi help2man libssl-devel libuuid-devel python3

ExclusiveArch: x86_64

%description
This package installs tools which can cryptographically sign
EFI binaries and drivers.

Currently it can only sign x86_64 EFI binaries and drivers.

%prep
%setup
%setup -T -D -n %name-%version/lib/ccan.git -a 1
%setup -T -D

%build
NOCONFIGURE=1 ./autogen.sh
%configure
# hack to make sure ccan uses correct config file
cp lib/ccan.git/config.h lib/ccan/
%make_build

%install
%makeinstall_std
find %buildroot -name '*.la' -delete

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Nov 01 2012 Michael Shigorin <mike@altlinux.org> 0.6-alt1
- built for ALT Linux (based on openSUSE package)
