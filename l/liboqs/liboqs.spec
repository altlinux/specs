# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: liboqs
Version: 0.10.1
Release: alt1
Summary: C library for prototyping and experimenting with quantum-resistant cryptography
License: MIT and BSD-3-Clause and Apache-2.0 and ALT-Public-Domain and CC0-1.0
Group: System/Libraries
Url: https://openquantumsafe.org/liboqs/
Vcs: https://github.com/open-quantum-safe/liboqs/
# NIST: https://csrc.nist.gov/Projects/post-quantum-cryptography/

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-ninja-build
BuildRequires: astyle
BuildRequires: banner
BuildRequires: chrpath
BuildRequires: cmake
BuildRequires: libssl-devel
BuildRequires: ninja-build
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist

%description
liboqs is part of the Open Quantum Safe (OQS) project led by Douglas
Stebila and Michele Mosca, which aims to develop and integrate into
applications quantum-safe cryptography to facilitate deployment and
testing in real world contexts.

Supported key encapsulation mechanisms (KEMs): BIKE, Classic McEliece,
  FrodoKEM, HQC, CRYSTALS-Kyber, NTRU-Prime.

Supported signature schemes: CRYSTALS-Dilithium, Falcon, SPHINCS+.

Warning: WE DO NOT CURRENTLY RECOMMEND RELYING ON THIS LIBRARY IN A
PRODUCTION ENVIRONMENT OR TO PROTECT ANY SENSITIVE DATA. This library is
meant to help with research and prototyping. While we make a best-effort
approach to avoid security bugs, this library has not received the level
of auditing and analysis that would be necessary to rely on it for high
security use. See Limitations and Security in README.md.

%package devel
Summary: %summary
Group: Development/C
Requires: %name = %EVR

%description devel
Development files for %name.

%package tests
Summary: Tests utilites from liboqs
Group: Development/Tools
Requires: %name = %EVR

%description tests
Tests that run different OQS algorithms.

%prep
%setup
# Add armh to the list of supported arm32 arches.
sed -i '/CMAKE_SYSTEM_PROCESSOR.*armhf/s/")/|armv8l&/' CMakeLists.txt

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
# CMake options https://github.com/open-quantum-safe/liboqs/wiki/Customizing-liboqs
# -DOQS_ENABLE_TEST_CONSTANT_TIME=ON -- does not pass.
%cmake -B build \
	-GNinja \
	-DCMAKE_ASM_FLAGS='%optflags' \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=ON \
	-DOQS_DIST_BUILD=ON \
	-DOQS_OPT_TARGET=generic
%ninja_build -C build --verbose

%install
%ninja_install -C build

cp -a build/tests build-tests
pushd build-tests
find -maxdepth 1 -type f -perm -1 -printf '%%f\n' | xargs -i -n1 mv {} oqs-{}
rename '_' '-' oqs-*_*
rename '_' '-' oqs-*_*
chrpath -k oqs-* | grep RPATH= | cut -d: -f1 | xargs chrpath -d
install -Dp oqs-* -t %buildroot%_bindir
popd

%check
grep -Px '#define OQS_VERSION_TEXT "\Q%version\E"' %buildroot%_includedir/oqs/oqsconfig.h
export LD_LIBRARY_PATH=%buildroot%_libdir
%buildroot/%_bindir/oqs-kat-kem ||:
%buildroot/%_bindir/oqs-kat-sig ||:
banner tests
# Tests require lowercase 'build' dir.
export LD_LIBRARY_PATH=$PWD/build/lib
# https://github.com/open-quantum-safe/liboqs/wiki/Minimal-example-of-a-post-quantum-signature
  cc -Ibuild/include -Lbuild/lib tests/example_sig.c -o example_sig -loqs
  ./example_sig
# https://github.com/open-quantum-safe/liboqs/wiki/Minimal-example-of-a-post-quantum-KEM
  cc -Ibuild/include -Lbuild/lib tests/example_kem.c -o example_kem -loqs
  ./example_kem
