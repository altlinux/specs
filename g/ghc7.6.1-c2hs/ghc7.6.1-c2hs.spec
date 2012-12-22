%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name c2hs
%define f_pkg_name c2hs
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.16.4
Release: alt1
License: GPL-2
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.cse.unsw.edu.au/~chak/haskell/c2hs/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: C->Haskell FFI tool that gives some cross-language type safety



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common ghc7.6.1-syb libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-cpphs ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-language-c

%description
C->Haskell assists in the development of Haskell bindings to C libraries.
It extracts interface information from C header files and generates Haskell
code with foreign imports and marshaling. Unlike writing foreign imports by
hand (or using hsch2s), this ensures that C functions are imported with the
correct Haskell types.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.16.4-alt1
- Spec created by cabal2rpm 0.20_08
