%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name X11
%define f_pkg_name x11
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.5.0.0
Release: alt8.1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://code.haskell.org/X11
Source: %name-%version.tar
Summary: A binding to the X11 graphics library
BuildRequires: ghc ghc-syb
BuildRequires: imake libICE-devel libX11-devel libXext-devel libXinerama-devel xorg-cf-files
BuildRequires(pre): rpm-build-haskell

%description
A Haskell binding to the X11 graphics library. The binding is a direct
translation of the C binding; for documentation of these calls, refer to
"The Xlib Programming Manual", available online at
<http://tronche.com/gui/x/xlib/>.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%hsc_namever-%f_pkg_name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 1.5.0.0-alt8.1
- rebuild with shared objects support

* Wed Dec 08 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5.0.0-alt8
- ghc 7.0.1

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5.0.0-alt7
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5.0.0-alt6
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5.0.0-alt3
- fix build requires

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5.0.0-alt2
- ghc 6.12.3

* Tue Sep 07 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5.0.0-alt1
- Spec created by cabal2rpm 0.20_08
