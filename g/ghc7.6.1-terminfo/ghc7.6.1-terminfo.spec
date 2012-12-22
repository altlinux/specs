%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name terminfo
%define f_pkg_name terminfo
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.2.5
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/terminfo
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Haskell bindings to the terminfo library.

BuildRequires: ghc7.6.1 ghc7.6.1-doc libgmp-devel libncurses-devel libtinfo-devel

%description
This library provides an interface to the terminfo database (via bindings
to the curses library). Terminfo allows POSIX systems to interact with a
variety of terminals using a standard set of capabilities.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.2.5-alt1
- Spec created by cabal2rpm 0.20_08
