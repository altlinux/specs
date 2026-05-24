%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define soname 42

Name: libtorrent
Epoch: 3
Version: 0.16.12
Release: alt1
Summary: libTorrent is a BitTorrent library written in C++ for *nix
Group: System/Libraries
# "libtorrent/src/utils/sha_fast.{cc,h}" is originally from the
# Mozilla NSS and is under a triple license; MPL, LGPL and GPL
License: GPLv2+ AND LGPL-2.1 AND MPL-1.1
Url: https://github.com/rakshasa/libtorrent
Vcs: https://github.com/rakshasa/libtorrent.git
Source: %name-%version.tar

Patch0: %name-alt-skip-tests.patch
Patch1: %name-utils-add-missing-inc.patch

BuildRequires: gcc-c++ cppunit-devel zlib-devel libcurl-devel libssl-devel

%def_disable static

%description
High performance torrent library for multiple clients.

LibTorrent is a BitTorrent library written in C++ for *nix, with a focus on
high performance and good code. The library differentiates itself from other
implementations by transferring directly from file pages to the network stack.

%package -n %name%soname
Summary: Development libraries and header files for libTorrent
Group: System/Libraries

%description -n %name%soname
High performance torrent library for multiple clients.

LibTorrent is a BitTorrent library written in C++ for *nix, with a focus on
high performance and good code. The library differentiates itself from other
implementations by transferring directly from file pages to the network stack.

%package devel
Summary: Development libraries and header files for libTorrent
Group: Development/C
Requires: %name%soname = %EVR
Conflicts: libtorrent-rasterbar-devel

%description devel
The libtorrent-devel package contains libraries and header files needed
to develop applications using libTorrent.

%prep
%setup
%ifarch %e2k
sed -i "/private:/{N;s|private:||;s|$|private:|}" src/torrent/poll_select.h
%endif
%autopatch -p1

mv -f COPYING COPYING.orig
ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# ix86 fails on test_extents::test_basic
%ifnarch %ix86
%check
%make_build check
%endif

%files -n %name%soname
%doc AUTHORS README.md
%doc --no-dereference COPYING
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Sun May 24 2026 L.A. Kostis <lakostis@altlinux.ru> 3:0.16.12-alt1
- 0.16.12.

* Fri Jan 23 2026 L.A. Kostis <lakostis@altlinux.ru> 3:0.16.6-alt1
- 0.16.6.

* Thu Dec 11 2025 L.A. Kostis <lakostis@altlinux.ru> 3:0.16.5-alt1
- 0.16.5.

* Mon Nov 17 2025 L.A. Kostis <lakostis@altlinux.ru> 3:0.16.2-alt1
- 0.16.2.
- BR: simplify according current upstream requirements.

* Tue Sep 02 2025 L.A. Kostis <lakostis@altlinux.ru> 3:0.15.6-alt1
- 0.15.6.

* Sat Jun 28 2025 L.A. Kostis <lakostis@altlinux.ru> 3:0.15.5-alt1
- 0.15.5.

* Thu Jun 19 2025 L.A. Kostis <lakostis@altlinux.ru> 3:0.15.4-alt1
- 0.15.4.

* Fri May 30 2025 L.A. Kostis <lakostis@altlinux.ru> 3:0.15.3-alt1
- 0.15.3.

* Sat Apr 19 2025 L.A. Kostis <lakostis@altlinux.ru> 3:0.15.2-alt1
- 0.15.2.
- Bump soname.
- Update licences.
- torrent/utils: add missing <algorithm>.

* Thu Feb 20 2025 L.A. Kostis <lakostis@altlinux.ru> 3:0.15.1-alt1
- 0.15.1.

* Wed Oct 16 2024 L.A. Kostis <lakostis@altlinux.ru> 3:0.14.0-alt1
- 0.14.0.
- Bump soname.
- Skip network tests (due hsh env).
- Skip tests on ix86 (failed on test_extents::test_basic).

* Mon Sep 20 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3:0.13.8-alt3
- Fixed build for Elbrus.

* Wed Sep 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3:0.13.8-alt2
- Disabled LTO.

* Thu Jun 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3:0.13.8-alt1
- Updated to upstream version 0.13.8.

* Wed Sep 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3:0.13.7-alt1
- Updated to upstream version 0.13.7.
- Applied patch for support of openssl-1.1.

* Wed Jan 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3:0.13.6-alt2
- Fixed build with new cppunit.
- Enabled tests.

* Mon Nov 09 2015 Afanasov Dmitry <ender@altlinux.org> 3:0.13.6-alt1
- 0.13.6

* Tue Mar 11 2014 Denis Smirnov <mithraen@altlinux.ru> 3:0.13.3-alt1
- 0.13.3
