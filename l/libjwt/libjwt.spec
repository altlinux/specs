%define _unpackaged_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define soversion 14

%def_with check

Name: libjwt
Version: 3.6.1
Release: alt1

Summary: JSON Web Token (JWT) C library
License: MPL-2.0
Group: System/Libraries
URL: https://github.com/benmcollins/libjwt
VCS: https://github.com/benmcollins/libjwt

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(openssl)
%if_with check
BuildRequires: pkgconfig(check)
BuildRequires: openssl
%endif

%description
LibJWT is a C library for creating, signing and verifying JSON Web
Tokens (RFC 7519) and JWE (RFC 7516). HMAC, RSA, ECDSA, RSA-PSS and
EdDSA algorithms are supported via the OpenSSL backend.

%package -n libjwt%soversion
Summary: JSON Web Token C library (runtime)
Group: System/Libraries

%description -n libjwt%soversion
Runtime shared library libjwt.so.%soversion.

%package -n jwt
Summary: Command-line tools for JWT and JWE
Group: Other

%description -n jwt
jwt-generate, jwt-verify, jwe-encrypt, jwe-decrypt, jwk2key and
key2jwk command-line tools.

%package devel
Summary: Development files for libjwt
Group: Development/C
Requires: libjwt%soversion = %EVR

%description devel
Headers, pkg-config and CMake metadata for developing against libjwt.

%package devel-static
Summary: Static library for libjwt
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
Static libjwt.a built with -ffat-lto-objects.

%prep
%setup

%build
%cmake -DWITH_TESTS=%{?_with_check:ON}%{?!_with_check:OFF}
%cmake_build

%install
%cmake_install
rm -r %buildroot%_defaultdocdir/LibJWT

%check
ctest -N --test-dir %_target_platform

%files -n libjwt%soversion
%doc LICENSE README.md
%_libdir/libjwt.so.%soversion
%_libdir/libjwt.so.%soversion.*

%files devel
%_includedir/jwt.h
%_includedir/jwt_export.h
%_libdir/libjwt.so
%_pkgconfigdir/libjwt.pc
%_libdir/cmake/LibJWT/

%files devel-static
%_libdir/libjwt.a

%files -n jwt
%_bindir/jwt-generate
%_bindir/jwt-verify
%_bindir/jwe-encrypt
%_bindir/jwe-decrypt
%_bindir/jwk2key
%_bindir/key2jwk
%_man1dir/*.1.*

%changelog
* Mon Aug 31 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.6.1-alt1
- Initial build for ALT Sisyphus.
