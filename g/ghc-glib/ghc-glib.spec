%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name glib
%define f_pkg_name glib
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: ghc-glib
Version: 0.12.0
Release: alt2.1
License: LGPL-2.1
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.haskell.org/gtk2hs/
Source: %name-%version.tar
Summary: Binding to the GLIB library for Gtk2Hs
# Automatically added by buildreq on Fri Sep 10 2010
BuildRequires: ghc-alex ghc(Cabal) ghc-happy glib2-devel gtk2hs-buildtools

BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell

%description
The GNU Library is a collection of C data structures and utility function
for dealing with Unicode. This package only binds as much functionality as
required to support the packages that wrap libraries that are themselves
based on GLib.

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
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.12.0-alt2.1
- rebuild with shared objects support

* Tue Aug 09 2011 Denis Smirnov <mithraen@altlinux.ru> 0.12.0-alt2
- rebuild

* Tue Mar 08 2011 Denis Smirnov <mithraen@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.2-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.2-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.2-alt1
- Spec created by cabal2rpm 0.20_08
