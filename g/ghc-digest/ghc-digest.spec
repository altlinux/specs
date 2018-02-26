%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name digest
%define f_pkg_name digest
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.0.0.9
Release: alt1.1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: Various cryptographic hashes for bytestrings; CRC32 and Adler32 for now.
# Automatically added by buildreq on Wed Mar 09 2011 (-bb)
BuildRequires: ghc-alex ghc-happy ghc-hscolour ghc-prof libnss-mdns rpm-build-haskell zlib-devel

BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



%description
This package provides efficient cryptographic hash implementations for
strict and lazy bytestrings. For now, CRC32 and Adler32 are supported; they
are implemented as FFI bindings to efficient code from zlib.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.0.0.9-alt1.1
- rebuild with shared objects support

* Wed Mar 09 2011 Denis Smirnov <mithraen@altlinux.ru> 0.0.0.9-alt1
- Spec created by cabal2rpm 0.20_08
