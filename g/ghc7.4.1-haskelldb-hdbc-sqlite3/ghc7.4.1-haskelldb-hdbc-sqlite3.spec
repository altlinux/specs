%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name haskelldb-hdbc-sqlite3
%define f_pkg_name haskelldb-hdbc-sqlite3
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.1.0
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://trac.haskell.org/haskelldb
Source: %name-%version.tar
Summary: HaskellDB support for the HDBC SQLite driver.



# Automatically added by buildreq on Thu Mar 22 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-convertible ghc7.4.1-haskelldb ghc7.4.1-hdbc ghc7.4.1-mtl ghc7.4.1-text ghc7.4.1-transformers ghc7.4.1-utf8-string libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-cpphs ghc7.4.1-happy ghc7.4.1-haskelldb-hdbc ghc7.4.1-hdbc-sqlite3 libsqlite3-devel

%description
HaskellDB requires this driver if HDBC will be used to connect to a
SQLlite3 database.

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
* Tue Mar 20 2012 Denis Smirnov <mithraen@altlinux.ru> 2.1.0-alt1
- Spec created by cabal2rpm 0.20_08
