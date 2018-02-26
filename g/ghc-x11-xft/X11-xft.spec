%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name X11-xft
%define f_pkg_name x11-xft
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3
Release: alt6.1
License: LGPL
Packager: Alex V. Myltsev <avm@altlinux.ru>
Group: Development/Haskell
Source: %name-%version.tar
Summary: Bindings to the Xft, X Free Type interface library, and some Xrender parts
BuildRequires: ghc
BuildRequires: ghc-utf8-string ghc-x11 libXext-devel libXft-devel libXinerama-devel
BuildRequires(pre): rpm-build-haskell



%description
Bindings to the Xft, X Free Type interface library, and some Xrender parts

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
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt6.1
- rebuild with shared objects support

* Thu Mar 03 2011 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt6
- rebuild

* Sat Dec 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt5.2
- rebuild

* Tue Dec 07 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt5.1
- rebuild with ghc 7.0/var/lib/altlinux/sisyphus/files/SRPMS/ghc-ansi-terminal-0.5.3-alt1.src.rpm

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- Spec created by cabal2rpm 0.20_08
