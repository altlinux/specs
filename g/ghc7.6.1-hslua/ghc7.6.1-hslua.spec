%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hslua
%define f_pkg_name hslua
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.4
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/hslua
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A Lua language interpreter embedding in Haskell



# Automatically added by buildreq on Mon Dec 24 2012
# optimized out: ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour

%description
The Scripting.Lua module is a wrapper of Lua language interpreter as
described in www.lua.org.

The package is standalone: full Lua interpreter version 5.1.4 is
distributed in this package as well.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.4-alt1
- Spec created by cabal2rpm 0.20_08
