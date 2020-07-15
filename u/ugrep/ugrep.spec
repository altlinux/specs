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
Version: 2.4.1
Release: alt1

Summary: Universal grep: a feature-rich grep implementation with focus on speed
License: BSD-3-Clause
Group: File tools

Url: https://github.com/Genivia/ugrep
Source: https://github.com/Genivia/ugrep/archive/v%version.tar.gz#/%name-%version.tar.gz

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
* Wed Jul 15 2020 Michael Shigorin <mike@altlinux.org> 2.4.1-alt1
- initial build (thx opensuse)

