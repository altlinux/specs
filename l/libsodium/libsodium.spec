# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define sover 26
Name: libsodium
Summary: A modern, portable, easy to use crypto library
Version: 1.0.19
Release: alt1
License: ISC
Group: System/Libraries
Url: https://libsodium.org/
# 'stable' branch is recommended.
# About versioning https://github.com/jedisct1/libsodium/discussions/1136#discussioncomment-7012438
Vcs: https://github.com/jedisct1/libsodium
# Docs: https://doc.libsodium.org/

Source: %name-%version.tar

%description
Sodium is a new, easy-to-use software library for encryption, decryption,
signatures, password hashing and more.

It is a portable, cross-compilable, installable, packageable fork of
NaCl, with a compatible API, and an extended API to improve usability
even further.

Its goal is to provide all of the core operations needed to build
higher-level cryptographic tools.

The design choices emphasize security and ease of use. But despite the
emphasis on high security, primitives are faster across-the-board than
most implementations.

%package -n libsodium%sover
Summary: %summary
Group: System/Libraries
# Will be used for kinds like python3-module-libnacl
Provides: libsodium = %EVR

%description -n libsodium%sover
%summary.

%package devel
Summary: Development files for libsodium
Group: Development/C
Requires: libsodium%sover = %EVR

%description devel
%summary.

%package checkinstall
Summary: CI tests for %name
Group: Development/Other
BuildArch: noarch
Requires(post): gcc
Requires(post): libsodium-devel = %EVR

%description checkinstall
%summary.

Check that libsodium-devel basically works before we start building other
packages.

%prep
%setup

%build
# libsoidum uses asm() which is not supportable with LTO.
# Adding -ffat-lto-objects is workaround to this problem:
#   https://gcc.gnu.org/bugzilla/show_bug.cgi?id=89147
%global optflags_lto %optflags_lto -ffat-lto-objects
%ifarch x86_64
%add_optflags -fanalyzer
%endif
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall

%check
%make_build check

%post checkinstall
set -xeuo pipefail
tmp=$(mktemp -d)
cd $tmp && trap "rm -vrf $tmp" 0
cat > test.c <<"EOF"
#include <sodium.h>
#include <stdio.h>
int main(void) { return printf("%s\n", sodium_version_string()), sodium_init(); }
EOF
gcc -Wall -Werror -o test test.c $(pkg-config libsodium --libs)
./test
# Double check that internal version is correct one.
./test | grep -Fx "%version"

%files devel
%doc AUTHORS LICENSE README.markdown THANKS ChangeLog
%_libdir/libsodium.so
%_libdir/pkgconfig/libsodium.pc
%_includedir/sodium.h
%_includedir/sodium

%files -n libsodium%sover
%_libdir/libsodium.so.%{sover}*

%files checkinstall

%changelog
* Fri Sep 15 2023 Vitaly Chikunov <vt@altlinux.org> 1.0.19-alt1
- Update to 1.0.19 (2023-09-13).
- Provide libsodium name for packages like python3-module-libnacl.
- Enable LFS on 32-bit systems.
- Add checkinstall package with a basic build test.

* Thu Aug 26 2021 Vitaly Chikunov <vt@altlinux.org> 1.0.18-alt2
- Do not build libsodium-devel-static package.
- spec: Fix build with LTO.

* Tue May 25 2021 Vitaly Chikunov <vt@altlinux.org> 1.0.18-alt1
- Update to 1.0.18 (2019-05-30).

* Sun Feb 11 2018 Denis Smirnov <mithraen@altlinux.ru> 1.0.16-alt1
- new version 1.0.16

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 1.0.12-alt1
- new version 1.0.12

* Tue Oct 27 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt1
- new version 1.0.5

* Wed Oct 21 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.4-alt1
- new version 1.0.4

* Sat Jan 17 2015 Denis Smirnov <mithraen@altlinux.ru> 1.0.2-alt1
- new version 1.0.2

* Tue Nov 25 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt1
- new version 1.0.1

* Fri Sep 26 2014 Denis Smirnov <mithraen@altlinux.ru> 1.0.0-alt1
- new version 1.0.0

* Mon Sep 22 2014 Denis Smirnov <mithraen@altlinux.ru> 0.7.1-alt1
- new version 0.7.1

* Mon Aug 25 2014 Denis Smirnov <mithraen@altlinux.ru> 0.7.0-alt1
- new version 0.7.0

* Sat Jul 26 2014 Denis Smirnov <mithraen@altlinux.ru> 0.6.1-alt1
- new version 0.6.1

* Fri Jul 04 2014 Denis Smirnov <mithraen@altlinux.ru> 0.6.0-alt1
- new version 0.6.0

* Wed Jun 25 2014 Denis Smirnov <mithraen@altlinux.ru> 0.5.0-alt1
- first build for Sisyphus
