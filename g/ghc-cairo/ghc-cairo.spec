%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name cairo
%define f_pkg_name cairo
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: ghc-cairo
Version: 0.12.0
Release: alt2.1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.haskell.org/gtk2hs/
Source: %name-%version.tar
Summary: Binding to the Cairo library
# Automatically added by buildreq on Fri Sep 10 2010
BuildRequires: ghc-alex ghc(Cabal) ghc-happy ghc(mtl) gtk2hs-buildtools libcairo-devel

BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell

%description
Cairo is a library to render high quality vector graphics. There exist
various backends that allows rendering to Gtk windows, PDF, PS, PNG and SVG
documents, amongst others.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_docdir/%hsc_namever-%f_pkg_name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
%_datadir/%name-%version
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.12.0-alt2.1
- rebuild with shared objects support

* Wed May 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2
- added unpackaged data files

* Tue Mar 08 2011 Denis Smirnov <mithraen@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.0-alt1
- Spec created by cabal2rpm 0.20_08
