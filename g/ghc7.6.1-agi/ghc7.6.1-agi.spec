%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name AGI
%define f_pkg_name agi
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.3
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://src.seereason.com/haskell-agi
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A library for writing AGI scripts for Asterisk



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common ghc7.6.1-mtl ghc7.6.1-parsec ghc7.6.1-text ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-network ghc7.6.1-random ghc7.6.1-syb

%description
Asterisk is an open-source Voice over IP server (VoIP). Asterisk provides
an Asterisk Gateway Interface (AGI), which can be used to write external
programs that interact with Asterisk. It is typically used for creating
Interactive Voice Response (IVR) systems.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt1
- Spec created by cabal2rpm 0.20_08
