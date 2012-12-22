%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name stateref
%define f_pkg_name stateref
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3
Release: alt1
License: PublicDomain
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/~mokus/stateref/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Abstraction for things that work like IORef.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-mtl ghc7.6.1-stm

%description
A collection of type-classes generalizing the read\/write\/modify
operations for stateful variables provided by things like IORef, TVar, &c.
Note that The interface has changed a bit from the 0.2.* version. \"*Ref\"
functions are now called \"*Reference\" and new \"*Ref\" function exist
with simpler signatures. The new 'Ref' existential type provides a
convenient monad-indexed reference type, and the HasRef class indicates
monads for which there is a default reference type for every referent.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- Spec created by cabal2rpm 0.20_08
