%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name SHA
%define f_pkg_name sha
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.6.4.4
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/SHA
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Implementations of the SHA suite of message digest functions

BuildRequires: ghc8.6.4 ghc8.6.4-doc


%description
This library implements the SHA suite of message digest functions,
according to NIST FIPS 180-2 (with the SHA-224 addendum), as well as the
SHA-based HMAC routines. The functions have been tested against most of the
NIST and RFC test vectors for the various functions. While some attention
has been paid to performance, these do not presently reach the speed of
well-tuned libraries, like OpenSSL.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Fri Aug 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.4.4-alt1
- Build new version for ghc8.6.4.
