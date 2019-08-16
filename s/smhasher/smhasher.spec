%define _unpackaged_files_terminate_build 1

Name: smhasher
Version: 0.0.1
Release: alt1.git61a0530
Summary: Test suite designed to test the distribution, collision, and performance properties of non-cryptographic hash function
Group: Other
License: MIT
Url: https://github.com/aappleby/smhasher

# https://github.com/aappleby/smhasher.git
Source: %name-%version.tar

Patch1: %name-alt-build.patch
Patch2: %name-alt-timer.patch

BuildRequires: gcc-c++ cmake

Requires: lib%name = %EVR

%description
SMHasher is a test suite designed to test the distribution,
collision, and performance properties of non-cryptographic hash functions.

This is the home for the MurmurHash family of hash functions
along with the SMHasher test suite used to verify them.
SMHasher is released under the MIT license.
All MurmurHash versions are public domain software,
and the author disclaims all copyright to their code.

SMHasher is a test suite designed to test the distribution,
collision, and performance properties of non-cryptographic hash functions
- it aims to be the DieHarder of hash testing,
and does a pretty good job of finding flaws with a number of popular hashes.

The SMHasher suite also includes MurmurHash3, which is the latest version
in the series of MurmurHash functions - the new version is faster, more robust,
and its variants can produce 32- and 128-bit hash values efficiently
on both x86 and x64 platforms.

%package -n lib%name
Summary: Library containing implementation of various non-cryptographic hashes
Group: System/Libraries

%description -n lib%name
SMHasher is a test suite designed to test the distribution,
collision, and performance properties of non-cryptographic hash functions.

This is the home for the MurmurHash family of hash functions
along with the SMHasher test suite used to verify them.
SMHasher is released under the MIT license.
All MurmurHash versions are public domain software,
and the author disclaims all copyright to their code.

SMHasher is a test suite designed to test the distribution,
collision, and performance properties of non-cryptographic hash functions
- it aims to be the DieHarder of hash testing,
and does a pretty good job of finding flaws with a number of popular hashes.

The SMHasher suite also includes MurmurHash3, which is the latest version
in the series of MurmurHash functions - the new version is faster, more robust,
and its variants can produce 32- and 128-bit hash values efficiently
on both x86 and x64 platforms.

%package -n lib%name-devel
Summary: Library containing implementation of various non-cryptographic hashes
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
SMHasher is a test suite designed to test the distribution,
collision, and performance properties of non-cryptographic hash functions.

This is the home for the MurmurHash family of hash functions
along with the SMHasher test suite used to verify them.
SMHasher is released under the MIT license.
All MurmurHash versions are public domain software,
and the author disclaims all copyright to their code.

SMHasher is a test suite designed to test the distribution,
collision, and performance properties of non-cryptographic hash functions
- it aims to be the DieHarder of hash testing,
and does a pretty good job of finding flaws with a number of popular hashes.

The SMHasher suite also includes MurmurHash3, which is the latest version
in the series of MurmurHash functions - the new version is faster, more robust,
and its variants can produce 32- and 128-bit hash values efficiently
on both x86 and x64 platforms.

This package contains development files.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
pushd src
%cmake
%cmake_build
popd

%install
pushd src
%cmakeinstall_std
popd

%files
%_bindir/*

%files -n lib%name
%doc README.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name
%_libdir/*.so

%changelog
* Fri Aug 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.1-alt1.git61a0530
- Initial build for ALT.