time timeout --kill-after=300 200 %ninja_build -C build run_tests

%files
%doc LICENSE.txt README.md RELEASE.md SECURITY.md
%_libdir/liboqs.so.*

%files devel
%doc LICENSE.txt README.md RELEASE.md CONTRIBUTORS CODE_OF_CONDUCT.md
%doc tests/example_*.c docs/algorithms
%_includedir/oqs
%_libdir/cmake/liboqs
%_libdir/liboqs.so
%_pkgconfigdir/liboqs.pc

%files tests
%_bindir/oqs-*

%changelog
* Sat Jun 08 2024 Vitaly Chikunov <vt@altlinux.org> 0.10.1-alt1
- Update to 0.10.1 (2024-06-07).

* Tue Mar 26 2024 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt1
- Update to 0.10.0 (2024-03-23).

* Wed Jan 17 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.2-alt1
- Update to 0.9.2 (2024-01-16).

* Sat Dec 23 2023 Vitaly Chikunov <vt@altlinux.org> 0.9.1-alt1
- Update to 0.9.1 (2023-12-22).

* Fri Oct 13 2023 Vitaly Chikunov <vt@altlinux.org> 0.9.0-alt1
- Update to 0.9.0 (2023-10-12).

* Thu Jul 20 2023 Vitaly Chikunov <vt@altlinux.org> 0.8.0-alt3
- spec: Remove obsolete armh build workaround that isn't suitable for GCC10.

* Mon Jun 12 2023 Vitaly Chikunov <vt@altlinux.org> 0.8.0-alt2
- spec: Update %%description to reflect remaining algorithms list.

* Sun Jun 11 2023 Vitaly Chikunov <vt@altlinux.org> 0.8.0-alt1
- Update to 0.8.0 (2023-06-07).

* Mon Aug 22 2022 Vitaly Chikunov <vt@altlinux.org> 0.7.2-alt1
- Updated to 0.7.2 (2022-08-21).
- Re-enable HQC KEM since it's passed into fourth NIST PQC round. Note that
  this is still non-constant time implementation.
- Re-enable FALCON SIG on armh.
- Rainbow-I and SIKE are removed by upstream due to being broken.

* Sun Jul 03 2022 Vitaly Chikunov <vt@altlinux.org> 0.7.1-alt3
- Disable HQC KEM as it does not build on GCC12 and isn't constant time.
- Disable FALCON SIG on armh because it's so slow that tests didn't finish.

* Sat Mar 26 2022 Vitaly Chikunov <vt@altlinux.org> 0.7.1-alt2
- Fix beekeeper package rebuild (yamllint test failure).

* Mon Dec 20 2021 Vitaly Chikunov <vt@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1 (2021-12-16).
- Build liboqs.so without executable stack.
- Fixed lfs=strict build on 32-bit systems.

* Sat Nov 13 2021 Vitaly Chikunov <vt@altlinux.org> 0.7.0-alt3
- Workaround re-build on GCC 11.

* Mon Aug 30 2021 Vitaly Chikunov <vt@altlinux.org> 0.7.0-alt2
- Increase SOVERSION (to 1) to fix dynamic linking to older libs.

* Sat Aug 14 2021 Vitaly Chikunov <vt@altlinux.org> 0.7.0-alt1
- Update to 0.7.0 (2021-08-11).

* Wed Jun 23 2021 Vitaly Chikunov <vt@altlinux.org> 0.6.0-alt2
- Optimistic port to x86 and ppc64le.

* Thu Jun 10 2021 Vitaly Chikunov <vt@altlinux.org> 0.6.0-alt1
- Update to 0.6.0 (2021-06-08).

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.5.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Fri Mar 12 2021 Vitaly Chikunov <vt@altlinux.org> 0.5.0-alt1
- Update to 0.5.0 (2021-03-10).

* Mon Feb 22 2021 Vitaly Chikunov <vt@altlinux.org> 0.4.0-alt1
- First import of 0.4.0 (2020-08-11) + update (2021-02-18).
