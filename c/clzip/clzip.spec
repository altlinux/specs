#
# spec file for package clzip
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2011-2013 Pascal Bleser <pascal.bleser@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: clzip
Version: 1.16
Release: alt1

Summary: Lossless Data Compressor based on LZMA
License: GPL-2.0-or-later
Group: Archiving/Compression

Url: http://www.nongnu.org/lzip/clzip.html
Source: http://download.savannah.gnu.org/releases/lzip/clzip/%name-%version.tar.gz

%description
Clzip is a lossless data compressor based on the LZMA algorithm, with
very safe integrity checking and a user interface similar to that of
gzip or bzip2. Clzip decompresses almost as fast as gzip and
compresses better than bzip2, which makes it well suited for software
distribution and data archiving. Clzip uses the lzip file format; the
files produced by clzip are fully compatible with lzip-1.4 or newer.
Clzip is, in fact, a C language implementation of lzip, intended for
embedded devices or systems lacking a C++ compiler.

%prep
%setup

%build
# not autoconf
./configure \
	--prefix="%prefix" \
	--bindir="%_bindir" \
	--datadir="%_datadir" \
	--infodir="%_infodir" \
	--mandir="%_mandir" \
	--sysconfdir="%_sysconfdir" \
	CFLAGS="%optflags"
%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc COPYING ChangeLog README
%_bindir/clzip
%_man1dir/clzip.1*
%_infodir/clzip.info*

%changelog
* Fri Aug 07 2026 Michael Shigorin <mike@altlinux.org> 1.16-alt1
- initial build for ALT Sisyphus
- adapted from openSUSE 1.16 package with rpmcs
  (original spec by Pascal Bleser and Jan Engelhardt)

