%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name xhtml
%define f_pkg_name xhtml
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 3000.2.0.1
Release: alt6.1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: An XHTML combinator library
# Automatically added by buildreq on Fri Sep 10 2010
BuildRequires: ghc-alex ghc(Cabal) ghc-happy

BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell



%description
This package provides combinators for producing XHTML 1.0, including the
Strict, Transitional and Frameset variants.

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
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 3000.2.0.1-alt6.1
- rebuild with shared objects support

* Wed Mar 09 2011 Denis Smirnov <mithraen@altlinux.ru> 3000.2.0.1-alt6
- rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 3000.2.0.1-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 3000.2.0.1-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 3000.2.0.1-alt1
- Spec created by cabal2rpm 0.20_08
