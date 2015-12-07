#
# spec file for package hashcat
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: hashcat
Version: 2.00
Release: alt1

Summary: CPU-based password recovery utility
License: MIT
Group: System/Base

Url: https://hashcat.net
Source: https://github.com/hashcat/hashcat/archive/%version.tar.gz
Patch1: 0001-fixes-issue-10-compiler-warning-for-possible-memory-.patch
#Git-Clone:	git://github.com/hashcat/hashcat
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libgmp-devel
ExclusiveArch: %ix86 x86_64

%description
Hashcat is an advanced CPU-based password recovery utility,
supporting seven unique modes of testing for over 100 optimized
hashing algorithms.

%prep
%setup
%patch -P 1 -p1

%build
%make_build \
	CFLAGS="%optflags -Iinclude" \
	LIBGMP_POSIX32="%prefix" \
	LIBGMP_POSIX64="%prefix" \
%ifarch x86_64
	posix64
%else
	posix32
%endif

%install
%ifarch x86_64
install -pDm755 hashcat-cli64.bin "%buildroot%_bindir/%name"
%endif
%ifarch %ix86
install -pDm755 hashcat-cli32.bin "%buildroot%_bindir/%name"
%endif

%files
%doc README.md docs/license.txt
%_bindir/%name

%changelog
* Mon Dec 07 2015 Michael Shigorin <mike@altlinux.org> 2.00-alt1
- initial build for ALT Linux Sisyphus (based on openSUSE package)

* Sun Dec  6 2015 jengelh@inai.de
- Initial package for build.opensuse.org (version 2.00)
