%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name X11
%define f_pkg_name x11
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.6.0.2
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: https://github.com/haskell-pkg-janitors/X11
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A binding to the X11 graphics library



# Automatically added by buildreq on Tue Dec 25 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common libX11-devel libXrender-devel libgmp-devel pkg-config python-base rpm-build-haskell xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour imake libICE-devel libXext-devel libXinerama-devel libXrandr-devel xorg-cf-files

%description
A Haskell binding to the X11 graphics library. The binding is a direct
translation of the C binding; for documentation of these calls, refer to
"The Xlib Programming Manual", available online at
<http://tronche.com/gui/x/xlib/>.

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
* Tue Dec 25 2012 Denis Smirnov <mithraen@altlinux.ru> 1.6.0.2-alt1
- 1.6.0.2

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5.0.1-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5.0.1-alt1
- Spec created by cabal2rpm 0.20_08
