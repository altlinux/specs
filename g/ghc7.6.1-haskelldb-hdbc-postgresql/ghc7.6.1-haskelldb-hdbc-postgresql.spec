%set_verify_elf_method rpath=relaxed

%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name haskelldb-hdbc-postgresql
%define f_pkg_name haskelldb-hdbc-postgresql
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.1.2
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: https://github.com/m4dc4p/haskelldb
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: HaskellDB support for the HDBC PostgreSQL driver.



# Automatically added by buildreq on Mon Dec 24 2012
# optimized out: ghc7.6.1 ghc7.6.1-common ghc7.6.1-convertible ghc7.6.1-haskelldb ghc7.6.1-hdbc ghc7.6.1-mtl ghc7.6.1-parsec ghc7.6.1-text ghc7.6.1-transformers ghc7.6.1-utf8-string libgmp-devel pkg-config
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-haskelldb-hdbc ghc7.6.1-hdbc-postgresql ghc7.6.1-hscolour libpq-devel

%description
HaskellDB requires this driver if HDBC will be used to connect to a
PostgreSQL database.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.1.2-alt1
- Spec created by cabal2rpm 0.20_08
