%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hscolour
%define f_pkg_name hscolour
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.20.2
Release: alt1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/~malcolm/hscolour/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Colourise Haskell code.



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy

%description
hscolour is a small Haskell script to colourise Haskell code. It currently
has six output formats: ANSI terminal codes (optionally XTerm-256colour
codes), HTML 3.2 with <font> tags, HTML 4.01 with CSS, HTML 4.01 with CSS
and mouseover annotations, XHTML 1.0 with inline CSS styling, LaTeX, and
mIRC chat codes.

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
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 1.20.2-alt1
- Spec created by cabal2rpm 0.20_08
