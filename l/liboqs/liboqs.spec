# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: liboqs
Version: 0.4.0
Release: alt1
Summary: C library for prototyping and experimenting with quantum-resistant cryptography
License: MIT
Group: System/Libraries
Url: https://openquantumsafe.org/liboqs/
Vcs: https://github.com/open-quantum-safe/liboqs/
# NIST: https://csrc.nist.gov/Projects/post-quantum-cryptography/

# Only supported arches ar: x86_64, arm64, and arm.
ExclusiveArch: x86_64 aarch64 armh

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-ninja-build
BuildRequires: astyle
BuildRequires: banner
BuildRequires: cmake
BuildRequires: libssl-devel
BuildRequires: ninja-build
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
%ifarch armh
# Temporary ARM workaround
# https://github.com/open-quantum-safe/liboqs/issues/921
  sed -i '/target_compile_definitions(picnic.*PICNIC_STATIC/s/$/ NO_MISALIGNED_ACCESSES/' \
      src/sig/picnic/CMakeLists.txt
%endif

%build
# CMake options https://github.com/open-quantum-safe/liboqs/wiki/Customizing-liboqs
# Default (oqsdefault) algos was (see .CMake/alg_support.cmake):
#   OQS_KEM_DEFAULT "OQS_KEM_alg_frodokem_640_aes" (~Microsoft) L1
#   OQS_SIG_DEFAULT "OQS_SIG_alg_dilithium_2" (~IBM) L2
# for the sake of diversity I change them (in cmake invocation) to
# D. J. Bernstein teams':
#   OQS_KEM_DEFAULT="OQS_KEM_alg_ntruprime_ntrulpr653" L2
#   OQS_SIG_DEFAULT="OQS_SIG_alg_sphincs_haraka_192f_simple" L3
# with (claimed) NIST security level not less than before.
%cmake \
	-GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=ON \
	-DOQS_PORTABLE_BUILD=ON \
	-DOQS_USE_CPU_EXTENSIONS=ON \
	-DOQS_KEM_DEFAULT="OQS_KEM_alg_ntruprime_ntrulpr653" \
	-DOQS_SIG_DEFAULT="OQS_SIG_alg_sphincs_haraka_192f_simple"
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%check
banner tests
# Tests require lowercase 'build' dir.
mv BUILD build
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
* Mon Feb 22 2021 Vitaly Chikunov <vt@altlinux.org> 0.4.0-alt1
- First import of v0.4.0 (2020-08-11) + update (2021-02-18).
