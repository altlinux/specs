%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name HDBC-postgresql
%define f_pkg_name hdbc-postgresql
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.3.2.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/hdbc/hdbc-postgresql
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: PostgreSQL driver for HDBC



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-convertible ghc7.4.2-mtl ghc7.4.2-text ghc7.4.2-transformers ghc7.4.2-utf8-string libgmp-devel libpq-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-hdbc ghc7.4.2-hscolour ghc7.4.2-parsec postgresql-devel

%description
This package provides a PostgreSQL driver for HDBC

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
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 2.3.2.1-alt1
- Spec created by cabal2rpm 0.20_08
