%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name deepseq
%define f_pkg_name deepseq
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.1.0.2
Release: alt1.1
License: BSD3
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: Fully evaluate data structures
BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell



%description
This package provides a \"deep\" version of seq, for fully evluating data
structures.

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
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 1.1.0.2-alt1.1
- rebuild with shared objects support

* Wed Dec 08 2010 Denis Smirnov <mithraen@altlinux.ru> 1.1.0.2-alt1
- 1.1.0.2

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.1.0.0-alt8
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.1.0.0-alt7
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.1.0.0-alt6
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.1.0.0-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.1.0.0-alt2
- cleanup spec

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.1.0.0-alt1
- Spec created by cabal2rpm 0.20_08
