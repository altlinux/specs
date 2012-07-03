%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name texmath
%define f_pkg_name texmath
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Serial: 1
Version: 0.5.0.1
Release: alt2.1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://github.com/jgm/texmath
Source: %name-%version.tar
Summary: Conversion of LaTeX math formulas to MathML.
# Automatically added by buildreq on Wed Mar 09 2011 (-bb)
BuildRequires: ghc-alex ghc-happy ghc-hscolour ghc-parsec ghc-prof ghc-syb ghc-xml libnss-mdns rpm-build-haskell

BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



%description
The texmathml library provides functions to convert LaTeX math formulas to
presentation MathML. It supports basic LaTeX and AMS extensions, and it can
parse and apply LaTeX macros.

Use the @test@ flag to install a standalone executable, @texmath@, that
reads a LaTeX formula from @stdin@ and writes MathML to @stdout@.

Use the @cgi@ flag to install a cgi script, @texmath-cgi@. 

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
%_datadir/%name-%version
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 1:0.5.0.1-alt2.1
- rebuild with shared objects support

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:0.5.0.1-alt2
- build with different tagname

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:0.5.0.1-alt1
- 0.5.0.1

* Wed May 18 2011 Igor Vlasenko <viy@altlinux.ru> 1:0.4-alt2
- added unpackaged data files

* Tue Apr 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:0.4-alt1
- revert to 0.4 (from Fedora)

* Wed Mar 09 2011 Denis Smirnov <mithraen@altlinux.ru> 0.5.0.1-alt1
- Spec created by cabal2rpm 0.20_08
