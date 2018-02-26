%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name cabal-install-ghc74
%define f_pkg_name cabal-install-ghc74
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: cabal-install-ghc74
Version: 0.10.4
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://www.haskell.org/cabal/
Source: %name-%version.tar
Summary: Temporary version of cabal-install for ghc-7.4

Provides: cabal-install = %version-%release
Obsoletes: cabal-install < %version-%release
Conflicts: cabal-install < %version-%release

# Automatically added by buildreq on Tue Mar 20 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-mtl ghc7.4.1-network ghc7.4.1-parsec ghc7.4.1-text ghc7.4.1-transformers libgmp-devel pkg-config python-base
BuildRequires: ghc7.4.1-alex ghc7.4.1-happy ghc7.4.1-http ghc7.4.1-random ghc7.4.1-zlib zlib-devel

%description
This is a naive adaption of cabal-install-ghc72 for ghc 7.4.1. Don't
complain if it does not work for you.

The \'cabal\' command-line program simplifies the process of managing
Haskell software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.

cabal-install-0.10.2 does not build with the packages that come with
ghc-7.4. This package is a copy of cabal-install-0.10.2 with dependency
version changes made in the cabal file and the bootstrap.sh file to be
compatible with ghc-7.4 packages. Thanks to beastaugh on github for
describing these changes at https://gist.github.com/1169332. This package
will be removed once a new version of cabal-install comes out that is
compatible with the next version of ghc, 7.4.

Known bug: cabal sdist does not work with the version. You must build your
own source package using tar czf.

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

%files
%_bindir/cabal

%changelog
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10.4-alt1
- Spec created by cabal2rpm 0.20_08
