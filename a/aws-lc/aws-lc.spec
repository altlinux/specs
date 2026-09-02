%define sover 0

Name: aws-lc
Version: 1.71.0
Release: alt1

Summary: General-purpose cryptographic library maintained by AWS

License: Apache-2.0
Group: System/Libraries
URL: https://github.com/aws/aws-lc
# Source-url: https://github.com/aws/aws-lc/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ninja-build
BuildRequires: perl-base
BuildRequires: libunwind-devel

ExcludeArch: armh

%description
AWS-LC is a general-purpose cryptographic library maintained by the AWS
Cryptography team for AWS and their customers. It is based on code from
the Google BoringSSL project and the OpenSSL project.

AWS-LC provides FIPS-validated cryptographic algorithms including AES,
SHA, RSA, elliptic curve, and AEAD ciphers. Libraries are installed
with -awslc suffix to coexist with system OpenSSL.

%package -n libcrypto-awslc%sover
Summary: AWS-LC crypto shared library
Group: System/Libraries

%description -n libcrypto-awslc%sover
AWS-LC crypto shared library (libcrypto-awslc).

%package -n libssl-awslc%sover
Summary: AWS-LC SSL shared library
Group: System/Libraries

%description -n libssl-awslc%sover
AWS-LC SSL shared library (libssl-awslc).

%package devel
Summary: Development files for AWS-LC
Group: Development/C
Requires: libcrypto-awslc%sover = %EVR
Requires: libssl-awslc%sover = %EVR

%description devel
Headers and development files for building software against AWS-LC.
Headers are installed to %_includedir/aws-lc/openssl/ to avoid
conflicts with system OpenSSL.

%prep
%setup

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DENABLE_DIST_PKG=ON \
    -DENABLE_DIST_PKG_OPENSSL_SHIM=OFF \
    -DBUILD_TESTING=OFF \
    -DBUILD_TOOL=OFF \
    -DDISABLE_GO=ON \
    %nil
%cmake_build

%install
%cmake_install

%files -n libcrypto-awslc%sover
%_libdir/libcrypto-awslc.so.%sover
%_libdir/libcrypto-awslc.so.%version

%files -n libssl-awslc%sover
%_libdir/libssl-awslc.so.%sover
%_libdir/libssl-awslc.so.%version

%files devel
%_includedir/aws-lc/
%_libdir/libcrypto-awslc.so
%_libdir/libssl-awslc.so
%_libdir/pkgconfig/aws-lc.pc
%_libdir/pkgconfig/libcrypto-awslc.pc
%_libdir/pkgconfig/libssl-awslc.pc
%_libdir/crypto/
%_libdir/ssl/

%changelog
* Sat Apr 04 2026 Vitaly Lipatov <lav@altlinux.ru> 1.71.0-alt1
- initial build for ALT Sisyphus

