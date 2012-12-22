%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name network
%define f_pkg_name network
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.3.2.0
Release: alt3
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/haskell/network
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Low-level networking interface



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common ghc7.6.1-mtl ghc7.6.1-text ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-parsec

%description
Low-level networking interface

%prep
%setup
%patch -p1

%build
cp /usr/share/gnu-config/* .
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Sat Feb 09 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.3.2.0-alt3
- Applied upstream patch to fix build with gcc >= 5.
- Updated gnu-config scripts (to fix build on ppc64le).

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.3.2.0-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.3.2.0-alt1
- Spec created by cabal2rpm 0.20_08
