%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define f_pkg_name pandoc
%define h_pkg_name pandoc
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: pandoc
Version: 1.9.2
Release: alt1
Summary: Markup conversion tool for markdown

Group: Publishing
License: GPLv2+
Url: http://hackage.haskell.org/package/%name

Source: http://hackage.haskell.org/packages/archive/%name/%version/%name-%version.tar.gz

BuildRequires: ghc%ghc_version-base64-bytestring ghc%ghc_version-citeproc-hs ghc%ghc_version-highlighting-kate ghc%ghc_version-http ghc%ghc_version-random ghc%ghc_version-tagsoup ghc%ghc_version-temporary ghc%ghc_version-texmath ghc%ghc_version-zip-archive zlib-devel
BuildRequires(pre): rpm-build-haskell

%description
Pandoc is a Haskell library for converting from one markup format to
another, and a command-line tool that uses this library. It can read
markdown and (subsets of) reStructuredText, HTML, and LaTeX, and it can
write markdown, reStructuredText, HTML, LaTeX, ConTeXt, Docbook,
OpenDocument, ODT, RTF, MediaWiki, groff man pages, EPUB, and S5 and
Slidy HTML slide shows.

%prep
%setup -q

%build
rm -f man/man1/pandoc.1
runghc Setup configure --bindir=%_bindir --libdir=%_libdir --datadir=%_datadir --docdir=%_docdir
runghc Setup build

%install
runghc Setup copy --destdir=%buildroot

%files
%doc BUGS COPYING COPYRIGHT README
%attr(755,root,root) %_bindir/%name
%_datadir/%name-%version
%_libdir/%name-%version
%attr(644,root,root) %_man1dir/*
%attr(644,root,root) %_man5dir/*

%changelog
* Wed May 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Mon Mar 19 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.1.2-alt1
- 1.9.1.2

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2.1-alt1
- 1.8.2.1

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.0.1-alt1
- initial from Fedora
