Name: sbsigntools
Version: 0.6
Release: alt2

Summary: Canonical EFI binary signing tools
License: GPLv3
Group: System/Kernel and hardware

Source0: %name-%version.tar.gz
Source1: ccan-0.0.2.tar.gz

# Automatically added by buildreq on Thu Nov 01 2012
# optimized out: perl-Encode perl-Locale-gettext pkg-config python3-base
BuildRequires: binutils-devel git-core gnu-efi help2man libssl-devel libuuid-devel python3

# NB: !x86_64 is fake here at the moment,
#     need to have another look at pesign
ExclusiveArch: x86_64 %ix86

%description
%ifarch x86_64
This package installs tools which can cryptographically sign
EFI binaries and drivers.

Currently it can only sign x86_64 EFI binaries and drivers.
%else
This is a dummy package on non-x86_64 platforms.
%endif

%prep
%setup
%ifarch x86_64
%setup -T -D -n %name-%version/lib/ccan.git -a 1
%setup -T -D
%endif

%ifarch x86_64
%build
NOCONFIGURE=1 ./autogen.sh
%configure
# hack to make sure ccan uses correct config file
cp lib/ccan.git/config.h lib/ccan/
%make_build
%endif

%ifarch x86_64
%install
%makeinstall_std
find %buildroot -name '*.la' -delete
%endif

%files
%ifarch x86_64
%_bindir/*
%_man1dir/*
%endif

%changelog
* Thu Jan 10 2013 Michael Shigorin <mike@altlinux.org> 0.6-alt2
- fake 32-bit x86 package (since archdep buildrequires are worse)

* Thu Nov 01 2012 Michael Shigorin <mike@altlinux.org> 0.6-alt1
- built for ALT Linux (based on openSUSE package)
