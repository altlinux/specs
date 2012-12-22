%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name haskelldb-hdbc
%define f_pkg_name haskelldb-hdbc
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.2.2
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: https://github.com/m4dc4p/haskelldb
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: HaskellDB support for HDBC.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common ghc7.6.1-convertible ghc7.6.1-mtl ghc7.6.1-text ghc7.6.1-transformers ghc7.6.1-utf8-string libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-haskelldb ghc7.6.1-hdbc ghc7.6.1-hscolour

%description
HaskellDB requires this driver to work with any of HDBC's drivers.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.2.2-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.2.2-alt1
- Spec created by cabal2rpm 0.20_08
