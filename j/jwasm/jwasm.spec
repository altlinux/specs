#
# spec file for package jwasm
#
# Copyright (c) 2013 Peter Conrad
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name: jwasm
Version: 2.12
Release: alt1
License: Sybase Open Watcom Public License
Summary: MASM-compatible assembler
Url: http://jwasm.github.io/
Group: Development/Other
# https://github.com/JWasm/JWasm
Source: %name-%version.tar
# PATCH-FIX-UPSTREAM conrad@quisquis.de
Patch: jwasm-undef.patch
# PATCH-FIX-UPSTREAM conrad@quisquis.de
Patch1: jwasm-bof.patch

# Automatically added by buildreq on Wed Nov 30 2016
# optimized out: python-base
BuildRequires: dos2unix unzip

%description
JWasm is a free MASM-compatible assembler with these features:

* native support for output formats Intel OMF, MS Coff (32/64-bit),
  Elf (32/64-bit), Binary, Windows PE (32/64-bit) and DOS MZ.
* Instructions up to AVX are supported.
* JWasm is written in C. The source is portable and has successfully been
  tested with Open Watcom, MS VC, GCC and more.
* C header files can be converted to include files for JWasm with h2incX.
* JWasm's source code is released under the Sybase Open Watcom Public License,
  which allows free commercial and non-commercial use.

JWasm started as a fork of Open Watcom's Wasm in March 2008. Today, the part of
Wasm source lines still contained in JWasm is approximately 0.2

%prep
%setup
%patch -p1
%patch1 -p1
sed -i '/instruction table/a#include "expreval.h"' H/parser.h

%build
dos2unix *.txt Doc/*
%ifarch x86_64
IS_64=-DLONG_IS_64BITS
%endif
make DEBUG=1 extra_c_flags="%optflags -DDEBUG_OUT -fno-strict-aliasing $IS_64" -f GccUnix.mak GccUnixD GccUnixD/omfint.o
%make_build DEBUG=1 extra_c_flags="%optflags -DDEBUG_OUT $IS_64" -f GccUnix.mak

%install
install -D GccUnixD/jwasm %buildroot%_bindir/jwasm

%files
%doc *.txt Doc/* Regress
%_bindir/%name

%changelog
* Wed Nov 30 2016 Fr. Br. George <george@altlinux.ru> 2.12-alt1
- Update to GH current version
- Copy Regression sources

* Wed Nov 30 2016 Fr. Br. George <george@altlinux.ru> 2.11-alt1
- Initial build from FC19
* Sat Nov 30 2013 conrad@quisquis.de
- Upgrade to upstream-2.11a
* Wed Apr 24 2013 conrad@quisquis.de
- Fixed x86_64 build
- Fixed debug packages
* Mon Apr 22 2013 conrad@quisquis.de
- Upgrade to upstream-2.10
* Fri Apr 19 2013 conrad@quisquis.de
- Fixed Group header
* Fri Apr 19 2013 conrad@quisquis.de
- Added bof patch
- Avoid strict-aliasing warning in one file
* Fri Apr 19 2013 conrad@quisquis.de
- Added undef patch
* Fri Apr 19 2013 conrad@quisquis.de
- Initial project creation
