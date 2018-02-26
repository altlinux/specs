%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name texmath
%define f_pkg_name texmath
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.0.6
Release: alt1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/jgm/texmath
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Conversion of LaTeX math formulas to MathML or OMML.



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-mtl ghc7.4.2-text ghc7.4.2-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-hscolour ghc7.4.2-parsec ghc7.4.2-syb ghc7.4.2-xml

%description
The texmathml library provides functions to convert LaTeX math formulas to
presentation MathML (which can be used in HTML) or OMML (Office Math Markup
Language, used in Microsoft Office). It supports basic LaTeX and AMS
extensions, and it can parse and apply LaTeX macros.

Use the @test@ flag to install a standalone executable, @texmath@, that
reads a LaTeX formula from @stdin@ and writes MathML to @stdout@.

Use the @cgi@ flag to install a cgi script, @texmath-cgi@.

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
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.6.0.6-alt1
- Spec created by cabal2rpm 0.20_08
