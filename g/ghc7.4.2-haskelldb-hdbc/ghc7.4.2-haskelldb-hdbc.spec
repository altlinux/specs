%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name haskelldb-hdbc
%define f_pkg_name haskelldb-hdbc
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.1.0
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://trac.haskell.org/haskelldb
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: HaskellDB support for HDBC.



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-convertible ghc7.4.2-mtl ghc7.4.2-text ghc7.4.2-transformers ghc7.4.2-utf8-string libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-haskelldb ghc7.4.2-hdbc ghc7.4.2-hscolour

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
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 2.1.0-alt1
- Spec created by cabal2rpm 0.20_08
