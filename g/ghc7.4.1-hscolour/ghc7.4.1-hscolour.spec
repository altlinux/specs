%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hscolour
%define f_pkg_name hscolour
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.19
Release: alt1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://code.haskell.org/~malcolm/hscolour/
Source: %name-%version.tar
Summary: Colourise Haskell code.



# Automatically added by buildreq on Fri Mar 23 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-cpphs ghc7.4.1-happy

%description
hscolour is a small Haskell script to colourise Haskell code. It currently
has six output formats: ANSI terminal codes (optionally XTerm-256colour
codes), HTML 3.2 with <font> tags, HTML 4.01 with CSS, HTML 4.01 with CSS
and mouseover annotations, XHTML 1.0 with inline CSS styling, LaTeX, and
mIRC chat codes.

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
%_bindir/HsColour
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_datadir/%name-%version

%changelog
* Fri Mar 23 2012 Denis Smirnov <mithraen@altlinux.ru> 1.19-alt1
- Spec created by cabal2rpm 0.20_08
