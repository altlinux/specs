# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: liboqs
Version: 0.7.1
Release: alt1
Summary: C library for prototyping and experimenting with quantum-resistant cryptography
License: MIT
Group: System/Libraries
Url: https://openquantumsafe.org/liboqs/
Vcs: https://github.com/open-quantum-safe/liboqs/
# NIST: https://csrc.nist.gov/Projects/post-quantum-cryptography/

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-ninja-build
BuildRequires: astyle
BuildRequires: banner
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
  FrodoKEM, HQC, Kyber, NTRU, NTRU-Prime, SABER, SIKE.

Supported signature schemes: Dilithium, Falcon, Picnic, Rainbow,
  SPHINCS+.

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

%prep
%setup
sed -i '\!DESTINATION!s!lib!%_libdir!' src/CMakeLists.txt
# Add armh to the list of supported arm32 arches.
sed -i '/CMAKE_SYSTEM_PROCESSOR.*armhf/s/")/|armv8l&/' CMakeLists.txt

%build
%add_optflags %(getconf LFS_CFLAGS) -Wa,--noexecstack
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

%check
banner tests
# Tests require lowercase 'build' dir.
export LD_LIBRARY_PATH=$PWD/build/lib
# https://github.com/open-quantum-safe/liboqs/wiki/Minimal-example-of-a-post-quantum-signature
  cc -Ibuild/include -Lbuild/lib tests/example_sig.c -o example_sig -loqs
  ./example_sig
# https://github.com/open-quantum-safe/liboqs/wiki/Minimal-example-of-a-post-quantum-KEM
  cc -Ibuild/include -Lbuild/lib tests/example_kem.c -o example_kem -loqs
  ./example_kem
%ninja_build -C build run_tests

%files
%doc LICENSE.txt README.md RELEASE.md
%_libdir/liboqs.so.*

%files devel
%doc LICENSE.txt README.md RELEASE.md
%_includedir/oqs
%_libdir/cmake/liboqs
%_libdir/liboqs.so

%changelog
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
