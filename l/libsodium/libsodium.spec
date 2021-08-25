# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: libsodium
Summary: A modern, portable, easy to use crypto library
Version: 1.0.18
Release: alt2
License: ISC
Group: System/Libraries
Url: https://libsodium.org/
# 'stable' branch is recommended.
Vcs: https://github.com/jedisct1/libsodium
# Docs: https://doc.libsodium.org/
# Docs vcs: https://github.com/jedisct1/libsodium-doc

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

%package -n libsodium23
Summary: %summary
Group: System/Libraries

%description -n libsodium23
%summary.

%package devel
Summary: Development files for libsodium
Group: Development/C

%description devel
%summary.

%prep
%setup

%build
# libsoidum uses asm() which is not supportable with LTO.
# Adding -ffat-lto-objects is workaround to this problem:
#   https://gcc.gnu.org/bugzilla/show_bug.cgi?id=89147
%global optflags_lto %optflags_lto -ffat-lto-objects

%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall

%check
%make_build check

%files devel
%doc AUTHORS LICENSE README.markdown THANKS
%_libdir/libsodium.so
%_libdir/pkgconfig/libsodium.pc
%_includedir/sodium.h
%_includedir/sodium

%files -n libsodium23
%_libdir/libsodium.so.23*

%changelog
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
