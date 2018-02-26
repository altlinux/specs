%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name gio
%define f_pkg_name gio
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: ghc-gio
Version: 0.12.0
Release: alt2.1
License: LGPL-2.1
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.haskell.org/gtk2hs/
Source: %name-%version.tar
Summary: Binding to the GIO
# Automatically added by buildreq on Fri Sep 10 2010
BuildRequires: ghc-alex ghc(Cabal) ghc-glib ghc-happy gtk2hs-buildtools libgio-devel

BuildRequires: ghc ghc(mtl)
BuildRequires(pre): rpm-build-haskell

%description
GIO is striving to provide a modern, easy-to-use VFS API that sits at the
right level in the library stack. The goal is to overcome the shortcomings
of GnomeVFS and provide an API that is so good that developers prefer it
over raw POSIX calls. Among other things that means using GObject. It also
means not cloning the POSIX API, but providing higher-level,
document-centric interfaces.

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

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt6
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt5
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt2
- fix build requires

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt1
- Spec created by cabal2rpm 0.20_08
