%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name pango
%define f_pkg_name pango
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.12.3
Release: alt1
License: LGPL-2.1
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://projects.haskell.org/gtk2hs/
Source: %name-%version.tar
Summary: Binding to the Pango text rendering engine.



# Automatically added by buildreq on Tue Mar 20 2012
# optimized out: fontconfig fontconfig-devel ghc7.4.1 ghc7.4.1-common ghc7.4.1-mtl ghc7.4.1-transformers glib2-devel libcairo-devel libfreetype-devel libgmp-devel pkg-config
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-cairo ghc7.4.1-cpphs ghc7.4.1-glib ghc7.4.1-happy gtk2hs-buildtools libpango-devel

%description
This package provides a wrapper around the Pango C library that allows
high-quality rendering of Unicode text. It can be used either with Cairo to
output text in PDF, PS or other documents or with Gtk+ to display text
on-screen.

%prep
%setup

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.12.3-alt1
- Spec created by cabal2rpm 0.20_08
