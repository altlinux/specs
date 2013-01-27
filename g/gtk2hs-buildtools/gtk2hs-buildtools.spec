%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name gtk2hs-buildtools
%define f_pkg_name gtk2hs-buildtools
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %f_pkg_name
Version: 0.12.4
Release: alt2
License: GPL-2

Group: Development/Haskell
Url: http://www.haskell.org/gtk2hs/
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Summary: Tools to build the Gtk2Hs suite of User Interface libraries

BuildRequires(pre): rpm-build-haskell

# Automatically added by buildreq on Mon Dec 24 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-random

%description
This package provides a set of helper programs necessary to build the
Gtk2Hs suite of libraries. These tools include a modified c2hs binding tool
that is used to generate FFI declarations, a tool to build a type hierarchy
that mirrors the C type hierarchy of GObjects found in glib, and a
generator for signal declarations that are used to call back from C to
Haskell. These tools are not needed to actually run Gtk2Hs programs.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Sun Jan 27 2013 Denis Smirnov <mithraen@altlinux.ru> 0.12.4-alt2
- cleanup

* Mon Dec 24 2012 Denis Smirnov <mithraen@altlinux.ru> 0.12.4-alt1
- 0.12.4

* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.12.3.1-alt1
- 0.12.3.1

* Tue Mar 20 2012 Denis Smirnov <mithraen@altlinux.ru> 0.12.3-alt1
- 0.12.3

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.2-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.2-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.2-alt1
- Spec created by cabal2rpm 0.20_08
