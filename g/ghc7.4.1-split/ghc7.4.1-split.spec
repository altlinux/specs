%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name split
%define f_pkg_name split
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.4.2
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://code.haskell.org/~byorgey/code/split
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Combinator library for splitting lists.



# Automatically added by buildreq on Sun Mar 25 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-cpphs ghc7.4.1-happy ghc7.4.1-hscolour

%description
Combinator library and utility functions for splitting lists.

%prep
%setup
%patch -p1

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
* Sun Mar 25 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.4.2-alt1
- Spec created by cabal2rpm 0.20_08
