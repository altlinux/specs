%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name SDL
%define f_pkg_name sdl
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.4
Release: alt1
License: BSD3
Group: Development/Haskell
Url: http://hackage.haskell.org/package/SDL
Source: SDL-%version.tar.gz
Summary: Binding to libSDL
# Automatically added by buildreq on Mon Oct 22 2012
# optimized out: ghc7.4.2 ghc7.4.2-common libgmp-devel pkg-config
BuildRequires: ghc7.4.2-alex ghc7.4.2-c2hs ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-hscolour libSDL-devel

BuildRequires(pre): rpm-build-haskell

%description
Simple DirectMedia Layer \(libSDL\) is a cross-platform multimedia library
designed to provide low level access to audio, keyboard, mouse, joystick,
3D hardware via OpenGL, and 2D video framebuffer. It is used by MPEG
playback software, emulators, and many popular games, including the award
winning Linux port of \"Civilization: Call To Power.\"

%prep
%setup -n SDL-%version

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
* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 0.6.4-alt1
- Autobuild version bump to 0.6.4

* Mon Sep 26 2011 Fr. Br. George <george@altlinux.ru> 0.6.2-alt1
- Spec created by cabal2rpm 0.20_08
