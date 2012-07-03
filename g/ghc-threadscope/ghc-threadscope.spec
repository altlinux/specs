%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name threadscope
%define f_pkg_name threadscope
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.2
Release: alt8
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: A graphical thread profiler.
# Automatically added by buildreq on Wed Mar 23 2011 (-bb)
BuildRequires: ghc-alex ghc-ghc-events ghc-glade ghc-happy ghc-hscolour libglade-devel libxml2-devel

BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell

%description
A graphical viewer for GHC eventlog traces. 

%prep
%setup

%build
%hs_configure2
%hs_build

%install
runghc Setup copy --destdir=%buildroot

%files
%_bindir/*
%_datadir/%name-%version
%_datadir/doc/%name-%version

%changelog
* Wed Mar 23 2011 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt8
- fix build

* Mon Mar 14 2011 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt7
- fix build

* Tue Sep 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt6
- fix build

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt1
- first build for Sisyphus
