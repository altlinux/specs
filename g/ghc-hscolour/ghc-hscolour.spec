%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name hscolour
%define f_pkg_name hscolour
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.19
Release: alt1
License: GPL
Group: Development/Haskell
URL: http://www.cs.york.ac.uk/fp/darcs/hscolour/
Source: %name-%version.tar
Summary: Colourise Haskell code.
# Automatically added by buildreq on Fri Sep 10 2010
BuildRequires: ghc-alex ghc(Cabal) ghc-happy

BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell



%description
hscolour is a small Haskell script to colourise Haskell code. It currently
has four output formats: ANSI terminal codes, HTML 3.2 with <font> tags,
HTML 4.01 with CSS, and LaTeX.

%prep
%setup

%build
%hs_configure2 --datadir=%_datadir --datasubdir=%name-%version
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%hsc_namever-%f_pkg_name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%_bindir/HsColour
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_datadir/%name-%version
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Sat Sep 03 2011 Denis Smirnov <mithraen@altlinux.ru> 1.19-alt1
- 1.19

* Wed Aug 31 2011 Denis Smirnov <mithraen@altlinux.ru> 1.9-alt7.1.1
- rebuild with new ghc

* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 1.9-alt7.1
- rebuild with shared objects support

* Thu Mar 03 2011 Denis Smirnov <mithraen@altlinux.ru> 1.9-alt7
- rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.9-alt6
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1.9-alt5
- auto rebuild

* Sat Sep 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1.9-alt2
- add /usr/bin/HsColour

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.9-alt1
- Spec created by cabal2rpm 0.20_08
