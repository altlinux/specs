#
# spec file for package ugrep
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name: ugrep
Version: 2.5.2
Release: alt1

Summary: Universal grep: a feature-rich grep implementation with focus on speed
License: BSD-3-Clause
Group: File tools

Url: https://github.com/Genivia/ugrep
Source0: https://github.com/Genivia/ugrep/archive/v%version.tar.gz#/<project>-%{version}.tar.gz
Source100: ugrep.watch

BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(zlib)

%description
Ugrep supports an interactive query UI and can search file systems, source
code, text, binary files, archives, compressed files, documents and use
fuzzy search.

%prep
%setup

%build
%ifarch %e2k
# cpuid.h is x86-specific
%add_optflags -UHAVE_SSE2
%endif
%configure \
	--disable-avx \
	--enable-color
%make_build

%install
%makeinstall_std

%check
%make_build test

%files
%doc README.md LICENSE.txt
%_bindir/*
%_man1dir/*.1*
%_datadir/%name

%changelog
* Wed Aug 12 2020 Michael Shigorin <mike@altlinux.org> 2.5.2-alt1
- new version (watch file uupdate)

* Mon Aug 10 2020 Michael Shigorin <mike@altlinux.org> 2.5.1-alt1
- new version (watch file uupdate)

* Tue Jul 28 2020 Michael Shigorin <mike@altlinux.org> 2.5.0-alt1
- 2.5.0
- added debian watch file

* Wed Jul 15 2020 Michael Shigorin <mike@altlinux.org> 2.4.1-alt2
- E2K: ftbfs workaround (SIMD related)

* Wed Jul 15 2020 Michael Shigorin <mike@altlinux.org> 2.4.1-alt1
- initial build (thx opensuse)

