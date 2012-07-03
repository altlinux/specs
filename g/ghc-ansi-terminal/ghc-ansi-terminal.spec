%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name ansi-terminal
%define f_pkg_name ansi-terminal
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.3
Release: alt1.1.1
License: BSD3
Group: Development/Haskell
URL: http://batterseapower.github.com/ansi-terminal
Source: %name-%version.tar
Summary: Simple ANSI terminal support, with Windows compatibility
BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell



%description
ANSI terminal support for Haskell: allows cursor movement, screen clearing,
color output showing or hiding the cursor, and changing the title.
Compatible with Windows and those Unixes with ANSI terminals, but only GHC
is supported as a compiler.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

#cd %buildroot%_datadir/doc/%hsc_namever-%f_pkg_name-%version
#rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.5.3-alt1.1.1
- rebuild with shared objects support

* Tue Dec 07 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.3-alt1.1
- rebuild with ghc 7.0

* Wed Sep 15 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.3-alt1
- Spec created by cabal2rpm 0.20_08
