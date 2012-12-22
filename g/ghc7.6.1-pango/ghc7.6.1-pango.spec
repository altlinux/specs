%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name pango
%define f_pkg_name pango
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.12.4
Release: alt1
License: LGPL-2.1
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://projects.haskell.org/gtk2hs/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Binding to the Pango text rendering engine.



# Automatically added by buildreq on Mon Dec 24 2012 (-bb)
# optimized out: elfutils fontconfig fontconfig-devel ghc7.6.1 ghc7.6.1-common ghc7.6.1-mtl ghc7.6.1-transformers glib2-devel libcairo-devel libfreetype-devel libgmp-devel libwayland-client libwayland-server pkg-config python-base rpm-build-haskell zlib-devel
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cairo ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-glib ghc7.6.1-happy ghc7.6.1-hscolour gtk2hs-buildtools libpango-devel

%description
This package provides a wrapper around the Pango C library that allows
high-quality rendering of Unicode text. It can be used either with Cairo to
output text in PDF, PS or other documents or with Gtk+ to display text
on-screen.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.12.4-alt1
- Spec created by cabal2rpm 0.20_08
